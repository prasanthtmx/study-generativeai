# Project 1: Grocery Shopping Cart
# Add, remove, view items and calculate the total cost.

grocery_store = {
    "milk": 40,
    "bread": 30,
    "eggs": 6,
    "rice": 60,
    "apple": 20,
}

cart = []


def show_store():
    print("\nAvailable items:")
    for item, price in grocery_store.items():
        print(f"  {item} : Rs {price}")


def add_item():
    item = input("Enter item name to add: ").strip().lower()

    if item in grocery_store:
        cart.append(item)
        print(f"{item} added to cart.")
    else:
        print(f"{item} is not in the store.")


def remove_item():
    item = input("Enter item name to remove: ").strip().lower()

    if item in cart:
        cart.remove(item)
        print(f"{item} removed from cart.")
    else:
        print(f"{item} is not in the cart.")


def view_cart():
    if len(cart) == 0:
        print("\nCart is empty.")
        return

    print("\nYour cart:")
    total = 0
    for item in cart:
        price = grocery_store[item]
        total = total + price
        print(f"  {item} : Rs {price}")

    print(f"Total amount: Rs {total}")


def checkout():
    view_cart()
    print("\nThank you for shopping with us!")


print("==== Welcome to Grocery Shopping Cart ====")
show_store()

while True:
    print("\nMenu:")
    print("  1. Add item")
    print("  2. Remove item")
    print("  3. View cart")
    print("  4. Checkout")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        checkout()
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
