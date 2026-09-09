
sales_database = []


def calculate_total_sales(sales_database):
    """Calculate the total value of sales."""

    total = 0

    for _, quantity, price in sales_database:
        total += quantity * price

    return total


def calculate_best_selling_product(sales_database):
    """Identify the best-selling product by quantity."""

    if not sales_database:
        return None, 0

    sales_by_product = {}

    for product, quantity, _ in sales_database:
        sales_by_product[product] = (
            sales_by_product.get(product, 0) + quantity
        )

    best_selling_product = max(
        sales_by_product,
        key=sales_by_product.get
    )

    return (
        best_selling_product,
        sales_by_product[best_selling_product]
    )


def calculate_total_quantity(sales_database):
    """Calculate the total quantity of products sold."""

    return sum(
        quantity for _, quantity, _ in sales_database
    )


def calculate_average_sales(sales_database):
    """Calculate the average sales value per unit."""

    total_quantity = calculate_total_quantity(
        sales_database
    )

    if total_quantity == 0:
        return 0

    total_sales = calculate_total_sales(
        sales_database
    )

    return total_sales / total_quantity


# Sales registration

register_sale = input(
    "Do you want to register a sale? (y/n): "
).lower()

while register_sale == "y":

    product = input(
        "Enter the product name: "
    )

    quantity = int(
        input("Enter the product quantity: ")
    )

    price = float(
        input("Enter the product price: ")
    )

    sales_database.append(
        (product, quantity, price)
    )

    register_sale = input(
        "Do you want to register another sale? (y/n): "
    ).lower()


# Calculate results

total_sales = calculate_total_sales(
    sales_database
)

total_quantity = calculate_total_quantity(
    sales_database
)

best_selling_product, best_selling_quantity = (
    calculate_best_selling_product(
        sales_database
    )
)

average_sales = calculate_average_sales(
    sales_database
)


# Display results

print("\n===== SALES SUMMARY =====")

print(
    f"Total sales: R$ {total_sales:.2f}"
)

print(
    f"Total quantity of products sold: {total_quantity}"
)

if best_selling_product:

    print(
        f"Best-selling product: "
        f"{best_selling_product} "
        f"(Quantity: {best_selling_quantity})"
    )

else:

    print(
        "Best-selling product: "
        "No sales registered."
    )

print(
    f"Average sales value per unit: "
    f"R$ {average_sales:.2f}"
)

