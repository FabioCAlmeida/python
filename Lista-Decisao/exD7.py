import math
numero = float(input("Digite o número:"))

if numero >= 0:
    raiz = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raiz}")
else:
    print("Não é possível calcular a raiz quadrada de número negativo")