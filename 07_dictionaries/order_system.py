menu = {
    100: ("Hot Dog", 1.20),
    101: ("Simple Bauru", 1.30),
    102: ("Bauru with Egg", 1.50),
    103: ("Hamburger", 1.20),
    104: ("Cheeseburger", 1.30),
    105: ("Soft Drink", 1.00)
}


def calcular_total_pedido(pedido):
    total = 0.0

    for codigo, quantidade in pedido.items():
        nome, preco = menu[codigo]
        total += preco * quantidade

    return total


pedido = {}

while True:
    pergunta = input("Do you want to place an order? (y/n): ").strip().lower()

    if pergunta == "n":
        break

    if pergunta != "y":
        print("Invalid option. Please enter 'y' or 'n'.")
        continue

    try:
        codigo = int(input("Enter the item code: "))
    except ValueError:
        print("Invalid code. Please enter a number.")
        continue

    if codigo not in menu:
        print("Invalid code. Please try again.")
        continue

    try:
        quantidade = int(input("Enter the quantity: "))
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        continue

    if quantidade <= 0:
        print("Quantity must be greater than zero.")
        continue

    if codigo in pedido:
        pedido[codigo] += quantidade
    else:
        pedido[codigo] = quantidade


total = calcular_total_pedido(pedido)

print("\n--- ORDER SUMMARY ---")

if not pedido:
    print("No items were ordered.")
else:
    for codigo, quantidade in pedido.items():
        nome, preco = menu[codigo]
        subtotal = preco * quantidade

        print(
            f"{nome} | "
            f"Code: {codigo} | "
            f"Quantity: {quantidade} | "
            f"Unit price: R$ {preco:.2f} | "
            f"Subtotal: R$ {subtotal:.2f}"
        )

    print(f"\nTotal order: R$ {total:.2f}")
