# Distance.py
# Program that calculates the distance between two points in a 2 dimensional space

from math import sqrt


# Square function, to calculate the square of any value
def square(x):
    valuesquared = x * x
    return valuesquared


# Main
def main():
    print("This program calculates the distance between two points in a 2 dimensional space")
    x1 = float(input("Enter the x coordinate for point 1"))
    y1 = float(input("Enter the y coordinate for point 1"))
    x2 = float(input("Enter the x coordinate for point 2"))
    y2 = float(input("Enter the y coordinate for point 2"))

    distance = sqrt(square(x2-x1) + square(y2-y1))
    print("The distance between the two points is:")
    print(round(distance, 2))


main()
