# with open("weather_data.csv") as data_file:
#    data = data_file.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))

temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))

print(sum(temp_list)/len(temp_list))
print(data["temp"].mean())
print(data["temp"].max())

# get data in columns
print(data["condition"])
print(data.condition)

# get data in rows

print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = monday.temp
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# create a data from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")
