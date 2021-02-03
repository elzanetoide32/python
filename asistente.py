import webbrowser
import speech_recognition as sr
r= sr.Recognizer()
with sr.Microphone() as source:
    print("hola, soy tu asistente virtual: ")
    audio=r.listen(source)
    try:
        text= r.recognize_google(audio)
        print("'has dicho: {}".format(text))
        print(text)
        if "youtube" in text:
            webbrowser.open('https://www.youtube.com/?gl=AR&tab=w1')
        if"clarin"in text:
            webbrowser.open('https://www.clarin.com/')
    except:
        print("no te he entendido")