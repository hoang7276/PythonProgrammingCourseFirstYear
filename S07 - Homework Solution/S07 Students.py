def main():
    print("This program will print the name of your student after inputing it")

    StudentName = input("Enter the name of a student (press <Enter> to quit)>> ")
    while StudentName != "":
        print(StudentName)
        StudentName = input("Enter the name of a student (press <Enter> to quit)>> ")

main()
