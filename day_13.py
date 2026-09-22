# Day 13


# Problem 41
inventory = [
    {"product": "Laptop", "stock": 8, "reorder_level": 5, "price": 50000},
    {"product": "Mouse", "stock": 3, "reorder_level": 10, "price": 800},
    {"product": "Keyboard", "stock": 12, "reorder_level": 8, "price": 2000},
    {"product": "Monitor", "stock": 4, "reorder_level": 5, "price": 15000},
    {"product": "Chair", "stock": 7, "reorder_level": 7, "price": 4500},
    {"product": "Desk", "stock": 2, "reorder_level": 5, "price": 7000},
]

def analyze_inventory(inventory):
  analysis = {
    "products": {},
    "reorder_count": 0,
    "total_inventory_value": 0
  }

  for item in inventory:
    status = "OK" if item["stock"] >= item["reorder_level"] else "Reorder"
    value = item["stock"] * item["price"]
    (analysis["products"])[item["product"]] = {
      "stock": item["stock"],
      "reorder_level": item["reorder_level"],
      "status": status,
      "inventory_value": value
    }
    
    analysis["reorder_count"] += 1 if status == "Reorder" else 0
    analysis["total_inventory_value"] += value
    
  return analysis

pprint(analyze_inventory(inventory), sort_dicts=False)

print("\n-------------------------------------------------------------------\n")


# Problem 42
purchases = [
    {"customer": "Rahul", "product": "Laptop", "quantity": 1, "price": 50000},
    {"customer": "Priya", "product": "Mouse", "quantity": 2, "price": 800},
    {"customer": "Rahul", "product": "Keyboard", "quantity": 1, "price": 2000},
    {"customer": "Aman", "product": "Laptop", "quantity": 2, "price": 50000},
    {"customer": "Priya", "product": "Keyboard", "quantity": 1, "price": 2000},
    {"customer": "Rahul", "product": "Mouse", "quantity": 3, "price": 800},
]

def analyze_purchases(purchases):
  analysis = {
    "customers": {},
    "highest_spender": None
  }
  spendings = {}
  
  for purchase in purchases:
    if purchase["customer"] not in spendings:
      spendings[purchase["customer"]] = purchase["price"] * purchase["quantity"]
    else:
      spendings[purchase["customer"]] += purchase["price"] * purchase["quantity"]
  
  for purchase in purchases:
    value = purchase["price"] * purchase["quantity"]
    quantity = purchase["quantity"]
    
    if purchase["customer"] not in analysis["customers"]:
      (analysis["customers"])[purchase["customer"]] = {
          "total_spent": value,
          "total_items": quantity,
          "purchase_count": 1
      }
    else:
      ((analysis["customers"])[purchase["customer"]])["total_spent"] += value
      ((analysis["customers"])[purchase["customer"]])["total_items"] += quantity
      ((analysis["customers"])[purchase["customer"]])["purchase_count"] += 1

  if purchases:
    highest_spent = max(spendings.values())
    highest_spender = []
  
  for customer, spending in spendings.items():
    if spending == highest_spent:
      highest_spender.append(customer)
    if highest_spender:
      analysis["highest_spender"] = highest_spender
  
  return analysis

pprint(analyze_purchases(purchases), sort_dicts = False)

print("\n-------------------------------------------------------------------\n")


# Problem 43
sales = [
    {"employee": "Rahul", "sales": 120000},
    {"employee": "Priya", "sales": 95000},
    {"employee": "Aman", "sales": 120000},
    {"employee": "Simran", "sales": 75000},
    {"employee": "Karan", "sales": 95000},
]

def sales_leaderboard(sales):
  if sales:
    leaderboard = {
      "employees": {},
      "highest_sales": 0
    }
    employee_sales = sorted([], reverse=True)
    sales_dict = {}
    
    for sale in sales:
      employee_sales.append(sale["sales"])
    
    leaderboard["highest_sales"] += employee_sales[0]
  
    index = 1
    
    for sale in employee_sales:
      if sale not in sales_dict:
        sales_dict[sale] = index
        index += 1
        
    
    for sale in sales:
      (leaderboard["employees"])[sale["employee"]] = {"sales": sale["sales"], "rank": sales_dict[sale["sales"]]}
      
    return leaderboard
  else:
    return {
      "employees": {},
      "highest_sales": 0
    }

pprint(sales_leaderboard(sales), sort_dicts=False)

print("\n-------------------------------------------------------------------\n")