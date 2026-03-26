num = int(input("Escreva um numero de 0 à 99: "))
dezenas = num // 10


if num > 99:
    print("Escreva um número de 0 à 99!")

if num < 0:
    print("Escreva um número de 0 à 99!")


if num >= 0:
    if num <= 99:
        print("A quantidade de dezenas é: ", dezenas, "e a quantidade de unidades é: ", num)




