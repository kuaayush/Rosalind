def Fibonacci_number(number):
    a, b = 1,1
    for i in range(0, number-1):
        b, a = a, a+b
    return b

print(Fibonacci_number(25))