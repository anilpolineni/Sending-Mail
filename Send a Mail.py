def sendmail():
    send=int(input("How many friends to send email:\n"))
    friends=[]
    emails=[]
    message=input("Enter Message To Send:\n")
    if send!=0:
        for s in range(0,send):
            name=input("Enter Friend Name:\n")
            email=input("Enter Friend Email:\n")
            friends.append(name)
            emails.append(email)
        print(s)
        import smtplib
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()#transport layer security#ssl
        server.login("anilpolineni008@gmail.com","anil@1234")

        for friend in range(0,len(friends)):
            print(message,":",friends[friend],":",emails[friend])
            server.sendmail("anilpolineni008@gmail.com",emails[friend],message)
        server.quit()
sendmail()    
            
        
    
