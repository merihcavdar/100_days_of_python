print("welcome to the tip calculator")
total_bill_as_float = float(input("what was the total bill? $"))
percentage_as_int = int(input("what percentage would you like to give? 10, 12 or 15? "))
people_as_int = int(input("how many people to split the bill? "))
bill_with_tip = total_bill_as_float + total_bill_as_float*percentage_as_int/100;

tip = round(bill_with_tip / people_as_int, 2)
final_tip = "{:.2f}".format(tip)
print(f"tip per person is {final_tip}")

