#This program calculates the weekly wage considering overtime salary


def main():
    print("Weekly salary calculator")
    print("Please input your hourly wage", end=" ")
    HourlyWage=float(input())
    print("Please input the number of hours worked this week", end=" ")
    HoursWorked=float(input())
    if HoursWorked>40:
        Salary = 40*HourlyWage + (HoursWorked-40)*(1.5*HourlyWage)
    else:
        Salary = HourlyWage * HoursWorked
    print("Your salary for", HoursWorked, "hours is:", Salary)


main()
