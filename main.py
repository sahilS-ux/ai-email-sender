from email_sender import EmailSender



sender = EmailSender()
my_email = input("Enter your email address: ")
to_email = input("Enter receiver email address: ")
topic = input("Enter topic: ")
friends_name = input("Enter friends name: ")
my_name = input("Enter your name: ")

email_content = sender.generate_email(topic, friends_name, my_name)


print(email_content)
print("---------------------")

confirm = input("\nAre you sure you want to send this email? (y/n): ")

if confirm.lower() == "y":
    sender.send_email(my_email, to_email, my_name, email_content)
    print("Email sent successfully!")
else:
    print("Email cancelled.")