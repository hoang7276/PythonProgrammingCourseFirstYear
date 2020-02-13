# SpareChange.py  -  A program that calculates my spare change in dollars


def main():
    print("Spare Change Counter")
    print("Please enter the count of each coin type.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
    print()
    print("The total value of your change is", total)
    print("Please enter USD to EUR exchange rate to convert the amount from USD to EUR ", end=" ")
    ExchangeRate = float(input())
    print("Your spare change in EUR amounts to: ", total * ExchangeRate)


main()
