import pyautogui
import os
quest = input('Запуск!?')

if quest == 'yes':
    os.startfile(r'C:\Users\Тимур\AppData\Roaming\Telegram Desktop/Telegram.exe')
    b = input('Вы готовы?')
    if b == 'yes':
        how = int(input('Сколько сообщений отправить?'))
        name = input("Какой текст в сообщении(ENG)")
        x = -1
        pyautogui.hotkey('alt', 'tab')
        while x < how:
            pyautogui.write(f'{name}')
            pyautogui.press('enter')
            x = x + 1


