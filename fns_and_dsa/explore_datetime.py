from datetime import datetime, timedelta

def display_current_datetime():
  current_date = datetime.now()
  formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print("Current date and time:", formatted_date)
  
display_current_datetime()

number_of_days = int(input("Enter number of days to add: "))

def calculate_future_date():
  future_date = datetime.now() + timedelta(days=number_of_days)
  formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Date after {number_of_days} days will be:", formatted_future_date)

calculate_future_date()