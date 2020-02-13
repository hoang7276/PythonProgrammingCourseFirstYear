def main():
    print("This program is a calculator, it will allow you to input 10 mathematical operations")
    for i in range(10):
        print("Input a simple mathematical operation to see the result (remaining attempts:", (10-i), "): ", end=" ")
        result=eval(input())
        print(result)

main()
