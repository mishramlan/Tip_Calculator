def calculate_tip(bill, people, tip_percent):
    tip = (bill/people) * (tip_percent/100)
    total = (bill/people) + tip
    return tip, total

if __name__ == "__main__":
    print("Welcome to the tip calculator!\n")
    bill = float(input("What was the total bill?\n$"))
    people = int((input("How many people do you want to split the bill with?\n")))
    tip_percent = float(input("What percentage of your bill would you want your tip to be?\n"))
    tip, total = calculate_tip(bill, people, tip_percent)
    print(f"Each person should pay: ${total:.2f}")