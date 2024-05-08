menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = int(input("Valor do Depósito: "))
        if deposito > 0:
            saldo = saldo + deposito
            extrato = extrato + "\n Depósito: +"+ str(deposito)
            print("Depósito realizado com sucesso!")
        else:    
            print("Valor inválido! Informe um valor maior que zero!")


    elif opcao == "s":
        if numero_saques < 3:
            saque = int(input("Valor do Saque: "))
            if saque > 0:
                if saque <= saldo:
                    numero_saques += 1
                    saldo = saldo - saque
                    extrato = extrato + "\n Saque...: -"+ str(saque)
                    print("Saque realizado com sucesso!")
                else:
                    print("Saldo insuficiente!!")        
            else:
                print("Valor inválido! Informe um valor maior que zero!")
        else:
            print("Você excedeu o limite de saques diário! Volte amanhã por favor!!")
       


    elif opcao == "e":
        print(f"Extrato: {extrato}")
        print(f"\n Saldo...: R$ {saldo:.2f}")


    elif opcao == "q":
        print("Obrigado por usar nosso Banco. Até breve! \n")
        break

    else:

        print("opção Inválida! Selecione uma das opções disponíveis ou q para Sair")

