def greet():
    print("hallo")
    print("how do you do?")
    print("Isn't the weather nice today?")


greet()

# daf some_function(parameter)
# some_function(argument)

def greet_with_name(name):
    print(f"hallo {name}")
    print(f"how do you do {name}?")


greet_with_name("Merih")

# functions with more than one input (positional arguments)
def greet_with(name, location):
    print(f"hello {name}")
    print(f"what is it like to be in {location}")

greet_with("merih", "münchen")

# keyword arguments

greet_with(location="london", name="sabina")