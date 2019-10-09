from uteis import menuCad, campoInt, campoStr
from acesso_bd import conectar
import os.path

class CadContas:
    def listarRegistros(self, id=0, imp=True):
        try:
            conn = conectar()
            cursor = conn.cursor()
            if id == 0:
                ret = cursor.execute(f"Select id, descricao, agencia, numero From contas")
            else:
                ret = cursor.execute(f"Select id, descricao, agencia, numero From contas Where id = {id}")
            row = cursor.fetchone()
            if not row:
                print('-' * 40)
                print('Não há registros!')
                print('-' * 40)
                return False
            else:
                if imp:
                    if id == 0:
                        print('=' * 40)
                    else:
                        print('-' * 40)
                    while row:
                        reg = {'Código': row[0], 'Descrição': row[1], 'Agência': row[2], 'Número da Conta': row[3]}
                        print(reg)
                        print('-' * 40)
                        row = cursor.fetchone()
                    if id == 0:
                        print('=' * 40)
                    return reg
                else:
                    lista = list()
                    while row:
                        reg = {'Código': row[0], 'Descrição': row[1], 'Agência': row[2], 'Número da Conta': row[3]}
                        lista.append(reg)
                        row = cursor.fetchone()
                    return lista
            conn.close()
        except Exception as erro:
            print(f'Ocorreu um erro na consulta dos dados, por favor tente novamente.')
            return False

    def cad_contas(self):
        while True:
            try:
                print('{:=^40}'.format(' CADASTRO DE CONTAS '))
                menuCad()
                op = int(input('Selecione uma opção: '))
            except KeyboardInterrupt:
                continue
            except (ValueError, TypeError):
                print('Tipo de dado incorreto, por favor selecione um número de 1 a 7.')
                continue
            except Exception as erro:
                print(f'Ocorreu um erro ao selecionar a opção, por favor tente novamente.')
                continue

            if op == 1:
                self.cadastrar()
            elif op == 2:
                self.alterar()
            elif op == 3:
                self.excluir()
            elif op == 4:
                self.consultar()
            elif op == 5:
                self.listar()
            elif op == 6:
                self.exportar()
            elif op == 7:
                break
            else:
                print('Opção inválida, por favor selecione um número de 1 a 7.')
                continue

    def cadastrar(self):
        desc = campoStr('Descrição ', 50)
        age = campoStr('Agência ', 10)
        num = campoStr('Número da Conta ', 20)
        try:
            conn = conectar()
            cursor = conn.cursor()
            ret = cursor.execute(
                f"Insert Into contas(descricao, agencia, numero) Values('{desc}', '{age}', '{num}')")
            conn.commit()
            conn.close()
            print('-' * 40)
            print(f'Registro incluído com sucesso.')
            print('-' * 40)
        except Exception as erro:
            print(f'Ocorreu um erro ao inserir, por favor tente novamente.')

    def alterar(self):
        id = campoInt('Código: ')
        reg = self.listarRegistros(id)
        if reg:
            try:
                desc = campoStr('Descrição ', 50, True, 'Descrição', reg['Descrição'])
                age = campoStr('Agência ', 10, True, 'Agência', reg['Agência'])
                num = campoStr('Número da Conta ', 20, True, 'Número da Conta', reg['Número da Conta'])

                conn = conectar()
                cursor = conn.cursor()
                ret = cursor.execute(
                    f"Update contas Set descricao = '{desc}', agencia = '{age}', numero = '{num}' Where id = {id}")
                conn.commit()
                conn.close()
                print('-' * 40)
                print(f'Registro alterado com sucesso.')
                print('-' * 40)
            except Exception as erro:
                print(f'Ocorreu um erro ao alterar, por favor tente novamente.')

    def excluir(self):
        id = campoInt('Código: ')
        reg = self.listarRegistros(id)
        if reg:
            try:
                while True:
                    resp = str(input('Tem certeza que deseja excluir o registro acima? [S/N]: ')).strip().upper()
                    if resp in 'SN':
                        break
                if resp == 'S':
                    conn = conectar()
                    cursor = conn.cursor()
                    ret = cursor.execute(f"Delete From contas Where id = {id}")
                    conn.commit()
                    conn.close()
                    print('-' * 40)
                    print(f'Registro excluído com sucesso.')
                    print('-' * 40)
                else:
                    print('-' * 40)
                    print(f'O registro NÃO foi excluído.')
                    print('-' * 40)
            except Exception as erro:
                print(f'Ocorreu um erro ao alterar, por favor tente novamente.')

    def consultar(self):
        id = campoInt('Código: ')
        self.listarRegistros(id)

    def listar(self):
        self.listarRegistros()

    def exportar(self):
        id = campoInt('Código [0 = Todos]: ')
        reg = self.listarRegistros(id, False)
        if reg:
            arq = campoStr('Informe o nome do arquivo onde serão salvos os dados: ', 50)
            while True:
                dir = campoStr('Informe o caminho completo do arquivo [C = Cancelar]: ', 100)
                if dir in 'Cc' or os.path.exists(dir):
                    break
                else:
                    print('Diretório inexistente!')
            if dir not in 'Cc':
                try:
                    dir = dir.replace('\\', '/')
                    if dir[-1:] != '/':
                        dir += '/'
                    if arq[-4:] != '.txt':
                        arq += '.txt'
                    a = open(dir + arq, 'w')
                    conteudo = ''
                    for i in reg:
                        conteudo += str(i) + '\n'
                    a.write(conteudo)
                    a.close()
                    print('-' * 40)
                    print(f'Registro exportado com sucesso.')
                    print('-' * 40)
                except Exception as erro:
                    print(f'Ocorreu um erro ao exportar os dados, por favor tente novamente.')
