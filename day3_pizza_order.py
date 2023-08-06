print("welcome to python pizza deliveries")
size = input("what size pizz do you want? S, M or L? ")
add_pepperoni = input ("do you want pepporoni? Y or N. ")
extra_cheese = input("do you want extra cheese? Y or N.")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("you entered something wrong")

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"your final bill is ${bill}")
