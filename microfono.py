import speech_recognition as sr
import webbrowser
import pyttsx3 as habla

lupita= habla.init()
r= sr.Recognizer()
acentos= lupita.getProperty("voices")
print(acentos)

for acento in acentos:
    print(acento.id)

lupita.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0")
lupita.setProperty('rate', 250)

while True:
    with sr.Microphone() as source:
        print("di algo...")
        audio=r.listen(source)
        
        try:
            text= r.recognize_google(audio, language='es-ES')
            print("dijistes: {}".format(text))
            
            if "poneme música" in text:
                webbrowser.open('https://www.youtube.com/watch?v=FR5youNV7Cg&list=LL&index=9')
                lupita.say("abriendo youtube")
                lupita.runAndWait()
                
            if "Qué pasó de nuevo"in text:
                webbrowser.open('https://www.clarin.com/')
                lupita.say("abriendo clarin")
                lupita.runAndWait()
                    
        except:
            print("perdona no te entendi")







