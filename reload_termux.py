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
import urllib
import os
import json
from urllib.request import Request
from urllib.error import HTTPError
from fake_useragent import FakeUserAgent
import pyautogui
import ctypes

citata = random.choice([
    'Сила по силе - осилишь; а сила не под силу - осядешь.',
    'Кость да жила, да все сила.',
    'И сила уму уступает.',
    'сила слова — в правде.', 
    'Депрессия не признак слабости — это признак того, что вы пытались быть сильным слишком долго...',
    'Настоящая сила требует сочетания настойчивости, доброты и храбрости.',
    'Не хвались силою, чтоб не заплатить спиною ',
    'Сосредоточенность — вот в чем секрет силы.',
    'Сила слаба тем, что верит только в силу.'
])





fake = Faker()
banner = '''
██████  ███████ ██      ████████  █████  ██████  
██   ██ ██      ██      ██    ██ ██   ██ ██   ██ 
██████  ███████ ██      ██    ██ ███████ ██   ██ 
██   ██ ██      ██      ██    ██ ██   ██ ██   ██ 
██   ██ ███████ ███████ ████████ ██   ██ ██████  
'''


def error():
    print('Этот способ пока что не существует, в разработке...')
    input('Нажмите Enter для продолжения...')
    cls()

def universal_search_dumps():
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVkX2F0IjoxNzIyNDE0ODQ4LCJhcHBfaWQiOjE3MjI0MTQ4NDh9.fG6zDjmfGifLiOj7kcv9wPfrKZIeAkM68CioDTvh6Ds'
    query = input('Введите любой запрос, примеры запросов\n█ip - 192.168.12.12\n█number - 79999999090\n█email - hello@example.com\n\n>>>')

    url = 'https://api.usersbox.ru/v1/explain'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    params = {'q': query}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        result = response.json()
        if result['status'] == 'success':
            count = result['data']['count']
            items = result['data']['items']

            print(f'Количество документов, соответствующих запросу "{query}": {count}')
            if count > 0:
                print("\nПодробности по базам данных:")
                for item in items:
                    database = item['source']['database']
                    collection = item['source']['collection']
                    hits_count = item['hits']['count']

                    print(f"  |База данных: {database}")
                    print(f"  |Коллекция: {collection}")
                    print(f"  |Найдено документов: {hits_count}")
                input('Нажмите Enter для продолжения...')
                cls()
        else:
            print('Не удалось получить результат. Статус:', result['status'])
            input('Нажмите Enter для продолжения...')
            cls()
    except requests.RequestException as e:
        print(f'Ошибка запроса: {e}')
        input('Нажмите Enter для продолжения...')
        cls()

def check_dumps():
    def main_work():
        request = input('Введите email, пример - hello@example.com\n>>>')
        api = '4358f4908efdbdb79c92f1006e2ec0374b0f24c4'
        url = f'https://leakcheck.io/api/public?key={api}&check={request}'
        ua = FakeUserAgent()
        user_agent = ua.random
        headers = {'UserAgent': user_agent}
        request_1 = Request(url, headers=headers)
        try:
            response = urllib.request.urlopen(request_1)   
            data = json.load(response)
            if data:
                for entry in data['result']:
                    print(f"status - {entry['success']}")
                    print(f"кол-во утечек - {entry['found']}")
                    print(f"утечки - {entry['name']} - date - {entry['date']}")
                input('Нажмите Enter для продолжения...')
                cls()
            else:
                print('Произошла ошибка соединения.. попробуйте снова')
                input('Нажмите Enter для продолжения...')
                cls()
        except Exception as e:
            print(f'Ошибка: {e}')
            input('Нажмите Enter для продолжения...')
            cls()

    note = ('ОБРАТИТЕ ВНИМАНИЕ, ЧТО ДАННЫЙ ТИП ЗАПРОСОВ ЛИМИТИРОВАН СЕРВЕРОМ, И ПОСТАРАЙТЕСЬ НЕ ПРЕВЫШАТЬ ЛИМИТ ЗАПРОСОВ\n'
            'ПОДУМАЙТЕ О ДРУГИХ ПОЛЬЗОВАТЕЛЯХ!\n\n ---> ENABLE VPN <---\n\n ---> ENABLE VPN <---\n\n ---> ENABLE VPN <---')
    print(note)
    note_check = input('Вы согласны с правилами использования опции? (y/n)\n>>>')
    if note_check == 'y':
        main_work()
    elif note_check == 'n':
        return
    else:
        cls()

def check_email():
    print('ОШИБКА\nПОКА В РАЗРАБОТКЕ..\nСТАТУС: ЖДУ ПОЛУЧЕНИЕ API EMAILCHECK')  
    input('Нажмите Enter для продолжения...')
    cls()

def haweibeenpwned():
    account = input('Введите вашу почту в формате qwerty@example.com\n>>>')
    url = f'https://haveibeenpwned.com/api/breachedaccount/{account}'
    ua = FakeUserAgent()
    user_agent = ua.random
    headers = {'UserAgent': user_agent}

    try:
        request = Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        data = json.load(response)

        if data:
            print(f'|Учетная запись {account} была скомпрометирована в следующих утечках данных:')
            for breach in data:
                print(f"| {breach['Name']}: {breach['BreachDate']}")
            input('Нажмите Enter для продолжения...')
            cls()
        else:
            print(f'|Учетная запись {account} не была найдена в известных утечках данных.')
            input('Нажмите Enter для продолжения...')
            cls()

    except HTTPError as e:
        if e.code == 404:
            print(f'|Учетная запись {account} не была найдена в известных утечках данных.')
        elif e.code == 400:
            print('|Ошибка запроса. Проверьте правильность введенного email.')
        else:
            print(f'|Произошла ошибка: {e}')
        input('Нажмите Enter для продолжения...')
        cls()
    except Exception as e:
        print(f'|Возникла ошибка при обработке запроса: {e}')
        input('Нажмите Enter для продолжения...')
        cls()

def parser_vk():
    username = input('ВВЕДИТЕ ССЫЛКУ НА СТРАНИЦУ, ЕСЛИ У ВАС ТОЛЬКО ID ТО С @\n>>>')
    print('идет поиск..')
    url = f'https://vk.com/{username}'
    r = requests.get(url)
    
    if r.status_code == 200:
        try:
            soup = BeautifulSoup(r.content, 'html.parser')
            user_name_tag = soup.find('title')
            user_name = user_name_tag.text.strip() if user_name_tag else 'Не найдено'
            records_tag = soup.find('span', class_='ui_tab_content_new')
            records_count_tag = records_tag.find_next_sibling('span', class_='visually-hidden') if records_tag else None
            records_count = records_count_tag.text.strip() if records_count_tag else 'Не найдено'
            posts_tag = soup.find('div', class_='page_block')
            posts = posts_tag.text.strip() if posts_tag else 'Не найдено'

            auth_post_tag = soup.find('a', class_='author')
            auth_post = auth_post_tag.text.strip() if auth_post_tag else 'Не найдено'

            print(f'\n|Ваш запрос обработан успешно, статус запроса - {r.status_code}')
            print(f'|Имя - {user_name}\n|Посты - {posts}\n|Количество записей - {records_count}\n|Авторы постов - {auth_post}')
            input('Нажмите Enter для продолжения...')
            cls()
        except Exception as error:
            print(f'Возникла ошибка при обработке данного запроса, попробуйте снова..\nКод ошибки - {error}\nПРИЧИНЫ - ВОЗМОЖНО, СТРАНИЦА СКРЫТА, ТОГДА ПОЛУЧИТЬ ИНФОРМАЦИЮ БУДЕТ ОЧЕНЬ ТЯЖЕЛО')
    else:
        print('Не удалось соединиться с VK, попробуйте использовать русский VPN')
        time.sleep(1)
        cls()

def ddos():
    print('''                                   !ВНИМАНИЕ!\nСОВЕТУЕМ ВКЛЮЧИТЬ ВПН, ТАК КАК ЗАПРОСЫ МОГУТ ИДТИ С ВАШЕГО USER-AGENT'A!''')
    try:
        url = input('Введите ссылку\n>>>')
        while True:
            number_requests = 0
            r = requests.get(url)
            if r.status_code == 200:
                number_requests += 1
                print(f'[+] - чтобы остановить поток нужно зажать ctrl + C\nуспешный запрос №{number_requests}')
            else:
                print('Возникла ошибка при обработке запроса, возвращаю в меню..')
                time.sleep(0.5)
                cls()
    except Exception as e:
        print(f'Произошла ошибка {e}\nВозвращаю в меню..')
        time.sleep(0.5)

def gen_pass():
    k1 = int(input('Введите число символов в пароле\n>>>'))
    try:
        response = ''.join(random.choices(string.ascii_letters + string.digits, k=k1))
        print(f'Ваш новый пароль - {response}\n')
        input('Нажмите Enter для продолжения...')
        cls()
    except Exception as e:
        print(f'Ошибка - {e}\n')
        input('Нажмите Enter для продолжения...')
        cls()
def ip_lookup():
    try:
        import json
        from urllib.request import urlopen
        query = input('Введите IP адрес\n>>>')
        url = f'http://ip-api.com/json/{query}'
        response = urlopen(url)
        result = json.load(response)
        print(f'| Статус запроса - {result["status"]}')
        print(f'| Страна - {result["country"]}')
        print(f'| Регион - {result["regionName"]}')
        print(f'| Город - {result["city"]}')
        print(f'| Провайдер - {result["isp"]}')
        print(f'| Организация - {result["org"]}')
        print(f'| Наличие прокси - {result["proxy"]}')
        input('Нажмите Enter для выхода в меню')
        cls()

    except Exception as e:
        print(f'Произошла ошибка - {e}')
        input('Нажмите Enter для выхода в меню')
        cls()
def fake_gen():
    from faker import Faker
    fake = Faker()
    print(f'| Имя - {fake.name()}')
    print(f'| Email - {fake.email()}')
    print(f'| Кредитная карта - {fake.credit_card_number(card_type=None)}')
    print(f'| Дата рождения - {fake.date_of_birth()}')
    print(f'| Адрес - {fake.address()}')
    print(f'| Компания - {fake.company()}')
    print(f'| Должность - {fake.job()}')
    print(f'| Username - {fake.user_name()}')
    input('Нажмите Enter для выхода в меню')
    cls()
def parser_tg():
    nick = input('Введите nickname\n>>>')
    url = f'https://t.me/{nick}'

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        user_name_tag = soup.find('meta', property='og:title')
        user_description_tag = soup.find('meta', property='og:description')

        if user_name_tag and user_description_tag:
            username = user_name_tag.get('content', '').strip()
            description = user_description_tag.get('content', '').strip()
            print(f'| ИМЯ В СИСТЕМЕ - {username}\n| BIO - {description}\n| ПРЯМАЯ ССЫЛКА НА ДИАЛОГ - t.me/{nick}\n')
        elif user_name_tag:
            username = user_name_tag.get('content', '').strip()
            print(f'| Такой ник существует - {username}')
        else:
            print(f'| Такого username не существует')
    else:
        print('| Не удалось подключиться к Telegram')
        input('| Нажмите ENTER, чтобы выйти в меню ')
        cls()
def phone():
    try:
        number = input('Введите номер телефона в формате (+7999...)\n>>>')
        my_number = phonenumbers.parse(number)

        print(f'| Оператор: {carrier.name_for_number(my_number, "en")}')
        print(f'| Часовой пояс: {timezone.time_zones_for_number(my_number)}')
        print(f'| Регион: {geocoder.description_for_number(my_number, "en")}')
        print(f'| Валидный ли номер? {phonenumbers.is_valid_number(my_number)}')
        print(f'| Возможен ли номер? {phonenumbers.is_possible_number(my_number)}')
        print(f'| Ссылки на соц-сети (могут быть не рабочими):')
        print(f'| Telegram: t.me/{number}')
        print(f'| WhatsApp: wa.me/{number}')

        set_func = input('Продолжить поиск вторым типом запроса? (y/n)\n>>>')
        if set_func.lower() == 'y':
            import json
            from urllib.request import urlopen
            url = f'http://num.voxlink.ru/get/?num={number}'
            response = urlopen(url)
            response_json = json.load(response)
            print(f'| Полный номер - {response_json["full_num"]}')
            print(f'| Оператор - {response_json["operator"]}')
            print(f'| Точный город - {response_json["region"]}')
            input('Нажмите ENTER, чтобы выйти')
            cls()
        else:
            cls()
    except Exception as e:
        print(f'Произошла ошибка - {e}')
        input('Для выхода в меню нажмите ENTER')
        cls()
def email():
    api_key = 'https://www.1secmail.com/api/v1/'
    domains = ["1secmail.com", "1secmail.org", "1secmail.net", "wwjmp.com", "esiix.com", "xojxe.com", "yoggm.com"]
    domain_choice = random.choice(domains)

    def generate_mail():
        custom_choice = input('Выберите действие\n> 1 - выбрать никнейм для почты самому [!ОШИБКИ В РАБОТЕ! - сообщать админу!]\n> 2 - рандом выбор [!РАБОТАЕТ КОРРЕКТНО!]\n>>>')
        
        if custom_choice == '1':
            while True:
                user_name = input('Введите никнейм (не менее 5 символов)\n>>>')
                if len(user_name) >= 5:
                    break
                else:
                    print('Ошибка: Никнейм должен содержать не менее 5 символов.')
        elif custom_choice == '2':
            name_chars = string.ascii_lowercase + string.digits
            user_name = ''.join(random.choice(name_chars) for _ in range(5))
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")
            return generate_mail()

        return f"{user_name}@{domain_choice}"

    def check_mail(mail):
        request = f'{api_key}?action=getMessages&login={mail.split("@")[0]}&domain={mail.split("@")[1]}'
        r = requests.get(request).json()
        req_answer = len(r)
        if req_answer == 0:
            print('Ожидание писем (пока что нет), следующая проверка через 10 секунд...\n')
            time.sleep(10)
            cls()
            print('Проверяем снова...\n')
            check_mail(mail)
        else:
            ids = [msg["id"] for msg in r]
            print(f"Почта обновлена, у вас {req_answer} сообщений\n")

            for i in ids:
                read_ans = f'{api_key}?action=readMessage&login={mail.split("@")[0]}&domain={mail.split("@")[1]}&id={i}'
                r = requests.get(read_ans).json()
                s = r.get('from')
                sub = r.get('subject')
                mail1 = r.get('textBody')
                print('ВАШЕ СООБЩЕНИЕ:')
                print(f"От кого: {s}\n")
                print(f"Тема: {sub}\n")
                print(f"Сообщение: {mail1}\n")
                
            user_choice = input("Введите 1, чтобы удалить почту. 2 - чтобы выйти из приложения\n>>> ")
            if user_choice == '1':
                delete_mail(mail)
            elif user_choice == '2':
                input('Нажмите ENTER, чтобы выйти')
                cls()
            else:
                print('Ошибка ввода')

    def delete_mail(mail):
        request = f'{api_key}?action=deleteMail&login={mail.split("@")[0]}&domain={mail.split("@")[1]}'
        response = requests.get(request)
        if response.status_code == 200:
            print("Почта успешно удалена")
        else:
            print("Ошибка при удалении почты")

    mail = generate_mail()
    print(f'Сгенерирована почта: {mail}\n')
    check_mail(mail)
def hello():
    from datetime import datetime
    now = datetime.now()
    hour = now.hour
    
    if 5 <= hour < 12:
        greeting = "Доброе утро!"
    elif 12 <= hour < 18:
        greeting = "Добрый день!"
    elif 18 <= hour < 23:
        greeting = "Добрый вечер!"
    else:
        greeting = "Доброй ночи!"
    print(banner)
    print(f'{greeting}, добро пожаловать в RELOAD!')
    choice = input('''                          
        +============================+=================================+=================================+
        || TELEGRAM>@PYTHON_PIONEER  ||        0 - ИЗМЕНИТЬ ЦВЕТ       ||    CHANNEL>@pythoneer_projects||
        +----------------------------+---------------------------------+---------------------------------+
        |1 > ПОИСК ПО IP             |2 > ЛЕГКИЙ DDOS (ВКЛЮЧИТЬ VPN)   |11 > TRY ВК ПАРСИНГ ИНФЫ         |
        +----------------------------+---------------------------------+---------------------------------+
        |3 > ГЕНЕРАТОР ПАРОЛЕЙ       |4 > ПРОВЕРКА НОМЕРА ТЕЛЕФОНА     |12 > ПРОВЕРКА ПОЧТЫ НА УТЕЧКИ    |
        +----------------------------+---------------------------------+---------------------------------+
        |5 > МАНУАЛ ПО USB-KILLER    |6 > ВРЕМЕННАЯ ПОЧТА (с вашим nick)|13 > ПРОВЕРИТЬ РЕГИСТРАЦИЮ EMAIL |
        +----------------------------+---------------------------------+---------------------------------+
        |7 > ПАРСИНГ НИКА ТЕЛЕГРАМ   |8 > ФЕЙК ЛИЧНОСТЬ                |14 > ПРОВЕРИТЬ УТЕЧКИ EMAIL (WORK)|
        +----------------------------+---------------------------------+---------------------------------+
        |9 > ШАБЛОНЫ ИНФА ОГЭ        |10 > 0 СОФТ                      |15 > УНИВЕРСАЛЬНЫЙ ПОИСК УТЕЧЕК  |
        +----------------------------+---------------------------------+---------------------------------+                           
        |16 > ВК ПОИСК (не работает) |17 > dev...                      |18 > dev...                      |
        +----------------------------+---------------------------------+---------------------------------+\n\nchoose variant --->  ''')
    if choice == '0':
        os.system('python3 reload.py')
    elif choice == '1':
        ip_lookup()
    # ... и так далее для остальных вариантов
    elif choice == '1':
        ip_lookup()
    elif choice == '1488':
      pass
    elif choice == '2':
        ddos()  
    elif choice == '3':
        gen_pass()
    elif choice == '4':
        phone()
    elif choice == '5':
        error()
    elif choice == '6':
        email()
    elif choice == '7':
        parser_tg()
    elif choice == '8':
        fake_gen()
    elif choice == '9':
        print('пока в разработке.. ')
    elif choice == '10':
        pyautogui.alert('ЭТА ОТКРЫТАЯ ПРОГРАММА ОБЩЕГО ПОЛЬЗОВАНИЯ!\nЕСЛИ ТЕБЯ ЗАСКАМИЛИ НА НЕЕ, ТО ПИШИ МНЕ @PYTHON_PIONEER\nмой канал - @pythoneer_projects\n date: 25.07.24')
        cls()
    elif choice == '11':
        parser_vk()
    elif choice == '12':
        pyautogui.alert('временно запросы не поддерживаются с российских ip\nсоветую включить vpn, чтобы программа корректно работала.')
        time.sleep(2)
        haweibeenpwned()
    elif choice == '13':
        check_email()
    elif choice == '14':
        check_dumps()
    elif choice == '15':
        universal_search_dumps()
    elif choice == '16':
        error()
    else:
        error()
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    hello()
name = input('[?] Введите ваше имя\n>>>')
cls()

