while True:
    print("\nSimple Calculator")
    a = float(input("First number: "))
    op = input("Operator (+,-,*,/): ")
    b = float(input("Second number: "))

    if op == "+":
        print("Result =", a + b)
    elif op == "-":
        print("Result =", a - b)
    elif op == "*":
        print("Result =", a * b)
    elif op == "/":
        print("Result =", a / b)
    else:
        print("Invalid operator")

    if input("Continue? (y/n): ").lower() != "y":
        break
