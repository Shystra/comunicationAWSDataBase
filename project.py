import pyodbc
import mysql.connector

conn = pyodbc.connect( # CONEXÃO COM BANCO DE DADOS SQL
                      )


cursor = conn.cursor()
cursor.execute("""

                    SELECT DISTINCT --TOP 100

                    # ...DADOS TABELAS

                    FROM // CHAVE API

                    # ...DADOS TABELAS

                    --ORDER

                """)  # Executing a query

# Configuração da conexão MYsql Aws
config = { ##### CONEXÃO BANCO DE DADOS AWS RDS #######
#   'host':
#   'user': 
#   'password': 
#   'database': 
#   'auth_plugin' : 
}

cnx = mysql.connector.connect(**config)
print("Conexao bem Sucedida - Mysql aws Plataformas")

cursor2 = cnx.cursor()

# Criar a lista de tuplas com os valores a serem inseridos
values = []
for row in cursor.fetchall():
    # values.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

# Inserir as linhas na tabela correspondente do MySQL
insert_query = # TABELAR DADOS
cursor2.execute("")
cursor2.executemany(insert_query, values)


# Confirmar as alterações
cnx.commit()

# Fechar a conexão e o cursor
cursor.close()
cnx.close()