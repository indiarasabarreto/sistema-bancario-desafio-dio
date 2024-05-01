menu = '''

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Erro na operação. Operação inválida!")
    
    elif opcao == "s":
        valor = float(input("Informe valor do saque: "))
        
        saldo_excedido = valor > saldo

        limite_execedido = valor > limite

        saque_excedido = numero_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print("Saldo insuficiente!")
        
        elif limite_execedido:
            print("Limite insuficiente!")
        
        elif saque_excedido:
            print("Saldo insuficiente!")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Valor informado inválido")
    
    
    elif opcao == "e":
        print("\n---------- EXTRATO ----------")
        print("Movimentações não realizadas." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-------------------------------")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")