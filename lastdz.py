import requests
import telebot
from telebot import types
import sqlite3

connection = sqlite3.connect('PATH')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS CATS (
Cat_id TEXT,
Mark INTEGER
)
''')
connection.commit()
connection.close()
url = "https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=1"
api_key = 'YOUR API KEY'

TOKEN = 'YOUR TG TOKEN'
bot = telebot.TeleBot(TOKEN)

def catget():
    global x
    for i in range(5):
        request = requests.get(url,headers={'x_api_key':api_key}).json()
        if '-' not in request[0]['id']:
            id = request[0]['id']
            img = request[0]['url']
            x = [img,id]
            break

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text=='/start':
        catget()
        bot.send_message(message.from_user.id, 'Cat_ID: '+x[1])
        bot.send_photo(message.from_user.id,photo=x[0],parse_mode='html',reply_markup=keyboard())
    elif int(message.text) in range(1,11):
        connection = sqlite3.connect('PATH')
        cursor = connection.cursor()
        cursor.execute("Insert into CATS (Cat_id, Mark) VALUES (?, ?)", (x[1],int(message.text)))
        connection.commit()
        connection.close()
        catget()
        bot.send_message(message.from_user.id, 'Cat_ID: '+x[1])
        bot.send_photo(message.from_user.id,photo=x[0],parse_mode='html',reply_markup=keyboard())

def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('1')
    btn2 = types.KeyboardButton('2')
    btn3 = types.KeyboardButton('3')
    btn4 = types.KeyboardButton('4')
    btn5 = types.KeyboardButton('5')
    btn6 = types.KeyboardButton('6')
    btn7 = types.KeyboardButton('7')
    btn8 = types.KeyboardButton('8')
    btn9 = types.KeyboardButton('9')
    btn10 = types.KeyboardButton('10')
    markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10)
    return markup

bot.polling(none_stop=True, interval=0)


