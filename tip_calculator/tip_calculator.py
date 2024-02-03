import argparse

def calculate_tip(bill, people, tip_percent):
    tip = (bill/people) * (tip_percent/100)
    total = (bill/people) + tip
    return tip, total

def main():
    parser = argparse.ArgumentParser(description="Calculate the tip you want to pay")
    parser.add_argument("bill", type=float, help="Billed Amount")
    parser.add_argument("people", type=int, help="Number of people you want to split the bill with")
    parser.add_argument("tip_percent", type=float, help="The percentage of bill you want to tip")
    args = parser.parse_args()
    tip, total = calculate_tip(args.bill, args.people, args.tip_percent)
    print(f"Each person should pay: ${total:.2f}")
if __name__ == "__main__":
    main()