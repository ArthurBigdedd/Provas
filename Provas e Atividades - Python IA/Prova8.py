import os

diretorio = '.'
conteudo = os.listdir(diretorio)

print(f"{'NOME':<30} | {'TIPO'}")
print("-" * 40)

for nome in conteudo:
    caminho_total = os.path.join(diretorio, nome)
    tipo = "Diretório" if os.path.isdir(caminho_total) else "Arquivo"
    print(f"{nome:<30} | {tipo}")