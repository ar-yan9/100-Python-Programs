import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "your_app_password"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("d:/GITHUB/100 Python Programs/Birthday Wisher/birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"d:/GITHUB/100 Python Programs/Birthday Wisher/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
        print("Email sent successfully!")
