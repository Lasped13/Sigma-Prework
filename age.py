import datetime
from datetime import date


def get_date():
    user_year = int(input("\nPlease enter a valid year: \n"))
    user_month = int(input("Please enter a valid month: \n"))
    user_day = int(input("Please enter a valid day: \n"))
    return datetime.date(user_year, user_month, user_day)


print("""
Greetings!
I am an age calculator.
If you input a date, I will calculate the difference between today's date, and the date given in years.
Please enter a date!""")

current_date = date.today()
active = True

while active:
    user_date = get_date()
    diff_in_date = current_date - user_date
    print("\nThe difference in years between today's date and the date you provided is: \n" +
          str(int(diff_in_date.days / 365)))
    user_choice = int(input(
        "\nWould you like to pick another date?\nEnter 1 to continue or 2 to quit:\n"))
    if user_choice == 2:
        print("\nGoodbye!")
        active = False
    else:
        print("\nLet's start again!")
        continue
