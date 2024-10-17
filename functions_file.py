def multiply_two_numbers(num1, num2):
    print("multiple of 2 numbers is", num1 * num2)


multiply_two_numbers(2, 3)
multiply_two_numbers(3, 3)
multiply_two_numbers(3, 5)



def multiply_any_numbers(*nums):
    print("multiple of any numbers is", end="\t")
    answer = 1
    for num in nums:
        answer *= num
    print(answer)

multiply_any_numbers(2,3,3)
print("finished ----------------------------------")


def print_third_child(*kids):
  print("The youngest child is " + kids[2])

print_third_child("Emil", "Tobias", "Linus")

print("finished ----------------------------------")


def print_third_child_arb(**kids):
    print("The youngest child is " + kids["child2"])

print_third_child_arb(child3 = "Emil", child2 = "Tobias", child1 = "Linus")
print("finished ----------------------------------")


def print_third_child_default(kid = "akanksha"):
    print("The child is " + kid)

print_third_child_default("rohan")
print_third_child_default()

print("finished ----------------------------------")


def return_double_value(x):
    return x * 2
y = return_double_value(5)
print(y)

