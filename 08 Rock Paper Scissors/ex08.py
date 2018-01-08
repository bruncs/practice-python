"""
  Exercise 8
"""
# pylint: disable=invalid-name
import os
clear = lambda: os.system('cls') # Função para limpar o console
playAgain = "s"

while playAgain == "s":

    clear()
    print("Seja bem-vindo ao Joquempy!")
    player1 = input("Jogador 1: ")
    player2 = input("Jogador 2: ")
    clear()

    player1play = input(player1 + " joga (Pedra/Papel/Tesoura): ")
    clear()
    player2play = input(player2 + " joga (Pedra/Papel/Tesoura): ")
    clear()

    if player1play == "Pedra":
        if player2play == "Pedra":
            print("Empatou!")
        elif player2play == "Papel":
            print("Vitória de " + player2)
        elif player2play == "Tesoura":
            print("Vitória de " + player1)
        else:
            print("O "+ player2 + " não sabe digitar.")
    elif player1play == "Papel":
        if player2play == "Pedra":
            print("Vitória de " + player1)
        elif player2play == "Papel":
            print("Empatou!")
        elif player2play == "Tesoura":
            print("Vitória de " + player2)
        else:
            print("O "+ player2 + " não sabe digitar.")
    elif player1play == "Tesoura":
        if player2play == "Pedra":
            print("Vitória de " + player1)
        elif player2play == "Papel":
            print("Vitória de " + player2)
        elif player2play == "Tesoura":
            print("Empatou!")
        else:
            print("O "+ player2 + " não sabe digitar.")
    else:
        print("O "+ player1 + " não sabe digitar.")

    playAgain = input("Deseja jogar novamente (s/n)? ")

clear()
print("Obrigado por jogar Joquempy!")
