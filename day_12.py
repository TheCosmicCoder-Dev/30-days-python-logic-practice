# Day 12


# Problem 37
students = [
    {"name": "Rahul", "grade": "A"},
    {"name": "Priya", "grade": "B"},
    {"name": "Aman", "grade": "A"},
    {"name": "Simran", "grade": "C"},
    {"name": "Karan", "grade": "B"},
    {"name": "Neha", "grade": "A"},
    {"name": "Ravi", "grade": "D"},
]

def group_by_grade(students):
  grouped_list = {}
  for student in students:
    if student["grade"] not in grouped_list:
      grouped_list[student["grade"]] = [student["name"]]
    else:
      (grouped_list[student["grade"]]).append(student["name"])
    
  return grouped_list

pprint(group_by_grade(students))

print("\n------------------------------------------------------------------- \n")


# Problem 38
customers = [
    {"name": "Rahul", "spent": 5000},
    {"name": "Priya", "spent": 8000},
    {"name": "Aman", "spent": 3000},
    {"name": "Simran", "spent": 8000},
    {"name": "Karan", "spent": 2000},
    {"name": "Neha", "spent": 8000},
]

def highest_spenders(customers):
  if not(customers):
    return []
  else:
    spendings = []
    
    for customer in customers:
      spendings.append(customer["spent"])
    
    highest_spent = max(spendings)
  
    return [customer["name"] for customer in customers if customer["spent"] == highest_spent]

pprint(highest_spenders(customers))

print("\n------------------------------------------------------------------- \n")

# Problem 39
transactions = [
    {"type": "deposit", "amount": 1000},
    {"type": "withdraw", "amount": 300},
    {"type": "deposit", "amount": 500},
    {"type": "withdraw", "amount": 200},
    {"type": "transfer", "amount": 9999},   
    {"type": "deposit", "amount": 0},       
    {"type": "withdraw", "amount": 0},      
    {"type": "deposit", "amount": 700},
]

def calculate_balance(transactions):
  balance = 0
  
  for transaction in transactions:
    if transaction["type"] == "deposit":
      balance += transaction["amount"]
    elif transaction["type"] == "withdraw":
      balance -= transaction["amount"]
  
  return balance

print(calculate_balance(transactions))

print("\n------------------------------------------------------------------- \n")


# Problem 40
sales = [
    {"product": "Laptop", "quantity": 2, "price": 50000},
    {"product": "Mouse", "quantity": 5, "price": 800},
    {"product": "Laptop", "quantity": 1, "price": 50000},
    {"product": "Mouse", "quantity": 3, "price": 800},
    {"product": "Keyboard", "quantity": 2, "price": 2000},
    {"product": "Mouse", "quantity": 0, "price": 800},
]

def product_report(sales):
  report = {"products": {},"total_revenue": 0}

  for sale in sales:
    if sale["product"] not in report["products"]:
      (report["products"])[sale["product"]] = {"quantity": sale["quantity"], "revenue": sale["price"] * sale["quantity"]}
    else:
      ((report["products"])[sale["product"]])["quantity"] += sale["quantity"]
      ((report["products"])[sale["product"]])["revenue"] += sale["price"] * sale["quantity"]
    report["total_revenue"] += sale["price"] * sale["quantity"]
  
  return report

pprint(product_report(sales))

print("\n------------------------------------------------------------------- \n")