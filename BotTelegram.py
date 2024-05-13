import telebot, requests, os, re, threading, glob
from telebot import types

bot = telebot.TeleBot('6149957194:AAHvsUnLJPLMWzxHP3Qik6dhqxiSZziuV04')
requests.get('https://t.me/@TestMapInChatBot')

groups = [619484745]  # chat id
dict = {'Приморья': 'https://192.168.233.171:25443/'}

@bot.message_handler(func=lambda message: message.chat.id not in groups)
def some(message):
    bot.send_message(message.chat.id, 'Доступ ограничен')
def remove_pic(test_name):
    folder_path = './Results/Results_sc'
    file_list = os.listdir(folder_path)
    try:
        for file_name in file_list:
            if file_name.endswith(''+test_name+'.png'):
                file_path = os.path.join(folder_path, file_name)
                os.remove(file_path)
    except Exception:
        pass


def send_pic(message, test_name):
    try:
        a = open('./Results/Results_sc/Авторизация_'+test_name+'.png', 'rb')
        bot.send_photo(message.chat.id, a)
    except Exception:
        pass
    try:
        b = open('./Results/Results_sc/Дневник_'+test_name+'.png', 'rb')
        bot.send_photo(message.chat.id, b)
    except Exception:
        pass
    try:
        c = open('./Results/Results_sc/Расписание_'+test_name+'.png', 'rb')
        bot.send_photo(message.chat.id, c)
    except Exception:
        pass
    try:
        d = open('./Results/Results_sc/Госпитализация_'+test_name+'.png', 'rb')
        bot.send_photo(message.chat.id, d)
    except Exception:
        pass
    try:
        i = open('./Results/Results_sc/Поиск_'+test_name+'.png', 'rb')
        bot.send_photo(message.chat.id, i)
    except Exception:
        pass
    try:
        r = open('./Results/Results_sc/РеестрПоликлиники_'+test_name+'.png', 'rb')
        bot.send_photo(message.chat.id, r)
    except Exception:
        pass
    try:
        r2 = open('./Results/Results_sc/РеестрСтационара_'+test_name+'.png', 'rb')
        bot.send_photo(message.chat.id, r2)
    except Exception:
        pass

def create_log(message, test_name):
    if not os.path.exists("Results/Results_"+test_name+".log"):
        with open("Results/Results_"+test_name+".log", "w") as file:
            file.write('В данный момент проводится тестирование продуктивного стенда.\nПодождите окончания тестирования (примерно 2-3 минуты).')
        pass
    else:
        with open("Results/Results_"+test_name+".log", "r") as file:
            f = file.read()
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=f)
            file.close()
            exit()

def autotest_prod(message, test_name, address):
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text="🔴Начата проверка крит. модулей продуктивного стенда <a href='"+address+"'>"'<u><b>'+test_name+'</b></u>'"</a>", parse_mode='html')
    remove_pic(test_name)
    create_log(message, test_name)
    os.system('pytest --testit -s '+test_name+'.py > Results/'+test_name+'.log')  # команда запуска скрипта test.py и запись результата в файл logs.txt
    with open('Results/'+test_name+'.log', 'r', -1, 'utf-8') as file:
        f = file.read()
        opt_3 = f[f.find('['): f.rfind('~')]
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text="🟢Закончена проверка крит. модулей продуктивного стенда <a href='"+address+"'><u><b>"+test_name+"</b></u></a>", parse_mode='html')
    bot.send_message(message.chat.id, opt_3)
    send_pic(message, test_name)
    os.remove("./Results/Results_" + test_name + ".log")

def start_autotest_thread(message, test_name, address):
    thread = threading.Thread(target=autotest_prod, args=(message, test_name, address))
    thread.start()

@bot.message_handler(commands=["start"])
def any_msg(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Приморский край", callback_data="Приморья")
    btn2 = types.InlineKeyboardButton(text="Пример(🚫)")
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, "Выберите регион/отдельного клиента, для тестирования\nкрит. модулей продуктивного стенда сервиса - МИС", reply_markup=markup)

@bot.message_handler(commands=["help"])
def help_msg(message):
    bot.send_message(message.chat.id, '<b>Правила по эксплуатации бота:</b>'
                                      '\n▪️  <b>М</b>аксимальное кол-во активных сессий тестирования стендов - 10;'
                                      '\n▪️  <b>Е</b>сли возникла ошибка при попытке создания записи или тестового '
                                      'пациента - следует его удалить (<i>обратитеть к Дежурному СЦ (@bg_sitcenter)</i>);'
                                      '\n▪️  <b>П</b>ользоваться ботом только в чате - "AUTO-TEST", для отчетности;'
                                      '\n▪️  <b>Е</b>сли крит. модуль отрабатывается суммарно более - 200 секунд, '
                                      'вероятно причина в деградации производительности '
                                      '(<i><u><b>проверить</b></u> чтение/запись на дисках и CPU нагрузку на DB/WEB</i>);'
                                      '\n▪️  <b>П</b>ри возникновении вопросов/предложений обращаться к разработчику или руководителю отдела.'
                                      '\n\n<b>Разбор ошибок:</b>'
                                      '\n▶️  <b>Message: Not found</b> - Не найден элемент страницы, возможные причины: смена элемента или некорректно прописан. Следует обратиться к <u>разработчику</u>.'
                                      '\n▶️  <b>Message: Element not interactable</b> - с элементом страницы нельзя взаимодействовать, возможные причины: не заполнены все обязательные поля, не донесены настройки, блокирование. Следует протестировать стенд, при выявлении ошибок эскалировать в чат <u>ОКК</u> и <u>разработчику</u>.'
                                      '\n▶️  <b>Message: Element click intercepted</b> - взаимодействие с элементом страницы перехвачено каким либо действием самой системы. Следует протестировать стенд, при выявлении ошибок эскалировать <u>разработчику</u>.'
                                      '\n\n<b>Контакты:</b>'
                                      '\nРазработчик - Ахтямов Тимур (<i>@ELCUY</i>).'
                                      '\nРуководитель отдела - Александр Плотников (<i>@glafkon</i>).', parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline_1(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == call.data:
            start_autotest_thread(call.message, test_name=call.data, address=dict[call.data])
        else:
            print('Кнопка не имеет функционала')
            pass


# bot.polling(none_stop=True, interval=0)
bot.infinity_polling(none_stop=True)
# bot.polling(none_stop=True, timeout=123)
