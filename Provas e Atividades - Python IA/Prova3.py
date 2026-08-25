carrinho_compras = {}
print("--- Cadastro de Produtos ---")

for i in range(5):
    nome = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço de {nome}: "))
    carrinho_compras[nome] = preco

valor_total = sum(carrinho_compras.values())

print("-" * 30)
print(f"O valor total da compra é: R$ {valor_total:.2f}")