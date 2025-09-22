def display_menu():
  print("Shopping List Manager")
  print("1. Add item")
  print("2. Remove item")
  print("3. View items")
  print("4. Exit")
  
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"{item} added to the shopping list.")
        
        if choice == "2":
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the shopping list.")
            else:
                print(f"{item} not found in the shopping list.")
                
        if choice == "3":
            if shopping_list:
                print("Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("The shopping list is empty.")
                
        if choice == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()