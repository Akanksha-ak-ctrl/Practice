# main.py

from palindrome_checker import is_palindrome

def main():
    string = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

if __name__ == "__main__":
    main()
