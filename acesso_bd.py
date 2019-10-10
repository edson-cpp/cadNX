def conectar():
    import pyodbc

    server = 'localhost\DEV'
    database = 'cadNX'
    username = 'UNX'
    password = '1234'
    try:
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server +
                              ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        return conn
    except Exception as erro:
        print('Ocorreu um erro na conexão com a base de dados.')
        return False

'''conn = conectar()
cursor = conn.cursor()
ret = cursor.execute(f"Select id, nome, rua, num, cep, estado,"
                         f" cidade, bairro, fone, cpf, email From clientes Where id = 1")
row = cursor.fetchone()
if row:
    print('>0')
else:
    print('0')
while row:
    print(row[0])
    row = cursor.fetchone()
conn.close()'''
