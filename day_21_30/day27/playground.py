def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(3, 4, 5))


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
        print(kwargs["add"])
        n += kwargs["add"]
        n *= kwargs["multiply"]


calculate(5, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make= "Nissan", model="SkyLine")

print(my_car.model)
print(my_car.make)