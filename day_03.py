# Day 3


# Problem 7
nums = [2, 5, 3, 7, 4, 6, 1, 5, 3, 0]
def count_peaks(nums):
  peaks = 0
  for index,num in enumerate(nums[1 : -1], start=1):
    if num > nums[index+1] and num > nums[index-1]:
      peaks += 1
  return peaks

print(f"No. of Peaks: {count_peaks(nums)}")

print("\n------------------------------------------------------------------- \n")


# Problem 8
nums = [1, 1, 2, 2, 2, 3, 1, 1, 4, 4, 5, 6, 5, 5, 8, 2, 9, 9]
def remove_consecutive(nums):
  return [key for key,group in groupby(nums)]
print(f"{nums} => {remove_consecutive(nums)}")

print("\n------------------------------------------------------------------- \n")


# Problem 9
nums = [4, 10, 15, 21, 30]
dict_nums = dict.fromkeys(nums, 0)
target = 17
def closest_number(nums, target):
  for num in nums:
    if num < target:
      difference = target - num
    elif num > target:
      difference = num - target
    else:
      difference = 0
    dict_nums[num] += difference
  return min(dict_nums, key=dict_nums.get)

print(f"Number closest to {target} is: {closest_number(nums, target)}")

print("\n------------------------------------------------------------------- \n")


# Problem 10
n = 123
n_list =[]
while n > 0:
  n_list.append(n%10)
  n //= 10
n_list.reverse()
def is_special(num_list):
  if sum(num_list) != math.prod(num_list):
    return False
  else:
    return True

print(f"Is_Special? = {is_special(n_list)}")

print("\n------------------------------------------------------------------- \n")