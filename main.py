import os
import telebot

TOKEN = 8223605030:AAHJ_y9uckQPrWeHF4WKTqMUtQp1Gn3kjTY
bot = @Steven_coest_bot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 မင်္ဂလာပါ! Telegram Code Bot မှ ကြိုဆိုပါတယ်။\n`/check <code_number>` ဟု ရိုက်ပြီး စစ်ဆေးနိုင်ပါတယ်။", parse_mode="Markdown")

@bot.message_handler(commands=['check'])
def check_code(message):
    try:
        user_code = message.text.split()[1]
        bot.reply_to(message, f"🎯 **Code Result**\n• Code: `{user_code}`\n• Status: 🟢 Valid", parse_mode="Markdown")
    except IndexError:
        bot.reply_to(message, "⚠️ ကျေးဇူးပြု၍ Code နံပါတ် ထည့်ပါ။ ဥပမာ - `/check 785181`", parse_mode="Markdown")

bot.infinity_polling()
