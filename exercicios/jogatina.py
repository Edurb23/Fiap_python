#Lakers X Warriors
#Celtics X 76ers 
#Phoenix X Denver
#Miami Heat X Knicks
import random

def simula_resultados(timeA, timeB):
    ptsA = random.randint(80, 125)
    ptsB = random.randint(80, 125)
    print(timeA, ptsA, "X", ptsB, timeB)
    if ptsA > ptsB:
        return timeA
    else:
        return timeB

jogos = ["Lakers", "GSW", "", "Celtics", "76ers", "", 
         "Phoenix", "Denver", "", "Miami", "Knicks", ""]

i = 0
k = 0
while i < 4:
    print(jogos[k], "X", jogos[k + 1])
    jogos[k + 2] = input("Palpite: ")
    i = i + 1
    k = k + 3
print("Simulando jogos")
acertos = 0
i = 0
k = 0
while i < 4:
    winner = simula_resultados(jogos[k], jogos[k + 1])
    if winner == jogos[k + 2]:
        acertos = acertos + 1

    i = i + 1
    k = k + 3

print(acertos, "acertos")    
#print(jogos)