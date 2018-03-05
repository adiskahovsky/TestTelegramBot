# -*- coding: utf-8 -*-
import time
import telebot
import constants
import sqlite3
import os
import  random
import urllib.request as urllib2





test = "'" + 'Test' + "',"
test2 = "'" + 'Test2' + "'"

bot = telebot.TeleBot(constants.token)






def myupd(bot,text,text2):
    while text == text2 :
        text = bot.last_update_id                   #Функция по сравнению last_updaate_id
        time.sleep(0.3)







#----------------------------Команды----------------------------
@bot.message_handler(commands=['start'])
def handle_commands(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True,False)

    user_markup.row('Photo', 'Audio')
    user_markup.row('Interview')
    bot.send_message(message.chat.id,'Выберите команду',reply_markup=user_markup )







#----------------------------Текст----------------------------

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Interview':
        hide_markup = telebot.types.ReplyKeyboardRemove()
        text = bot.last_update_id
        bot.send_message(message.chat.id, constants.Key[0], reply_markup=hide_markup)

        text2 = bot.last_update_id
        myupd(bot,text,text2)
        text = bot.last_update_id
        bot.send_message(message.chat.id,constants.Key[1])

        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Photo', 'Audio')
        user_markup.row('Interview')
        text2 = bot.last_update_id
        myupd(bot, text, text2)

        bot.send_message(message.chat.id, constants.Key[2],reply_markup = user_markup)
        #----------------------------БД----------------------------
        Name = "'" + str(message.from_user.first_name) + "',"
        Surname = "'" + str(message.from_user.last_name) + "'"
        test=str(Name)
        test2=str(Surname)

        conn = sqlite3.connect('BotBD5.db')
        c = conn.cursor()
        def data_entry():

            print(test)
            print(test2)
            text = "INSERT INTO Interview VALUES("
            text2 = ")"

            c.execute(text + test + test2 + text2)
            conn.commit()
            c.close()
            conn.close()
        data_entry()

    elif message.text == 'Photo':
        directoryPh = 'photo/'
        all_files_in_directoryPh = os.listdir(directoryPh)
        random_filePh = random.choice(all_files_in_directoryPh)

        img = open(directoryPh+'/'+random_filePh,'rb')
        bot.send_chat_action(message.chat.id,'upload_photo')
        bot.send_photo(message.chat.id,img)
        img.close()

    elif message.text == 'Audio':
        directoryAu = 'audio/'
        all_files_in_directoryAu = os.listdir(directoryAu)
        random_fileAu = random.choice(all_files_in_directoryAu)

        au = open(directoryAu+'/'+random_fileAu,'rb')
        bot.send_chat_action(message.chat.id,'upload_audio')
        bot.send_audio(message.chat.id,au)







bot.polling(none_stop=True,interval=0)













