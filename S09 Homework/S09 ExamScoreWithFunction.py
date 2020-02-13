# ExamScoreWithFunction.py
# This program calculates the exam score from the 100-point grade


# Function that translates numeric grade into the final grade
def score(grade):
    if grade > 100:
        return "A"
    elif grade >= 90:
        return "B"
    elif grade >= 80:
        return "C"
    elif grade >= 70:
        return "D"
    elif grade >= 60:
        return "E"
    else:
        return "F"


# Main function with input and output statements and where score function is invoked
def main():
    print("This program calculates the exam score from the 100-point grade")
    print("Enter the grade here:", end=" ")
    grade = float(input())
    print("Your exam score is", score(grade))


main()
