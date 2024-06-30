import textwrap

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR${valor:.2f}\n"
        print("\nDepósito relizado com sucesso!")

    else:
        print("\nOperação não realizada! O valor do depósito é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if saldo == 0 or valor > saldo:
        print("\nOperação não realizada! Saldo insuficiente.")

    elif valor > limite:
        print("\nOperação não realizada! O valor do saque excede o limite permitido.")

    elif numero_saques >= limite_saques:
        print("\nOperação não realizada! Limite de saques diários excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR${valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")

    else:
        print("\nOperação não realizada! O valor do depósito é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n====== DioBank - Extrato ======")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR${saldo:.2f}")
    print("\n===============================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nNúmero de CPF já cadastrado!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nUsuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None                          

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nOperação não realizada! Usuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

menu = """

Bem-vindo ao DioBank, por favor selecione uma das operações do menu abaixo:

================================== MENU ==================================

[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[4]\tCriar Usuário
[5]\tCriar Conta Corrente
[6]\tListar Contas
[0]\tSair

=>"""

AGENCIA = "0001"
LIMITE_SAQUES = 3

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []

while True:
    opcao = input(textwrap.dedent(menu))

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "4":
        criar_usuario(usuarios)

    elif opcao == "5":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "6":
        listar_contas(contas)

    elif opcao == "0":
        print("\nObrigado por usar nosso sistema.")
        break

    else:
        print("\nOperação inválida! Por favor, selecione a operação desejada.")