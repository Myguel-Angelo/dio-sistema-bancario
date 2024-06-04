lista_cpfs = []
lista_usuários = []
lista_contas = []

numero_conta = 0
lista_extratos = []
saldo_padrao = 0


# FUNÇÕES DA ÁREA DE LOGIN:
def cadastrar_usuario():
    print('Cadastrando novo usuário...')
    global lista_cpfs, lista_usuários
    nome = input('Nome: ')
    cpf = input('CPF: ')
    
    if cpf in lista_cpfs:
        print('O Cpf já esta cadastrado em um usuário')
        return 'Erro'
    
    lista_cpfs.append(cpf)
    data = input('Data de Nascimento: ')
    endereco = input('Endereço: ')
    lista_usuários.append(
        {cpf: {'Nome': nome, 'Data Nascimento': data, 'Endereço': endereco}}
    )

def criar_conta_corrente():
    print('Criando nova Conta Corrente...')
    global lista_cpfs, numero_conta, lista_usuários
    cpf_digitado = input('Informe o CPF do Usuário: ')
    
    if cpf_digitado not in lista_cpfs:
        print('Usuário não identificado, informe um cpf válido!')
        return 'Erro'
    
    numero_conta+=1
    agencia_numero = f'0001-{numero_conta}'
    for user in lista_usuários:
        if cpf_digitado in tuple(user.keys()):
            dono_conta = user[cpf_digitado]['Nome'] 
        
    lista_contas.append(
        {agencia_numero: cpf_digitado}
    )
    print(f'Agencia e Numero da conta: {agencia_numero}, Nome do dono: {dono_conta}')


def entrar():
    global lista_contas
    print('Digite a Agência e o Número da Conta')
    entrada = input('>>> ')
    for conta in lista_contas:
        if entrada in tuple(conta.keys()):
            return conta
    print('Conta Corrente não Encontrada')
    return None


# Interfaces do banco
interface_login = '''
---------------------------------------------------------
                BANCO DIO - ÁREA DE LOGIN
---------------------------------------------------------

Ações disponíveis:
1. Cadastrar Usuário
2. Criar Conta-Corrente
3. Entrar
4. Encerrar

obs: para criar uma conta, é necessário um usuário'''

interface_user = '''
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

def abrir_area_usuario(conta):
    global saldo_padrao, lista_extratos
    lista_extratos = []
    saldo_padrao = 1000.00
    

    # FUNÇÕES DA ÁREA DE USUÁRIO:
    def salvar_extrato(operacao, valor, saldo):
        global lista_extrato
        
        # Adiciona um extrato formatado à lista de extratos
        lista_extratos.append(f'''        
        Operação de {operacao} no valor de R$ {valor:.2f}
        Saldo final: {saldo:.2f}
        ''')

    def depositar(valor):
        global saldo_padrao
        print('O valor foi depositado a sua conta')
        
        # Salva o extrato:
        saldo_padrao += valor
        salvar_extrato('Depósito', valor, saldo_padrao)

    def sacar(valor, saques_realizados):
        global saldo_padrao
        if saques_realizados == 3:            # Verifica se o limite de saques diários foi atingido
            print('   Limite de Saque diário estourado!\nPor favor tente novamente amanhã...')
            return
        if valor > saldo_padrao:              # Verifica se o valor do saque é maior que o saldo disponível
            print(f'   Operação não Realizada\nValor disponível para saque: R$ {saldo_padrao:.2f}')
            return
        if valor > 500:                       # Verifica se o valor do saque é maior que o limite permitido
            print('   Valor máximo de saque: R$500,00\nPor favor tente novamente...')
            return
        
        print('Sacando Valor! retire abaixo do caixa')
        
        # Salva o extrato: 
        saldo_padrao -= valor
        salvar_extrato('Saque', valor, saldo_padrao)
        return True

    
    global lista_contas, lista_usuários, interface_login
    print(
        'Entrando na conta localizada:',
        f'Dados: {conta}'
    )
    print(interface_user)
    saques_realizados = 0 # Contador de saques realizados

    while True:
        print(f'\nSaldo atual: R$ {saldo_padrao:.2f}')
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
            print('\n', interface_login)
            break
        
        else:
            print('Digite uma operação existente, por favor!')


print(interface_login)
while True:
    acao = input('\nAção: ')
    if acao == '1':
        if cadastrar_usuario() is not None:
            print('Tente cadastrar novamente...')
            continue
        print('Usuário Cadastrado com SUCESSO!')
        
    elif acao == '2':
        if len(lista_usuários) == 0:
            print('Ainda não há usuários Cadastrados\nNão será possível criar uma conta corrente')
            continue
        if criar_conta_corrente() is not None:
            print('Tente criar a conta novamente...')
            continue
        print('Conta Corrente criada com SUCESSO!')
        
    elif acao == '3':
        conta_logada = entrar()
        if conta_logada is None:
            print('Tente em uma conta existemte, ou crie uma nova')
            continue
        abrir_area_usuario(conta_logada)
        
    elif acao == '4':
        print('ENCERRANDO O SISTEMA...')
        break
    
    else:
        print('Digite uma ação existente, por favor!')