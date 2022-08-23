import string

from introductionToPython.encoding import letters, letters_code, encoded_word


def encoding():
    word = input("what will you like to encode: ")
    key = int(input(" your key? "))

    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase

    lower_letters_code = lower_letters[key:] + lower_letters[:key]
    upper_letters_code = upper_letters[key:] + upper_letters[:key]

    letters = lower_letters + upper_letters
    letters_code = lower_letters_code + upper_letters_code
print(encoding())


def decoding():
    decoded_word = encoded_word.translate(str.maketrans(letters_code, letters))
print(decoding())