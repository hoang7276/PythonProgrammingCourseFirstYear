# This program will calculate the average of numbers entered by the grades of all students
# And present the average grade of each student, together with its name


def main():
    print("This program will calculate the average of all grades for each student you indicate")
    print("How many grades do students have in this course?: ")
    GradeRepetitions = int(input())

    StudentName = input("\nEnter a student name (press <Enter> to quit)>> ")      # Sentinel/data identifier for the students loop
    while StudentName != "":
        print(StudentName)

        SumOfNumbers = 0.0                                                      # Initialized for each student as floats since I will ask for floats
        AvgOfNumbers = 0                                                        # Accumulator to count amount of numbers to average for each student
        for i in range(GradeRepetitions):
            print("Enter grade number", i+1, "for", StudentName, ">> ", end=" ")
            x = float(input())
            SumOfNumbers = SumOfNumbers + x
            AvgOfNumbers = AvgOfNumbers + 1

        print("\nThe average grade for", StudentName, "is", SumOfNumbers/AvgOfNumbers)
        StudentName = input("\nEnter a student name (press <Enter> to quit)>> ")  # Get sentinel again to iterate through the students loop



main()
