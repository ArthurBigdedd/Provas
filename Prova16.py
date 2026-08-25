import sqlite3

conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Produtos (
        ProdutoID INTEGER PRIMARY KEY,
        NomeProduto TEXT NOT NULL,
        Quantidade INTEGER,
        Preco REAL
    );
    """)
    print("Tabela 'Produtos' criada com sucesso.")

    dados_produtos = [
        (101, 'Notebook Gamer', 5, 4500.00),
        (102, 'Mouse Sem Fio', 50, 120.50),
        (103, 'Monitor 24 Polegadas', 15, 899.90)
    ]

    cursor.executemany("""
    INSERT OR IGNORE INTO Produtos (ProdutoID, NomeProduto, Quantidade, Preco)
    VALUES (?, ?, ?, ?)
    """, dados_produtos)

    conexao.commit()
    print("Registros inseridos com sucesso.")

    print("\n--- Inventário de Produtos ---")
    cursor.execute("SELECT * FROM Produtos")
    for produto in cursor.fetchall():
        print(f"ID: {produto[0]} | Produto: {produto[1]} | Qtd: {produto[2]} | Preço: R$ {produto[3]:.2f}")

except sqlite3.Error as erro:
    print(f"Ocorreu um erro: {erro}")

finally:
    conexao.close()