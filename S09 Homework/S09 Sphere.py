# Sphere.py
# Program that calculates the area and volume of a sphere given the radius r

# Import libraries
from math import pi


# Function to calculate area of a sphere for a given radius r
def spherearea(r):
    from math import pi
    area = 4 * pi * r**2
    return area


# Function to calculate volume of a sphere for a given radius r
def spherevolume(r):

    volume = 4/3 * pi * r**3
    return volume


# Main function to get r, invoke functions and print result
def main():
    print("Program that calculates the area and volume of a sphere for a given radius")
    r = float(input("enter the radius desired in cm: "))
    print("The area is", round(spherearea(r), 2), "cm2 and the volume is", round(spherevolume(r), 2), "cm3")

    

main()
