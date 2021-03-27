
def calculadora(operacao, n1, n2):
    if operacao == 'soma':
        operacao = n1 + n2
    elif operacao == 'subtracao':
        operacao = n1 - n2
    elif operacao == 'divisao':
        try:
            operacao = n1 / n2
        except:
            print('Não é possível dividir por Zero')
    elif operacao == 'multiplicacao':
        operacao = n1 * n2
    
    return operacao


while True:
    print('=====Escolha umas das operações a serem realizadas: soma, subtracao, divisao ou multiplicacao =====')
    print('===== Para encerrar o programa, pressione enter com o campo vazio =====')
    operacao = input('Digite a operação que quer realizar: ')
    if operacao == '':
        break

    else:
        n1 = float(input('Informe um número: '))
        n2 = float(input('Informe um número: '))
        print(calculadora(operacao, n1, n2))

