# Day 5


# Problem 14
customers = [
    {"name": "Rahul", "age": 17, "purchases": 3},
    {"name": "Priya", "age": 16, "purchases": 0},
    {"name": "Aman", "age": 18, "purchases": 5},
    {"name": "Simran", "age": 17, "purchases": 2},
    {"name": "Arjun", "age": 16, "purchases": 0},
  {"name": "Saksham", "age": 13, "purchases": 10},
]

def active_customers(customers):
  active_customers_list = []
  for customer in customers:
    if customer["purchases"] == 0:
      continue
    else:
      active_customers_list.append(customer)
  return active_customers_list

print("Active Customers: ")
pprint(active_customers(customers))

print("\n------------------------------------------------------------------- \n")


# Problem 15
customers = [
    {"name": "Rahul", "age": 17, "purchases": 3},
    {"name": "Priya", "age": 16, "purchases": 0},
    {"name": "Aman", "age": 18, "purchases": 5},
    {"name": "Simran", "age": 17, "purchases": 2},
]

def prepare_customer_data(customers):
  customer_data = []
  for customer in customers:
    customer_data.append({"name": customer["name"], "purchases": customer["purchases"]})
  return customer_data

print("Customer Data: ")
pprint(prepare_customer_data(customers))

print("\n------------------------------------------------------------------- \n")


# Problem 16
students = [
    {"name": "Rahul", "math": 82, "science": 76},
    {"name": "Priya", "math": 91, "science": 88},
    {"name": "Aman", "math": 64, "science": 71},
    {"name": "Simran", "math": 95, "science": 93},
    {"name": "Arjun", "math": 58, "science": 62},
]

def get_strong_students(students):
  students_list = []
  for student in students:
    average = (student["math"] + student["science"])/2
    if average >= 75:
      students_list.append({"name": student["name"], "average": average})
  return students_list

print("Strong Students: ")
pprint(get_strong_students(students))

print("\n------------------------------------------------------------------- \n")