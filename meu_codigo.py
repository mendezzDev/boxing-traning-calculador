print("===== RELATORIO DE LUTADOR =====")
nome = input("qual seu nome guerreiro? ")
idade = int(input("qual sua idade?"))
minutos = int(input("quantos minutos de corda voce fez?"))
rounds = int(input("quantos rounds voce fez? "))
quilometros = float(input("quantos quilometros voce correu? "))
pontos = 0
print("===== RELATORIO FINAL =====")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Minutos de corda: {minutos}")
if minutos >= 10:
    pontos += 10
    print("voce ganhou 10 pontos")
else:
    print("voce nao ganhou nada, de pontos")
print(f"Rounds: {rounds}")
if rounds >= 4:
    pontos += 20
    print("voce ganhou 20 pontos")
else:
    print("voce nao ganhou nada, de pontos")
print(f"Quilometros corridos: {quilometros}")
if quilometros >= 5:
    pontos += 30
    print("voce ganhou 30 pontos")
else:
    print("voce nao ganhou nada, de pontos")
print(f"seu total de pontos foi: {pontos}")
if pontos >= 50:
        print("parabens voce e nivel Rocky Balboa")
else:
        print("da para melhorar")