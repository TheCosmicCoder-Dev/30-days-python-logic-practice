# Day 4


# Problem 11
nums = [12, 5, 8, 20, 15, 20, 3, 17, 19, 19, 18]
dict_nums = dict.fromkeys(nums, 0)
target = max(nums)
def closest_number(nums, target):
  for num in nums:
    if num < target:
      difference = target - num
    elif num == target:
      pass
    dict_nums[num] += difference
  return f"Second greatest no. is: {min(dict_nums, key=dict_nums.get)}"

print(closest_number(nums, target))

print("\n------------------------------------------------------------------- \n")


# Problem 12
transactions = [
  ("Rahul", 1200),
  ("Aman", 500),
  ("Rahul", 800),
  ("Priya", 1500),
  ("Aman", 700),
  ("Rahul", 500),
  ("Priya", 500),
  ("Aman", 300),
  ("Priya", 500),
]
transactions_dict = {}
def analyze_transactions(transactions):
  if transactions:
    for transaction in transactions:
      (name, amount) = transaction
      if name not in transactions_dict:
        transactions_dict[name] = 0
        transactions_dict[name] += amount
      else:
        transactions_dict[name] += amount
    transactions_list = list(transactions_dict.items())
    transactions_list.sort(reverse=True)
    if len(transactions_list) >= 3:
      print(transactions_list[:3])
    else:
      print(transactions_list)
  else:
    print("No transactions 🫤")

analyze_transactions(transactions)

print("\n------------------------------------------------------------------- \n")


# Problem 13
old_inventory = {
  "laptop": 10,
  "mouse": 25,
  "keyboard": 15,
  "monitor": 8,
  "headphones": 20
}

new_inventory = {
  "laptop": 7,
  "mouse": 30,
  "keyboard": 15,
  "webcam": 12,
  "headphones": 14
}

inventory_changes = {}

def compare_inventory(old, new):
  for item in new:
    if item in old and new[item] - old[item] < 0 or item in old and new[item] - old[item]> 0:
      inventory_changes[item] = new[item] - old[item]
    elif item not in old:
      inventory_changes[item] = new[item]
  return inventory_changes

def analyze_inventory(old, new):
  results = {
    "added": [],
    "removed": [],
    "increased": [],
    "decreased": [],
    "unchanged": [],
  }
  for item in new:
    if item not in old:
      results["added"].append(f"{item}({inventory_changes[item]})")
    elif new[item] == old[item]:
      results["unchanged"].append(item)
    elif inventory_changes[item] > 0:
      results["increased"].append(f"{item}({inventory_changes[item]})")
    elif inventory_changes[item] < 0:
      results["decreased"].append(f"{item}({inventory_changes[item]})")
  for item2 in old:
    if item2 not in new:
      results["removed"].append(f"{item2}({old[item2]})")
    else:
      continue
  return results
      
print("Inventory Changes: ")
pprint(compare_inventory(old_inventory, new_inventory))
print("Analysis: ")
pprint(analyze_inventory(old_inventory, new_inventory))

print("\n------------------------------------------------------------------- \n")