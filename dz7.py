import logging
from aiogram import Bot, Dispatcher, executor, types


#уровень логов
logging.basicConfig(level=logging.INFO)

#инициализация
API_TOKEN=''
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#"""TelegramBot"""

@dp.message_handler(commands=['start'])
async def startbot(message: types.Message):
    await message.reply("Привет!")

@dp.message_handler(commands=['help'])
async def helpcom(message: types.Message):
    await message.reply("Я повторю за тобой и текст и скажу твой id!")

@dp.message_handler()
async def popugai(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text+', '+msg.from_user.id)



#Запускаем лог
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)