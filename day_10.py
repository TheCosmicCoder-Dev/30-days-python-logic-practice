# Day 10


# Problem 31
sales = [
    {"product": "Laptop", "category": "Electronics", "quantity": 3, "price": 50000},
    {"product": "Mouse", "category": "Electronics", "quantity": 10, "price": 800},
    {"product": "Laptop", "category": "Electronics", "quantity": 2, "price": 50000},
    {"product": "Chair", "category": "Furniture", "quantity": 5, "price": 4500},
    {"product": "Mouse", "category": "Electronics", "quantity": 4, "price": 800},
    {"product": "Desk", "category": "Furniture", "quantity": 2, "price": 7000},
]

def product_performance(sales):
  performance_details = {
    "products": {},
    "best_selling_product": None,
    "highest_revenue_product": None}
  sale_quantity = {}
  sale_revenue = {}
  for sale in sales:
    # Set values as default only when the product isn't already assigned. If not, add to the value
    if sale["product"] not in sale_quantity:
      sale_quantity[sale["product"]] = sale["quantity"]
    else:
      sale_quantity[sale["product"]] += sale["quantity"]
    if sale["product"] not in sale_revenue:
      sale_revenue[sale["product"]] = sale["quantity"] * sale["price"]
    else:
      sale_revenue[sale["product"]] += sale["quantity"] * sale["price"]
    # Get the values of products from sale_quantity and sale_revenue and insert into "products"
    (performance_details["products"])[(sale["product"])] = {
        "quantity_sold": sale_quantity[sale["product"]],
        "revenue": sale_revenue[sale["product"]]}
  if sale_quantity:
    data = sale_quantity
    highest_quantity = max((data).values())
    performance_details["best_selling_product"] = [product for product, quantity in data.items() if quantity == highest_quantity]
  else:
    pass
  if sale_revenue:
    data = sale_revenue
    highest_revenue = max((data).values())
    performance_details["highest_revenue_product"] = [product for product, revenue in data.items() if revenue == highest_revenue]
  else:
    pass
  return performance_details

pprint(product_performance(sales))

print("\n------------------------------------------------------------------- \n")


# Problem 32
students = [
    {"name": "Rahul", "marks": [85, 78, 91]},
    {"name": "Priya", "marks": [92, 88, 95]},
    {"name": "Aman", "marks": [64, 72, 69]},
    {"name": "Simran", "marks": [45, 52, 48]},
    {"name": "Karan", "marks": [32, 41, 38]},
]

def classify_students(students):
  result = {
    "students": {},
    "grade_counts": {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }
  }
  
  for student in students:
    if student["marks"]:
      if all(0 <= mark <= 100 for mark in student["marks"]):
        average = round(sum(student["marks"]) / len(student["marks"]), 2)
        if average >= 90:
          grade = "A"
        elif average >= 75:
          grade = "B"
        elif average >= 60:
          grade = "C"
        elif average >= 40:
          grade = "D"
        else:
          grade = "F"
        (result["students"])[student["name"]] = {
          "average": average,
          "grade": grade
        }
        
        (result["grade_counts"])[grade] += 1
      else:
         print("Invalid Marks!")
    else:
        average, grade = None, None
        (result["students"])[student["name"]] = {
            "average": average,
            "grade": grade
        }
  
  return result

pprint(classify_students(students))

print("\n------------------------------------------------------------------- \n")


# Problem 33
transactions = [
    {"user": "Rahul", "type": "purchase", "amount": 500},
    {"user": "Aman", "type": "purchase", "amount": 1200},
    {"user": "Rahul", "type": "refund", "amount": 100},
    {"user": "Priya", "type": "purchase", "amount": 800},
    {"user": "Aman", "type": "purchase", "amount": 300},
    {"user": "Rahul", "type": "purchase", "amount": 700},
    {"user": "Priya", "type": "refund", "amount": 200},
]

def transaction_summary(transactions):
  summary = {}
  
  for transaction in transactions:
    if transaction["type"] == "purchase":
      if transaction["user"] not in summary:
        summary[transaction["user"]] = {
          "total_purchased": transaction["amount"],
          "total_refunded": 0,
          "net_spending": transaction["amount"],
          "transaction_count": 1
        }
      else:
        (summary[transaction["user"]])["total_purchased"] += transaction["amount"]
        (summary[transaction["user"]])["net_spending"] += transaction["amount"]
        (summary[transaction["user"]])["transaction_count"] += 1
    elif transaction["type"] == "refund":
      if transaction["user"] not in summary:
        summary[transaction["user"]] = {
          "total_purchased": 0,
          "total_refunded": transaction["amount"],
          "net_spending": -(transaction["amount"]),
          "transaction_count": 1
        }
      else:
        (summary[transaction["user"]])["total_refunded"] += transaction["amount"]
        (summary[transaction["user"]])["net_spending"] -= transaction["amount"]
        (summary[transaction["user"]])["transaction_count"] += 1
    else:
      if transaction["user"] not in summary:
        summary[transaction["user"]] = {
          "total_purchased": 0,
          "total_refunded": 0,
          "net_spending": 0,
          "transaction_count": 1
        }
      else:
        (summary[transaction["user"]])["total_refunded"] += transaction["amount"]
        (summary[transaction["user"]])["net_spending"] -= transaction["amount"]
        (summary[transaction["user"]])["transaction_count"] += 1
  
  return summary

pprint(transaction_summary(transactions))