import sqlite3

conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Clientes (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Idade INTEGER,
        Cidade TEXT
    );
    """)
    print("Tabela 'Clientes' verificada/criada com sucesso.")

    clientes_exemplo = [
        ('Ana Souza', 30, 'Rio de Janeiro'),
        ('Carlos Alberto', 25, 'Curitiba'),
        ('Beatriz Rocha', 42, 'Salvador')
    ]

    cursor.executemany("""
    INSERT INTO Clientes (Nome, Idade, Cidade) 
    VALUES (?, ?, ?)
    """, clientes_exemplo)
    
    conexao.commit()
    print(f"{len(clientes_exemplo)} clientes inseridos com sucesso.")

    print("--- Conteúdo da Tabela Clientes ---")
    cursor.execute("SELECT * FROM Clientes")
    for linha in cursor.fetchall():
        print(f"ID: {linha[0]} | Nome: {linha[1]} | Idade: {linha[2]} | Cidade: {linha[3]}")

except sqlite3.Error as e:
    print(f"Erro no banco de dados: {e}")

finally:
    conexao.close()