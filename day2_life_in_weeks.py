age = input("what is your current age? ")

remaining_years = 90 - int(age)
remaining_days = remaining_years * 365
remaining_weeks = remaining_days / 7
remaining_months = remaining_years * 12

print(f"You have {remaining_days} days, {remaining_months} months, {round(remaining_weeks)} weeks, {remaining_years} years left.")
