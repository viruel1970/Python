def depositar(saldo, deposito, extrato,/):
    if deposito > 0:
        saldo += deposito
        extrato += f"\n Depósito: R$ {deposito:.2f}"
        print("\n >>> Depósito realizado com sucesso! <<<")
    else:   
        print("\n !!! Valor inválido! Informe um valor maior que zero! !!!")
    return saldo, extrato

def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        saque = float(input("Valor do Saque: "))
        if saque > 0:
                
            if saque <= saldo:
                    
                if saque <= limite:
                        numero_saques += 1
                        saldo -= saque
                        extrato += f"\n Saque...: R$ {saque:.2f}"
                        print("\n >>> Saque realizado com sucesso! <<<")
                else:
                        print("\n !!! Valor do Saque maior que seu limite de R$ 500,00 !!!")     
            else:
                    print("\n !!! Saldo insuficiente!! !!!")
        else:
                print("\n !!! Valor inválido! Informe um valor maior que zero! !!!")
    else:
            print("\n !!! Você excedeu o limite de saques diário! Volte amanhã por favor!! !!!")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n-------------EXTRATO-----------------")
    print(f"\n {extrato}")
    print(f"\n Saldo...: R$ {saldo:.2f}")
    print("\n-------------------------------------")

def cadastrar_cliente(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cpf_existe = buscar_cpf(cpf, clientes)
    if cpf_existe:
        print("\n !!! CPF já cadastrado! Por favor informe um novo CPF! !!!")
        return
    else:
        nome =            input("Nome do Cliente...: ")
        data_nascimento = input("Data de Nascimento: ")
        endereco        = input("Endereço completo.: ")
        clientes.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
        print("\n >>> Cliente cadastrado com sucesso! <<<")
                      

def buscar_cpf(cpf, clientes):
    cpf_validado = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return cpf_validado[0] if cpf_validado else None

def cadastrar_conta(agencia, contas, clientes):
    cpf = input("Informe o CPF do cliente: ")
    cpf_existe = buscar_cpf(cpf, clientes)
    if cpf_existe:
        nr_conta = len(contas) + 1
        contas.append({"agencia": agencia, "nr_conta": nr_conta, "Cliente": cpf_existe})
        print("\n >>> Conta cadastrada com sucesso! <<<")
    else:    
        print("\n !!! Não existe um cliente cadastrado para este CPF! !!!")

def exibir_contas(contas):
    print("\n-------------CONTAS CADASTRADAS-----------------\n")
    for conta in contas:
        linha = f"""\
            Titular:\t{conta['Cliente']['nome']}
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['nr_conta']}
            
        """
        print("=" * 100)
        print(linha)

menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Cliente
[o] Cadastrar Conta
[m] Mostrar contas
[q] Sair
==> '''

LIMITE_SAQUES = 3
AGENCIA = "0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
clientes = []
contas = []



while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Valor do Depósito: "))
        saldo, extrato = depositar(saldo, deposito, extrato) 


    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(
            saldo=saldo, 
            saque=0, 
            extrato=extrato, 
            limite=limite, 
            numero_saques=numero_saques , 
            limite_saques=LIMITE_SAQUES
       )


    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "c":  ## cadastrar cliente
        cadastrar_cliente(clientes)

    elif opcao == "o":  ## cadastrar conta
        cadastrar_conta(AGENCIA, contas, clientes)

    elif opcao == "m": ## exibir contas
        exibir_contas(contas)

    elif opcao == "q":
        print("\n >>> Obrigado por usar nosso Banco. Até breve! \n")
        break

    else:

        print("\n !!! opção Inválida! Selecione uma das opções disponíveis ou q para Sair! !!!")

