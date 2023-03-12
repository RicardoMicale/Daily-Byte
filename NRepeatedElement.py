# You are given an integer array, nums, which contains 2N elements.
# Within nums there are N + 1 unique elements and a specific element occurs N times.
# Return the element within nums that appears N times.
#Ex: given [3, 3, 5, 1], return 3

NUMS = [4, 2, 4, 5, 4, 1]

def checkNthNumber(nums) -> int:
  for num in nums:
    if nums.count(num) > 1:
      return num

  return None

print(checkNthNumber(NUMS))
