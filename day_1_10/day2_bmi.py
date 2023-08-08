height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / height **2

bmi_as_int = round(bmi)
print(f"your bmi is: {bmi_as_int}")

if bmi_as_int < 18.5:
    print("underweight")
elif bmi_as_int < 25:
    print("normal weight")
elif bmi_as_int <30:
    print("overweight")
elif bmi_as_int < 35:
    print("obese")
else:
    print("clinically obese")