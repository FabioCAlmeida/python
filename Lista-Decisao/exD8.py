idade = int(input("Informe sua idade:"))

if idade > 4 and idade < 8:
    print("Sua categoria é infantil")

elif idade > 7 and idade < 11:
    print("Sua categoria é juvenil")

elif idade > 10 and idade < 16:
    print("Sua categoria é adolescente")

elif idade > 15 and idade < 31:
    print("Sua categoria é adulto")

elif idade > 30:
    print("Sua categoria é senior")