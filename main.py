x=1
y=16
x = x*1

print(x)

print(x<2 and y<3)

# If condition example

if (x == y):
    print("x and y are equal")
    if (y > 2):
        print("y is greater than 20")
elif(x>20):
    print("x is greater than 2")
else:
    print("nothing matched the criteria")

print("if block is finished")

# while loop example
z = 1
while(z < 12):
    print("z is less than 10", z)
    z += 3


print("while block is finished")


# for loop example 1

fruits = ["first", "middle", "last"]
for i, x in enumerate(fruits):
    if i != 1:
        print(x)
    print(i)


# for loop example 2

for x in range(1,2):
   print(x)
   print(x+1)
   print(x+2)

   x+=3
   print(x)



# break in for loop example

names = ["firstname", "middlename", "lastname", "nickname", "surname"]
for i, name in enumerate(names):
    if i == 3:
        break
    print(name)
print("finished ----------------------------------")

# continue in for loop example

names = ["firstname", "middlename", "lastname", "nickname", "surname"]
for i, name in enumerate(names):
    if i == 3:
        continue
    print(name)
    print(name)
    print(name)
print("finished ----------------------------------")

# assert example

payment = 100
assert payment == 100
print("code to create order")


# nested for loop example 1

numbers = [1, 2, 3]
fruits = ["apple", "banana", "cherry"]

for number in numbers:
    for fruit in fruits:
        print(number, fruit)
print("finished ----------------------------------")


# nested for loop example 2

numbers = [1, 2, 3]
fruits = ["apple", "banana", "cherry"]
names = ["akku", "divya", "ginny"]
x = 1
for number in numbers:
    for fruit in fruits:
        for name in names:
            print(x, "(", number, fruit, name, ")")
            x = x + 1
print("finished ----------------------------------")
print()
print()
