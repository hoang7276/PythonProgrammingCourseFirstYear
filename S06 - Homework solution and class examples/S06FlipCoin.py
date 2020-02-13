# This program will flip a coin a number of times indicated by the user and then let the user know how many heads and tails were obtained

from random import random


def main():
    print("This program flips a coin several times and will let you know how many tails and heads were obtained")
    print("Input number of times you want the coin to be thrown:", end=" ")
    heads = 0
    tails = 0
    try:
        repetitions = int(input())
        for i in range(repetitions):
            if random() < 0.5:
                heads = heads + 1
            else:
                tails = tails + 1
        print("After flipping the coin", repetitions, "times,", heads, "heads and", tails, "tails were obtained")
    except ValueError:
        print("Error! Input does not have numeric format")
    except:
        print("Sorry, something went wrong")

main()
