# Day 6


# Problem 17
readings = [
  {"sensor": "A", "temperature": 24.5},    {"sensor": "B", "temperature": 31.2},    {"sensor": "C", "temperature": 18.7},
  {"sensor": "D", "temperature": 35.6},    {"sensor": "E", "temperature": 27.4},
]

def check_readings(readings):
  unsafe_readings = []
  for reading in readings:
    if reading["temperature"] > 30:
      unsafe_readings.append({"sensor": reading["sensor"], "temperature": reading["temperature"], "status": "high"})
    elif reading["temperature"] < 20:
      unsafe_readings.append({"sensor": reading["sensor"], "temperature": reading["temperature"], "status": "low"})
  return unsafe_readings

print("Unsafe sensor readings: ")
pprint(check_readings(readings))

print("\n------------------------------------------------------------------- \n")


# Problem 18
sales = [
  {"product": "Laptop", "quantity": 2},
  {"product": "Mouse", "quantity": 5},
  {"product": "Laptop", "quantity": 3},
  {"product": "Keyboard", "quantity": 4},
  {"product": "Mouse", "quantity": 2},
]

def summarize_sales(sales):
  sale_amount = {}
  for sale in sales:
    if sale["product"] not in sale_amount:
      sale_amount[sale["product"]] = sale["quantity"]
    else:
      sale_amount[sale["product"]] += sale["quantity"]
  return sale_amount

print(f"Sales Summary: {pformat(summarize_sales(sales))}")

print("\n------------------------------------------------------------------- \n")


# Problem 19
purchases = [
    {"customer": "Rahul", "amount": 500},
    {"customer": "Priya", "amount": 1200},
    {"customer": "Rahul", "amount": 300},
    {"customer": "Aman", "amount": 700},
    {"customer": "Priya", "amount": 800},
    {"customer": "Rahul", "amount": 200},
]

def summarize_customers(purchases):
  purchase_amount = {}
  for purchase in purchases:
    if purchase["customer"] not in purchase_amount:
      purchase_amount[purchase["customer"]] = {"total": purchase["amount"], "orders": 1}
    else:
     (purchase_amount[purchase["customer"]])["total"] += purchase["amount"]
     (purchase_amount[purchase["customer"]])["orders"] += 1
  return purchase_amount

print("Purchases Summary: ")
pprint(summarize_customers(purchases))

print("\n------------------------------------------------------------------- \n")


# Problem 20
purchases = [
    {"customer": "Rahul", "amount": 500},
    {"customer": "Priya", "amount": 1200},
    {"customer": "Rahul", "amount": 300},
    {"customer": "Aman", "amount": 700},
    {"customer": "Priya", "amount": 800},
    {"customer": "Rahul", "amount": 200},
    {"customer": "Aman", "amount": 100},
]

def analyze_customers(purchases):
  purchase_amount = {}
  purchase_analysis = {}
  for purchase in purchases:
    if purchase["customer"] not in purchase_amount:
      purchase_amount[purchase["customer"]] = {"total": purchase["amount"], "orders": 1}
    else:
     (purchase_amount[purchase["customer"]])["total"] += purchase["amount"]
     (purchase_amount[purchase["customer"]])["orders"] += 1
  for purchase in purchases:
    if (purchase_amount[purchase["customer"]])["total"] >= 1000:
      average = ((purchase_amount[purchase["customer"]])["total"])/((purchase_amount[purchase["customer"]])["orders"])
      purchase_analysis[purchase["customer"]] = {"total": (purchase_amount[purchase["customer"]])["total"], "orders": (purchase_amount[purchase["customer"]])["orders"], "average": round(average, 2)}
  return purchase_analysis
    
print("Active customers Analysis: ")
pprint(analyze_customers(purchases))

print("\n------------------------------------------------------------------- \n")