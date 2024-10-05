def display_menu():
    """Display the menu options."""
    print("\nShopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the shopping list")
    print("4. Exit")

def add_item(item):
    """Add an item to the shopping list."""
    shopping_list.append(item)
    print(f'Added "{item}" to the shopping list.')

def remove_item(item):
    """Remove an item from the shopping list."""
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'Removed "{item}" from the shopping list.')
    else:
        print(f'"{item}" not found in the shopping list.')

def view_list():
    """Display the current shopping list."""
    if shopping_list:
        print("\nCurrent Shopping List:")
        for item in shopping_list:
            print(f'- {item}')
    else:
        print("The shopping list is empty.")

def main():
    """Main function to run the shopping list manager."""
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(item)
        elif choice == '3':
            view_list()
        elif choice == '4':
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

shopping_list = []

if __name__ == "__main__":
    main()
