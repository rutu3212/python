# List of months categorized by season
summer_months = ["april", "may", "june", "july"]
winter_months = ["november", "december", "january", "february"]
monsoon_months = ["august", "september", "october", "march"]

# User input for month
your_month = input("Enter a month: ").lower()

if your_month in summer_months:
    print(f"Hey, {your_month} is a summer month!")
elif your_month in winter_months:
    print(f"Hey, {your_month} is a winter month!")
elif your_month in monsoon_months:
    print(f"Hey, {your_month} is a monsoon month!")
else:
    print("Please enter a valid month name.")

# Boolean type logic: Senior citizen discount eligibility
age = int(input("Enter your age: "))
is_member = True  # Assume the user is a member of a club
has_loyalty_card = False  # Assume the user does not have a loyalty card

if age >= 60 and is_member:
    print("Congratulations! You are eligible for a senior citizen discount.")
elif age < 60 and has_loyalty_card:
    print("You get a special discount for having a loyalty card!")
else:
    print("Sorry, no discount is available for you.")
