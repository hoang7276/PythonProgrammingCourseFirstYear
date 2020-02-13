# This program will calculate the surface of a Sphere

from math import pi


def main():
    print("Sphere surface and volume calculator")
    print("Please enter the radius of the sphere: ", end=" ")
    radius = float(input())
    spheresurface = 4 * radius * radius * pi
    spherevolume = (4/3)*pi*radius**3
    print("The surface of a sphere is ", spheresurface, "and the volume is", spherevolume)


main()
