# This program will throw a dice a number of times indicated by the user and then let the user know the numbers retrieved

from random import randrange


def main():
    print("This program throws a dice several times and will let you know how many times the value was 1 or 2, 3 or 4, 5 or 6")
    print("Input number of times you want the dice to be thrown:", end=" ")
    repetitions = int(input())
    dice12 = 0
    dice34 = 0
    dice56 = 0
    for repetition in range(repetitions):
        throwdice = randrange(1, 7)
        if throwdice < 3:
            dice12 = dice12 + 1
        else:
            if throwdice < 5:
                dice34 = dice34 + 1
            else:
                dice56 = dice56 + 1

    print("After flipping the coin", repetitions, "times,", dice12, "(1,2),", dice34, "(3,4) and", dice56, "(5,6) were obtained")


main()
