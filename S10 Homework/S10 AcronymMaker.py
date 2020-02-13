# AcronymMaker.py
# This program creates an acronym from a sentence


def main():
    print("Program that creates an acronym from a sentence")
    print("Please enter a sentence", end=" ")
    phrase = str(input())
    words = phrase.split()
    for i in words:
        print(i[0].upper(), end="")


main()
