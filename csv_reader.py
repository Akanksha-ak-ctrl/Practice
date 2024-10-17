class CustomException(Exception):
    pass

def read_csv(file_path, target_word):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if target_word in line:
                    raise CustomException(f"The word '{target_word}' is found in the CSV file.")
        print(f"The word '{target_word}' is not found in the CSV file.")
    except FileNotFoundError:
        print("The CSV file is not found.")
    except CustomException as e:
        print(e)

def main():
    file_path = 'data.csv'
    target_word = input("Enter the word to search in the CSV file: ")
    read_csv(file_path, target_word)

if __name__ == "__main__":
    main()
