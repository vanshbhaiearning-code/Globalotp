import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import time

TOKEN = "8479393909:AAF0ezFYoKMzO8xUNQqfsAmjlAp92zHuCi4"

ADMIN_ID = 6692986333

users = set()
broadcast_mode = {}

bot = telebot.TeleBot(TOKEN)

CHANNEL_1 = "@latestmodsapks"
CHANNEL_2 = "@latestmodsapp"

WELCOME_IMAGE = "https://i.ibb.co/9HYXy6Gt/file-000000000ad0720bad9aaa719ac271dd.png"

# ================= DEMO CODES =================

flipkart_codes = [
    ("6165789065431213", "981087"),
    ("0987543267895655", "878098"),
    ("1122398076564323", "115076"),
    ("1547745689006643", "654243"),
    ("5443422113247890", "082342"),
    ("6756907065438831", "550952"),
    ("3537890076543211", "948752"),
    ("6756188172891771", "676302"),
    ("0183736378181737", "842652"),
    ("9182736829198177", "327262")
]

amazon_codes = [
    ("AMAZ-7K2P-XQ9L-4MN8", "767872"),
    ("GIFT-3L9X-QP2N-7KD5", "901276"),
    ("AMZN-8P4L-MX7Q-2NT1", "769183"),
    ("SHOP-5Q2X-LN8P-4MK7", "878264"),
    ("CARD-9M7L-XP3Q-5KD2", "328264"),
    ("AMAZ-2N8Q-PL4X-7MT5", "428264"),
    ("PRIME-9Q3X-LK5P-2MN7", "768264"),
    ("GCODE-7M2L-XQ8P-4NT5", "978264"),
    ("AMGC-4P7L-MN2X-8QT1", "878264"),
    ("SAVE-6X1L-QP9N-3KD8", "668264")
]

play_codes = [
    "ABCDEFGHIJKLMNOP",
    "QWERTYUIOPASDFGH",
    "ZXCVBNMK-LQWERTYU",
    "PLMKOIJN-UHBYGTVF"
]

# ================= START =================

@bot.message_handler(commands=['start'])
def start(message):

    users.add(message.chat.id)

    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        InlineKeyboardButton(
            "📢 Join Channel",
            url=f"https://t.me/{CHANNEL_1.replace('@','')}"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            "🚀 Join Updates",
            url=f"https://t.me/{CHANNEL_2.replace('@','')}"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            "✅ Verify Access",
            callback_data="verify"
        )
    )

    caption = """
🎁 Welcome To ClaimKart Bot

⚡ Vouchers Gifts Code
🔒 Secure Access System
🎮 Easy To Use

📢 Join Channels To Continue
"""

    bot.send_photo(
        message.chat.id,
        WELCOME_IMAGE,
        caption=caption,
        reply_markup=keyboard
    )

# ================= VERIFY =================

@bot.callback_query_handler(func=lambda call: call.data == "verify")
def verify(call):

    user_id = call.from_user.id

    try:
        ch1 = bot.get_chat_member(CHANNEL_1, user_id)
        ch2 = bot.get_chat_member(CHANNEL_2, user_id)

        if ch1.status in ['member', 'administrator', 'creator'] and ch2.status in ['member', 'administrator', 'creator']:

            msg = bot.send_message(
                call.message.chat.id,
                """
🔄 Verifying User...

▓▓░░░░░░ 20%
"""
            )

            time.sleep(1)

            bot.edit_message_text(
                """
🔄 Verifying User...

▓▓▓▓▓░░░ 60%
""",
                call.message.chat.id,
                msg.message_id
            )

            time.sleep(1)

            bot.edit_message_text(
                """
✅ Verification Successful

▓▓▓▓▓▓▓▓ 100%
""",
                call.message.chat.id,
                msg.message_id
            )

            keyboard = InlineKeyboardMarkup(row_width=2)

            keyboard.add(
                InlineKeyboardButton(
                    "🎁 Get Voucher Codes",
                    callback_data="gifts"
                )
            )

            keyboard.add(
                InlineKeyboardButton(
                    "🎉 Daily Reward",
                    callback_data="daily"
                ),
                InlineKeyboardButton(
                    "👥 Refer & Earn",
                    callback_data="refer"
                )
            )
            keyboard.add(
    InlineKeyboardButton(
        "💎 Buy Subscription",
        callback_data="subscription"
    )
            )

            caption = """
🎉 Verification Successful

🎁 Welcome To ClaimKart Bot

🛒 Real Vouchers Gifts
🎮 Daily bonus: +1 Code every 24h
⚡ Flipkart, Amazon, Play Store Available

• 👥 Invite friends: +1 Point per referral
"""

            bot.send_photo(
                call.message.chat.id,
                WELCOME_IMAGE,
                caption=caption,
                reply_markup=keyboard
            )

        else:
            bot.answer_callback_query(
                call.id,
                "❌ Join all channels first"
            )

    except:
        bot.answer_callback_query(
            call.id,
            "⚠️ Verification Error"
        )

# ================= GIFT MENU =================

@bot.callback_query_handler(func=lambda call: call.data == "gifts")
def gifts(call):

    bot.send_message(
        call.message.chat.id,
        """
🎁 Opening Gift Center...
"""
    )

    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        InlineKeyboardButton(
            "🛒 Flipkart Voucher",
            callback_data="flipkart"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            "📦 Amazon Voucher",
            callback_data="amazon"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            "🎮 Redeem Code",
            callback_data="play"
        )
    )

    bot.send_photo(
        call.message.chat.id,
        WELCOME_IMAGE,
        caption="""
🎁 Select Gift Category
""",
        reply_markup=keyboard
    )

# ================= FLIPKART =================

@bot.callback_query_handler(func=lambda call: call.data == "flipkart")
def flipkart(call):

    code, pin = random.choice(flipkart_codes)

    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        InlineKeyboardButton(
            "🔄 Generate New",
            callback_data="flipkart"
        )
    )

    text = f"""
🛒 Flipkart Voucher

━━━━━━━━━━━━━━
Code : {code}
Pin  : {pin}
━━━━━━━━━━━━━━

⚠️ Refer & Earn Big Voucher Codes
"""

    bot.send_message(
        call.message.chat.id,
        text,
        reply_markup=keyboard
    )

# ================= AMAZON =================

@bot.callback_query_handler(func=lambda call: call.data == "amazon")
def amazon(call):

    code, pin = random.choice(amazon_codes)

    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        InlineKeyboardButton(
            "🔄 Generate New",
            callback_data="amazon"
        )
    )

    text = f"""
📦 Amazon Voucher

━━━━━━━━━━━━━━
Code : {code}
Pin  : {pin}
━━━━━━━━━━━━━━

⚠️ Refer & Earn Big Voucher Codes
"""

    bot.send_message(
        call.message.chat.id,
        text,
        reply_markup=keyboard
    )

# ================= PLAY STORE =================

@bot.callback_query_handler(func=lambda call: call.data == "play")
def play(call):

    code = random.choice(play_codes)

    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        InlineKeyboardButton(
            "🔄 Generate New",
            callback_data="play"
        )
    )

    text = f"""
🎮 Redeem Code

━━━━━━━━━━━━━━
{code}
━━━━━━━━━━━━━━

⚠️ Refer & Earn Big Voucher Codes
"""

    bot.send_message(
        call.message.chat.id,
        text,
        reply_markup=keyboard
    )

# ================= DAILY =================

@bot.callback_query_handler(func=lambda call: call.data == "daily")
def daily(call):

    bot.send_message(
        call.message.chat.id,
        """
🎉 Daily Reward Claimed

💎 +1 Points Added
"""
    )

# ================= REFER =================

@bot.callback_query_handler(func=lambda call: call.data == "refer")
def refer(call):

    username = bot.get_me().username

    link = f"https://t.me/{username}?start={call.from_user.id}"

    bot.send_message(
        call.message.chat.id,
        f"""
👥 Refer Friends & Earn

🔗 Your Referral Link:

{link}
"""
    )
# ================= SUBSCRIPTION =================

@bot.callback_query_handler(func=lambda call: call.data == "subscription")
def subscription(call):

    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton(
            "📅 1 Month ₹199",
            callback_data="sub_1month"
        ),
        InlineKeyboardButton(
            "♾ Lifetime ₹1000",
            callback_data="sub_lifetime"
        )
    )

    bot.send_message(
        call.message.chat.id,
        """
💎 Choose Subscription Plan

📅 1 Month = ₹199
♾ Lifetime = ₹1000

Get Earny access New Codes 🎁
""",
        reply_markup=keyboard
    )


# ================= 1 MONTH =================

@bot.callback_query_handler(func=lambda call: call.data == "sub_1month")
def sub_month(call):

    bot.answer_callback_query(call.id)

    try:

        bot.send_photo(
            call.message.chat.id,
            open("qr.jpg", "rb"),
            caption="""
💎 1 Month Subscription

💰 Amount : ₹199

🏦 UPI ID :
kathikathi@ptyes

━━━━━━━━━━━━━━

1️⃣ Scan QR Code

2️⃣ Pay ₹199

3️⃣ Send Screenshot Here

4️⃣ Wait For Admin Approval

━━━━━━━━━━━━━━
"""
        )

    except Exception as e:

        bot.send_message(
            call.message.chat.id,
            f"❌ Error:\n{e}"
        )

# ================= LIFETIME =================

@bot.callback_query_handler(func=lambda call: call.data == "sub_lifetime")
def sub_lifetime(call):

    bot.answer_callback_query(call.id)

    try:

        bot.send_photo(
            call.message.chat.id,
            open("qr.jpg", "rb"),
            caption="""
♾ Lifetime Subscription

💰 Amount : ₹1000

🏦 UPI ID :
kathikathi@ptyes

━━━━━━━━━━━━━━

1️⃣ Scan QR Code

2️⃣ Pay ₹1000

3️⃣ Send Screenshot Here

4️⃣ Wait For Admin Approval

━━━━━━━━━━━━━━
"""
        )

    except Exception as e:

        bot.send_message(
            call.message.chat.id,
            f"❌ Error:\n{e}"
        )



# ================= ADMIN PANEL =================

@bot.message_handler(commands=['panel'])
def panel(message):

    if message.from_user.id != ADMIN_ID:
        return

    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton(
            "📢 Broadcast",
            callback_data="broadcast"
        ),
        InlineKeyboardButton(
            "📊 Bot Stats",
            callback_data="stats"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            "👥 Total Users",
            callback_data="users"
        )
    )

    bot.send_message(
        message.chat.id,
        "⚙️ Admin Control Panel",
        reply_markup=keyboard
    )

# ================= TOTAL USERS =================

@bot.callback_query_handler(func=lambda call: call.data == "users")
def total_users(call):

    if call.from_user.id != ADMIN_ID:
        return

    bot.send_message(
        call.message.chat.id,
        f"👥 Total Users: {len(users)}"
    )

# ================= BOT STATS =================

@bot.callback_query_handler(func=lambda call: call.data == "stats")
def stats(call):

    if call.from_user.id != ADMIN_ID:
        return

    text = f'''
📊 Bot Statistics

👥 Users : {len(users)}

🟢 Status : Online
⚡ System : Active
'''

    bot.send_message(
        call.message.chat.id,
        text
    )

# ================= BROADCAST =================

@bot.callback_query_handler(func=lambda call: call.data == "broadcast")
def broadcast(call):

    if call.from_user.id != ADMIN_ID:
        return

    broadcast_mode[call.from_user.id] = True

    bot.send_message(
        call.message.chat.id,
        "📢 Send broadcast message now"
    )

# ================= ADMIN MESSAGE =================

@bot.message_handler(func=lambda m: m.from_user.id == ADMIN_ID)
def admin_messages(message):

    if broadcast_mode.get(message.from_user.id):

        success = 0

        for user in users:
            try:
                bot.send_message(user, message.text)
                success += 1
            except:
                pass

        broadcast_mode[message.from_user.id] = False

        bot.send_message(
            message.chat.id,
            f"✅ Broadcast sent to {success} users"
        )

# ================= APPROVE PAYMENT =================
@bot.message_handler(commands=['approve'])
def approve(message):
    ...

# ================= DECLINE PAYMENT =================
@bot.message_handler(commands=['decline'])
def decline(message):
    ...

# ================= PAYMENT SCREENSHOT =================
@bot.message_handler(content_types=['photo'])
def payment_screenshot(message):

    if message.from_user.id == ADMIN_ID:
        return

    caption = f"""
💰 New Payment Screenshot

👤 User : {message.from_user.first_name}
🆔 ID : {message.from_user.id}
"""

    bot.send_photo(
        ADMIN_ID,
        message.photo[-1].file_id,
        caption=caption
    )

    bot.reply_to(
        message,
        "✅ Screenshot received.\nWaiting for admin approval."
    )

        # ================= APPROVE PAYMENT =================

@bot.message_handler(commands=['approve'])
def approve(message):

    if message.from_user.id != ADMIN_ID:
        return

    try:
        user_id = int(message.text.split()[1])

        bot.send_message(
            user_id,
            """
✅ Payment Approved

💎 Subscription Activated Successfully.

Thank you for purchasing.
"""
        )

        bot.reply_to(
            message,
            f"✅ User {user_id} Approved Successfully"
        )

    except:
        bot.reply_to(
            message,
            "Use:\n/approve USER_ID"
        )

# ================= DECLINE PAYMENT =================

@bot.message_handler(commands=['decline'])
def decline(message):

    if message.from_user.id != ADMIN_ID:
        return

    try:
        user_id = int(message.text.split()[1])

        bot.send_message(
            user_id,
            "❌ Payment Declined\n\nPlease contact admin if payment was successful."
        )

        bot.reply_to(message, "Declined Successfully")

    except:
        bot.reply_to(message, "Use:\n/decline USER_ID")

bot.infinity_polling()
