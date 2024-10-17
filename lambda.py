# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

print("finished -----------")


# Practical use of Lambda Functions

def myfunc(n):
  return lambda a : a * n

double_the_number = myfunc(2)
triple_the_number = myfunc(3)

print(double_the_number(11))
print(triple_the_number(11))