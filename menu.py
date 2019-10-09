from uteis import menuPrin
from cadastros.cadcli import CadClientes
from cadastros.cadpro import CadProdutos
from cadastros.cadcont import CadContas


while True:
    try:
        print('{:=^40}'.format(' MENU PRINCIPAL '))
        menuPrin()
        op = int(input('Selecione uma opção: '))
    except KeyboardInterrupt:
        continue
    except (ValueError, TypeError):
        print('Tipo de dado incorreto, por favor selecione um número de 1 a 4.')
        continue
    except Exception as erro:
        print(f'Ocorreu um erro ao selecionar a opção, por favor tente novamente.')
        continue
    if op == 1:
        cadcli = CadClientes()
        cadcli.cad_clientes()
    elif op == 2:
        cadpro = CadProdutos()
        cadpro.cad_produtos()
    elif op == 3:
        cadcont = CadContas()
        cadcont.cad_contas()
    elif op == 4:
        break
    else:
        print('Opção inválida, por favor selecione um número de 1 a 4.')
        continue
