step = 0
message = "Enter a number: "
num1 = None
num2 = None

operations = ("+", "-", "*", "/")   
results = []                        

while True:
    if step == 0:
        userInput = input(message)
        try:
            num1 = int(userInput)
            message = "Enter an operation (+, -, *, /): "
            step = 1
        except ValueError:
            message = "Please enter a number: "
            continue

    if step == 1:
        userInput = input(message)
        if userInput not in operations:
            message = "Please enter an operation (+, -, *, /): "
            continue
        operation = userInput
        message = "Enter another number: "
        step = 2

    if step == 2:
        userInput = input(message)
        try:
            num2 = int(userInput)
        except ValueError:
            message = "Please enter a number: "
            continue

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2

    results.append(result)  # store result in list

    print(f"{num1} {operation} {num2} = {result}")
    print("Results so far:", results)

    print("Exiting..")
    break