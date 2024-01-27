# Inventory Management System

# The inventory is stored in a dictionary.
# Keys are item names and values are quantities.
inventory = {}

# Function to add an item to the inventory
def add_item(item, quantity):
    if item in inventory:
        # Item already exists, increase its quantity
        inventory[item] += quantity
    else:
        # Item doesn't exist, add it to the inventory
        inventory[item] = quantity

# Function to view all items in the inventory
def view_inventory():
    print("\nInventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

# Function to update the quantity of an existing item in the inventory
def update_item(item, quantity):
    if item in inventory:
        # Item exists, update its quantity
        inventory[item] = quantity
    else:
        # Item doesn't exist, print a message indicating it's not found
        print(f"Error: Item '{item}' not found in inventory.")

# Main function to manage the inventory
def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        # Process the user's choice
        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(item, quantity)
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            item = input("Enter item name: ")
            quantity = int(input("Enter new quantity: "))
            update_item(item, quantity)
        elif choice == '4':
            # Exit the program
            break
        else:
            print("Error: Invalid choice. Please enter 1, 2, 3, or 4.")

# Entry point of the program
if __name__ == "__main__":
    manage_inventory()
