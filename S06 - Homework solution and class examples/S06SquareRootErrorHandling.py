import math  # Makes the math library available.


def main():
    print("This program finds the real solutions to a quadratic equation")
    print()
    try:
        a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print()
        print("The solutions are:", root1, root2)
    except ValueError:
        print("No real roots")
    except :
       print("Something went wrong, sorry!")



main()
