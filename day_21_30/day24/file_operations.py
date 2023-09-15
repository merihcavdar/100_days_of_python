with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="a") as file:
    file.write("\nQuel temps fait-il?")


with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
