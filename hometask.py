#2
def decorator(func):
    def wrapper(expression):
        try:
            return func(expression)
        except IndexError:
            print("There is an index error")
        except NameError:
            print("There is a name error")
        except TypeError:
            print("There is a type error")
    return wrapper

@decorator
def calculate(expression):
    print(eval(expression))
calculate("2+2")
calculate("5+5")
calculate(5)
calculate("adadadad")