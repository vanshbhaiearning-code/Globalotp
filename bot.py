import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import time
import json
import os

TOKEN = "8615004462:AAF1YmbE0-NWSWPPp6Bpvpr6DpRKYoaXKAk"

bot = telebot.TeleBot(TOKEN)

CHANNEL_1 = "@latestmodsapks"
CHANNEL_2 = "@latestmodsapp"

BOT_NAME = "GlobalOTP Bot"

# =========================
# DATABASE
# =========================

DB_FILE = "users.json"

if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({}, f)


def load_users():
    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_users(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


# =========================
# START SYSTEM
# =========================

@bot.message_handler(commands=['start'])
def start(message):

    users = load_users()

    user_id = str(message.from_user.id)

    # REFERRAL SYSTEM
    args = message.text.split()

    if user_id not in users:
        users[user_id] = {
            "points": 0,
            "joined": False,
            "referred_by": None
        }

        if len(args) > 1:
            referrer = args[1]

            if referrer != user_id and referrer in users:
                users[referrer]["points"] += 5
                users[user_id]["referred_by"] = referrer

        save_users(users)

    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        InlineKeyboardButton(
            "📢 Join Updates Channel",
            url=f"https://t.me/{CHANNEL_1.replace('@','')}"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            "🚀 Join Main Channel",
            url=f"https://t.me/{CHANNEL_2.replace('@','')}"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            "✅ Verify Access",
            callback_data="check_join"
        )
    )

    text = f"""
╔════════════════════╗
      ⚡ {BOT_NAME}
╚════════════════════╝

🔒 Secure Demo Verification
🌍 Multi Country Access
⚡ Fast OTP Generator
🎁 Referral Rewards System

━━━━━━━━━━━━━━━━━━
📢 Join Channels To Continue
━━━━━━━━━━━━━━━━━━

🔥 Earn Points By Referring Friends
💎 Premium Modern Interface
"""

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=keyboard
    )


# =========================
# JOIN CHECK
# =========================

@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def check_join(call):

    user_id = call.from_user.id

    try:
        ch1 = bot.get_chat_member(CHANNEL_1, user_id)
        ch2 = bot.get_chat_member(CHANNEL_2, user_id)

        if ch1.status in ['member', 'administrator', 'creator'] and ch2.status in ['member', 'administrator', 'creator']:

            users = load_users()
            users[str(user_id)]["joined"] = True
            save_users(users)

            loading = bot.edit_message_text(
                """
⚡ Initializing Secure System...

▓░░░░░░░░ 10%
                """,
                call.message.chat.id,
                call.message.message_id
            )

            time.sleep(1)

            bot.edit_message_text(
                """
⚡ Initializing Secure System...

▓▓▓▓░░░░░ 50%
                """,
                call.message.chat.id,
                call.message.message_id
            )

            time.sleep(1)

            keyboard = InlineKeyboardMarkup(row_width=2)

            keyboard.add(
                InlineKeyboardButton("🇮🇳 INDIA", callback_data="india"),
                InlineKeyboardButton("🇺🇸 USA", callback_data="usa")
            )

            keyboard.add(
                InlineKeyboardButton("🇬🇧 UK", callback_data="uk"),
                InlineKeyboardButton("🇨🇦 CANADA", callback_data="canada")
            )

            keyboard.add(
                InlineKeyboardButton("🇩🇪 GERMANY", callback_data="germany"),
                InlineKeyboardButton("🇫🇷 FRANCE", callback_data="france")
            )

            keyboard.add(
                InlineKeyboardButton("👤 My Profile", callback_data="profile")
            )

            text = f"""
╔════════════════════╗
      ✅ VERIFIED
╚════════════════════╝

👋 Welcome To {BOT_NAME}

🌍 Select Your Country
📲 Access Demo Numbers
⚡ Instant OTP Generator
🔒 Encrypted System Active
"""

            bot.edit_message_text(
                text,
                call.message.chat.id,
                call.message.message_id,
                reply_markup=keyboard
            )

        else:
            bot.answer_callback_query(
                call.id,
                "❌ Join all channels first!"
            )

    except:
        bot.answer_callback_query(
            call.id,
            "⚠️ Verification Failed"
        )


# =========================
# PROFILE
# =========================

@bot.callback_query_handler(func=lambda call: call.data == "profile")
def profile(call):

    users = load_users()

    user_id = str(call.from_user.id)

    points = users[user_id]["points"]

    referral_link = f"https://t.me/{bot.get_me().username}?start={user_id}"

    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        InlineKeyboardButton("🎁 Referral Rewards", callback_data="rewards")
    )

    keyboard.add(
        InlineKeyboardButton("🔙 Back", callback_data="back_home")
    )

    text = f"""
╔════════════════════╗
        👤 PROFILE
╚════════════════════╝

🆔 User ID : {user_id}
💎 Points : {points}

━━━━━━━━━━━━━━━━━━
🎁 Referral Link
━━━━━━━━━━━━━━━━━━

{referral_link}

👥 Invite Friends & Earn 5 Points
"""

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=keyboard
    )


# =========================
# REWARDS
# =========================

@bot.callback_query_handler(func=lambda call: call.data == "rewards")
def rewards(call):

    text = """
╔════════════════════╗
      🎁 REWARDS SYSTEM
╚════════════════════╝

👥 1 Referral = 5 Points
⚡ Generate OTP = 2 Points

━━━━━━━━━━━━━━━━━━
🏆 BONUS LEVELS
━━━━━━━━━━━━━━━━━━

🥉 50 Points = Bronze User
🥈 100 Points = Silver User
🥇 250 Points = Gold User
💎 500 Points = VIP User
"""

    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton("🔙 Back", callback_data="profile")
    )

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=keyboard
    )


# =========================
# COUNTRY SYSTEM
# =========================

@bot.callback_query_handler(func=lambda call: call.data in ['india','usa','uk','canada','germany','france'])
def country(call):

    numbers = []

    if call.data == "india":
        numbers = [
            "+91 9876543210",
            "+91 9123456780",
            "+91 9988776655",
            "+91 9090909090"
        ]

    elif call.data == "usa":
        numbers = [
            "+1 2025550101",
            "+1 2025550145",
            "+1 2025550199"
        ]

    elif call.data == "uk":
        numbers = [
            "+44 7700900111",
            "+44 7700900222"
        ]

    elif call.data == "canada":
        numbers = [
            "+1 6475551111",
            "+1 6475552222"
        ]

    elif call.data == "germany":
        numbers = [
            "+49 1512345678",
            "+49 1761234567"
        ]

    elif call.data == "france":
        numbers = [
            "+33 612345678",
            "+33 698765432"
        ]

    keyboard = InlineKeyboardMarkup(row_width=1)

    for num in numbers:
        keyboard.add(
            InlineKeyboardButton(
                f"📱 {num}",
                callback_data=f"otp_{num}"
            )
        )

    keyboard.add(
        InlineKeyboardButton("🔙 Back", callback_data="back_home")
    )

    text = f"""
╔════════════════════╗
      📲 ACTIVE NUMBERS
╚════════════════════╝

🌍 Country Selected Successfully
⚡ Choose Available Number
🔒 Secure Demo Verification
"""

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=keyboard
    )


# =========================
# OTP GENERATOR
# =========================

@bot.callback_query_handler(func=lambda call: call.data.startswith("otp_"))
def otp(call):

    users = load_users()

    user_id = str(call.from_user.id)

    users[user_id]["points"] += 2

    save_users(users)

    fakeotp = random.randint(100000, 999999)

    bot.edit_message_text(
        """
⚡ Connecting Secure Server...

▓▓▓▓▓▓▓░░ 80%
        """,
        call.message.chat.id,
        call.message.message_id
    )

    time.sleep(2)

    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        InlineKeyboardButton(
            "🔄 Generate New OTP",
            callback_data="newotp"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            "👤 My Profile",
            callback_data="profile"
        )
    )

    text = f"""
╔════════════════════╗
      ✅ OTP GENERATED
╚════════════════════╝

🔐 Demo OTP Code

━━━━━━━━━━━━━━━━━━
       {fakeotp}
━━━━━━━━━━━━━━━━━━

⚡ Status : SUCCESS
🌍 Server : ONLINE
🔒 Encryption : ACTIVE
💎 +2 Points Added
"""

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=keyboard
    )


# =========================
# NEW OTP
# =========================

@bot.callback_query_handler(func=lambda call: call.data == "newotp")
def newotp(call):

    fakeotp = random.randint(100000, 999999)

    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            "🔄 Generate Again",
            callback_data="newotp"
        )
    )

    text = f"""
╔════════════════════╗
        🔄 NEW OTP
╚════════════════════╝

⚡ Fresh OTP Generated

━━━━━━━━━━━━━━━━━━
       {fakeotp}
━━━━━━━━━━━━━━━━━━

🔒 Secure System Active
"""

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=keyboard
    )


# =========================
# BACK BUTTON
# =========================

@bot.callback_query_handler(func=lambda call: call.data == "back_home")
def back_home(call):

    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("🇮🇳 INDIA", callback_data="india"),
        InlineKeyboardButton("🇺🇸 USA", callback_data="usa")
    )

    keyboard.add(
        InlineKeyboardButton("🇬🇧 UK", callback_data="uk"),
        InlineKeyboardButton("🇨🇦 CANADA", callback_data="canada")
    )

    keyboard.add(
        InlineKeyboardButton("🇩🇪 GERMANY", callback_data="germany"),
        InlineKeyboardButton("🇫🇷 FRANCE", callback_data="france")
    )

    keyboard.add(
        InlineKeyboardButton("👤 My Profile", callback_data="profile")
    )

    text = f"""
╔════════════════════╗
      ⚡ {BOT_NAME}
╚════════════════════╝

🌍 Select Your Country
📲 Demo Numbers Available
⚡ Fast OTP Generator
"""

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=keyboard
    )


print("⚡ Modern Bot Running Successfully...")
bot.infinity_polling()