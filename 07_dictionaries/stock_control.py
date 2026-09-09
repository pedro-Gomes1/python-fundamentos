stock = {
    "notebook": (10, 3500.00),
    "tablet": (5, 1500.00),
    "smartphone": (20, 2500.00),
    "mouse": (15, 100.00)
}


def calculate_total_stock_value(stock):
    """Calculate the total value of the stock."""
    total = 0

    for item, (quantity, price) in stock.items():
        total += quantity * price

    return total


def find_highest_value_item(stock):
    """Find the item with the highest total value."""
    highest_item = None
    highest_value = 0

    for item, (quantity, price) in stock.items():
        total_value = quantity * price

        if total_value > highest_value:
            highest_value = total_value
            highest_item = item

    return highest_item, highest_value


def find_largest_stock(stock):
    """Find the item with the largest quantity in stock."""
    largest_item = None
    largest_quantity = 0

    for item, (quantity, price) in stock.items():
        if quantity > largest_quantity:
            largest_quantity = quantity
            largest_item = item

    return largest_item, largest_quantity


def find_smallest_stock(stock):
    """Find the item with the smallest quantity in stock."""
    smallest_item = None
    smallest_quantity = 0

    for item, (quantity, price) in stock.items():
        if smallest_item is None or quantity < smallest_quantity:
            smallest_quantity = quantity
            smallest_item = item

    return smallest_item, smallest_quantity


total_quantity = sum(
    quantity for quantity, price in stock.values()
)

largest_item, largest_quantity = find_largest_stock(stock)
smallest_item, smallest_quantity = find_smallest_stock(stock)
highest_value_item, highest_value = find_highest_value_item(stock)
total_stock_value = calculate_total_stock_value(stock)


print("Stock Control:\n")

for item, (quantity, price) in stock.items():
    item_total = quantity * price

    print(f"Item: {item}")
    print(f"Quantity: {quantity}")
    print(f"Unit price: ${price:.2f}")
    print(f"Total value: ${item_total:.2f}")
    print("-" * 30)

print(f"Largest stock: {largest_item} ({largest_quantity} units)")
print(f"Smallest stock: {smallest_item} ({smallest_quantity} units)")
print(f"Total stock value: ${total_stock_value:.2f}")
print(f"Highest-value item: {highest_value_item} (${highest_value:.2f})")
print(f"Total quantity of items: {total_quantity}")
