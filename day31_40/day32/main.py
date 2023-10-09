import smtplib
import datetime as dt
import random

MY_EMAIL = "merihschach@gmail.com"
MY_PASSWORD = "xwkg gjpb svnt azog"

now = dt.datetime.now()
weekday = now.weekday()

year = now.year
if year == 2020:
    print("wear a mask")
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Monday Motivation\n\n{quote}"
                            )
date_of_birth = dt.datetime(year=1980, month=3, day=10, hour=4)
print(date_of_birth)
