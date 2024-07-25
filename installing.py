import sys
import os
import time
import subprocess
modules = [
    "pystyle",
    "urllib3",
    "beautifulsoup4",
    "phonenumbers",
    "faker",
    "pyautogui",
    "python-whois",
    "requests"
]

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def install_modules():
    print("Вас приветствует мастер установки reload.\nСейчас мы проведем установку всех зависимостей для правильной работы программы reload.\n")
    for module in modules:
        try:
            __import__(module)
            print(f"{module} уже установлен.")
        except ImportError:
            print(f"Установка {module}...")
            install(module)
            print(f"Установлен модуль {module}")


    print("Запускаем программу reload")
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('reload.py')
install_modules()