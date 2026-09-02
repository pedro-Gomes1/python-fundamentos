accounts = {}


def calculate_debt(debt_amount, interest_rate, installments):
    total_amount = debt_amount * (1 + interest_rate)
    installment_amount = total_amount / installments

    return total_amount, installment_amount


debt_amount = float(input("Enter the debt amount: "))

interest_rates = {
    1: 0.00,
    3: 0.10,
    6: 0.15,
    9: 0.20,
    12: 0.25
}


for installments, interest_rate in interest_rates.items():
    total_amount, installment_amount = calculate_debt(
        debt_amount,
        interest_rate,
        installments
    )

    accounts[installments] = (
        total_amount,
        installment_amount,
        interest_rate
    )


print("\nInstallment Table:")
print("Installments | Total Amount | Installment | Interest Rate")

for installments, (total_amount, installment_amount, interest_rate) in accounts.items():
    print(
        f"{installments:^12} | "
        f"R$ {total_amount:>12.2f} | "
        f"R$ {installment_amount:>11.2f} | "
        f"{interest_rate:>13.2%}"
    )
