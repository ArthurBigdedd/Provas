NUMERO_SECRETO = 7
MAX_TENTATIVAS = 3

tentativas_restantes = MAX_TENTATIVAS
acertou = False 

while not acertou and tentativas_restantes > 0:
    print(f"\nTentativas restantes: {tentativas_restantes}")

    try:
        palpite = int(input("Adivinhe o número secreto (entre 1 e 10): "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        continue 

    if palpite == NUMERO_SECRETO:
        acertou = True 
    elif palpite < NUMERO_SECRETO:
        print("O número é maior. Tente novamente!")
    else: 
        print("O número é menor. Tente novamente!")

    if not acertou:
        tentativas_restantes -= 1

print("-" * 30)

if acertou:
    print(f"🎉 PARABÉNS! Você acertou o número secreto: {NUMERO_SECRETO}!")
else:
    print(f"😞 Que pena! Suas {MAX_TENTATIVAS} tentativas acabaram.")
    print(f"O número secreto era: {NUMERO_SECRETO}.")