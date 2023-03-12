# Make a function that receives a string as a parameter
# and returns te same string reversed
# BONUS: Check if the string is a palindrome
# Palindrome: a word that is te same from start to en and from end to start

WORD = 'level'

def reverseString(word) -> str:
    letters: list = [char.lower() for char in word]
    letters.reverse()
    return ''.join(letters)

def checkPalindrome(word) -> bool:
    return word.lower() == reverseString(word)
