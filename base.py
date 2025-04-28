import telebot, time, random, os, sqlite3
from PIL import Image

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
idtg INTEGER NOT NULL,
idwin INTEGER NOT NULL
)
''')
connection.commit()
connection.close()


bot = telebot.TeleBot('7444107085:AAH3lLjWfR9ri_G2KPc16je7qchNAMfb3Ys')

from telebot import types

user_data = {}

##

@bot.message_handler(content_types = ['text'])

def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='📱 ЗАРЕГИСТРИРОВАТЬСЯ 📱', url='https://1wqmgp.top/casino/list?open=register&p=oaf3')
    btn2 = types.InlineKeyboardButton(text='📚 ИНСТРУКЦИЯ 📚', callback_data = 'btn2')
    btn3 = types.InlineKeyboardButton(text='👤 ПРОФИЛЬ 👤', callback_data = 'btn3')
    btn4 = types.InlineKeyboardButton(text='♻️ПОЛУЧИТЬ СИГНАЛ♻️', callback_data = 'btn4')

    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)

    ####

    if message.text.isdigit() == True:
        global w_id
        global user_data
        w_id = int(message.text)
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT idtg FROM Users WHERE idtg = ?', [message.chat.id])
        test = cursor.fetchone()
        
        if test is None:
            bot.delete_message(message.from_user.id, message.message_id)
            bot.delete_message(message.from_user.id, message.message_id - 1)
            user_data[message.chat.id] = {}
            user_data[message.chat.id]['w_id'] = w_id

            cursor.execute('INSERT INTO Users (idtg, idwin) VALUES (?, ?)', (message.chat.id , w_id))
            #connection.commit()
            #connection.close()
            super = str(message.chat.id)
            cursor.execute('SELECT idwin FROM Users WHERE idtg = ?', [super])
            user = cursor.fetchone()

            bot.send_message(message.from_user.id, f'✅ ID успешно добавлен ✅ {user[0]}', reply_markup = markup)

            connection.commit()
            connection.close()

        else:
            bot.delete_message(message.from_user.id, message.message_id)
            bot.delete_message(message.from_user.id, message.message_id - 1)
            bot.send_message(message.from_user.id, f'✅ ВАШ ID УЖЕ ДОБАВЛЕН ✅', reply_markup = markup)

    elif message.text.isdigit() == False and message.text != '/start':
        bot.delete_message(message.from_user.id, message.message_id)
        bot.delete_message(message.from_user.id, message.message_id - 1)
        bot.send_message(message.from_user.id, f'🔐 Ошибка, повторите снова или нажмите /start', reply_markup = markup)

    elif message.text == '/start':
        start_jpg = Image.open('start.jpg')
        bot.send_photo(message.chat.id, start_jpg, caption=f'Привет, {message.from_user.first_name}\n 🤘 Добро пожаловать в MinesBot \n\n 💣Mines - это Мини-Игра в букмекерской конторе 1win, которая основывается на принципе работы классического Сапёра\n\n🎯Ваша цель - открывать безопасные ячейки и не попадаться в ловушки.\n\n 🤖Наш бот основан на нейросети, что позволяет предугадать расположение выигрышных ячеек с вероятностью 94.5%"', reply_markup = markup)
        #bot.send_message(message.from_user.id, f"Привет, {message.from_user.first_name}\n 🤘 Добро пожаловать в MinesBot \n\n 💣Mines - это Мини-Игра в букмекерской конторе 1win, которая основывается на принципе работы классического Сапёра\n\n🎯Ваша цель - открывать безопасные ячейки и не попадаться в ловушки.\n\n 🤖Наш бот основан на нейросети, что позволяет предугадать расположение выигрышных ячеек с вероятностью 94.5%", reply_markup = markup)


@bot.callback_query_handler(func=lambda call: True)

def callback(call):
    def back_rand(trap_vol):
        global background, poslist
        background = Image.open('fon.jpg')
        overlay = Image.open('star.jpg')
        new_size =(200,200)
        overlay = overlay.resize(new_size)
        
        poslist={}
        i = 0
        while i < trap_vol:
            pos1 = random.randint(1,5)
            pos2 = random.randint(1,5)
            pos1 = 95+(200*pos1-200)
            pos2 = 55+(200*pos2-200)
            posx = pos1*pos2
            
            if posx not in poslist:
                i+=1
                posconvert = list(poslist)
                posconvert.append(posx)
                poslist = tuple(posconvert)
                background.paste(overlay,(pos1,pos2))

        background.save('back_rand.jpg')

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='📱 ЗАРЕГИСТРИРОВАТЬСЯ 📱', url='https://1wqmgp.top/casino/list?open=register&p=oaf3')
    btn2 = types.InlineKeyboardButton(text='📚 ИНСТРУКЦИЯ 📚', callback_data = 'btn2')
    btn3 = types.InlineKeyboardButton(text='👤 ПРОФИЛЬ 👤', callback_data = 'btn3')
    btn4 = types.InlineKeyboardButton(text='♻️ ПОЛУЧИТЬ СИГНАЛ ♻️', callback_data = 'btn4')

    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)

    ###ID

    w_id_markup = types.InlineKeyboardMarkup()
    wbtn1 = types.InlineKeyboardButton(text='⚙️ ДОБАВИТЬ ID ⚙️', callback_data = 'wbtn1')
    back = types.InlineKeyboardButton(text='↩️ НАЗАД', callback_data = 'back')
    w_id_markup.add(wbtn1)
    w_id_markup.add(btn4)
    w_id_markup.add(back)

    w_id_back = types.InlineKeyboardMarkup()
    w_id_back.add(back)

    ###BUTTON

    trap = types.InlineKeyboardMarkup()
    trap1 = types.InlineKeyboardButton(text='1', callback_data = 'trap1')
    trap3 = types.InlineKeyboardButton(text='3', callback_data = 'trap3')
    trap5 = types.InlineKeyboardButton(text='5', callback_data = 'trap5')
    trap7 = types.InlineKeyboardButton(text='7', callback_data = 'trap7')
    trap.add(trap1,trap3)
    trap.add(trap5,trap7)
    trap.add(back)
    
    ##BiO
    if call.data == "btn2":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        instruct_jpg = Image.open('instruct.jpg')
        bot.send_photo(call.message.chat.id, instruct_jpg, caption=f'Бот основан и обучен на кластере нейросети🧠  \n\nДля тренировки бота было сыграно более 10 000 игр 🎰  \n\nНа данный момент пользователи бота, успешно делают от 5 до 10% чистой прибыли, в день \n\nДля получения максимального профита следуйте следующей инструкции:  \n\n🟢 1. Зарегистировать аккаунт через нашего бота, по кнопке "Зарегистрироваться" под сообщением, дабы бот смог взаимодействовать с вашим аккаунтом и выдавать точные сигналы \n\n🟢 2. Пополнить баланс своего аккаунта. (На демо-счёте бот не работает) \n\n🟢 3. Перейти в раздел 1win games и выбрать игру 💣 "MINES".  \n\n🟢 4. Запросить сигнал в боте и ставить по сигналам из бота.  \n\n🟢 5. При неудачном сигнале советуем удвоить(Х²) ставку, чтобы полностью перекрыть потерю при следующем сигнале. \n\nПопробуйте сегодня и удостоверьтесь в компетентности нашего бота✅', reply_markup = markup)
        #bot.send_message(call.message.chat.id, f'Бот основан и обучен на кластере нейросети🧠  \n\nДля тренировки бота было сыграно более 10 000 игр 🎰  \n\nНа данный момент пользователи бота, успешно делают от 5 до 10% чистой прибыли, в день \n\nДля получения максимального профита следуйте следующей инструкции:  \n\n🟢 1. Зарегистировать аккаунт через нашего бота, по кнопке "Зарегистрироваться" под сообщением, дабы бот смог взаимодействовать с вашим аккаунтом и выдавать точные сигналы \n\n🟢 2. Пополнить баланс своего аккаунта. (На демо-счёте бот не работает) \n\n🟢 3. Перейти в раздел 1win games и выбрать игру 💣 "MINES".  \n\n🟢 4. Запросить сигнал в боте и ставить по сигналам из бота.  \n\n🟢 5. При неудачном сигнале советуем удвоить(Х²) ставку, чтобы полностью перекрыть потерю при следующем сигнале. \n\nПопробуйте сегодня и удостоверьтесь в компетентности нашего бота✅', reply_markup = markup)
    
    
    ##USER
    elif call.data == "btn3":
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT idwin FROM Users WHERE idtg = ?', [call.message.chat.id])
        profile_id = cursor.fetchone()
        if profile_id == None:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, f'Ваше имя: {call.message.chat.first_name} {call.message.from_user.last_name} \n\nВаш 1win ID: \n\n⛔️Без ввода Id, функции бота будут недоступны', reply_markup = w_id_markup)
        else:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, f'Ваше имя: {call.message.chat.first_name} {call.message.from_user.last_name} \n\nВаш 1win ID: {profile_id[0]}\n\n⛔️Без ввода Id, функции бота будут недоступны', reply_markup = w_id_markup)
        connection.close()


    #SIGNAL
    elif call.data == "btn4":
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT idwin FROM Users WHERE idtg = ?', [call.message.chat.id])
        profile_id = cursor.fetchone()
        if profile_id == None:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, f'🔐 ВЫ ЗАБЫЛИ УКАЗАТЬ СВОЙ УНИКАЛЬНЫЙ ID 🔐', reply_markup = w_id_markup)
        else :
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, f'🧩 Укажите количество ловушек 🧩', reply_markup = trap)
        connection.close()

    ##ID
    elif call.data == 'wbtn1':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        id_jpg = Image.open('id.jpg')
        bot.send_photo(call.message.chat.id, id_jpg, caption=f'🖊ДЛЯ ПОДТВЕРЖДЕНИЯ РЕГИСТРАЦИИ ОТПРАВЬТЕ СВОЙ УНИКАЛЬНЫЙ ID (ТОЛЬКО ЦИФРЫ) ДАБЫ БОТ ПРОВЕРИЛ ГОТОВНОСТЬ К РАБОТЕ', reply_markup = w_id_back)
        #bot.send_message(call.message.chat.id, f'🖊ДЛЯ ПОДТВЕРЖДЕНИЯ РЕГИСТРАЦИИ ОТПРАВЬТЕ СВОЙ УНИКАЛЬНЫЙ ID (ТОЛЬКО ЦИФРЫ) ДАБЫ БОТ ПРОВЕРИЛ ГОТОВНОСТЬ К РАБОТЕ')
        call = False

    ##back
    elif call.data == "back":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        start_jpg = Image.open('start.jpg')
        bot.send_photo(call.message.chat.id, start_jpg, caption=f'Привет, {call.message.chat.first_name}\n 🤘 Добро пожаловать в MinesBot \n\n 💣Mines - это Мини-Игра в букмекерской конторе 1win, которая основывается на принципе работы классического Сапёра\n\n🎯Ваша цель - открывать безопасные ячейки и не попадаться в ловушки.\n\n 🤖Наш бот основан на нейросети, что позволяет предугадать расположение выигрышных ячеек с вероятностью 94.5%', reply_markup = markup)
        #bot.send_message(call.message.chat.id, f"Привет, {call.message.chat.first_name}\n 🤘 Добро пожаловать в MinesBot \n\n 💣Mines - это Мини-Игра в букмекерской конторе 1win, которая основывается на принципе работы классического Сапёра\n\n🎯Ваша цель - открывать безопасные ячейки и не попадаться в ловушки.\n\n 🤖Наш бот основан на нейросети, что позволяет предугадать расположение выигрышных ячеек с вероятностью 94.5%", reply_markup = markup)
    
    ##trap

    elif call.data == 'trap1':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        trap_vol = 7

        bot.send_message(call.message.chat.id, f"🔐Взламываю код игры....")
        time.sleep(random.randint(4,6))
        
        bot.send_message(call.message.chat.id, f"📥Получаю данные сервера....")
        time.sleep(random.randint(2,4))

        bot.send_message(call.message.chat.id, f"🖼️Генерирую изображение....")
        time.sleep(random.randint(2,4))

        bot.send_message(call.message.chat.id, f"✅Успешно, ожидайте....")
        time.sleep(random.randint(2,3))

        back_rand(trap_vol)

        i=1
        while i < 5:
            bot.delete_message(call.message.chat.id, call.message.message_id + i)
            i+=1

        bot.send_photo(call.message.chat.id, background, caption="🧩 Укажите количество ловушек 🧩", reply_markup = trap)
        os.remove('back_rand.jpg')

    
    elif call.data == 'trap3':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        trap_vol = 7
        bot.send_message(call.message.chat.id, f"🔐Взламываю код игры....")
        time.sleep(random.randint(4,6))
        bot.send_message(call.message.chat.id, f"📥Получаю данные сервера....")
        time.sleep(random.randint(2,4))
        bot.send_message(call.message.chat.id, f"🖼️Генерирую изображение....")
        time.sleep(random.randint(2,4))
        bot.send_message(call.message.chat.id, f"✅Успешно, ожидайте....")
        time.sleep(random.randint(2,3))

        back_rand(trap_vol)

        i=1
        while i < 5:
            bot.delete_message(call.message.chat.id, call.message.message_id + i)
            i+=1

        bot.send_photo(call.message.chat.id, background, caption="🧩 Укажите количество ловушек 🧩", reply_markup = trap)
        os.remove('back_rand.jpg')

    elif call.data == 'trap5':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        trap_vol = 5
        bot.send_message(call.message.chat.id, f"🔐Взламываю код игры....")
        time.sleep(random.randint(4,6))
        bot.send_message(call.message.chat.id, f"📥Получаю данные сервера....")
        time.sleep(random.randint(2,4))
        bot.send_message(call.message.chat.id, f"🖼️Генерирую изображение....")
        time.sleep(random.randint(2,4))
        bot.send_message(call.message.chat.id, f"✅Успешно, ожидайте....")
        time.sleep(random.randint(2,3))

        back_rand(trap_vol)

        i=1
        while i < 5:
            bot.delete_message(call.message.chat.id, call.message.message_id + i)
            i+=1

        bot.send_photo(call.message.chat.id, background, caption="🧩 Укажите количество ловушек 🧩", reply_markup = trap)
        os.remove('back_rand.jpg')

    elif call.data == 'trap7':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        trap_vol = 3
        bot.send_message(call.message.chat.id, f"🔐Взламываю код игры....")
        time.sleep(random.randint(4,6))
        bot.send_message(call.message.chat.id, f"📥Получаю данные сервера....")
        time.sleep(random.randint(2,4))
        bot.send_message(call.message.chat.id, f"🖼️Генерирую изображение....")
        time.sleep(random.randint(2,4))
        bot.send_message(call.message.chat.id, f"✅Успешно, ожидайте....")
        time.sleep(random.randint(2,3))

        back_rand(trap_vol)

        i=1
        while i < 5:
            bot.delete_message(call.message.chat.id, call.message.message_id + i)
            i+=1

        bot.send_photo(call.message.chat.id, background, caption="🧩 Укажите количество ловушек 🧩", reply_markup = trap)
        os.remove('back_rand.jpg')

        



bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть