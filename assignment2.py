# Sachin Tendulkar born 24 April 1973 is an Indian legendary cricketer who bats with the right hand.
import calendar

# Example input for a different cricketer
fullname = input("Enter the player full name: ")
birth_date = int(input("Enter the birth date: "))
birth_month = int(input("Enter the birth month: "))
birth_year = int(input("Enter the birth year: "))
profession = input("Enter the profession: ")
batting_hand = input("Enter the batting hand: ")

# Convert the birth_month integer to the corresponding month name
birth_month_name = calendar.month_name[birth_month]

print(f"{fullname} born {birth_date} {birth_month_name} {birth_year} is an Indian {profession} who bats with the {batting_hand} hand.")
