# Day 1


from itertools import groupby
import math
from pprint import pprint, pformat


# Problem 1
nums = [1, 5, 3, 2, 4, 6, 7, 9, 10]
nums_list = []
nums_range = max(nums)
for k in range(1, nums_range+1):
  nums_list.append(k)
for i in nums_list:
  if i in nums:
    pass
  else:
    print(f"{i} is the missing number!")

print("\n------------------------------------------------------------------- \n")


# Problem 2
results = [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1]
streaks = []
def longest_streak(results):
  streak_count = 0
  for i in results:
    if i == 1:
      streak_count += 1
    streaks.append(streak_count)
    if i == 0:
      streak_count = 0
  
longest_streak(results)

print(f"Your highest streak is: {max(streaks)}")

print("\n------------------------------------------------------------------- \n")


# Problem 3
text = "saksham"
text_dict = dict.fromkeys(text, 0)

for i in list(text):
  text_dict[i] += 1
  try:
    repeated_char = next((k for k, v in text_dict.items() if v == 2))
  except StopIteration:
    continue
  print(f"The first repeated character is: {repeated_char}")
  break

print("\n------------------------------------------------------------------- \n")