#`````````````````````````````
#
#    Developed by Ivan Seagull
#
#`````````````````````````````


# Подключение всех необходимых библиотек
# Нам нужно: speech_recognition, os, sys, webbrowser
# Для первой бибилотеки прописываем также псевдоним
import speech_recognition as sr #голос
import os #ос
import sys #система
import webbrowser #веббраузер
from fuzzywuzzy import fuzz #расспазнователь голоса
import pyttsx3
import datetime #дата
import random #рандом
import calendar #календарь
import tkinter as tk #создавать вспомогательные окна
import pyowm # для погоды
import keyboard
#обращение команды и слова
path = "Ваш путь для папок"
opts = {
    "alias": ('субота','суббота','субботик','субба'),
    "tbr": ('скажи','расскажи','покажи','сколько','произнеси'),
    "cmds": {
        "ctime": ('текущее время','сейчас времени','который час'),
        "radio": ('включи музыку','воспроизведи радио','включи радио'),
        "stupid1": ('расскажи анекдот','рассмеши меня','ты знаешь анекдоты','расскажи шутку'),
        "newFolder": ('создай папку','новая папка','создай новую папку'),
        "opnBrowser": ('открой браузер','поиск','зайди в интернет','зайди в инет'),
        "opnArduino": ('открой arduino','запусти arduino'),
        "opnAtom": ('открой atom','запусти atom','запусти атом','открой атом'),
        "opnVK": ('открой вконтакте','вконтакте','vk','зайди в vk'),
        "HowAreYou": ('как дела','как ты','ты как'),
        "calendar": ('открой календарь','покажи календарь'),
        "weather": ('какая погода','какая сегодня погода','что по погоде'),
        "temperatura": ('какая температура','какая сегодня температура','как тепло','что по температуре'),
        "close": ('пока','давай закончим','потом поговорим','досвидания')
    }
}


#обрабатываем звук
def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):

            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")

#получаем команду из звука
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC

#выполняем команду
def execute_cmd(cmd):
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        #print(now)
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif cmd == 'radio':
        # воспроизвести радио
        os.startfile(r'Путь к радио')
        pass
    #
    elif cmd == 'HowAreYou':
        speak('Хорошо, спасибо что спросили')
    
    #Вывести календарь
    elif cmd=="calendar":
        now = datetime.datetime.now()
        print (c.formatmonth(now.year,now.month))
    
    # рассказать анекдот
    elif cmd == 'stupid1':
        joke = random.randint(1, 5)
        print(joke)
        if joke == 1:
          speak("Многие люди из шоу-бизнеса всерьез верят, что они талантливы. Ха Ха Ха")
        elif joke == 2:
            speak("Меня несколько удивляет, что собака — друг человека. Неужто собака получше никого для дружбы не смогла найти? Ха Ха Ха")
        elif joke== 3:
            speak("— Что вы все киваете, будто согласны со мной, я же говорю обидные для вас вещи! — Шею разминаю, у меня коронный — головой в челюсть.")
        elif joke == 4:
            speak("СМИ — Средства Манипулирования Идиотами. Ха Ха Ха")
        elif joke == 5:
            speak("Сантехник Сидоров был весьма удивлен, когда засунул руку в унитаз и ощутил чье- то ответное крепкое рукопожатие.")

    #запустить программу ардуино
    elif cmd == 'opnArduino':
       speak ("открываю arduino")
       os.startfile(r'Ваш путь к программе')

    #запустить атом
    elif cmd == 'opnAtom':
       speak ("открываю atom")
       os.startfile(r'Ваш путь к программе')
    
    # создай папку
    elif cmd == 'newFolder':
        #path = "Ваша папка"
        speak("Как называется папка?")
        #Запускаем окно
        maketk()
        #projectname=str(input("Kак называется папка:   "))
        fullpath = os.path.join(path, name) #projectname)
        speak ("Создаётся папка")
        speak(name)

        os.mkdir(fullpath)

    # открываем vk
    elif cmd == 'opnVK':
        speak("Открываю vk")
        webbrowser.open("https://vk.com/feed")
        
    # открываем браузер
    elif cmd == 'opnBrowser':
        speak("Открываю")
        webbrowser.open("www.google.com")

    #показывать температуру
    elif cmd == 'temperatura':
       speak ("Температура в Москве "+str(temperature)+" по цельсию")
    #
    показывать погоду
    elif cmd == 'weather':
      speak ("В Москве сейчас " + w.get_detailed_status())

    #закрыть программу
    elif cmd == 'close':
        speak("Пока")
        sys.exit()

    #Неизвестная команда
    else:
        print('Команда не распознана, повторите!')



#функция разговора
def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()




def Makefolder():
     global name
     name=edit.get()
     # Так. Я писал это два года назад вроде, когда учился программировать. Я бы мог это убрать и не позориться, 
     # но решил оставить так, чтобы помнить, с чего начинал. Ну и поржать конечно же
     if name=="":
          pass
     elif name== " ":
          pass
     elif name== "  ":
          pass
     elif name== "   ":
          pass
     elif name== "    ":
          pass
     elif name== "     ":
          pass
     else:
          print(name)
          w1.destroy()

#создание окна
def maketk():
#okno
     global w1
     w1=tk.Tk()
     w = w1.winfo_screenwidth() # ширина экрана
     h = w1.winfo_screenheight() # высота экрана
     w = w//2 # середина экрана
     h = h//2
     w = w - 200 # смещение от середины
     h = h - 200
     w1.geometry('450x200+{}+{}'.format(w,h))
     w1.title('info')
#label
     t1 = tk.Label(w1, text = "Как называется папка?", fg='black')
     t1.config(font=('Times',25))
     t1.pack()

#entry
     global edit
     edit=tk.Entry(w1,width=50)
     edit.pack()

#button
     b1=tk.Button(w1, text='Создать папку', command=Makefolder)
     b1.config(width=20, height=2)
     b1.pack()

     w1.mainloop()


#Получаем погоду
def weather():
    global weatherValue
    weatherValue=0
    try:
                owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language='ru')
                observation = owm.weather_at_place('Москва')
                global w
                global temperature
                global humidity
                global speedWind
                w = observation.get_weather()
                temperature=w.get_temperature('celsius')['temp']
                humidity=w.get_humidity()
                speedWind=w.get_wind()["speed"]
                weatherValue=1
    except:
        print(weatherValue)





#тупая инициализация все что можно было
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)
with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

c = calendar.TextCalendar(0)
# Вызов функции и передача строки
# именно эта строка будет проговорена компьютером
#speak("Привет, чем я могу помочь вам?")
speak("Добрый день, повелитель")
speak("Джарвис слушает")

weather()

def listen():
    while True:
        print("[log] Можете говорить")
        with m as source:
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            callback(r, audio)
            #break
            return False


while True:
    if keyboard.is_pressed('Shift + Alt + s'):
        print("Log")
        if listen():
            break
