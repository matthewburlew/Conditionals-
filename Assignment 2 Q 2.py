salary = float(input("Enter your annual salary: "))
score = int(input("Enter your performance score (0-100): "))

if score >= 90:
    bonus_percentage = 0.10
elif score >= 80:
    bonus_percentage = 0.10
elif score >= 70:
    bonus_percentage = 0.05
else: 
    bonus_percentage = 0.00

bonus_amout = salary *bonus_percentage

print("Performance Bonus: ", bonus_percentage*100, "%")
print("Bonus Amount: $", round(bonus_amout, ))

