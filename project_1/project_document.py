"""
Python Study — Project 1 document
Grocery Shopping Cart

This file is the study plan only.
It explains what we will build and which Python ideas we need.
The cart program itself comes next.
"""

print("=" * 50)
print("PROJECT 1: GROCERY SHOPPING CART")
print("=" * 50)
print("A simple console app to add, remove, view items")
print("and calculate the total cost.")
print()

# ------------------------------------------------------------------
# 1. DATA STORED
# ------------------------------------------------------------------
print("1. DATA STORED")
print("-" * 50)

# Dictionary: item name -> price
# A dictionary stores pairs. Key = item, value = price.
grocery_store = {
    "milk": 40,
    "bread": 30,
    "eggs": 6,
    "rice": 60,
    "apple": 20,
}

print("Grocery Store (dictionary): item : price")
for item, price in grocery_store.items():
    print(f"  {item} : Rs {price}")

print()
print("These prices stay fixed. The user cannot change them.")
print()

# List: items the user adds
# A list stores items in order. It grows and shrinks.
cart = ["milk", "apple", "bread"]

print("Cart (list): items added by the user")
print(f"  Example: {cart}")
print("  This list changes when the user adds or removes items.")
print()

# ------------------------------------------------------------------
# 2. PROGRAM FLOW
# ------------------------------------------------------------------
print("2. PROGRAM FLOW")
print("-" * 50)
print("  1. Start")
print("  2. Welcome message + show available items")
print("  3. Show menu in a loop:")
print("       add / remove / view / checkout")
print("  4. User enters a choice")
print("  5. Perform the action")
print("  6. Repeat the menu until checkout")
print("  7. Checkout: thank-you message and exit")
print()

# ------------------------------------------------------------------
# 3. ACTIONS
# ------------------------------------------------------------------
print("3. ACTIONS (WHAT HAPPENS)")
print("-" * 50)
print("  Add item")
print("    Check if the item exists in the store.")
print("    If yes, add it to the cart list.")
print()
print("  Remove item")
print("    Check if the item is in the cart.")
print("    If yes, remove it from the cart.")
print()
print("  View cart")
print("    Show every item in the cart with its price.")
print("    Calculate and display the total amount.")
print()
print("  Checkout")
print("    Thank-you message.")
print("    End the program.")
print()

# ------------------------------------------------------------------
# 4. PYTHON IDEAS USED IN THIS PROJECT
# ------------------------------------------------------------------
print("4. PYTHON IDEAS USED")
print("-" * 50)
print("  Dictionary  -> store items and prices")
print("  List        -> store the user's cart items")
print("  Loop        -> keep showing the menu")
print("  Conditions  -> decide add / remove / view / checkout")
print()

# Mini study: look up a price from the dictionary
sample_item = "milk"
print("Study example: look up a price")
print(f"  grocery_store['{sample_item}'] = Rs {grocery_store[sample_item]}")
print()

# Mini study: add the prices of items in the example cart
total = 0
print("Study example: calculate total from the example cart")
for item in cart:
    price = grocery_store[item]
    total = total + price
    print(f"  {item} : Rs {price}")
print(f"  Total = Rs {total}")
print()

# ------------------------------------------------------------------
# 5. GOAL
# ------------------------------------------------------------------
print("5. GOAL")
print("-" * 50)
print("Help the user manage their cart and calculate")
print("the total cost easily.")
print()
print("Next step: write the actual cart program.")
print("=" * 50)
