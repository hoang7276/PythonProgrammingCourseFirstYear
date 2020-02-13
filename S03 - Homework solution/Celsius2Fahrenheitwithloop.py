#Celsius2Fahrenheit.py
# A program to convert Celsius temps to Fahrenheit

def main():
    print("this program will ask celsius degrees and convert them to fahrenheit 5 times")
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = (9/5) * celsius + 32
        print("The temperature is ",fahrenheit," degrees Fahrenheit. Celsius degrees were ", celsius)

main()
