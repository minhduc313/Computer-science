def add(num1,num2):
    return num1 + num2
def subtract(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def divide(num1,num2):
    return num1/num2
def square(num1):
    return num1**(1/2)
def square2(num2):
    return num2**(1/2)
num1 = int(input("Num1?"))
num2 = int(input("num2?"))
print (num1)
print (num2)
menu = int(input("1 to add, 2 to subtract, 3 to multiply, 4 to divide,5 to find square root"))
print (menu)
while menu == 1 or 2 or 3 or 4 or 5:
    if menu == 1:
        print (add(num1,num2))
    if menu == 2:
        print (subtract(num1,num2))
    if menu == 3:
        print (multiply(num1,num2))
    if menu == 4:
        print (divide(num1,num2))
    if menu == 5:
        print (square(num1))
        print (square(num2))


