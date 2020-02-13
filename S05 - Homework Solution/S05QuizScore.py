# This program calculates the score for Python Quizzes


def main():
    print("Python Quiz score calculator")
    print("Please input your grade on the 0 to 5 scale:", end=" ")
    Grade = int(input())
    if Grade == 5:
        QuizGrade ='A'
    if Grade == 4:
        QuizGrade ='B'
    if Grade == 3:
        QuizGrade ='C'
    if Grade == 2:
        QuizGrade ='D'
    if Grade == 1:
        QuizGrade ='E'
    if Grade == 0:
        QuizGrade ='F'
    print("Your quiz grade is:", QuizGrade)


main()
