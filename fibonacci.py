def isFib(x):
    if x == 0 or x == 1:
        return True
    a, b = 0, 1
    while True:
        c = a + b
        a = b
        b = c
        if c == x:
            return True
        elif c >= x:
            return False
 
print("Digite um número: ")
x = int(input())

if isFib(x):
    print(x, "é um número de Fibonacci")
else:
    print(x, "não é um número de Fibonacci")