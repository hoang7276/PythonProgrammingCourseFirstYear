# This program calculates the price per sqm of a house


def main():
    print("Price per square meter calculator")
    print("Please enter the price of the house in EUR", end=" ")
    HousePrice = int(input())
    print("Please enter the number of square meters of the house", end=" ")
    HouseSurface = float(input())
    print("The price per square meter of the house is:", round(HousePrice/HouseSurface, 2), "EUR per square meter")


main()
