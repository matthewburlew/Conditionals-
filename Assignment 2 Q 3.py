def determine_risk(credit_score, income):
    if credit_score >= 720 and income >= 60000:
        return "Low Risk"
    elif credit_score >= 650 and income >= 40000:
        return "Medium Risk"
    else:
        return "High Risk"


def main():
    credit_score = int(input("Enter your credit score: "))
    income = float(input("Enter your annual income: "))

    risk = determine_risk(credit_score, income)

    print("Loan Risk Category:", risk)


if __name__ == "__main__":
    main()
