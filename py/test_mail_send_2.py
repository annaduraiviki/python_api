import smtplib,getpass,sys

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
pwd = getpass.getpass('please enter your mail password? ')
# Next, log in to the server
server.login("janacute.21@gmail.com", pwd)

# Send the mail
msg = "test!" # The /n separates the message from the headers
server.sendmail("janacute.21@@gmail.com", "janarthanandevs@gmail.com", msg)
