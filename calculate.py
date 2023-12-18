

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: not divisible by zero"

def get_numeric_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            num = float(user_input)
            return num
        except ValueError:
            print("Invalid input. Please enter a numeric value.")



def run_calculator():
    print("This is a basic calculator that helps you with simple everyday\ncalculations.")
    
    while True:
        
        num_1 = get_numeric_input("Enter your first digit: ")
        operator = input("Enter the operator: ")
        num_2 = get_numeric_input("Enter your second digit: ")
        
        if operator == "+":
            outcome = addition(num_1, num_2)
        elif operator == "-":
            outcome = subtraction(num_1, num_2)
        elif operator == "*":
            outcome = multiplication(num_1, num_2)
        elif operator == "/":
            if num_2 != 0:
                outcome = division(num_1, num_2)
            else:
                print("Error: Division by zero.")
                  # Continue to the next iteration of the loop if division by zero
        print("Result:", outcome)

        more_calculation = input("Would you like to perform another calculation? (yes/no): ")
        if more_calculation.lower() != "yes":
            print("Thank you for using the program.")
            break

if __name__ == "__main__":
    run_calculator()
