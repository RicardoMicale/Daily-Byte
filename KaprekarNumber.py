# Check the kaprekar constant
# The kaprekar constant is 6174
# Any 4-digit number with at least 2 different digits and the digits cant repeat more than once

KAPREKAR = 6174

def highToLow(number: str) -> int:
  digits = [char for char in number]
  digits.sort(reverse=True)
  stringDigits = ''.join(digits)
  return int(stringDigits)

def lowToHigh(number: str) -> int:
  digits = [char for char in number]
  digits.sort()
  stringDigits = ''.join(digits)
  return int(stringDigits)

def checkKaprekar(number: int) -> bool:
  if number < 0:
    return False

  descending: int = highToLow(str(number))
  ascending: int = lowToHigh(str(number))

  if descending == ascending:
    return False
  if (number / 1000 >= 10) or (number / 1000 < 1):
    return False

  newNumber = descending - ascending

  if(newNumber == KAPREKAR):
    return True
  else:
    return checkKaprekar(newNumber)

print(checkKaprekar(-1122))
