# Given a string, s, return whether or not some permutation of s could form a palindrome.

STRING = 'aaee'

def checkPalindrome(string: str) -> bool:
  # String char list
  charList: list = [char for char in string]

  stringLength: int = len(string)
  evenLength: bool = stringLength % 2 == 0
  oddLength: bool = stringLength % 2 != 0
  # For odd strings
  oddChars: int = 0

  for char in charList:
    if evenLength and (charList.count(char) % 2 != 0):
      return False

    if oddLength:
      if (charList.count(char) % 2) != 0:
        oddChars += 1

  if oddChars % 2 != 1 and oddLength:
    return False

  return True

print(checkPalindrome(STRING))

