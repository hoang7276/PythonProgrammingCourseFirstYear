# This program runs a gambling game based on coin tossing and dice throwing

from random import random
from random import randrange


def main():
    print("Welcome to the coin-tossing, dice-throwing gambling game!")
    print("Please input how much you want to bet:", end=" ")
    Money = int(input())
    CoinToss= random()      # Tails if value < 0.5
    DiceThrow = randrange(1, 7)
    if CoinToss < 0.5:
        Money = 0
        print("Coin Toss Result: Tails")
        print("Sorry! You got tails and lost everything. Better luck next time!")
    else:
        print("Coin Toss Result: Heads")
        print("Dice throw result:", DiceThrow)
        if DiceThrow < 5:
            print ("You did not earn anything and got your initial bet back")
        else:
            Money = 4* Money
            print ("You multiplied by 4 your initial investment! Now you have:", Money, "Euros")



main()
