from time import asctime
import requests
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackContext

admins = ["sevadp", "lajulienn"]
server = "http://193.178.169.224:5000/api/v1/parse/statistic?domain="


def get_metrics(domain="amazon.com"):
    headers = {"ADMIN": "not_real_secret_key"}
    data = requests.get(server + domain, headers=headers).json()["data"]
    if data == dict():
        return "Analyze Error"

    b = f'Статистика за последний месяц\n\n\tВсего визитов: {data["visits"]}\n\tВремя на сайте:' \
        f' {data["avg_time_onsite"]}' \
        f'\n\tСтраниц за визит: {data["pages_per_visit"]}\n\n\tГЕОГРАФИЯ\n\t'

    for i in data["best_geo"]:
        b += (i + " - " + data["best_geo"][i] + "\n\t")

    b += "\n\n\tИСТОЧНИКИ ТРАФИКА\n\t"
    names = {"banners": "Баннеры", "direct": "Прямой", "mails": "Почта",
             "referrals": "Рефералы", "search": "Поиск", "social": "Соц. сети"}
    for i in data["sources"]:
        b += (names[i] + " - " + data["sources"][i] + "\n\t")

    b += "\n\n\tРЕЙТИНГИ\n\t"
    for i in data["ratings"]:
        b += (i + " - " + data["ratings"][i] + "\n\t")

    return b


def help_bot(update: Update, context: CallbackContext):
    if update.message.from_user.username in admins:
        update.message.reply_text("Список команд:\n/metrics [domain] - Получить метрики по веб-сайту ")
    else:
        update.message.reply_text("Вы не являетесь администратором!")


def metrics(update: Update, context: CallbackContext):
    if update.message.from_user.username in admins:
        domain = update.message.text.split()[1]
        update.message.reply_text(get_metrics(domain))
    else:
        update.message.reply_text("Вы не являетесь администратором!")


def main():
    updater = Updater("1871457808:AAHIhLXZ0ywRB-ZX6cEc8_NyNEi6616VYP0", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("help", help_bot))
    dp.add_handler(CommandHandler("metrics", metrics))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()