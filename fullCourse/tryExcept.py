try:
    # value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divide by zero")
except ValueError:
    print("invalid input")

