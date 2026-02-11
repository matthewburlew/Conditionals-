salary = float(input("Enter your annual salary: "))
score = int(input("Enter your performance score (0-100): "))

if score >= 90:
    bonus_percentage = 0.20
elif score >= 80:
    bonus_percentage = 0.10
elif score >= 70:
    bonus_percentage = 0.05
else:
    bonus_percentage = 0.00

bonus_amount = salary * bonus_percentage

print("Performance Bonus:", int(bonus_percentage * 100), "%")
print(f"Bonus Amount: ${bonus_amount:.2f}")



