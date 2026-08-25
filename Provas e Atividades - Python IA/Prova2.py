contato = {}

print("--- Cadastro de Contato ---")
contato['nome'] = input("Digite o nome do contato: ")
contato['telefone'] = input("Digite o número de telefone: ")
contato['email'] = input("Digite o endereço de email: ")

print("--- Informações do Contato ---")
for chave, valor in contato.items():
    print(f"{chave.capitalize()}: {valor}")