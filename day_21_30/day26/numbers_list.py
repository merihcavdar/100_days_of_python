numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num*num for num in numbers]

result = [num for num in numbers if num % 2 == 0]

with open("file1.txt") as file1:
    file_1_data = file1.readlines()


with open("file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]

print(result)

