import random

def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    
    soma_total = dado1 + dado2
    
    return soma_total

resultado = lancar_dados()
print(f"O total do lançamento dos dois dados foi: {resultado}")
