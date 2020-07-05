import speech_recognition as sr
#import os
import sys
import re
import webbrowser
import requests
from pyowm import OWM
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import wikipedia
from time import strftime
import pyttsx3
def sofiaResponse(audio):
    "speaks audio passed as argument"
    print(audio)
    engine = pyttsx3.init()
    engine.getProperty('rate')    
    engine.setProperty('rate', 150)  
    engine.getProperty('volume')  
    engine.setProperty('volume',2.0)  
    engine.say(audio)
    engine.runAndWait()
    
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        sofiaResponse('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = myCommand();
    return command
def assistant(command):
    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        sofiaResponse('The Reddit content has been opened for you .')
    elif 'shutdown' in command:
        sofiaResponse('bye bye Have a nice day')
        sys.exit()
    elif 'open' in command:
        reg_ex = re.search('open (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            print(domain)
            url = 'https://www.' + domain
            webbrowser.open(url)
            sofiaResponse('The website you have requested has been opened for you .')
        else:
            pass
    elif 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            sofiaResponse('Hello . Good morning')
        elif 12 <= day_time < 18:
            sofiaResponse('Hello . Good afternoon')
        else:
            sofiaResponse('Hello . Good evening')
    elif 'help me' in command:
        print("""
        You can use these commands and I'll help you out:
        1. Say Hello
        2. Open xyz.com
        3. Current weather in {cityname}
        4. Open reddit subreddit 
        5. news for today
        6. time : Current system time
        7.tell me a joke
        8. tell me about xyz
        9.shutdown to exit
        """)
    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"})
        if res.status_code == requests.codes.ok:
            sofiaResponse(str(res.json()['joke']))
        else:
            sofiaResponse('oops!I ran out of jokes')
    elif 'news for today' in command:
        try:
            news_url="https://news.google.com/news/rss"
            Client=urlopen(news_url)
            xml_page=Client.read()
            Client.close()
            soup_page=soup(xml_page,"xml")
            news_list=soup_page.findAll("item")
            for news in news_list[:5]:
                sofiaResponse(news.title.text.encode('utf-8'))
        except Exception as e:
                print(e)
    elif 'current weather' in command:
        reg_ex = re.search('current weather in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
            obs = owm.weather_at_place(city)
            w = obs.get_weather()
            k = w.get_status()
            x = w.get_temperature(unit='celsius')
            sofiaResponse('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
    elif 'time' in command:
        import datetime
        now = datetime.datetime.now()
        sofiaResponse('Current time is %d hours %d minutes' % (now.hour, now.minute))
    elif 'tell me about' in command:
        reg_ex = re.search('tell me about (.*)', command)
        try:
            if reg_ex:
                topic = reg_ex.group(1)
                ny = wikipedia.page(topic)
                sofiaResponse(ny.content[:500].encode('utf-8'))
        except Exception as e:
                print(e)
                sofiaResponse(e)
sofiaResponse('Hi user,I am your personal voice assistant, Please give a command or say "help me" and I will tell you what all I can do for you.')
while True:
    assistant(myCommand())
    
    
    
    
