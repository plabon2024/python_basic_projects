print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

def add():
    a = float(input('Enter first number:'))
    b = float(input('Enter second number:'))
    print("Addition: ",a,'+', b,'=',float(a + b))
def sub():
    a = float(input('Enter first number:'))
    b = float(input('Enter second number:'))
    print("Subtraction: ",a,'-', b,'=',float(a - b))
def mul():
    a = float(input('Enter first number:'))
    b = float(input('Enter second number:'))
    print("Multiplication: ",a,'*', b,'=',float(a * b))
def div():
    a = float(input('Enter first number:'))
    b = float(input('Enter second number:'))
    if b == 0:
        print("You Cannot divide by zero ")
    else:
        print("Divition: ", a, '/', b, '=', float(a / b))
def modulus():
    a = float(input('Enter first number:'))
    b = float(input('Enter second number:'))
    if b == 0:
        print("You Can't do that modulus by zero is not allowed.")
    else:
        print("Modulus: ", a, '%', b, '=', float(a % b))
while True:
    try:
        select = int(input("Enter choice (1/2/3/4/5):"))
        if select == 1:
            add()
            break
        elif select == 2:
            sub()
            break
        elif select == 3:
            mul()
            break
        elif select == 4:
            div()
            break
        elif select == 5:
            modulus()
            break
        elif select != 1 or select != 2 or select != 3 or select != 4 or select != 5:
            print("Invalid action ! Try Again")
            continue
    except Exception as e:
        print(e)
        print("Invalid action ! Try Again")
        continue

