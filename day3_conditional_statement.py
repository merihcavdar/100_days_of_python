print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0
if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("what is your age? "))
    if age < 12:
        print("Child tickets are $5")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7")
        bill = 7
    elif 45 <= age <= 55:
        print("everything is going to be ok. have a free ride on us!")
    else:
        print("Adult tickets are $12")
        bill = 12

    wants_photo = input("do you want a  photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
        print(f"please pay totally {bill}")
    else:
        print(f"please totally {bill}")
else:
    print("sorry you have to grow taller before you can ride.")