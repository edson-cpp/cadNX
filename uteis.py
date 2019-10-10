def menuPrin():
    """
    ---> Exibe menu da tela principal
    :return: Sem retorno
    """
    print('[ 1 ] - Cadastro de Clientes')
    print('[ 2 ] - Cadastro de Produtos')
    print('[ 3 ] - Cadastro de Contas')
    print('[ 4 ] - Vendas')
    print('[ 5 ] - Sair')


def menuCad():
    """
    ---> Exibe menu das telas de cadastro
    :return: Sem retorno
    """
    print('[ 1 ] - Cadastrar')
    print('[ 2 ] - Alterar')
    print('[ 3 ] - Excluir')
    print('[ 4 ] - Consultar')
    print('[ 5 ] - Listar')
    print('[ 6 ] - Exportar')
    print('[ 7 ] - Menu')

def campoInt(msg):
    """
    ---> Controla possíveis erros de digitação ou de tipos incorretos passados pelo usuário: Formatação Int
    :param msg: Mensagem a ser passada no input - Type(str)
    :return: Retorna o valor digitado pelo usuário
    """
    valor = 0
    while True:
        try:
            valor = int(input(msg))
        except KeyboardInterrupt:
            continue
        except (ValueError, TypeError):
            print('Tipo de dado incorreto, por favor informe um valor inteiro.')
            continue
        except Exception as erro:
            print(f'Ocorreu um erro inesperado, por favor tente novamente.')
            continue
        else:
            break
    return valor

def campoFloat(msg):
    """
    ---> Controla possíveis erros de digitação ou de tipos incorretos passados pelo usuário: Formatação Float
    :param msg: Mensagem a ser passada no input - Type(str)
    :return: Retorna o valor digitado pelo usuário
    """
    valor = 0.0
    while True:
        try:
            str_val = input(msg)
            str_val = str_val.replace(',', '.')
            if str_val.count('.') > 1:
                print('Formato inválido, não informe pontuação na milhar. Use o formato: 1200,25')
                continue
            else:
                valor = float(f"{float(str_val):.2f}")
        except KeyboardInterrupt:
            continue
        except (ValueError, TypeError):
            print('Tipo de dado incorreto, por favor informe um valor numérico.')
            continue
        except Exception as erro:
            print(f'Ocorreu um erro inesperado, por favor tente novamente.')
            continue
        else:
            break
    return valor

def campoStr(msg, comp=0, alt=False, campo='', valor=''):
    """
    ---> Controla possíveis erros de digitação ou de tipos incorretos passados pelo usuário: Formatação String
    :param msg: Mensagem a ser passada no input - Type(str)
    :param comp: comprimento máximo do campo - Type(int)
    :param alt: Define se irá perguntar ao cliente se campo será alterado
    :param campo: Informa nome do campo que será exibido para o cliente perguntando se quer alterar
    :param valor: Valor que se encontra atualmente na base de dados
    :return: Retorna o valor digitado pelo usuário
    """
    alterar = 'S'
    while True:
        try:
            if alt:
                while True:
                    alterar = str(input(f'Alterar campo {campo}: [S/N]: ')).strip().upper()
                    if alterar in 'SN':
                        break
            if alterar == 'S':
                if comp == 0:
                    valor = str(input(msg)).strip()
                else:
                    valor = str(input(msg + f'[ Max {str(comp)}]: ')).strip()
        except KeyboardInterrupt:
            continue
        except (ValueError, TypeError):
            print('Tipo de dado incorreto, por favor tente novamente.')
            continue
        except Exception as erro:
            print(f'Ocorreu um erro inesperado, por favor tente novamente.')
            continue
        else:
            break
    return valor

def exportarArquivoTexto(cls, orig):
    """
    ---> Exporta dados para arquivo texto
    :param cls: classe que irá exportar os dados
    :param orig: origem dos dados a serem exportados (informar capitalizado)
    :return: Sem retorno
    """
    import os.path
    id = campoInt(f'Informe o Código do {orig} [0 = Todos]: ')
    reg = cls.listarRegistros(id, False)
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
