'\n    PEP-263 A company manages owns one of more stores.\xe2\x80\x8e\n    '

 
import smtplib
import getpass
 
fromAddress = raw_input("Enter your gmail address: ")
toAddress = raw_input("Enter the recipients email address: ")
subject = raw_input('Enter the subject of email: ')
bodyText = raw_input('Enter the body text: ')
 
msg = "Subject: " + subject + "\n\n" + bodyText
 
#msg="Subject: Hello\n\nHi!! How are you"
 
server=smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
 
password = getpass.getpass('Gmail Password: ')
server.login(fromAddress, password)
server.sendmail(fromAddress, toAddress, msg)
