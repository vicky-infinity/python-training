# Sending e-mails

# Importing the smtplib liberary for sending the email
import smtplib

# SMTP class from the smtplib liberary
smtob = smtplib.SMTP('smtp.gmail.com',587) #this is port number which means TLS enc

# This greets the server to initiate the connection 
print(smtob.ehlo())
print("If the string starts form the 250 which means the connection is good")

# This is to initiate the Enc
print(smtob.starttls())
print("At the end of tclshe string we can see ready to start TLS")



# Now we have to login
# email = input("Enter the Email")
# password =input("Enter the password")

email = "Enter your email"
password ="Enter the app password"

print(smtob.login(email,password))

from_address = email
to_address = email

# subject = input("Enter the subject: ")
# msg = input("Enter your message: ")
subject = "GLASS BOTTLE"
msg = "This is the message"
finalmsg = f"Subject: {subject}\n\n{msg}"


mailsend = smtob.sendmail(from_address, to_address, finalmsg)
print(mailsend)

# Close the session
smtob.quit()