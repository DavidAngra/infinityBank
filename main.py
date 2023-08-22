from banco import *

from operacoes.transferencia import transferir
from operacoes.saque import sacar
from operacoes.consulta import consultaSaldo
from operacoes.deposito import depositar

def menu():
    while True:
        print('----- BEM VINDO AO INFINITY BANK -----')
        print('1 - Adicionar conta')
        print('2 - Alterar nome')
        print('3 - Consultar conta')
        print('4 - Remover conta')
        print('5 - Listar contas')
        print('6 - Realizar saque')
        print('7 - Realizar depósito')
        print('8 - Consultar saldo')
        print('9 - Realizar transferência')
        print('10 - Sair')
        opcao = int(input('Selecione uma opção: '))

        if opcao == 1:
            nome = input('Digite o nome do cliente: ')
            saldo = float(input('Digite o saldo do cliente: '))
            adicionarConta(nome, saldo)
        elif opcao == 2:
            conta = int(input('Digite o número da conta: '))
            nome = input('Digite o novo nome: ')
            atualizarNome(conta, nome)
        elif opcao == 3:
            conta = int(input('Digite o número da conta: '))
            print(obterConta(conta))
        elif opcao == 4:
            conta = int(input('Digite o número da conta: '))
            deletarConta(conta)
        elif opcao == 5:
            listarContas()
        elif opcao == 6:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor do saque: '))
            sacar(conta, valor)
        elif opcao == 7:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor do depósito: '))
            depositar(conta, valor)
        elif opcao == 8:
            conta = int(input('Digite o número da conta: '))
            consultaSaldo(conta)
        elif opcao == 9:
            contaOri = int(input('Informe a conta de origem: '))
            contaDes = int(input('Informe a conta de destino: '))
            valor = float(input('Informe o valor: '))
            transferir(contaOri, contaDes, valor)
        elif opcao == 10:
            print('Você saiu do sistema!')
            break
        else:
            print('Opção inválida!')

menu()
