# Console-Based Tax Calculator using Python
# Developed according to FY 2024-25 tax slabs and PEP8 standards

def calculate_old_regime_tax(income):
    # Apply standard and 80C deductions
    deductions = 50000 + 150000  # Standard + 80C
    taxable_income = max(0, income - deductions)

    # Old regime tax slabs for FY 2024-25
    tax = 0
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = 12500 + (taxable_income - 500000) * 0.2
    else:
        tax = 12500 + 100000 + (taxable_income - 1000000) * 0.3
    return tax


def calculate_new_regime_tax(income):
    # No deductions applicable
    taxable_income = income

    # New regime tax slabs for FY 2024-25
    tax = 0
    if taxable_income <= 300000:
        tax = 0
    elif taxable_income <= 600000:
        tax = (taxable_income - 300000) * 0.05
    elif taxable_income <= 900000:
        tax = 15000 + (taxable_income - 600000) * 0.1
    elif taxable_income <= 1200000:
        tax = 15000 + 30000 + (taxable_income - 900000) * 0.15
    elif taxable_income <= 1500000:
        tax = 15000 + 30000 + 45000 + (taxable_income - 1200000) * 0.2
    else:
        tax = 15000 + 30000 + 45000 + 60000 + (taxable_income - 1500000) * 0.3
    return tax


def main():
    while True:
        try:
            ctc = float(input("Enter your CTC (Cost to Company): "))
            bonus = float(input("Enter your Bonus Amount: "))
            total_income = ctc + bonus

            print(f"\nTotal Income: Rs.{total_income:,.0f}")

            old_tax = calculate_old_regime_tax(total_income)
            new_tax = calculate_new_regime_tax(total_income)

            print(f"\nOld Regime Tax Deduction: Rs.{old_tax:,.0f}")
            print(f"New Regime Tax Deduction: Rs.{new_tax:,.0f}")

            if old_tax < new_tax:
                savings = new_tax - old_tax
                print(f"\nYou Save Rs.{savings:,.0f} more using the Old Regime.")
            elif new_tax < old_tax:
                savings = old_tax - new_tax
                print(f"\nYou Save Rs.{savings:,.0f} more using the New Regime.")
            else:
                print("\nBoth regimes result in the same tax deduction.")

            choice = input("\nDo you want to recalculate? (yes/no): ").strip().lower()
            if choice != 'yes':
                print("Thank you for using the Tax Calculator!")
                break
        except ValueError:
            print("Invalid input! Please enter numeric values.\n")


if __name__ == "__main__":
    main()
