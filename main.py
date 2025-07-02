
menu = """
Tecle uma opção:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu).lower()
  
    if opcao == 'd':
        valor = int(input("Informe o valor do depósito: R$"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
            print(f"Seu saldo atual é de R${saldo:.2f}")
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == 's':
        valor = float(input("Informe o valor do saque: R$"))
        
        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
            print(f"Seu saldo atual é de R${saldo:.2f}")
        else:
            print("Operação falhou! O valor informado é inválido.")
       
    elif opcao == 'e':
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("==========================================")

    elif opcao == 'q':
        break   
    else:
        print("Tecla irreconhecível pelo sistema!")