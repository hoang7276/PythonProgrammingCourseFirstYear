# MonthAbbreviation.py
# Program that obtains the 3-letter abbreviation given the number of the month


def main():
    print("This program obtains the 3-letter abbreviation given the number of the month")
    monthstring = "JanFebMarAprMayJunJulAugSepOctNovDec"
    month = int(input("Enter a number between 1-12: "))
    abbreviation = monthstring[(month-1)*3:month*3]
    print(abbreviation)


main()
