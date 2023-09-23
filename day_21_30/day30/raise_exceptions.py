height = float(input("height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("cant be over 3")

bmi = weight / height ** 2
