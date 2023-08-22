from banco import obterConta, banco

def depositar(conta: int, valor: float) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente['saldo'] += valor
        print('Depósito realizado com sucesso!')
    else:
        print('Conta não existe!')


if __name__ == '__main__':
    depositar(2, 500)
    print(banco)
