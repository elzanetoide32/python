import smtplib
#from decouple import config
mensaje= "hola, esto es una alarma guacho te estan robando"
subject= "prueba de correo"

mensaje='Subject: {}\n\n{}'.format(subject, mensaje)

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('lcgbrlzanetti@gmail.com','Martinaeze11')

server.sendmail('lcgbrlzanetti@gmail.com','lcgbrlzanetti@gmail.com',mensaje)
server.quit()

print("correo enviado exitosamente")