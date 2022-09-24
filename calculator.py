#간단한 계산기

a = int(input("a 값 입력: "))
b = int(input("b 값 입력: "))
calculate = input("연산 선택(+, -, *, /): ")

def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mult(x, y):
    return x * y
def divide(x, y):
    return x / y

if calculate == '+':
    print(add(a, b))

elif calculate == '-':
    print(sub(a, b))

elif calculate == '*':
    print(mult(a, b))

elif calculate == '/':
    print(divide(a, b))
