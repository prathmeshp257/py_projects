def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def modulo(a, b):
    return a % b

def Calculator():
    x = bool(True)
    while x:
        a = int(input("Take any Number: "))
        b = int(input("Take another Number: "))
        # Take choice from User for Operations
        choice = input("Please Select Operation: (+, -, *, /, %) & Hit Enter: ")

        if choice == '+':
            ans = add(a, b)
        elif choice == '-':
            ans = sub(a, b)
        elif choice == '*':
            ans = mul(a, b)
        elif choice == '/':
            ans = div(a, b)
        elif choice == '%':
            ans = modulo(a, b)
        else:
            print('wrong Input')
            return

        # Print the Answer
        print(ans)

        # User choice to end the program
        end = input("Do you want to Continue? (Y/N)")
        if end == 'Y':
            continue
        elif end == 'N':
            return "Thanks for Using this calculator"
        else:
            return "Invalid Input"



print(Calculator())
