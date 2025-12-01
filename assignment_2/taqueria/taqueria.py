
"""
taqueria.py
CS50 — Felipe's Taqueria
Prompt user for items until EOF (Ctrl-D). After each valid item, print cumulative total.
"""

MENU = {
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


def price_for(item: str) -> float:
    """
    Return price for a menu item (case-insensitive).
    If item not on menu, return None.
    """
    title = item.strip().title()
    return MENU.get(title)


def main():
    total = 0.0
    try:
        while True:
            item = input("Item: ")
            price = price_for(item)
            if price is not None:
                total += price
                # Print formatted with two decimals
                print(f"Total: ${total:.2f}")
            else:
                print("Item not found")
           
    except EOFError:
        # Move cursor to a new line if user hit Ctrl-D
        print()
        return


if __name__ == "__main__":
    main()
