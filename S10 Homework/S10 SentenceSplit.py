# SentenceSplit.py


def main():
    print("This program counts the number of words in a sentence")
    sentence = str(input("Please enter a sentence: "))
    words = sentence.split()
    print("The number of words in the sentence are: ", len(words))


main()
