
try:
    number = int(input("Enter a number: "))
    print(number)

except:
    print("Invalid input")

try:
    value = 10 / 0
except ZeroDivisionError:
    print("Divided by zero ")
except ValueError:
    print("Invalid input ")