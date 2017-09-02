import smtplib
connection = smtplib.SMTP_PORT  ('smtp.gmail.com' , 587) #SMTP domain name like gmail, yahoo, hotmail, etc.
connection.ehlo()
connection.starttls()
connection.login('kumar.nitish607@gmail.com' , 'Password') #Sender's userid and password.
connection.sendmail('kumar.nitish607@gmail.com' , 'singhpiyush884@gmail.com' , 'This is my massege') #Sender mailid, receiver mailid and massage.
connection.quit() #disconnect program.

#By Nitish Singh Chauhan