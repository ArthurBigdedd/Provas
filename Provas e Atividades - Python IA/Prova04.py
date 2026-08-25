n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

def media(n1, n2, n3):
    soma = n1 + n2 + n3
    resultado = soma / 3
    return resultado

print(f"A média é: {media(n1, n2, n3)}")
