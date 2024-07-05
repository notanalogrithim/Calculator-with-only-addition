#Simple calculator
def multiply(a, b):
    result = 0
    for _ in range(abs(b)):
        result += abs(a)
    if (a < 0) ^ (b < 0):
        result = -result
    return result

def exponent(base, exp):
    if exp == 0:
        return 1 
    result = base
    for _ in range (exp - 1):
        result = multiply(result, base)
    return result 
    result = 0
    for _ in range(abs(b)):
        result += abs(a)
    if (a < 0) ^ (b < 0):
        result = -result
    return result

def divide(dividend, divisor):
    decimal_places = 10
    quotient = 0
    negative = 0
    
    if dividend < 0:
        negative += 1
        dividend = -dividend
    if divisor < 0:
        negative += 1
        divisor = -divisor
        
    if divisor == 0:
        return "Undefined"

    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    
    decimal_part = 0
    power_of_ten = 1
    
    for _ in range(decimal_places):
        dividend = multiply(dividend, 10)
        digit = 0
        while dividend >= divisor:
            dividend -= divisor
            digit += 1
        decimal_part = multiply(decimal_part, 10) + digit
        power_of_ten = multiply(power_of_ten, 10)

    decimal_quotient = divide(decimal_part, power_of_ten)
    quotient += decimal_quotient
    
    if negative == 1:
        quotient = -quotient
    
    return quotient
run = True 
calculated = ""
result = 0
while run == True:
    print("What would you like to do")
    calculatorType = str(input("1: addition, 2: multiplication, 3: Exponential, 4: Subtraction, 5: Division "))
    if calculatorType == 3 or calculatorType.lower() == "exponential":
        x = int(input("First number (base): "))
        y = int(input("Second number (power): "))
    elif calculatorType == "5" or  calculatorType.lower() == "division":
        x = int(input("First number (dividen): "))
        y = int(input("Second number (divisor): "))
    else:
        x = int(input("First number: "))
        y = int(input("Second number: "))
    if calculatorType == "1" or calculatorType.lower() == "addition":
        calculated = x + y 
    elif calculatorType == "2" or  calculatorType.lower() == "multiplication":
        calculated = multiply(x,y)
    elif calculatorType == "3" or calculatorType.lower() == "exponential":           
        calculated = exponent(x,y)
    elif calculatorType == "4" or  calculatorType.lower() == "subtraction":
        calculated =  x + -y
    elif calculatorType == "5" or  calculatorType.lower() == "division":
        calculated = divide(x,y)
    else:
        print("Invalid option")
    print ("the answer is: " + str(calculated))
    again = input("Would you like to continue? 1: Yes, 2: No: ")
    if again == "2" or again.lower() == "no":
        run = False 


