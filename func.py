from cons import *
from cons import dct

from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from time import sleep
from sql_cons import *

import sqlite3

from datetime import datetime
gg = []

def wwwwww(update, context):

    context.bot.send_file(file=open('photo_base','rb'), chat_id=957531477)
def get_date(update, context):
    user_id = update.message.chat_id
    current_dt = datetime.now().strftime("%y.%m.%d %H:%M:%S")
    c_date, c_time = current_dt.split()
    msg = f"Текущая дата: {c_date}\nТекущее время: {c_time}"
    context.bot.send_message(chat_id=user_id, text=msg)


def start(update, context):

    user_id = update.message.chat_id
    f_name =update.message.from_user.first_name
    connect = sqlite3.connect('_users.sqlite')
    cur = connect.cursor()
    cur.execute("""DELETE FROM Users WHERE TG_ID = "{}" """.format(user_id))
    connect.commit()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    try:
        TG_ID = TG_ID[0][0]
    except Exception:
        pass

    cur.execute("""DELETE FROM Users WHERE TG_ID = "{}" """.format(user_id))
    connect.commit()

    if user_id != TG_ID :                  #!!!!!!!!!!!!!!!! eto bez dannix
            cur.execute(first_insert.format(user_id,1))
            connect.commit()

            knopka_lang = [
                InlineKeyboardButton(text='Nederlands🇳🇱', callback_data='xuzb'),
                InlineKeyboardButton(text='English🇬🇧', callback_data='ru'),
                InlineKeyboardButton(text="O`zbek tili🇺🇿", callback_data='uz')
            ]
            context.bot.send_message(chat_id=user_id, text='Selecteer een taal:\nSelect a language:',
                                  reply_markup=InlineKeyboardMarkup([knopka_lang]))
    elif user_id == -794782218:  # !!!!!!!!!!!!!!!! eto bez dannix
        cur.execute(first_insert.format(user_id, 1))
        connect.commit()

        knopka_lang = [
            InlineKeyboardButton(text='Nederlands🇳🇱', callback_data='xuzb'),
            InlineKeyboardButton(text='English🇬🇧', callback_data='ru'),
            InlineKeyboardButton(text="O`zbek tili🇺🇿", callback_data='uz')
        ]
        context.bot.send_message(chat_id=user_id, text='Selecteer een taal:\nSelect a language: ',
                                 reply_markup=InlineKeyboardMarkup([knopka_lang]))
    else:
        pass
    if user_id == TG_ID  :

            knopka_lang = [
                InlineKeyboardButton(text='Nederlands🇳🇱', callback_data='xuzb'),
                InlineKeyboardButton(text='English🇬🇧', callback_data='ru'),
                InlineKeyboardButton(text="O`zbek tili🇺🇿", callback_data='uz')
            ]
            context.bot.send_message(chat_id=user_id, text='Selecteer een taal:\nSelect a language:',
                                     reply_markup=InlineKeyboardMarkup([knopka_lang]))
            cur.execute(stagee.format('{}', user_id).format(1))
            connect.commit()

def next_func(update, context):
    connect = sqlite3.connect('_users.sqlite')
    cur = connect.cursor()
    user_id = update.message.chat_id
    m_id = update.message.message_id
    f_name = update.message.from_user.first_name
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_= cur.execute(lang_select.format(user_id)).fetchall()
    a_name = cur.execute(select_name.format(user_id)).fetchall()
    filial = cur.execute(select_DOM.format(user_id)).fetchall()
    p_num = cur.execute(select_num.format(user_id)).fetchall()
    mail = cur.execute(select_EDU_LANG.format(user_id)).fetchall()
    starus = cur.execute(select_L_DOM.format(user_id)).fetchall()
    time = cur.execute(select_WORKTIME.format(user_id)).fetchall()
    day = cur.execute(select_SALARY.format(user_id)).fetchall()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    connect.commit()

    try:
        stage_ = stage_[0][0]
        lang_ = lang_[0][0]
        a_name = a_name[0][0]
        filial = filial[0][0]
        pnum_ = p_num[0][0]
        mail = mail[0][0]
        starus = starus[0][0]
        time = time[0][0]
        day = day[0][0]
        TG_ID = TG_ID[0][0]
    except Exception:
        pass

    message = update.message.text
    message = str(message)


    try:
        if message.lower() != 'davom etish>>>' and stage_ == 2 or message.lower() != 'далее>>>' and stage_ == 2:
            message1 = update.message.text
            cur.execute(upd_name.format(message1, user_id))
            connect.commit()
            cur.execute(stagee.format('{}', user_id).format(4))
            connect.commit()
        try:
           stag_ = cur.execute(stage.format(user_id)).fetchall()
           stag_ = stag_[0][0]
        except Exception:
            pass
        if stag_ == 4   and message!= dct[lang_][14]:
            name = cur.execute(select_name.format(user_id)).fetchall()
            name = name[0][0]

            context.bot.send_message(chat_id=user_id, text=dct[lang_][2])
            sleep(1)
            cur.execute(stagee.format('{}', user_id).format(5))
            connect.commit()
        else:
            pass

        if stage_ ==  5 and message != dct[lang_][16]  :
            try:
                cur.execute(update_phone_num.format(int(message), user_id))
                connect.commit()
            except Exception:
                pass
            cur.execute(stagee.format('{}', user_id).format(6))
            connect.commit()
            mainkey = [KeyboardButton(text=maindct[lang_][0]),
                       KeyboardButton(text=maindct[lang_][1])]
            mainkey1= [KeyboardButton(text=maindct[lang_][2])]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][16], reply_markup=ReplyKeyboardMarkup([mainkey, mainkey1], resize_keyboard=True,  one_time_keyboard=True))
        if stage_ == 6 and message == maindct[lang_][0] or stage_ == 6 and message == maindct[lang_][2]:
            if message == maindct[lang_][2]:
                cur.execute(upd_L_DOM.format('{}', user_id).format('👨‍🔧Мастер ремонтник👨‍🔧'))
                connect.commit()
                print(maindct[1][2])

            cur.execute(stagee.format('{}', user_id).format(6.2))
            connect.commit()

            mainkey = [KeyboardButton(text=maindct[lang_][0]),
                       KeyboardButton(text=maindct[lang_][1])]
            mainkey1= [KeyboardButton(text=maindct[lang_][2])]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][6], reply_markup=ReplyKeyboardRemove([mainkey, mainkey1], resize_keyboard=True,  one_time_keyboard=True))

        if stage_ == 6.2 and message!=maindct[lang_][0]:
            cur.execute(stagee.format('{}', user_id).format(6.3))
            connect.commit()
            cur.execute(upd_EDU_LANG.format('{}', user_id).format(message))
            connect.commit()
            week = [KeyboardButton(text=weekdaydct[lang_][0]),KeyboardButton(text=weekdaydct[lang_][1])]
            week1 = [KeyboardButton(text=weekdaydct[lang_][2]),KeyboardButton(text=weekdaydct[lang_][3])]
            week2 = [KeyboardButton(text=weekdaydct[lang_][4]),KeyboardButton(text=weekdaydct[lang_][5])]
            week3 = [KeyboardButton(text=weekdaydct[lang_][6])]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][26],  reply_markup=ReplyKeyboardMarkup([week, week1, week2, week3], resize_keyboard=True,
                                                                      one_time_keyboard=True))
        if stage_ == 6.3 and message in weekdaydct[lang_]:
            cur.execute(stagee.format('{}', user_id).format(6.4))
            connect.commit()
            cur.execute(upd_SALARY.format('{}', user_id).format(message))
            connect.commit()

            def func_chunks_generators(lst, n):
                for i in range(0, len(lst), n):
                    yield lst[i: i + n]
            r = []
            for e in t:
                e = str(e)
                r.append(e)
            r = list(func_chunks_generators(r, 6))

            g = []
            for e in r:
                b = []
                for k in e:
                    k = k
                    a = KeyboardButton(text=str(k))

                    b.append(a)

                g.append(b)

            context.bot.send_message(chat_id=user_id, text=dct[lang_][27],
                                         reply_markup=ReplyKeyboardMarkup(g, resize_keyboard=True))
        if stage_ == 6.4 and message!=maindct[lang_][0]:

            cur.execute(stagee.format('{}', user_id).format(6.77))
            connect.commit()
            cur.execute(upd_WORKTIME.format('{}', user_id).format(message))
            connect.commit()
            mainkey = [KeyboardButton(text=maindct[lang_][0]),
                   KeyboardButton(text=maindct[lang_][1])]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][17],
                                 reply_markup=ReplyKeyboardRemove([mainkey], resize_keyboard=True, one_time_keyboard=True))


        if stage_ == 6.77 and message != maindct[lang_][0]:
            cur.execute(upd_FILIAL.format('{}', user_id).format(message))
            connect.commit()
            mainkey = [KeyboardButton(text=maindct[lang_][0]),
                   KeyboardButton(text=maindct[lang_][1])]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][12],
                                 reply_markup=ReplyKeyboardRemove([mainkey], resize_keyboard=True, one_time_keyboard=True))
            check = 'Имя: {}\nНомер: +{}\nПочта: {}\nДень: {}\nВремя: {}\nГород: {}'.format(a_name, p_num[0][0], mail, day, time, message)
            chec = '{}\n\nИмя: {}\nНомер: +{}\nПочта: {}\nДень: {}\nВремя: {}\nГород: {}'.format(maindct[1][2].upper(),a_name, p_num[0][0], mail, day, time, message)
            print(starus)
            if starus != maindct[1][2]:
              context.bot.send_message(chat_id=-696931399, text=check)
            if starus == maindct[1][2]:
              context.bot.send_message(chat_id=-696931399, text=chec)
            cur.execute("""DELETE FROM Users WHERE TG_ID = "{}" """.format(user_id))
            connect.commit()
        if stage_ == 6 and message==maindct[lang_][1]:
           lang_but = [KeyboardButton(text='Nederlands🇳🇱'),KeyboardButton(text='Русский язык🇷🇺')]
           lang_but1 = [KeyboardButton(text='O`zbek tili🇺🇿'), KeyboardButton(text='English🇬🇧')]
           context.bot.send_message(chat_id=user_id, text='Selecteer een taal:\nВыберите язык:\nTil tanlang:\nSelect a language:',
                                 reply_markup=ReplyKeyboardMarkup([lang_but, lang_but1], resize_keyboard=True, one_time_keyboard=True))
           cur.execute(stagee.format('{}', user_id).format(6.22))
           connect.commit()

        if stage_ == 6.22 and message in lang_dct.keys():
            cur.execute(stagee.format('{}', user_id).format(7))
            cur.execute(lang.format('{}', user_id).format(lang_dct[message][0]))
            connect.commit()
            lang_ = cur.execute(lang_select.format(user_id)).fetchall()
            try:
                lang_ = lang_[0][0]
            except Exception:
                pass

            context.bot.send_message(chat_id=user_id, text=dct[lang_][13])
        if stage_ == 7 and message!=maindct[4][1]:
            cur.execute(stagee.format('{}', user_id).format(8))
            connect.commit()
            cur.execute(upd_name.format('{}', user_id).format(message))
            connect.commit()
            context.bot.send_message(chat_id=user_id, text=dct[lang_][0])
        if stage_ ==8 and message!='edfe':
            cur.execute(stagee.format('{}', user_id).format(8.23))
            connect.commit()
            cur.execute(upd_EDU_LANG.format('{}', user_id).format(message))
            connect.commit()
            context.bot.send_message(chat_id=user_id, text=dct[lang_][17])

        if stage_ ==8 and message!='edfe':
            cur.execute(stagee.format('{}', user_id).format(9))
            connect.commit()
            cur.execute(upd_FILIAL.format('{}', user_id).format(message))
            connect.commit()
            context.bot.send_message(chat_id=user_id, text=dct[lang_][14])
    except Exception:
        cur.execute(first_insert.format(user_id, 1))
        connect.commit()
        knopka_lang = [
            InlineKeyboardButton(text='Nederlands🇳🇱', callback_data='xuzb'),
            InlineKeyboardButton(text='English🇬🇧', callback_data='ru'),
            InlineKeyboardButton(text="O`zbek tili🇺🇿", callback_data='uz')
        ]
        context.bot.send_message(chat_id=user_id, text='Selecteer een taal:\nSelect a language:',
                                 reply_markup=InlineKeyboardMarkup([knopka_lang]))
        cur.execute(stagee.format('{}', user_id).format(1))
        connect.commit()
    if user_id!=TG_ID:
        cur.execute(first_insert.format(user_id, 1))
        connect.commit()
        knopka_lang = [
            InlineKeyboardButton(text='Nederlands🇳🇱', callback_data='xuzb'),
            InlineKeyboardButton(text='English🇬🇧', callback_data='ru'),
            InlineKeyboardButton(text="O`zbek tili🇺🇿", callback_data='uz')
        ]
        context.bot.send_message(chat_id=user_id, text='Selecteer een taal:\nSelect a language:',
                                 reply_markup=InlineKeyboardMarkup([knopka_lang]))
        cur.execute(stagee.format('{}', user_id).format(1))
        connect.commit()
def xuzb(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('_users.sqlite')
    cur = connect.cursor()
    lang_choose = cur.execute(lang.format('{}', user_id).format(3)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='далее>>>')]
    context.bot.send_message(chat_id=user_id, text="""Hallo, hier kunt u huis schoonmaken of huishoudelijke hulp bestellen""")
    context.bot.send_message(chat_id=user_id,
                             text='Voer uw naam in:')

def ru(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('_users.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(4)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='далее>>>')]
    context.bot.send_message(chat_id=user_id, text='Hello, here you can order house cleaning or household help')
    context.bot.send_message(chat_id=user_id, text='Please enter your name:')
    sleep(1)

    connect.commit()
def uz(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('_users.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(2))
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='davom etish>>>')]
    context.bot.send_message(chat_id=user_id, text='SALOM! Siz bu yerda uy ishiga yordamchi buyurtma berishingiz mumkun')
    context.bot.send_message(chat_id=user_id, text='Iltimos, ismingizni kiriting:')
    sleep(1)
    connect.commit()

def get_contac(update, context):
    user_id = update.message.chat_id
    num = update.message.contact.phone_number
    num = str(num)
    conn = sqlite3.connect('_users.sqlite')
    cur = conn.cursor()
    cur.execute(update_phone_num.format(num, user_id))
    conn.commit()
    cur.execute(stagee.format('{}', user_id).format(6))
    conn.commit()


    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    conn.commit()

    lang_ = lang_[0][0]

    cur.execute(stagee.format('{}', user_id).format(6))
    conn.commit()
    mainkey = [KeyboardButton(text=maindct[lang_][0]),
               KeyboardButton(text=maindct[lang_][1])]
    mainkey1 = [KeyboardButton(text=maindct[lang_][2])]
    context.bot.send_message(chat_id=user_id, text=dct[lang_][16],
                             reply_markup=ReplyKeyboardMarkup([mainkey, mainkey1], resize_keyboard=True,
                                                              one_time_keyboard=True))

def adm(update, context):
    user_id = update.message.chat_id
    text = update.message.caption
    photo_id = update.message.photo[-1].file_id
    file = context.bot.getFile(photo_id)
    file.download('Picture.jpeg')
    connect = sqlite3.connect('_users.sqlite')
    cur = connect.cursor()
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    a_name = cur.execute(select_name.format(user_id)).fetchall()
    filial = cur.execute(select_DOM.format(user_id)).fetchall()
    p_num = cur.execute(select_num.format(user_id)).fetchall()
    mail = cur.execute(select_EDU_LANG.format(user_id)).fetchall()
    starus = cur.execute(select_L_DOM.format(user_id)).fetchall()
    time = cur.execute(select_WORKTIME.format(user_id)).fetchall()
    day = cur.execute(select_SALARY.format(user_id)).fetchall()
    connect.commit()
    try:
            stage_ = stage_[0][0]
            lang_ = lang_[0][0]
            a_name = a_name[0][0]
            filial = filial[0][0]
            pnum_ = p_num[0][0]
            mail = mail[0][0]
            starus = starus[0][0]
            time = time[0][0]
            day = day[0][0]
    except Exception:
            pass

    if stage_ == 9:
          chekd = 'Имя: {}\nНомер: +{}\nПочта: {}\nГород: {}'.format(a_name, p_num[0][0], mail, filial)
          context.bot.send_photo(photo=open('Picture.jpeg', 'rb'), chat_id=-757501637, caption=chekd)
          cur.execute(stagee.format('{}', user_id).format(6))
          connect.commit()
          context.bot.send_message(chat_id=user_id, text=dct[lang_][15])
          cur.execute("""DELETE FROM Users WHERE TG_ID = "{}" """.format(user_id))
          connect.commit()
    user_id = update.message.chat_id
    for e in admdict:
        if user_id == e:
            text = update.message.caption

            if text == None:
                pass
            elif text != 'slsllsslsllssllssllslslssls':
                try:
                    photo_id = update.message.photo[-1].file_id
                    file = context.bot.getFile(photo_id)
                    file.download('Picture.jpeg')
                    connect = sqlite3.connect('_users.sqlite')
                    cur = connect.cursor()
                    id = cur.execute('''
                SELECT TG_ID
                FROM Users
                WHERE TG_ID !=0
                ''').fetchall()
                    for e in id:
                        try:
                            e = e[0]
                            context.bot.send_photo(photo=open('Picture.jpeg', 'rb'), chat_id=e, caption=text)
                            sleep(1.5)
                        except Exception:
                            pass
                except Exception:
                    continue