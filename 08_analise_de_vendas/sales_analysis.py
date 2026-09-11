sales = [
    ("Notebook", "January", 3500),
    ("Mouse", "January", 80),
    ("Keyboard", "January", 150),

    ("Notebook", "February", 4200),
    ("Mouse", "February", 120),
    ("Keyboard", "February", 180),

    ("Notebook", "March", 3900),
    ("Mouse", "March", 100),
    ("Keyboard", "March", 200)
]


def calculate_total_revenue(sales):
    """Calculate the total revenue from all sales."""

    return sum(value for _, _, value in sales)


def revenue_by_product(sales):
    """Calculate total revenue for each product."""

    result = {}

    for product, _, value in sales:
        if product in result:
            result[product] += value
        else:
            result[product] = value

    return result


def product_with_highest_revenue(sales):
    """Identify the product with the highest revenue."""

    result = revenue_by_product(sales)

    product = max(
        result,
        key=result.get
    )

    return product, result[product]


def revenue_by_month(sales):
    """Calculate total revenue for each month."""

    result = {}

    for _, month, value in sales:
        if month in result:
            result[month] += value
        else:
            result[month] = value

    return result


def month_with_highest_revenue(sales):
    """Identify the month with the highest revenue."""

    result = revenue_by_month(sales)

    month = max(
        result,
        key=result.get
    )

    return month, result[month]


def calculate_average_revenue(sales):
    """Calculate the average revenue per sale."""

    if not sales:
        return 0

    total_revenue = calculate_total_revenue(sales)
    number_of_sales = len(sales)

    return total_revenue / number_of_sales


# Results

total_revenue = calculate_total_revenue(sales)

print(f"Total revenue: R${total_revenue:.2f}")

product, revenue = product_with_highest_revenue(sales)
print(f"Product with highest revenue: {product} - R${revenue:.2f}")

month, revenue = month_with_highest_revenue(sales)
print(f"Month with highest revenue: {month} - R${revenue:.2f}")

average_revenue = calculate_average_revenue(sales)
print(f"Average revenue per sale: R${average_revenue:.2f}")


print("\nRevenue by product:")

for product, revenue in revenue_by_product(sales).items():
    print(f"{product}: R${revenue:.2f}")


print("\nRevenue by month:")

for month, revenue in revenue_by_month(sales).items():
    print(f"{month}: R${revenue:.2f}")

