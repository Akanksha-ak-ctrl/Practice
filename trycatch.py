import io
from custom_exceptions import MyCustomError

# try catch example

# try:
#   print(x)
# except:
#   print("found a exception")


# handle multiple exceptions

try:
    # y = 4 / 0
    # print(x)
    io.open("asdf.py", "r").read()
except ZeroDivisionError:
    print("zero division error caught")
except NameError:
    print("Name Error occured")
except:
    print("some random exception occured")

print("complete")

# else and finally block

try:
    # y = 4 / 0
    # print(x)
    io.open("testasdf.py", "r").read()
except ZeroDivisionError:
    print("zero division error caught")
except NameError:
    print("Name Error occured")
except:
    print("some random exception occured")
else:
    print("no exception occured")
finally:
    print("try catch is finished")

# throw exception ourself

try:
    y = 4 / 1
    # raise ZeroDivisionError
except ZeroDivisionError:
    print("zero division error caught")
finally:
    print("finished")

# throw custom exception ourself

try:
    y = 4 / 1
    if (y > 2):
        raise MyCustomError()
except ZeroDivisionError:
    print("zero division error caught")
except MyCustomError:
    print("y cannot be greater than 2")
finally:
    print("finished")
