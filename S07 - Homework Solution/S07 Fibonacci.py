# Program to calculate the nth Fibonacci number


def main():
    print("This program calculates the nth Fibonacci number")
    print("Please indicate which number in the Fibonacci sequence you want to obtain >> ")
    repetitions = int(input()) - 1                              # Remember the 1st number of the Fibonacci sequence is known before the loop
    FiboSum = 0                                                 # Number to initialize the fibonacci sum sequence with
    FiboCalc = 1                                                # Number of the fibonacci sequence
    for i in range(repetitions):
        FiboCalc, FiboSum = FiboCalc + FiboSum, FiboCalc        # Remember we can do simultaneous assignment
    print (FiboCalc)


main()
