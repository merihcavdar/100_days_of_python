for number in range(1, 10): # not including ten
    print(number)

for number in range(1, 10, 3): # not including ten, third parameter is increment
    print(number)

total = 0
for number in range(2,101, 2): # 101 because to include 100
    total += number
print(total)

total2 = 0
for number in range(1,101):
    if number % 2 == 0:
        total2 += number
print(total2)

