# This program calculates the score for Python Quizzes


def main():
    print("Python Exam score calculator")
    print("Please input your exam grade on the 100 to 0 scale:", end=" ")
    Grade = int(input())
    if Grade >= 90:
        ExamGrade ='A'
    elif Grade >= 80:
        ExamGrade ='B'
    elif Grade >= 70:
        ExamGrade ='C'
    elif Grade >= 60:
        ExamGrade ='D'
    else:
        ExamGrade ='F'
    print("Your exam grade is:", ExamGrade)


main()
