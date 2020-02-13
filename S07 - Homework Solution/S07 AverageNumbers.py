# This program will calculate the average of numbers entered by the user
# The amount of numbers to average will not be decided beforehand


def main():
    print("This program will calculate the average of all the numbers you enter")
    SumOfNumbers = 0.0          # Initialized as floats since I will ask for floats
    AvgOfNumbers = 0            # Accumulator to count amount of numbers to average
    GetMoreData = "y"           # Control variable for the loop

    while GetMoreData == "y":
        x = float(input("Enter a number >> "))
        SumOfNumbers = SumOfNumbers + x
        AvgOfNumbers = AvgOfNumbers + 1
        GetMoreData = input("If you have more numbers press <y> and if not press <n>:  ")

    print("\nThe average of numbers entered is", SumOfNumbers/AvgOfNumbers)


main()
