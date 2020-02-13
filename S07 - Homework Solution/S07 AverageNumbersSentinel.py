# This program will calculate the average of numbers entered by the user
# The amount of numbers to average will not be decided beforehand


def main():
    print("This program will calculate the average of all the numbers you enter")
    SumOfNumbers = 0.0                                                      # Initialized as floats since I will ask for floats
    AvgOfNumbers = 0                                                        # Accumulator to count amount of numbers to average
    AvgSentinel = input("Enter a number (press <Enter> to quit)>> ")        # Sentinel/data identifier for the loop

    while AvgSentinel != "":
        x = float(AvgSentinel)                                              # Sentinel checked, now convert to data
        SumOfNumbers = SumOfNumbers + x
        AvgOfNumbers = AvgOfNumbers + 1
        AvgSentinel = input("Enter a number (press <Enter> to quit)>> ")    # Get sentinel again to iterate

    print("\nThe average of numbers entered is", SumOfNumbers/AvgOfNumbers)


main()
