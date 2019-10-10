from uteis import menuCad, campoInt, campoStr, campoFloat
from acesso_bd import conectar
import os.path
from cadastros.cadcli import CadClientes
from cadastros.cadpro import CadProdutos
from datetime import datetime

class Vendas:
    def listarRegistros(self, id=0, imp=True, item=0):
        try:
            conn = conectar()
            cursor = conn.cursor()
            if id == 0:
                if item == 0:
                    ret = cursor.execute(f"Select id, nome_clientes, dataven, totalven From vendas")
                else:
                    ret = cursor.execute(f"Select id, descricao_produtos, preco, qtde, total_item From proven")
            else:
                if item == 0:
                    ret = cursor.execute(f"Select id, nome_clientes, dataven, totalven From vendas Where id = {id}")
                else:
                    ret = cursor.execute(f"Select id_produtos, descricao_produtos,"
                                         f" preco, qtde, total_item From proven Where id_vendas = {id}")
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
                        if item == 0:
                            reg = {'Código': row[0], 'Nome do Cliente': row[1], 'Data da Venda': row[2], 'Total': row[3]}
                        else:
                            reg = {'Código do Produto': row[0], 'Descrição': row[1], 'Preço': row[2], 'Qtde': row[3], 'Total do Item': row[4]}
                        print(reg)
                        print('-' * 40)
                        row = cursor.fetchone()
                    if id == 0:
                        print('=' * 40)
                    return reg
                else:
                    lista = list()
                    while row:
                        if item == 0:
                            reg = {'Código': row[0], 'Nome do Cliente': row[1], 'Data da Venda': row[2], 'Total': row[3]}
                        else:
                            reg = {'Código': row[0], 'Descrição': row[1], 'Preço': row[2], 'Qtde': row[3], 'Total do Item': row[4]}
                        lista.append(reg)
                        row = cursor.fetchone()
                    return lista
            conn.close()
        except Exception as erro:
            print(f'Ocorreu um erro na consulta dos dados, por favor tente novamente.')
            return False

    def venda(self):
        while True:
            try:
                print('{:=^40}'.format(' VENDAS '))
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
        while True:
            id = campoInt('Informe o código do cliente [0 para listar os cadastros, -1 para cancelar a inclusão]: ')
            cadcli = CadClientes()
            if id == 0:
                CadClientes.listarRegistros(CadClientes.__init__(cadcli))
            elif id == -1:
                return
            else:
                reg = CadClientes.listarRegistros(CadClientes.__init__(cadcli), id, False)
                if reg:
                    idcli = id
                    nomecli = reg[0]['Nome']
                    break

        proven = list()
        while True:
            id = campoInt('Informe o código do produto [0 para listar os cadastros, -1 para cancelar a inclusão]: ')
            cadpro = CadProdutos()
            if id == 0:
                CadProdutos.listarRegistros(CadProdutos.__init__(cadpro))
            elif id == -1:
                return
            else:
                reg = CadProdutos.listarRegistros(CadProdutos.__init__(cadpro), id, False)
                if reg:
                    qtde = campoFloat('Informe a quantidade vendida: ')
                    reg[0]['Qtde'] = qtde
                    proven.append(reg[0])
                    while True:
                        resp = campoStr('Incluir outro produto? [S/N]: ').upper()
                        if resp in 'SN':
                            break
                    if resp == 'N':
                        break

        totven = 0
        for i in proven:
            totven += float(i['Preço']) * i['Qtde']

        try:
            conn = conectar()
            cursor = conn.cursor()
            ret = cursor.execute(
                f"Insert Into vendas(id_clientes, nome_clientes, dataven, totalven) "
                f"Values({idcli}, '{nomecli}', '{str(datetime.today())[:19]}', {totven})")
            ret = cursor.execute("Select max(id) From vendas")
            row = cursor.fetchone()
            for i in proven:
                cod = i['Código']
                desc = i['Descrição']
                preco = i['Preço']
                qtde = i['Qtde']
                ret = cursor.execute(
                    f"Insert Into proven(id_vendas, id_produtos, descricao_produtos, preco, qtde, total_item) "
                    f"Values({row[0]}, {cod}, '{desc}', {preco}, {qtde}, {float(preco) * qtde})")
            conn.commit()
            print('-' * 40)
            print(f'Registro incluído com sucesso.')
            print('-' * 40)
        except Exception as erro:
            conn.rollback()
            print(f'Ocorreu um erro ao inserir, por favor tente novamente.')
        finally:
            conn.close()

    def alterar(self):
        print('-' * 40)
        print('Função não implementada!')
        print('-' * 40)
        return

        #Função incompleta
        '''id = campoInt('Código: ')
        reg = self.listarRegistros(id)
        if reg:
            idven = id
            idcli = 0
            while True:
                altven = campoStr('Alterar dados da venda? [S/N/C]: ').upper()
                if altven == 'C':
                    return
                if altven in 'SN':
                    break
            if altven == 'S':
                while True:
                    id = campoInt('Informe o código do cliente [0 para listar os cadastros, -1 para cancelar a alteração]: ')
                    cadcli = CadClientes()
                    if id == 0:
                        CadClientes.listarRegistros(CadClientes.__init__(cadcli))
                    elif id == -1:
                        return
                    else:
                        reg = CadClientes.listarRegistros(CadClientes.__init__(cadcli), id, False)
                        if reg:
                            idcli = id
                            nomecli = reg[0]['Nome']
                            break

            while True:
                altven = campoStr('Alterar dados dos produtos? [S/N/C]: ').upper()
                if altven == 'C':
                    return
                if altven in 'SN':
                    break
            if altven == 'S':
                regpro = self.listarRegistros(idven, False, 1)
                while True:
                    id = campoInt('Informe o código do produto [0 para listar os cadastros, -1 para cancelar a alteração]: ')
                    cadpro = CadProdutos()
                    if id == 0:
                        CadProdutos.listarRegistros(CadProdutos.__init__(cadpro))
                    elif id == -1:
                        return
                    else:
                        for i in regpro:
                            if id == i[0]['Código do Produto']:
                                while True:
                                    resp = campoStr('Produto já está na venda. [A] Alterar, [E] Excluir: ')
                                    if resp in 'AE':
                                        break
                                regpro[i]['Ação'] = resp
                        reg = CadProdutos.listarRegistros(CadProdutos.__init__(cadpro), id, False)
                        if reg:
                            idcli = id
                            nomecli = reg[0]['Nome']
                            break

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
                print(f'Ocorreu um erro ao alterar, por favor tente novamente.')'''

    def excluir(self):
        while True:
            id = campoInt('Código [0 para listar]: ')
            reg = self.listarRegistros(id)
            if id != 0:
                break

        if reg:
            try:
                while True:
                    resp = str(input('Tem certeza que deseja excluir o registro acima? [S/N]: ')).strip().upper()
                    if resp in 'SN':
                        break
                if resp == 'S':
                    conn = conectar()
                    cursor = conn.cursor()
                    ret = cursor.execute(f"Delete From vendas Where id = {id}")
                    ret = cursor.execute(f"Delete From proven Where id_vendas = {id}")
                    conn.commit()
                    print('-' * 40)
                    print(f'Registro excluído com sucesso.')
                    print('-' * 40)
                else:
                    print('-' * 40)
                    print(f'O registro NÃO foi excluído.')
                    print('-' * 40)
            except Exception as erro:
                conn.rollback()
                print(f'Ocorreu um erro ao alterar, por favor tente novamente.')
            finally:
                conn.close()

    def consultar(self):
        id = campoInt('Código: ')
        self.listarRegistros(id)

    def listar(self):
        self.listarRegistros()

    def exportar(self):
        id = campoInt('Informe o Código da Venda [0 = Todas]: ')
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
                        regpro = self.listarRegistros(i['Código'], False, 1)
                        for x in regpro:
                            conteudo += '    ' + str(x) + '\n'
                        conteudo += '\n'
                    a.write(conteudo)
                    a.close()
                    print('-' * 40)
                    print(f'Registro exportado com sucesso.')
                    print('-' * 40)
                except Exception as erro:
                    print(f'Ocorreu um erro ao exportar os dados, por favor tente novamente.')
