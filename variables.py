

name = "Jack"
print(name)
name = "Angela"
print(name)


name = input("What is your name? ")
length = len(name)
print(length)

a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

print("Welcome to the band name generator.")
city = input("What's the name of city that you grew up in?\n")
pet = input("What's the name of your pet?\n")
print("Your band name is: " + city + " " + pet)
