preco = int(input("qual é o valor do produto: "))


percentual = int(input("Qual é o valor percentual: "))



valordesconto = preco * percentual / 100
precodesconto = preco - valordesconto
valoracrescimo = preco + valordesconto



escolha = (input("É acrescimo ou desconto: "))


if escolha == "desconto":
    print("o valor do desconto é: ", valordesconto, ", o valor final é :", precodesconto)



elif escolha == "acrescimo":


    print("O valor do acrescimo é: ", valordesconto, ", o valor do produto com acrescimo é: ", valoracrescimo)

else:
    print("Escolha uma opção! ")
