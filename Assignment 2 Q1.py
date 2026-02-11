def calculate_discount(amount, member):
    if member == "yes":
        if amount >= 100:
            return 0.15
        else:
            return 0.05
    elif member == "no":
        if amount >= 150:
            return 0.10
        else:
            return 0.00
    else:
        print("Please enter yes or no next time.")
        return 0.00


def main():
    amount = float(input("Enter purchase amount: "))
    member = input("Are you a member (yes/no): ").strip().lower()

    discount = calculate_discount(amount, member)
    final_price = amount * (1 - discount)

    print("Discount applied:", int(discount * 100), "%")
    print("Final price: $", round(final_price, 2))


if __name__ == "__main__":
    main()

