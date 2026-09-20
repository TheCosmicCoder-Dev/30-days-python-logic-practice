Day 7


# Problem 21
class Profile:
  def __init__(self, name, headline, skills, experience, location, password):
    self.name = name
    self.headline = headline
    self.skills = skills
    self.experience = experience
    self.location = location
    self.__password = password
  
  def display_profile(self):
    return pformat({(f"Name: {self.name}, Headline: {self.headline}, Skills: {self.skills}, Experience: {self.experience}, Location: {self.location}")})
    
  def add_skill(self, skill_to_add):
    self.skills.append(skill_to_add)
    print(f"- Skill added: {skill_to_add}")
    
  def remove_skill(self, skill_to_remove):
    self.skills.pop(self.skills.index(skill_to_remove))
    print(f"- Skill removed: {skill_to_remove}")
    
  def update_headline(self, new_headline):
    self.headline = new_headline
    print(f"- Headline Updated: {new_headline}")
    
  def change_password(self):
    validation = input(">>> Enter old password: ")
    if validation == self.__password:
      new_password = input(">>> Enter new password: ")
      self.__password = new_password
      print("- Password Changed Successfully! ")
      return
    print("- Wrong Password!")

user = Profile(
    "Saksham",
    "Student",
    ["Python", "HTML", "CSS", "Cyber Security"],
    "Nil",
    "Punjab, India",
    "69696969"
   )
print(user.display_profile())
print("\n")
user.add_skill("Table-Tennis")
user.remove_skill("Cyber Security")
user.update_headline("Student and Python Coder")
user.change_password()

print("\n-------------------------------------------------------------------\n")


# Problem 22
class BankAccount:
  def __init__(self,balance):
    if balance < 0:
      raise ValueError("Balance cannot be negative!")
    self.balance = balance
    self.transactions = []
    
  def deposit(self):
    try:
      depo = int(input("Enter Deposit Amount: ₹"))
      if depo == 0:
          pass
      elif depo > 0:
        self.balance += depo
        print(f"Deposit Successful, Current Balance: ₹{self.balance}")
        self.transactions.append(f"Deposited: ₹{depo}")
      else:
        print("Deposit Amount has to be postive!")
        return
    except ValueError:
      print("Deposit amount has to be a number!")
      return
    
  def withdraw(self):
    try:
      withdrawal_amount = int(input("Enter withdrawal Amount: ₹"))
      if withdrawal_amount == 0:
          pass
      elif withdrawal_amount < 0:
        print("Withdrawal Amount has to be positive!")
        return
      elif withdrawal_amount <= self.balance:
        self.balance -= withdrawal_amount
        print(f"Withdrawal Successful, Current Balance: ₹{self.balance}")
        self.transactions.append(f"Withdrew: ₹{withdrawal_amount}")
      else:
        print("Insufficient Funds!")
        return
    except ValueError:
      print("Withdrawal Amount has to be a number!")
      return
    
  def check_balance(self):
    print(f"Balance: ₹{self.balance}")
      
  def show_transactions(self):
      if self.transactions == []:
          pass
      else:
          print(self.transactions)
    
Rahul = BankAccount(100000)
Rahul.deposit()
Rahul.withdraw()
Rahul.check_balance()
Rahul.show_transactions()

print("\n-------------------------------------------------------------------\n")


# Problem 23
class ShoppingCart:  
  def __init__(self):  
    self.cart = {}  
    
  def add_item(self, name, price, quantity):  
    if name not in self.cart:   
      self.cart[name] = {"price": price, "quantity": quantity}  
      print(f"- Product added to cart: {name}")  
      return  
    (self.cart[name])["quantity"] += quantity  
      
  def remove_item(self, name):  
    try:  
      del self.cart[name]  
      print(f"Product removed from cart: {name}")  
    except KeyError:  
      print("Product not in cart!")  
      
  def calculate_total(self):  
    total = 0  
    for product in self.cart:  
      total += (self.cart[product])["price"] * (self.cart[product])["quantity"]  
    print(f"Your Total is: {total}")  
      
  def display_cart(self):  
    print(self.cart)  
  
cart = ShoppingCart()  
  
cart.add_item("Keyboard", 1200, 1)  
cart.add_item("Mouse", 700, 2)  
cart.add_item("Keyboard", 1200, 2)  
  
cart.calculate_total()  
cart.display_cart()

print("\n-------------------------------------------------------------------\n")