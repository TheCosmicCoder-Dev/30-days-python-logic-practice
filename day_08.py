# Day 8


# Problem 24
class TaskManager:
  def __init__(self):
    self.completed = False
    self.tasks = {}

  def add_task(self, title, priority):
    if title not in self.tasks:
      self.tasks[title] = {"priority": priority, "completed": self.completed}
      print(f"- Task added: {title}")
      return
    print("Task already in list!")

  def remove_task(self, title):
    if title in self.tasks:
      del self.tasks[title]
      print(f"- Task removed: {title}")
      return
    print("No such task!")

  def complete_task(self, title):
    if title in self.tasks:
      (self.tasks[title])["completed"] = True
      return
    print("No such task!")

  def get_pending_tasks(self):
    pending_tasks = {}
    for task in self.tasks:
      if (self.tasks[task])["completed"] == False:
        pending_tasks[task] = self.tasks[task]
    return pending_tasks

  def display_tasks(self):
    pprint(self.tasks)

manager = TaskManager()

manager.add_task("Finish Python practice", "high")
manager.add_task("Read ML article", "medium")
manager.add_task("Clean downloads folder", "low")
print("\n")
manager.complete_task("Clean downloads folder")
manager.get_pending_tasks()
print("\n")
manager.display_tasks()

print("\n------------------------------------------------------------------- \n")

# Problem 25
activities = [
    {"user": "Rahul", "action": "login"},
    {"user": "Aman", "action": "login"},
    {"user": "Rahul", "action": "purchase"},
    {"user": "Rahul", "action": "logout"},
    {"user": "Aman", "action": "purchase"},
    {"user": "Priya", "action": "login"},
]

def summarize_activity(activities):
  activity_summary = {}
  for activity in activities:
    user_action = activity["action"]
    if activity["user"] not in activity_summary:
      user_data = {"login": 0, "purchase": 0, "logout": 0}
      activity_summary[activity["user"]] = user_data
      (activity_summary[activity["user"]])[user_action] += 1
    else:
      (activity_summary[activity["user"]])[user_action] += 1
  return activity_summary

print("Activity Summary: ")
pprint(summarize_activity(activities))

print("\n------------------------------------------------------------------- \n")


# Problem 26
stock = {
  "laptop": 10,
  "mouse": 25,
  "keyboard": 15,
  "headphones": 8
}

updates = [
  {"item": "laptop", "change": -2},
  {"item": "mouse", "change": 5},
  {"item": "keyboard", "change": -15},
  {"item": "webcam", "change": 6},
]

def update_inventory(stock, updates):
  updated_stock = stock.copy()
  for update in updates:
    if update["item"] in updated_stock:
      if updated_stock[update["item"]] + update["change"] >= 0:
        updated_stock[update["item"]] += update["change"]
      else:
        print(f"Invalid update: {(update['item']).capitalize()} would have negative stock.")
    else:
      if update["change"] > 0:
        updated_stock[update["item"]] = update["change"]
      else:
        print(f"Invalid update: {(update['item']).capitalize()} has negative or no stock.")
  return updated_stock

print(f"Updated Stock: {update_inventory(stock, updates)}")

print("\n------------------------------------------------------------------- \n")