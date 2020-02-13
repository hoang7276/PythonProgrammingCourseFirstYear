#Celsius2Fahrenheit.py
# A program to convert Celsius temps to Fahrenheit

def main():
    try:
        celsius = float(input("What is the Celsius temperature? "))
        fahrenheit = (9/5) * celsius + 32
        print("The temperature is ",fahrenheit," degrees Fahrenheit.")
    except ValueError:
        print("Error. The value entered is not a number")
    except:
        print("Sorry, something went wrong")
main()
