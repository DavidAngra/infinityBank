from banco import obterConta, banco

def consultaSaldo(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        print(f'Seu saldo = {cliente["saldo"]}')
    else:
        print('Conta não existe!')

if __name__ == '__main__':
    consultaSaldo(1)
    print(banco)
