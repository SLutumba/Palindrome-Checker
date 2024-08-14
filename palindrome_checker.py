def main():
    print("A palindrome is a word that is read the same forwards and back.\n"
          "This program will check if any word you enter is a palindrome\n")
    check = "y"

    while repeat(check):
        # prompt user for input
        word = prompt()

        # ensure user enters only one word
        while not verify_input(word):
            print("Please enter only one word")
            word = str(input()).lower()

        # check if the word entered is a palindrome
        palindrome_checker(word)

        # prompt for a repeat of the app or exit
        print("To check another word, press 'y' and to end the program, press 'n': ")
        check = input().lower()


def prompt() -> str:
    print("Enter the word you want to check is a palindrome: ")
    word = str(input()).lower()
    return word


def verify_input(word: str) -> bool:
    # check if user entered only one word
    if " " in word:
        print("Invalid input, enter only one word")
        return False
    return True


def palindrome_checker(word: str):
    if word == word[::-1]:
        print(f"'{word}' is a palindrome")
    else:
        print(f"'{word}' is not a palindrome")


def repeat(check: str) -> bool:
    while check != "y" and check != "n":
        print("Invalid input please enter 'y' to check another word or 'n' to exit: ")
        check = input().lower()
    if check == "y":
        return True
    return False


if __name__ == "__main__":
    main()
