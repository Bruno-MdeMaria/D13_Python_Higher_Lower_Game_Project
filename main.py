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
    a_dict = int(comp_a['follower_count'])
    b_dict = int(comp_b['follower_count'])
   
    placar = 0
    if resposta == "a" and a_dict > b_dict:
        placar += 1
        print(placar) #TEMP
    elif resposta == "b" and a_dict < b_dict:
        placar += 1
        print(placar)#TEMP
    else: print(f"Você errou! Seu placar é de {placar}")
    


comp_a = escolha()
comp_b = escolha()
print(comp_b)
print(comp_a)
rodada(comp_a, comp_b)
resposta = input("Quem tem mais seguidores no Instagram? Digite 'A' ou 'B': ").lower()
comparar(comp_a, comp_b, resposta)
