def multiply_two_numbers(num1, num2):
    print("multiple of 2 numbers is", num1 * num2)

def multiply_three_numbers(num1, num2, num3):
    print("multiple of 3 numbers is", num1 * num2 * num3)

def multiply_any_numbers(*nums):
    print("multiple of any numbers is", end="\t")
    answer = 1
    for num in nums:
        answer *= num
    print(answer)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}