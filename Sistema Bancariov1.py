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
        deposito = float(input("Valor do Depósito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"\n Depósito: R$ {deposito:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:   
            print("Valor inválido! Informe um valor maior que zero!")


    elif opcao == "s":
        if numero_saques < 3:
            saque = float(input("Valor do Saque: "))
            if saque > 0:
                
                if saque <= saldo:
                    
                    if saque <= 500:
                        numero_saques += 1
                        saldo -= saque
                        extrato += f"\n Saque...: R$ {saque:.2f}\n"
                        print("Saque realizado com sucesso!")
                    else:
                        print("Valor do Saque maior que seu limite de R$ 500,00")     
                else:
                    print("Saldo insuficiente!!")
            else:
                print("Valor inválido! Informe um valor maior que zero!")
        else:
            print("Você excedeu o limite de saques diário! Volte amanhã por favor!!")
       


    elif opcao == "e":
        print("\n-------------EXTRATO-----------------")
        print(f"Extrato: {extrato}")
        print(f"\n Saldo...: R$ {saldo:.2f}")
        print("\n-------------------------------------")


    elif opcao == "q":
        print("Obrigado por usar nosso Banco. Até breve! \n")
        break

    else:

        print("opção Inválida! Selecione uma das opções disponíveis ou q para Sair")

