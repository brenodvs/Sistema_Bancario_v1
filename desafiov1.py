menu= """
    Banco NE
    
    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Sair
=> """
saldo=0
extrato=""
limitesaque=500
limite_saque_dia=3
quantidade_saque=0

while True:
    opcao=int(input(menu))
    
    if opcao==1:
        valor=float(input('Informe o valor a ser depositado: '))
        if(valor<=0):
            print('Valor invalido!')
        else:
            saldo+=valor
            extrato+=f"Deposito: R${valor:.2f}\n"
    elif opcao==2:
        if(quantidade_saque==limite_saque_dia):
            print('Limite de saque diario atingido. Tente novamente outro dia')
        else:
            saque=float(input('Digite o valor que deseja sacar: '))
            if(saque<=0):
                print('Valor invalido! Não é possivel fazer saque negativo.')
            elif(saque>limitesaque):
                print('Valor invalido! O valor de saque é maior que o limite.')
            elif(saque>saldo):
                print('Não existe saldo suficiente para esse saque.')
            else:
                quantidade_saque+=1
                saldo-=saque
                extrato+=f"Saque: R${saque:.2f}\n"
    elif opcao==3:
        print('\n#################### Extrato ####################')        
        print('Não foi realizado movimentações' if not extrato else extrato)
        print(f'Seu saldo é de: R${saldo:.2f}')
        print('#################################################')
    elif opcao==4:
        print("Volte Sempre!")
        break
    else:
        print('Valor invalido. Tente novamente!')

