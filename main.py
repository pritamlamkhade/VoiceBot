import speech_recognition as sr
import pyttsx3
l1 = ["yes","sure","han bolo","tell me","haan","hanji","hanji bataiye","please","boliye","haanji boliye","hmmm","yes yes","why not","yes you can","you can","sure you can","ok","yes tell me","bolo madam"]
l2 = ["online","google pay","paytm","airtel payment bank"]
l3 = ["no","nahi","na","ji nahi","stop","dont disturb","kya","kyu","kaun"," "]

engine = pyttsx3.init()
engine.getProperty('rate')    
engine.setProperty('rate', 150)  
engine.getProperty('volume')  
engine.setProperty('volume',2.0) 
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)
print('Dear Customer,this is Riya from Bajaj Finance Collections department,Can you Spare two minutes of your time?') 
engine.say('Dear Customer,this is Riya from Bajaj Finance Collections department,Can you Spare two minutes of your time?')
engine.runAndWait()


r = sr.Recognizer()
with sr.Microphone() as source:
    print('>>>')
    r.pause_threshold = 1
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source,phrase_time_limit = 3)
  
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    except sr.UnknownValueError:
        print('Can you repeat again please')
        engine.say('Can you repeat again please')
        engine.runAndWait()
        with sr.Microphone() as source:
            print('>>>')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source,phrase_time_limit = 3)
            command = r.recognize_google(audio).lower()
            print('You said: ' + command + '\n')
    except Exception as e:
                print('bye')
                print(e)
                
if command in l1:
    print('Thank you for being our valued customer.Your Bajaj Finserv Loan EMI of Rs 1000 has been rejected by your bank.Please make the payment today and confirm the mode of payment online,google pay,paytm, airtel payment bank,bajaj branch')
    engine.say('Thank you for being our valued customer.Your Bajaj Finserv Loan EMI of Rs 1000 has been rejected by your bank.Please make the payment today and confirm the mode of payment online,google pay,paytm, airtel payment bank,bajaj branch')
    engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('>>>')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source,phrase_time_limit = 3)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    except sr.UnknownValueError:
        print('....')
        
    if command in l2:
        print('Thank you for selecting your preferred payment channel , I will call you back to confirm the payment details.Have a good day.')
        engine.say('Thank you for selecting your preferred payment channel , I will call you back to confirm the payment details.Have a good day.')
        engine.runAndWait()
    elif 'bajaj branch' in command:
        print('Thank you for confirmation,Please carry your checkbook and bank book to register NACH Mandate,Have a good day.')
        engine.say('Thank you for confirmation,Please carry your checkbook and bank book to register NACH Mandate,Have a good day.')
        engine.runAndWait()
elif command in l3:
    print('This is important call , Please Spare a minute. Your Bajaj Finserv Loan EMI of Rs  1000 has been rejected by your bank Please make the payment today and confirm the mode of payment online,google pay,paytm, airtel payment banks, bajaj branch')
    engine.say('This is important call , Please Spare a minute. Your Bajaj Finserv Loan EMI of Rs  1000 has been rejected by your bank Please make the payment today and confirm the mode of payment online,google pay,paytm, airtel payment banks, bajaj branch')
    engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('>>>')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source,phrase_time_limit = 3)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    except sr.UnknownValueError:
        print('....')
    if command in l2:
        print('Thank you for selecting your preferred payment channel , I will call you back to confirm the payment details.Have a good day.')
        engine.say('Thank you for selecting your preferred payment channel , I will call you back to confirm the payment details.Have a good day.')
        engine.runAndWait()
    elif 'bajaj branch' in command:
        print('Thank you for confirmation,Please carry your checkbook and bank book to register NACH Mandate,Have a good day.')
        engine.say('Thank you for confirmation,Please carry your checkbook and bank book to register NACH Mandate,Have a good day.')
        engine.runAndWait()
