
# Import libraries to import: IMPORT ALL OF THESE BEFORE THE DOING THE EXERISE OR ANY EXAM!!1
import math
from random import random
from random import randrange
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


# Hashtag: This is single line comment
"""
This is a multi-line comment
Just intended to show how multi-line comments are also ignored
"""

"""
1)DATATYPES AND VARIABLES

    # There are 3 main data type you need to remember
        #String(letters):"""

x = "abc"

        #Interger, (whole number)

x = 12

        #Float, (delcimal number;
x = 12.5
"""
        #Remeber that when you set the variable with a new value, the old value that is embeded in the value will be removed

    #In every program, you need to run the "main" finction, which is like the spiral the program"""

def main():
    x = 12.5
    print(x)
main()
"""
    # Taking in user input
        # Explaination:
            # print(): Make the given text, values, or constants appear in the console, screen
            # eval() -> a function to ensure that trge program and take safe data
            # input, remind the program that at this line, user will type something and it will take equals to the variable given
                # WARNING: THE PROGRAM WONT PRINT OUT THE VALUE IF THE VARIABLE IS NOT CALLED IN print()
            #Example 1
"""



def main():
    print("This program asks for three grades and calculates the average")
    grade1=eval(input("first grade: "))
    grade2=eval(input("second grade: "))
    grade3=eval(input("third grade: "))
    average=(grade1+grade2+grade3)/3
    print(average)
main()

        #Example 2:
            #end = "" : This make the input, or fllowing print sentence will not go down the following line
def main():
    print("This program is a calculator, input a simple mathematical operation to see the result: ",end=" ")
    result=eval(input())
    print(result)

main()

"""
    MATH LIBRARY:(import math): This libary allow to use, perform cetain math number and equation
    WARNING. add "math." before the variable
        pi:  π -An approximation of pi
        e:   e -An approximation of e
        sqrt(x): √x - The square root of x
        sin(x): sin x -The sine of x
        cos(x): cos x -The cosine of x
        tan(x): tan x - The tangent of x
        asin(x): arcsin x -The inverse of sine x
        acos(x): arccos x -The inverse of cosine x
        atan(x): arctan x -The inverse of tangent x
        log(x): ln x -The natural (base e) logarithm of x
        log10(x): log10 x -The common (base 10) logarithm of x
        exp(x):ex -The exponential of x
        ceil(x): ┌x┐ The smallest whole number >= x
        floor(x) └x┘ The largest whole number <= x
"""
def main():
    x = 3
    result = x * math.pi #This is the same as 3*3.14
    result = math.sqrt(3) #This is the same the square root of 3
    print(result)
main()

"""
    Random(import random): generate a number or a seqeunce or random number 
"""
def main():
    x = random() #Generate a random number between 0 and 1 (e.g: 0.23 ; 0.54)
    x  = randrange(10)  # Integer from 0 to 9 inclusive
    x = randrange(1,6) # Generate a random range of number from 1 to 6
    x = randrange (5,105,5) #Returs a random between 5 and 105 as a multiple of 5
main()

"""
2) DECISION STRUCTURE
"""

"""
    if <condition>; 
        <statements>
      else:
         <statements>
         
    1) The if <condition> is evaluated
    2) If <condition> is true, <statements> under if are executed and those under else
    will not be. Then the flow continues as usual
    3) If <condition> is true, <statements> under if are not executed, those under else will be executed instead. Then the flow continues as usual
"""
def main():
    x = randrange(1,6)

    print("The generated value is x =", x)
    if x<3:
        print("The generate value is less than 3")
    else:
        print("The generate value is more than 3")
main()

"""
    Nesting if
    if <condition>; 
        <statements>
      else:
        if <condition>; 
            <statements>
        else:
            <statements>
"""
    
def main():
    x = randrange(1,6)

    print("The generated value is x =", x)
    if x>4:
        print("The generate value is more than 4")
    else:
        if x>2:
            print("The generate value is more than 2 and less than 4")
        else:
            print("The generate value is less than 2")
main()


"""
    3)Loop Structures and Booleans
"""
def main():
    for i in range(10):
        print(i)  # will print0,1,2,3,4,5,6,7,8,9

    for i in [0, 1, 2, 3, 4, 6, 6, 6, 6, 0]:
        print(i)
        # will print 0,1,2,3,4,6,6,6,6,0 in that order
    for country in ["Spain", "Portugal", "Italy", "Greece"]:
        print(country)
        # will print tSpain, Portugal, Italy and Greece in tha torder

    print("How many numbers would you like to average?", end =" " )
    repetitions = int(input())
    totalsum = 0
    for i in range(repetitions): #take the repetision based on user input, in this case let assum euser put in 3 -> lead to repear rhe following block of code 3 times
        x = float(input("enter a number here ")) # tae in user input, assume user in put 3 first time, 2 second time and 4 the third time
        totalsum = totalsum + x # the variabe will calculate the total 0+3 first time, 3 + 2 second time, 5+4 third tine
        print("The average of the number is", totalsum / repetitions)  # take the total divide by repetition: 9/3 = 3
main()

"""
    While loop
        while <condition>: 
            <body>
    
    1) <condition> is a boolean expression, the same as in if statements.
    2) The <body> will execute repeatedly as long as <condition> remains true. When <condition> becames false, the loop will terminate
"""
def main():
    i=0
    while i<10:
        print (i)
main() # This will print 0,1,2,3,4,5,6,7,8,9

"""
    Interactive loop
"""
def main():
    sum = 0.0
    count = 0
    moredata = "y"

    while moredata == "y":
        # initialized as float since later we ask for floats # accumulator variable to count loop repetitions # while loop control variable
        x = float(input("Enter a number >> "))
        sum=sum+x
        count = count + 1
        moredata = input("If you have more numbers press <y> and if not press <n>")
    print("\nThe average of the numbers is", sum / count)





