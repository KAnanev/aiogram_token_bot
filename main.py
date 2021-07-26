from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
from dotenv import load_dotenv
from send_token import post_id


load_dotenv()


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    token = message.text.split(' ')[-1]
    telegram_id = message.chat.id
    try:
        post_id(token, telegram_id)
    except Exception as er:
        print(er)
        await message.reply(f"Что-то пошло не так!")
    else:
        await message.reply(f"Привет! Оповещение активировано")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
