x1 = int(input("Digite o primeiro numero: "))
op = input("Digite a opração: ")
x2 = int(input("Digite o segundo numero: "))

if op == "+":
    print(x1 + x2)
elif op == "-":
    print(x1 - x2)
elif op == "*":
    print(x1 * x2)
elif op == "/":
    print(x1 / x2)
else:
    print("Operador inválido!")