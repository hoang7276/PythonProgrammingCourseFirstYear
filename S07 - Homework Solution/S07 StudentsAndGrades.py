# This program will calculate the average of numbers entered by the grades of all students
# And present the average grade of each student, together with its name


def main():
    print("This program will calculate the average of all grades for each student you indicate")

    StudentName = input("\nEnter a student name (press <Enter> to quit)>> ")      # Sentinel/data identifier for the students loop
    while StudentName != "":
        print(StudentName)

        SumOfNumbers = 0.0                                                      # Initialized for each student as floats since I will ask for floats
        AvgOfNumbers = 0                                                        # Accumulator to count amount of numbers to average for each student
        AvgSentinel = input("Enter a number (press <Enter> to quit)>> ")        # Sentinel/data identifier for the average grade loop
        while AvgSentinel != "":
            x = float(AvgSentinel)                                              # Sentinel checked, now convert to data
            SumOfNumbers = SumOfNumbers + x
            AvgOfNumbers = AvgOfNumbers + 1
            AvgSentinel = input("Enter a number (press <Enter> to quit)>> ")    # Get sentinel again to iterate through the average grade loop

        print("\nThe average grade for", StudentName, "is", SumOfNumbers/AvgOfNumbers)
        StudentName = input("\nEnter a student name (press <Enter> to quit)>> ")  # Get sentinel again to iterate through the students loop



main()
