

def add(*args):
    sum_numbers = 0
    for n in args:
        sum_numbers += n
    return sum_numbers

# print(add(5,344,3))


def calculate(n, **kwargs):
    print(kwargs)

    # loop through kwargs as it is done in a normal dictionary
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])    ##returns the value of the key add which is 3
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

# calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("color")
        self.seats = kw.get("seats")
        # benefit of get instead of square brackets:
        # it returns None and there is no error


my_car = Car(make="Nissan")
# print(my_car.model)
