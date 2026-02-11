def calculate_bonus_percentage(score):
    if score >= 90:
        return 0.20
    elif score >= 80:
        return 0.10
    elif score >= 70:
        return 0.05
    else:
        return 0.00


def main():
    salary = float(input("Enter your annual salary: "))
    score = int(input("Enter your performance score (0-100): "))

    bonus_percentage = calculate_bonus_percentage(score)
    bonus_amount = salary * bonus_percentage

    print("Performance Bonus:", int(bonus_percentage * 100), "%")
    print(f"Bonus Amount: ${bonus_amount:.2f}")


if __name__ == "__main__":
    main()





