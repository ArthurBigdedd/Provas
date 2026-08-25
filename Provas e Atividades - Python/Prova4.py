
try:
    inicio = int(input("Digite o número inteiro inicial do intervalo (inclusivo): "))
    fim = int(input("Digite o número inteiro final do intervalo (inclusivo): "))
except ValueError:
    print("Erro: Por favor, insira apenas números inteiros válidos.")
    exit()

if inicio > fim:

    inicio, fim = fim, inicio
    print(f"\nNota: O início e o fim foram trocados para o intervalo [{inicio}, {fim}].")

soma_pares = 0
par_encontrado = False 

print(f"\nCalculando a soma dos números pares no intervalo de {inicio} a {fim}...")
for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        soma_pares += numero
        par_encontrado = True

else:
    if par_encontrado:
        print(f"\n✅ A soma total dos números pares no intervalo é: **{soma_pares}**")
    else:
        print("\n😔 Não foram encontrados números pares neste intervalo.")