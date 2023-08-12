# like table, key -> value

# {Key: Value}
# {'bug': 'amkuyleakuyk'}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary['Bug'])
# print(programming_dictionary['bug']) // case sensitive
# print(programming_dictionary[Function]) # not a string

programming_dictionary["Loop"] = "The action of doing something over and over again."

empty_list = []
empty_dictionary = {}

# wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

# Editing an item in a dictionary
programming_dictionary["Bug"] = "new definition"

print(programming_dictionary)

# loop through a dictionary
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])