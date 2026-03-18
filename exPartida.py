gols_time_a = int(input("Gols do time A: "))
gols_time_b = int(input("Gols do time B: "))

if gols_time_a > gols_time_b:
    print("Time A venceu a partida")
    print(f"{gols_time_a} X {gols_time_b}")

else:
    if gols_time_a < gols_time_b:
        print("Time B venceu a partida")
        print(f"{gols_time_b} X {gols_time_a}")

    else: 
        print("Os time empataram")
        print(f"{gols_time_b} X {gols_time_a}")