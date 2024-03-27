
menu = """
[d] depositar
[s] sacar
[e] extrato
[q] sair            
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limete_saques = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe valor a ser depositado "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito de RS {valor:.2f}\n"
            print("\nDeposito Realizado com Sucesso !\n")
        else:
            print("operacao falhou! o valor informado é invalido.")            

    elif opcao == "s":
        valor = float(input("informe o valor do saque:"))
        passou_saldo = valor > saldo
        passou_limite = valor > limite
        passou_saques = numero_saques >= limete_saques

        if passou_saldo:
            print("saldo insuficiente...")
        elif passou_limite:
            print("o valor do salque passou do limite permitido")
        elif passou_saques:
            print("ops so pode fazer 3 saques por dia, volte amanha")
        elif valor >0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques += 1 
            print("\nSaque Realizado!\n ")
        else:
            print("operacao falhou !  O valor informado é invalido .")
    elif opcao == "e":
        print("\n =================== EXTRATO =================== ")
        print(f"\nSaldo: R$ {saldo:.2f}\n")
        print(extrato)
        print("\n ====================================== ")
    elif opcao == "q":
        print("Ate mais... ")
        break
    else:
        print("opcao invalida, por favor digite opcao valida")