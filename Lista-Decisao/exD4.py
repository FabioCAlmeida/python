time1 = input("Qual é o nome do primeiro time: ")
time2 = input("Qual é o nome do segundo time: ")

gt1 = int(input(f"Quantos gols o time {time1} fez? "))
gt2 = int(input(f"Quantos gols o time {time2} fez? "))

if gt1 > gt2:
    print(f"O time {time1} venceu com {gt1} gols, placar final: {time1} {gt1} - {gt2} {time2}")
elif gt2 > gt1:
    print(f"O time {time2} venceu com {gt2} gols, placar final: {time1} {gt1} - {gt2} {time2}")
else:
    print(f"Empate, placar final: {time1} {gt1} - {gt2} {time2}")