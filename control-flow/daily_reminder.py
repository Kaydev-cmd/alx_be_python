task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

if time_bound == "yes":
  match priority:
    case "high":
      print(f"{task} is a high priority task that requires immediate attention today!")
    case "medium":
      print(f"{task} is a medium priority task that requires immediate attention today")
    case "low":
      print(f"{task} is a low priority task that requires immediate attention today")
    case _:
      print("Invalid error")
else:
  match priority:
    case "high":
      print(f"{task} is a high priority task. Consider completing it when you have free time.")
    case "medium":
      print(f"{task} is a medium priority task. Consider completing it when you have free time.")
    case "low":
      print(f"{task} is a low priority task.  Consider completing it when you have free time.")
    case _:
      print("Invalid error")