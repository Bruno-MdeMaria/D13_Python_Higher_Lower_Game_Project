from secrets import choice
from art import logo, vs
from game_data import data
import random

def escolha():
    return random.choice(data)

def rodada(comp_a, comp_b):
    print(f"COMPARE A: {comp_a['name']}, um(a) {comp_a['description']} do(a) {comp_a['country']}.")
    print(vs)
    print(f"COM B: {comp_b['name']}, um(a) {comp_b['description']} do(a) {comp_b['country']}.")


comp_a = escolha()
comp_b = escolha()
rodada(comp_a, comp_b)
resposta = input("Quem tem mais seguidores no Instagram? Digite 'A' ou 'B': ").lower()
