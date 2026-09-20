# Day 11


# Problem 34
sales = [
    {"product": "Laptop", "category": "Electronics", "quantity": 3, "price": 50000},
    {"product": "Mouse", "category": "Electronics", "quantity": 5, "price": 800},
    {"product": "Chair", "category": "Furniture", "quantity": 2, "price": 4500},
    {"product": "Laptop", "category": "Electronics", "quantity": 1, "price": 50000},
    {"product": "Desk", "category": "Furniture", "quantity": 2, "price": 7000},
    {"product": "Mouse", "category": "Electronics", "quantity": 3, "price": 800},
    {"product": "Pen", "category": "Stationery", "quantity": 10, "price": 20},
    {"product": "Notebook", "category": "Stationery", "quantity": 4, "price": 50},
    {"product": "Pen", "category": "Stationery", "quantity": 5, "price": 20},
    {"product": "Monitor", "category": "Electronics", "quantity": 0, "price": 15000},
]

def category_sales(sales):
  sales_categories = {}
  
  for sale in sales:
    if sale["category"]  not in sales_categories:
      sales_categories[sale["category"]] = {
        "quantity": sale["quantity"],
        "revenue": sale["price"] * sale["quantity"]
      }
    else:
      (sales_categories[sale["category"]])["quantity"] += sale["quantity"]
      (sales_categories[sale["category"]])["revenue"] += sale["price"] * sale["quantity"]
      
  return sales_categories

pprint(category_sales(sales))

print("\n------------------------------------------------------------------- \n")


# Problem 35
products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mouse", "price": 800},
    {"name": "Keyboard", "price": 2000},
    {"name": "Monitor", "price": 15000},
    {"name": "Headphones", "price": 2000},
    {"name": "Pen", "price": 20},
]

def filter_expensive_products(products, cutoff):
  expensive_products = []

  for product in products:
    if product["price"] >= cutoff:
      expensive_products.append(product)
  
  return expensive_products

pprint(filter_expensive_products(products, 2000))

print("\n------------------------------------------------------------------- \n")


# Problem 36
employees = [
    {"name": "Rahul", "department": "IT", "salary": 50000},
    {"name": "Priya", "department": "HR", "salary": 45000},
    {"name": "Aman", "department": "IT", "salary": 60000},
    {"name": "Simran", "department": "HR", "salary": 50000},
    {"name": "Karan", "department": "Sales", "salary": 40000},
    {"name": "Neha", "department": "IT", "salary": 55000},
]

def salary_summary(employees):
  salary_summary = {}
  
  for employee in employees:
    if employee["department"] not in salary_summary:
      salary_summary[employee["department"]] = {
        "employees": 1,
        "total_salary": employee["salary"]
      }
    else:
      (salary_summary[employee["department"]])["employees"] += 1
      (salary_summary[employee["department"]])["total_salary"] += employee["salary"]
  
  return salary_summary

pprint(salary_summary(employees))

print("\n------------------------------------------------------------------- \n")