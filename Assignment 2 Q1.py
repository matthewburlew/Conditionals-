amount = float(input("Enter purchase amount: "))
member = input("Are you a member (yes/no): ").strip().lower()

if member == "yes":
    if amount >= 100:
        discount = 0.15
    else:
        discount = 0.05
elif member == "no":
    if amount >= 150:
        discount = 0.10
    else:
        discount = 0.00
else:
    discount = 0.00
    print("Please enter yes or no next time.")

final_price = amount * (1 - discount)

print("Discount applied:", int(discount * 100), "%")
print("Final price: $", round(final_price, 2))
