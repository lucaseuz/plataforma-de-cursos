import mysql.connector
import pandas as pd
import os

# Conectar ao banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="test",
    password="test",
    database="test",
    auth_plugin='mysql_native_password'
)

# Definir o caminho da pasta para salvar os arquivos CSV
pasta_destino = '../plataforma-de-cursos/lake/'  # Substitua pelo caminho desejado


# Tabelas e arquivos CSV
tabelas = {
    'usuarios': 'dados_usuarios.csv',
    'cursos': 'dados_cursos.csv',
    'transacoes': 'dados_transacoes.csv'
}

for tabela, nome_arquivo in tabelas.items():
    # Ler dados da tabela
    query = f"SELECT * FROM {tabela}"
    df = pd.read_sql(query, conexao)

    # Definir o caminho completo do arquivo CSV
    caminho_completo = os.path.join(pasta_destino, nome_arquivo)

    # Salvar os dados no arquivo CSV
    df.to_csv(caminho_completo, index=False)
    print(f"Dados da tabela '{tabela}' exportados com sucesso para {caminho_completo}")

# Fechar a conexão
conexao.close()
