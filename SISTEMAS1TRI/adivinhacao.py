import random

print(" 1 NIVEL FACIL ")
print(" 2 NIVEL MEDIO ")
print(" 3 NIVEL DIFICIL")
opcao = int(input("Digite a opção desejada:"))
if (opcao == 1):
    numero_max = 10
    limite_tentativas = 3
elif (opcao == 2):
    numero_max = 20
    limite_tentativas = 5
elif (opcao == 3):
    numero_max = 50
    limite_tentativas = 10
else: 
    print("Opção inválida. Selecionado fácil automaticamente")
    numero_max = 10
    limite_tentativas = 3


sorteio = random.randint(1, numero_max)
#print(sorteio)
print("### JOGO DA ADIVINHAÇÃO ###")
print("Adivinhe o número que estou pensando, de 1 a ",numero_max)
tentativa = 1
while (limite_tentativas >= tentativa):
    print("Tentativa", tentativa)
    chute = int(input("Digite o seu chute:"))
    if (chute == sorteio):
        print("Parabéns, você acertou!")
        break
    elif (chute > sorteio):
        print("Chute um número menor!")
    elif (chute < sorteio):
        print("Chute um número maior!")
    tentativa = tentativa + 1
    # FINAL DO LAÇO WHILE
print("O número sorteado era: ##", sorteio, "##")
print("### FIM DO JOGO ###")