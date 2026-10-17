"""
Soroush Plus Bot — Full Featured Bot with Inline Keyboards
Created by DarkMaster using PYConnection SDK
"""

import json
import time
import threading
from pyconnection import PYConnectionClient


# ======================== CONFIG ========================
BOT_TOKEN = "YOUR_API_KEY"
API_BASE = f"https://api.splus.ir/bot{BOT_TOKEN}"

# Global client
client = PYConnectionClient(api_id=0, api_hash="", phone_number="")

# Track processed updates to avoid duplicates
processed_updates = set()
# ========================================================


def api_call(method: str, params: dict = None, files: dict = None) -> dict:
    """Call Soroush Plus Bot API method."""
    if params:
        # Filter out None values
        params = {k: v for k, v in params.items() if v is not None}
        r = client.http_post(f"{API_BASE}/{method}", json=params)
    else:
        r = client.http_post(f"{API_BASE}/{method}")
    return r.json()


# ==================== INLINE KEYBOARDS ====================

def kb_start_menu() -> dict:
    """Main menu inline keyboard."""
    return {
        "inline_keyboard": [
            [{"text": "📋 درباره بات", "callback_data": "about"}],
            [{"text": "📊 آمار", "callback_data": "stats"},
             {"text": "⚙️ تنظیمات", "callback_data": "settings"}],
            [{"text": "🎮 بازی", "callback_data": "game"},
             {"text": "📞 تماس", "callback_data": "contact"}],
            [{"text": "🌐 لینک سایت", "url": "https://splus.ir"}],
        ]
    }


def kb_back_menu() -> dict:
    """Back button keyboard."""
    return {
        "inline_keyboard": [
            [{"text": "🔙 بازگشت به منو", "callback_data": "back"}]
        ]
    }


def kb_game_menu() -> dict:
    """Game selection keyboard."""
    return {
        "inline_keyboard": [
            [{"text": "🎯 تاس انداختن", "callback_data": "roll_dice"},
             {"text": "🎲 عدد تصادفی", "callback_data": "random_num"}],
            [{"text": "🪨📂✂️ سنگ-کاغذ-قیچی", "callback_data": "rps"}],
            [{"text": "🔙 بازگشت", "callback_data": "back"}],
        ]
    }


def kb_rps_menu() -> dict:
    """Rock-Paper-Scissors keyboard."""
    return {
        "inline_keyboard": [
            [{"text": "🪨 سنگ", "callback_data": "rps_rock"},
             {"text": "📂 کاغذ", "callback_data": "rps_paper"},
             {"text": "✂️ قیچی", "callback_data": "rps_scissors"}],
            [{"text": "🔙 بازگشت به بازی‌ها", "callback_data": "game"}],
        ]
    }


def kb_settings_menu() -> dict:
    """Settings keyboard."""
    return {
        "inline_keyboard": [
            [{"text": "🔹 زبان: فارسی", "callback_data": "lang_fa"},
             {"text": "🔸 زبان: English", "callback_data": "lang_en"}],
            [{"text": "🔔 اعلان‌ها: فعال", "callback_data": "notif_on"}],
            [{"text": "🔕 اعلان‌ها: غیرفعال", "callback_data": "notif_off"}],
            [{"text": "🔙 بازگشت", "callback_data": "back"}],
        ]
    }


# ==================== BOT LOGIC ====================

def handle_start(chat_id, message_id=None):
    """Handle /start command."""
    text = (
        "🎋 **به بات سروش پلاس خوش آمدید!**\n\n"
        "این بات توسط **DarkMaster** ساخته شده است.\n\n"
        "🔹 از دکمه‌های زیر استفاده کنید:\n\n"
        "📋 `درباره بات` — اطلاعات بیشتر\n"
        "📊 `آمار` — آمار بات\n"
        "🎮 `بازی` — بازی‌های سرگرم‌کننده\n"
        "⚙️ `تنظیمات` — شخصی‌سازی\n\n"
        "📝 برای شروع از منوی زیر استفاده کنید:"
    )
    api_call("sendMessage", {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "reply_markup": kb_start_menu(),
    })


def handle_about(chat_id, message_id=None):
    """Handle about callback."""
    text = (
        "🤖 **درباره این بات**\n\n"
        "📛 نام: DarkBot\n"
        "👨‍💻 سازنده: DarkMaster\n"
        "📆 نسخه: 2.0.0\n"
        "📚 کتابخانه: PYConnection (spluslib + requests)\n\n"
        "🔹 قابلیت‌ها:\n"
        "• پاسخ به پیام‌ها\n"
        "• Inline Keyboard\n"
        "• بازی‌های تعاملی\n"
        "• مدیریت تنظیمات"
    )
    api_call("sendMessage", {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "reply_markup": kb_back_menu(),
    })


def handle_stats(chat_id, message_id=None):
    """Handle stats callback."""
    text = (
        "📊 **آمار بات**\n\n"
        "👥 کاربران: 1,234\n"
        "💬 پیام‌ها امروز: 5,678\n"
        "⏱️ آپ‌تایم: 99.9%\n"
        "🖥️ سرور: ایران\n"
        "📡 پاسخ در: ۰.۵ ثانیه"
    )
    api_call("sendMessage", {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "reply_markup": kb_back_menu(),
    })


def handle_settings(chat_id, message_id=None):
    """Handle settings callback."""
    text = "⚙️ **تنظیمات بات**\n\nاز گزینه‌های زیر انتخاب کنید:"
    api_call("sendMessage", {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "reply_markup": kb_settings_menu(),
    })


def handle_game(chat_id, message_id=None):
    """Handle game callback."""
    text = "🎮 **بازی‌ها**\n\nیکی از بازی‌های زیر رو انتخاب کن:"
    api_call("sendMessage", {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "reply_markup": kb_game_menu(),
    })


def handle_rps(chat_id, message_id=None):
    """Handle rock-paper-scissors game."""
    text = "🪨📂✂️ **سنگ، کاغذ، قیچی**\n\nانتخاب کن:"
    api_call("sendMessage", {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "reply_markup": kb_rps_menu(),
    })


def handle_roll_dice(chat_id, message_id=None):
    """Roll a dice."""
    import random
    dice = random.randint(1, 6)
    dice_faces = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
    text = f"🎯 **تاس انداختی!**\n\n{dice_faces.get(dice, dice)} عدد: **{dice}**\n\nدوباره تاس بنداز یا برگرد:"
    api_call("sendMessage", {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "reply_markup": {
            "inline_keyboard": [
                [{"text": "🎯 دوباره!", "callback_data": "roll_dice"}],
                [{"text": "🔙 بازگشت به بازی‌ها", "callback_data": "game"}],
            ]
        },
    })


def handle_random_num(chat_id, message_id=None):
    """Generate random number."""
    import random
    num = random.randint(1, 100)
    text = (
        f"🎲 **عدد تصادفی**\n\n"
        f"عدد شما: **{num}**\n\n"
        f"🍀 شانس بخت رو بسنج!"
    )
    api_call("sendMessage", {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "reply_markup": {
            "inline_keyboard": [
                [{"text": "🎲 عدد جدید", "callback_data": "random_num"}],
                [{"text": "🔙 بازگشت به بازی‌ها", "callback_data": "game"}],
            ]
        },
    })


def handle_rps_choice(chat_id, choice, message_id=None):
    """Handle rock-paper-scissors choice."""
    import random
    choices = ["rock", "paper", "scissors"]
    choice_fa = {"rock": "🪨 سنگ", "paper": "📂 کاغذ", "scissors": "✂️ قیچی"}
    bot_choice = random.choice(choices)

    user_emoji = choice_fa.get(choice, choice)
    bot_emoji = choice_fa.get(bot_choice, bot_choice)

    # Determine winner
    if choice == bot_choice:
        result = "🤝 **مساوی!**"
    elif (choice == "rock" and bot_choice == "scissors") or \
         (choice == "paper" and bot_choice == "rock") or \
         (choice == "scissors" and bot_choice == "paper"):
        result = "🎉 **بردی!**"
    else:
        result = "😅 **باختی!**"

    text = (
        f"🪨📂✂️ **سنگ، کاغذ، قیچی**\n\n"
        f"شما: {user_emoji}\n"
        f"بات: {bot_emoji}\n\n"
        f"{result}\n\n"
        f"دوباره بازی کن یا برگرد:"
    )
    api_call("sendMessage", {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "reply_markup": {
            "inline_keyboard": [
                [{"text": "🪨 سنگ", "callback_data": "rps_rock"},
                 {"text": "📂 کاغذ", "callback_data": "rps_paper"},
                 {"text": "✂️ قیچی", "callback_data": "rps_scissors"}],
                [{"text": "🔙 بازگشت", "callback_data": "game"}],
            ]
        },
    })


def handle_contact(chat_id, message_id=None):
    """Handle contact callback."""
    text = (
        "📞 **تماس با ما**\n\n"
        "🌐 وب‌سایت: [splus.ir](https://splus.ir)\n"
        "📧 ایمیل: support@splus.ir\n"
        "📱 تلفن: ۰۲۱-۱۲۳۴۵۶۷۸\n\n"
        "🌐 [لینک کانال ما](https://splus.ir)"
    )
    api_call("sendMessage", {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False,
        "reply_markup": {
            "inline_keyboard": [
                [{"text": "🌐 سایت سروش پلاس", "url": "https://splus.ir"}],
                [{"text": "🔙 بازگشت", "callback_data": "back"}],
            ]
        },
    })


# ==================== CALLBACK ROUTER ====================

def handle_callback(callback_query: dict):
    """Route callback queries to appropriate handlers."""
    query_id = callback_query["id"]
    data = callback_query.get("data", "")
    message = callback_query.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    message_id = message.get("message_id")

    # Always answer the callback first
    api_call("answerCallbackQuery", {"callback_query_id": query_id})

    if data == "about":
        handle_about(chat_id)
    elif data == "stats":
        handle_stats(chat_id)
    elif data == "settings":
        handle_settings(chat_id)
    elif data == "game":
        handle_game(chat_id)
    elif data == "contact":
        handle_contact(chat_id)
    elif data == "rps":
        handle_rps(chat_id)
    elif data == "roll_dice":
        handle_roll_dice(chat_id)
    elif data == "random_num":
        handle_random_num(chat_id)
    elif data == "rps_rock":
        handle_rps_choice(chat_id, "rock")
    elif data == "rps_paper":
        handle_rps_choice(chat_id, "paper")
    elif data == "rps_scissors":
        handle_rps_choice(chat_id, "scissors")
    elif data == "back":
        handle_start(chat_id)
    elif data == "lang_fa":
        api_call("sendMessage", {"chat_id": chat_id, "text": "✅ زبان فارسی انتخاب شد!"})
    elif data == "lang_en":
        api_call("sendMessage", {"chat_id": chat_id, "text": "✅ English selected!"})
    elif data == "notif_on":
        api_call("sendMessage", {"chat_id": chat_id, "text": "🔔 اعلان‌ها فعال شد!"})
    elif data == "notif_off":
        api_call("sendMessage", {"chat_id": chat_id, "text": "🔕 اعلان‌ها غیرفعال شد!"})
    else:
        api_call("sendMessage", {"chat_id": chat_id, "text": f"❓ دستور ناشناخته: {data}"})


def handle_message(message: dict):
    """Handle incoming messages."""
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "")

    if text == "/start":
        handle_start(chat_id)
    elif text == "/help":
        handle_start(chat_id)
    elif text == "/menu":
        handle_start(chat_id)
    elif text == "/about":
        handle_about(chat_id)
    elif text == "/game":
        handle_game(chat_id)
    elif text == "/stats":
        handle_stats(chat_id)
    else:
        # Echo with keyboard
        api_call("sendMessage", {
            "chat_id": chat_id,
            "text": (
                f"🗣️ **پیام شما:**\n\n{text}\n\n"
                "🔹 از `/start` برای شروع استفاده کنید\n"
                "🔹 از `/game` برای بازی‌ها استفاده کنید"
            ),
            "parse_mode": "Markdown",
            "reply_markup": kb_start_menu(),
        })


# ==================== MAIN LOOP ====================

def get_updates(offset: int = 0):
    """Get updates using long polling."""
    result = api_call("getUpdates", {"offset": offset, "timeout": 30, "limit": 100})
    return result.get("result", [])


def process_update(update: dict):
    """Process a single update."""
    update_id = update.get("update_id")

    if update_id in processed_updates:
        return update_id + 1
    processed_updates.add(update_id)

    # Handle callback queries
    if "callback_query" in update:
        handle_callback(update["callback_query"])

    # Handle messages
    elif "message" in update:
        handle_message(update["message"])

    return update_id + 1


def main():
    """Main bot loop."""
    print("=" * 50)
    print("🤖 Soroush Plus Bot Started!")
    print("👨‍💻 Created by: DarkMaster")
    print("📚 Using: PYConnection SDK")
    print("=" * 50)
    print("⏳ Waiting for updates...\n")

    offset = 0
    while True:
        try:
            updates = get_updates(offset)
            for update in updates:
                offset = process_update(update)
        except KeyboardInterrupt:
            print("\n🛑 Bot stopped.")
            break
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(1)


if __name__ == "__main__":
    main()
