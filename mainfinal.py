from ast import While
from art import logo, vs
from game_data import data
import random
import os

def escolha():
    '''Escolhe aleatoriamente um item da lista data'''
    return random.choice(data)

def rodada(comp_a, comp_b):
    """"Apresenta a rodada comparando os itens escolhidos"""
    print(f"Compare A: {comp_a['name']}, um(a) {comp_a['description']} do(a) {comp_a['country']}.")
    print(vs)
    print(f"Contra B: {comp_b['name']}, um(a) {comp_b['description']} do(a) {comp_b['country']}.")

def comparar(comp_a, comp_b, resposta):
    seguidores_a = int(comp_a['follower_count'])
    seguidores_b = int(comp_b['follower_count'])
    global PARAR
    global PLACAR
    
    if resposta == "a" and seguidores_a > seguidores_b:
        PLACAR += 1
        os.system("cls")
        print(logo)
        print(F"Você está certo. Sua pontuação atual: {PLACAR}")
        return comp_a
    elif resposta == "b" and seguidores_a < seguidores_b:
        PLACAR += 1
        os.system("cls")
        print(logo)
        print(F"Você está certo. Sua pontuação atual: {PLACAR}")
        return comp_b
    else:
        os.system("cls")
        print(logo)
        print(f"Desculpe você errou! Seu placar final: {PLACAR}") 
        PARAR = True
fim_jogo = False
while not fim_jogo:

    print(logo)
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

    novamente = input("\nGostaria de tentar novamente e melhorar o seu placar? Digite 'S' ou 'N':  ").lower()
    if novamente == "n":
        fim_jogo = True