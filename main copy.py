from ast import While
from art import logo, vs
from game_data import data
import random

def escolha():
    return random.choice(data)

def rodada(comp_a, comp_b):
    print(f"COMPARE A: {comp_a['name']}, um(a) {comp_a['description']} do(a) {comp_a['country']}.")
    print(vs)
    print(f"COM B: {comp_b['name']}, um(a) {comp_b['description']} do(a) {comp_b['country']}.")

def comparar(comp_a, comp_b, resposta):
    seguidores_a = int(comp_a['follower_count'])
    seguidores_b = int(comp_b['follower_count'])
    global PARAR
    global PLACAR
    
    if resposta == "a" and seguidores_a > seguidores_b:
        PLACAR += 1
        return comp_a
    elif resposta == "b" and seguidores_a < seguidores_b:
        PLACAR += 1
        return comp_b
    else: 
        PARAR = True

               
comp_a = escolha()
PARAR = False
PLACAR = 0

while PARAR == False:
    comp_b = escolha()
    print(comp_a)
    print(comp_b)
    rodada(comp_a, comp_b)
    resposta = input("Quem tem mais seguidores no Instagram? Digite 'A' ou 'B': ").lower()

    comp_a = comparar(comp_a, comp_b, resposta)
    print(f"Você errou! Seu placar é de {PLACAR}")
  
