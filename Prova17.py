import sqlite3

conn = sqlite3.connect('sistema_estoque.db')
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Produtos (
    ProdutoID INTEGER PRIMARY KEY,
    NomeProduto TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Fornecedores (
    FornecedorID INTEGER PRIMARY KEY,
    NomeFornecedor TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Estoque (
    EstoqueID INTEGER PRIMARY KEY,
    ProdutoID INTEGER,
    FornecedorID INTEGER,
    Quantidade INTEGER NOT NULL,
    DataEntrada DATE NOT NULL,
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
    FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID)
);
""")

try:
    cursor.execute("ALTER TABLE Estoque ADD COLUMN ValorUnitario DECIMAL(10, 2);")
    print("Coluna 'ValorUnitario' adicionada com sucesso.")
except sqlite3.OperationalError:
    print("A coluna 'ValorUnitario' já existe.")

cursor.execute("INSERT OR IGNORE INTO Produtos (ProdutoID, NomeProduto) VALUES (1, 'Teclado Mecânico')")
cursor.execute("INSERT OR IGNORE INTO Fornecedores (FornecedorID, NomeFornecedor) VALUES (101, 'Logitech Brasil')")
cursor.execute("INSERT INTO Estoque (EstoqueID, ProdutoID, FornecedorID, Quantidade, DataEntrada, ValorUnitario) VALUES (1, 1, 101, 50, '2023-10-27', 250.00)")

print("--- Relatório de Quantidade por Fornecedor ---")
cursor.execute("""
    SELECT FornecedorID, SUM(Quantidade) 
    FROM Estoque 
    GROUP BY FornecedorID
""")

for linha in cursor.fetchall():
    print(f"Fornecedor ID: {linha[0]} | Total em Estoque: {linha[1]}")

conn.commit()
conn.close()

print("Operações concluídas com sucesso!")