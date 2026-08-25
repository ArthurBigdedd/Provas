def calcular_media_alunos():
    """
    Calcula a média de notas de vários alunos, verifica aprovação/reprovação
    e calcula a média geral da turma.
    """
    medias_turma = []
    
    while True:
        try:
            num_alunos = int(input("Digite o número de alunos na disciplina: "))
            if num_alunos > 0:
                break
            else:
                print("O número de alunos deve ser um valor positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    print("-" * 30)

    for i in range(1, num_alunos + 1):
        print(f"--- Aluno {i} ---")
        
        nome_aluno = input(f"Digite o nome do aluno {i}: ")
        
        notas = []
        for j in range(1, 4):
            while True:
                try:
                    nota = float(input(f"Digite a nota {j} de {nome_aluno}: "))
                    if 0.0 <= nota <= 10.0:
                        notas.append(nota)
                        break
                    else:
                        print("A nota deve estar entre 0.0 e 10.0.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número para a nota.")
        
        soma_notas = sum(notas)
        
        media = soma_notas / len(notas)
        
        medias_turma.append(media)
        
        MEDIA_MINIMA_APROVACAO = 7.0
        
        if media >= MEDIA_MINIMA_APROVACAO:
            situacao = "APROVADO"
        else:
            situacao = "REPROVADO"
        
        print("-" * 30)
        print(f"Nome do Aluno: {nome_aluno}")
        print(f"Notas Lançadas: {notas}") 
        print(f"Média Final: {media:.2f}") 
        print(f"Situação: **{situacao}**")
        print("-" * 30)
        print()

    print("=" * 40)
    print("RESUMO DA TURMA")
    print("=" * 40)

    if medias_turma:
        soma_medias_turma = sum(medias_turma)
        
        media_geral = soma_medias_turma / len(medias_turma)
        
        print(f"Número total de alunos processados: {num_alunos}")
        print(f"Média Geral da Turma: **{media_geral:.2f}**")
    else:
        print("Nenhum aluno foi processado.")

if __name__ == "__main__":
    calcular_media_alunos()