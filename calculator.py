#간단한 계산기

a = int(input("a 값 입력: "))
b = int(input("b 값 입력: "))
calculate = input("연산 선택(+, -, *, /): ")

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

if calculate == '+':
    print(add(a, b))

elif calculate == '-':
    print(subtract(a, b))

elif calculate == '*':
    print(multiply(a, b))

elif calculate == '/':
    print(divide(a, b))