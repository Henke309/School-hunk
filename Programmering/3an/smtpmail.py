# Skicka mail i 

import smtplib, sys, email.utils, mailconfig, getpass 

mailserver = mailconfig.smtpservername

# From, To, Tos, Subj, Date

From = mailconfig.smtpusername
To = input("Till? ").strip()
Tos = To.split(";")
Subj = input("Ämne? ").strip()
Date = email.utils.formatdate() #datetime, rfc2822

text = "From: {}\nto: {}\nDate: {}\nSubject: {}\n\n".format(From, To, Date, Subj)

print("Skriv ditt meddelande. Avsluta med CTRL+Z")

while True:
    line = sys.stdin.readline()
     if not line:
         break    #Avslutar med CTRL+Z
    text += line 

print("Connecting...")
mailpasswd = getpass.getpass("Password för användaren? ")

server = smtplib.SMTP_SSL(mailserver)
server.login(From, mailpasswd)

failed = server.sendmail(From, Tos, text)

if failed:
    print("Det blev fel!")
else:
    print("Det gick bra!")
    