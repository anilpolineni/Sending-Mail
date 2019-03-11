import smtplib   
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls() #transport layer security
server.login('anilpolineni008@gmail.com','anil@1234')
server.sendmail('anilpolineni008@gmail.com','anil.p@apssdc.in',"hi i'm anil from apssdc")
print('successfully send...!')
