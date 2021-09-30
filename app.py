from smtplib import SMTP

try:

    subcjet = "Test"
    message = "Merhaba Ben Yusuf"
    content = "Subject: {0}\n\n{1}".format(subcjet,message)


    myMailAdress ="1yazilimdiski@gmail.com"
    password = "yusuf1903"

    sendTo = "12yazilimdiski@gmail.com"

    mail = SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(myMailAdress,password)
    mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
    print("ok")
except Exception as e:
    print("error".format(e))