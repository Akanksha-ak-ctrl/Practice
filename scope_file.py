x = 1
def scope_of_x():
    x = 2
    x = x + 20
    def myinnerfunc():
        global x
        x = 7
        print(x)

    myinnerfunc()
    print(x)

scope_of_x()
print(x)

# Introduction to Variable Scope

# Local Scope in Python
def myfunc():
  x = 300
  print(x)

myfunc()


# Function Inside Function
def myfunc():
  x = 400
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()



# Global Scope.
x = 500

def myfunc():
  x = 300
  print(x)

myfunc()

print(x)



# Global Keyword.
x = 600
def myfunc():
  global x
  x = 900

myfunc()

print(x)
