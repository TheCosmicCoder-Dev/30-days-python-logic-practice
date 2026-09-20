# Day 2


# Problem 4
nums = [1, 1, 2, 2, 2, 5, 5, 3, 3, 1, 1, 1, 5, ]
def count_changes(nums):
  changed = 0
  for i,j in enumerate(nums):
    if i == 0:
      continue
    k = nums[i-1]
    if j == k:
      continue
    elif j != k:
      changed += 1
  return changed

print(f"No. of changes: {count_changes(nums)}")

print("\n------------------------------------------------------------------- \n")


# Problem 5
text = "Hello World Python"
words_list = text.split(" ")
def reverse_words():
  wordlist = []
  for i in words_list:
    wordlist.append(i[::-1])
  return " ".join(wordlist)

print(f"{text} => {reverse_words()} (Reversed)")

print("\n------------------------------------------------------------------- \n")


# Problem 6
nums = [10, 3, 8, 15, 6]
def check_difference(nums):
  differences = []
  nums.sort(reverse=True)
  for i,j in enumerate(nums):
    if i < len(nums)-1:
      differences.append(j - nums[i+1])
  return min(differences)
  
print(f"Smallest Difference: {check_difference(nums)}")

print("\n------------------------------------------------------------------- \n")