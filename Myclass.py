class MyClass:
    # Class variables
    class_variable = 10

    # Constructor
    def __init__(self, arg1, arg2):
        self._instance_variable1 = arg1
        self.instance_variable2 = arg2

    # Defining methods
    def method1(self):
        return self._instance_variable1 + self.instance_variable2

    def method2(self, x):
        return self._instance_variable1 * x
    def getInstance1(self):
        return self._instance_variable1
    def setInstance1(self, x1):
        self._instance_variable1 = x1


# Creating objects of MyClass
obj1 = MyClass(10, 20)
obj2 = MyClass(30, 40)
# Accessing instance variables
print(obj1._instance_variable1)

# Accessing class variables
print(MyClass.class_variable)

# Calling methods
print(obj1.method1())
print(obj1.method2(7))

class SubClass(MyClass):
    # Additional methods or attributes can be defined here
    pass

# Creating an object of SubClass
obj3 = SubClass(50, 90)
print(obj3.method1())
obj3.setInstance1(600)
print(obj3.getInstance1())