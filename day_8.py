# Day 8


# Problem 27
customers = [
    {"id": 101, "name": "Rahul", "email": "rahul@example.com"},
    {"id": 102, "name": "Priya", "email": "priya@example.com"},
    {"id": 101, "name": "Rahul", "email": "rahul@example.com"},
    {"id": 103, "name": "Aman", "email": "aman@example.com"},
    {"id": 102, "name": "Priya2", "email": "priya@example.com"},
]

def customers_cleanup(customers):
  customer_ids = {}
  for customer in customers:
    if "#id" + str(customer["id"]) not in customer_ids:
      customer_ids["#id" + str(customer["id"])] = {"name": customer["name"], "email": customer["email"]}
  return customer_ids

print("Customer IDs: ")
pprint(customers_cleanup(customers))

print("\n------------------------------------------------------------------- \n")


# Problem 28
sales = [
    {"product": "Laptop", "category": "Electronics", "quantity": 2, "price": 50000},
    {"product": "Mouse", "category": "Electronics", "quantity": 5, "price": 800},
    {"product": "Chair", "category": "Furniture", "quantity": 3, "price": 4500},
    {"product": "Laptop", "category": "Electronics", "quantity": 1, "price": 50000},
    {"product": "Desk", "category": "Furniture", "quantity": 2, "price": 7000},
    {"product": "Mouse", "category": "Electronics", "quantity": 2, "price": 800},
]

def sales_report(sales):
  report = {
    "total_revenue": 0,
    "total_quantity": 0,
    "revenue_by_product": {},
    "revenue_by_category": {}
}
  for sale in sales:
    report["total_revenue"] += sale["quantity"] * sale["price"]
    report["total_quantity"] += sale["quantity"]
    if (sale["product"] not in report["revenue_by_product"]):
      (report["revenue_by_product"])[sale["product"]] = sale["quantity"] * sale["price"]
    else:
      (report["revenue_by_product"])[sale["product"]] += sale["quantity"] * sale["price"]
    if sale["category"] not in report["revenue_by_category"]:
      (report["revenue_by_category"])[sale["category"]] = sale["quantity"] * sale["price"]
    else:
      (report["revenue_by_category"])[sale["category"]] += sale["quantity"] * sale["price"]
  return report

print(sales_report(sales))

print("\n------------------------------------------------------------------- \n")


# Problem 29
orders = [
    {"customer": "Rahul", "product": "Laptop", "quantity": 1, "price": 50000},
    {"customer": "Priya", "product": "Mouse", "quantity": 2, "price": 800},
    {"customer": "Rahul", "product": "Keyboard", "quantity": 1, "price": 2000},
    {"customer": "Aman", "product": "Laptop", "quantity": 2, "price": 50000},
    {"customer": "Priya", "product": "Keyboard", "quantity": 1, "price": 2000},
    {"customer": "Rahul", "product": "Mouse", "quantity": 3, "price": 800},
]

def customer_order_summary(orders):
  order_summary = {}
  for order in orders:
    if order["customer"] not in order_summary:
      order_summary[order["customer"]] = {"total_spent": order["price"]*order["quantity"], "total_items": order["quantity"], "orders": 1}
    else:
      (order_summary[order["customer"]])["total_spent"] += order["price"]*order["quantity"]
      (order_summary[order["customer"]])["total_items"] += order["quantity"]
      (order_summary[order["customer"]])["orders"] += 1
  return order_summary

pprint(customer_order_summary(orders))

print("\n------------------------------------------------------------------- \n")


# Problem 30
students = [
    {"name": "Rahul", "subject": "Math", "marks": 85},
    {"name": "Priya", "subject": "Math", "marks": 92},
    {"name": "Rahul", "subject": "Science", "marks": 78},
    {"name": "Aman", "subject": "Math", "marks": 64},
    {"name": "Priya", "subject": "Science", "marks": 88},
    {"name": "Rahul", "subject": "English", "marks": 91},
    {"name": "Aman", "subject": "Science", "marks": 72},
]

def performance_report(students):
  report = {
  "average_by_student": {},
  "average_by_subject": {},
  "top_student": None
}
  marks_entries = {}
  subject_entries = {}
  for student in students:
    # Preparing marks_entries
    if student["name"] not in marks_entries:
      # Setting values to the student name in marks_entries if the student does not yet exist in marks_entries
      marks_entries[student["name"]] = {"marks": student["marks"], "entries": 1}
    else:
      # Adding to the values of the student name in marks_entries if the student already exists in marks_entries
      (marks_entries[student["name"]])["marks"] += student["marks"]
      (marks_entries[student["name"]])["entries"] += 1
  for student in students:
    # Determining the values of average_by_students in report
    average = round(((marks_entries[student["name"]])["marks"]) / ((marks_entries[student["name"]])["entries"]), 2)
    (report["average_by_student"])[student["name"]] = average
  for student in students:
    # Preparing subject_entries
    if student["subject"] not in subject_entries:
      # Setting values to the student name in subject_entries if the student does not yet exist in subject_entries
      subject_entries[student["subject"]] = {"marks": student["marks"], "entries": 1}
    else:
      # Adding to the values of the student name in subject_entries if the student already exists in subject_entries
      (subject_entries[student["subject"]])["marks"] += student["marks"]
      (subject_entries[student["subject"]])["entries"] += 1
  for student in students:
    # Determining the values of average_by_subjects in report
    average = round(((subject_entries[student["subject"]])["marks"]) / ((subject_entries[student["subject"]])["entries"]), 2)
    (report["average_by_subject"])[student["subject"]] = average
  # Determining top_student in report
  if report["average_by_student"]:
    data = report["average_by_student"]
    highest_average = max((data).values())
    report["top_student"] = [student for student, marks in data.items() if marks == highest_average]
  else:
    pass
  return report

pprint(performance_report(students))

print("\n------------------------------------------------------------------- \n")