# palindrome_checker.py

def is_palindrome(s):
    """
    Check if the given string is a palindrome.
    """
    s = s.lower()  # Convert the string to lowercase for case-insensitive comparison
    return s == s[::-1]
