# Inicializa a lista de extratos e o saldo da conta
lista_extratos = []
saldo = 1000.00

# Função para salvar o extrato de operações
def salvar_extrato(operacao, valor, saldo):
    global lista_extrato
    
    # Adiciona um extrato formatado à lista de extratos
    lista_extratos.append(f'''        
    Operação de {operacao} no valor de R$ {valor:.2f}
    Saldo final: {saldo:.2f}
    ''')

# Função para depositar um valor na conta
def depositar(valor):
    global saldo
    print('O valor foi depositado a sua conta')
    
    # Salva o extrato:
    saldo += valor
    salvar_extrato('Depósito', valor, saldo)

# Função para sacar um valor da conta
def sacar(valor, saques_realizados):
    global saldo
    if saques_realizados == 3:            # Verifica se o limite de saques diários foi atingido
        print('   Limite de Saque diário estourado!\nPor favor tente novamente amanhã...')
        return
    if valor > saldo:                     # Verifica se o valor do saque é maior que o saldo disponível
        print(f'   Operação não Realizada\nValor disponível para saque: R$ {saldo:.2f}')
        return
    if valor > 500:                       # Verifica se o valor do saque é maior que o limite permitido
        print('   Valor máximo de saque: R$500,00\nPor favor tente novamente...')
        return
    
    print('Sacando Valor! retire abaixo do caixa')
    
    # Salva o extrato: 
    saldo -= valor
    salvar_extrato('Saque', valor, saldo)
    return True

# Interface do usuário
interface = '''
---------------------------------------------------------
               BANCO DIO - ÁREA DE USUÁRIO
---------------------------------------------------------

Opções de Operação:
1. Depositar
2. Sacar 
3. Extrato
4. Sair

obs: Saques de até R$ 500,00
---------------------------------------------------------'''
print(interface)

saques_realizados = 0 # Contador de saques realizados

while True:
    print(f'\nSaldo atual: R$ {saldo:.2f}')
    operacao = input('Operação: ')
    
    if operacao == '1':
        valor_deposito = input('Digite o valor do depósito: ').replace(',', '.')
        
        # Tenta converter o valor do depósito para float e realizar a operação
        try:
            depositar(float(valor_deposito))
        except ValueError:
            print('Valor digitado inválido!')

    elif operacao == '2':
        valor_saque = input('Digite o valor do saque: ').replace(',', '.')
        
        # Tenta converter o valor do saque para float e realizar a operação
        try:
            if sacar(float(valor_saque), saques_realizados):
                saques_realizados += 1
        except ValueError:
            print('Valor digitado inválido!')
        
    elif operacao == '3':
        # Verifica se a lista de extratos está vazia
        if len(lista_extratos) == 0:
            print('Lista de Extratos Vazia! ')
            continue
        
        # Exibe todos os extratos salvos
        print('Extratos da conta:')
        for extrato in lista_extratos:
            print(extrato)
            
    elif operacao == '4':
        # Finaliza o programa
        print('Obrigado por utilizar o Banco DIO, até mais!')
        break
    
    else:
        print('Digite uma operação existente, por favor!')
