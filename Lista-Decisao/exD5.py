dias_uteis = int(input("Digite o número de dias úteis do mês: "))
horas_trabalhadas = float(input("Digite o total de horas trabalhadas: "))
valor_hora = float(input("Digite o valor recebido por hora: "))


horas_normais = dias_uteis * 8


if horas_trabalhadas > horas_normais:
    horas_extras = horas_trabalhadas - horas_normais
else:
    horas_extras = 0


salario_base = horas_normais * valor_hora
valor_hora_extra = valor_hora * 1.5
valor_extra = horas_extras * valor_hora_extra

salario_final = salario_base + valor_extra


print(f"Horas extras: {horas_extras}")
print(f"Valor recebido em horas extras: R$ {valor_extra:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")