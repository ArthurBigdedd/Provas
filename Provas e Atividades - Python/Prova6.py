USUARIO_CORRETO = "admin"
SENHA_CORRETA = "senha123"

MAX_TENTATIVAS = 3

print("--- Bem-vindo ao Sistema de Login ---")
print(f"Você tem {MAX_TENTATIVAS} tentativas para entrar.")

for tentativa_atual in range(1, MAX_TENTATIVAS + 1):
    usuario = input(f"\nTentativa {tentativa_atual} - Digite o nome de usuário: ")
    senha = input(f"Tentativa {tentativa_atual} - Digite a senha: ")

    if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
        print("\nLogin bem-sucedido!")
        print(f"Boas-vindas, {USUARIO_CORRETO}!")
        break
    else:
        tentativas_restantes = MAX_TENTATIVAS - tentativa_atual
        if tentativas_restantes > 0:
            print(f"Credenciais incorretas. Você tem mais {tentativas_restantes} tentativa(s) restante(s).")
else:
    print("\nTodas as tentativas esgotadas.")

    for _ in range(3):
        print("Acesso bloqueado!")