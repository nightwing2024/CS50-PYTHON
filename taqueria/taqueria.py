# Dictionary of items and prices
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_cost = 0
while True:
    try:
        item = input("Enter item: ").title()
    except EOFError:
        break
    if item in menu:
        total_cost += menu[item]
        print(f"Total: ${total_cost:.2f}")
    else:
        print("Invalid item. Please enter a valid item from the menu.")
