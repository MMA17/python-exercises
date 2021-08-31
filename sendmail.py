import smtplib, ssl

port = 465  # For SSL
username = input("Nhap email/username: ")
password = input("Nhap mat khau: ")
sender_email = username  # Enter your address
receiver_email = sender_email  # Enter receiver address
message = "hello world"
# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(username, password)
    print ("Xin chao " + str(username))
    # TODO: Send email here
    server.sendmail(sender_email, receiver_email, message)