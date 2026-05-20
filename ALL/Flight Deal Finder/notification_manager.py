import smtplib

MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "your_app_password"

class NotificationManager:
    def send_emails(self, email_list, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in email_list:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:Low Price Alert!\n\n{message}"
                )
                print(f"Email sent to {email}")