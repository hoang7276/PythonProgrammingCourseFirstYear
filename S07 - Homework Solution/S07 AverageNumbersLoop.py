# This program will calculate the average of numbers entered by the user
# The amount of numbers to average is decided beforehand


def main():
    print("This program will calculate the average of all the numbers you enter")
    print ("Let me know how many numbers you want to average: ")
    repetitions = int(input())
    SumOfNumbers = 0.0          # Initialized as floats since I will ask for floats
    AvgOfNumbers = 0            # Accumulator to count amount of numbers to average

    for i in range(repetitions):
       x = float(input("Enter a number >> "))
       SumOfNumbers = SumOfNumbers + x
       AvgOfNumbers = AvgOfNumbers + 1

    print("\nThe average of numbers entered is", SumOfNumbers/AvgOfNumbers)


main()
