def is_palindrome(word):
    """
    Checks whether a word is a palindrome or not.
    """
    # Convert the word to lowercase
    word = word.lower()

    # Remove any spaces from the word
    word = word.replace(" ", "")

    # Reverse the word
    reversed_word = word[::-1]

    # Check if the reversed word is the same as the original word
    if word == reversed_word:
        return True
    else:
        return False


# Take input from the user
word = input("Enter a word to check if it's a palindrome: ")

# Check if the input word is a palindrome
if is_palindrome(word):
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")



