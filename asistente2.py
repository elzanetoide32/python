import pyttsx3 as habla
lupita= habla.init()
#help(lupita)

acentos= lupita.getProperty("voices")
print(acentos)

for acento in acentos:
    print(acento.id)

lupita.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0")


lupita.setProperty('rate', 150)
lupita.say("hola como anda luca ¿hoy se siente cansado y fatigado? ¿quiere que le lea un cuento?")
lupita.runAndWait()