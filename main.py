'''
Instruções:
Apenas 1 usuário
3 opções no menu: Depósito, Saque e Extrato
Saques: Apenas 3 saques diários  e limite de 500 reais por saque. Se não houver saldo, o sistema deve informar o usuário.
O extrato deve exibir os depósitos, os saques e o saldo, em formato RS com 2 casas decimais

'''



# menu
from decimal import Decimal
option = ''
error_count = 0
balance = Decimal(0.00)
withdrawal_count = 0
MAXWITHDRAWAL = Decimal(500.00)
deposit_rec = []
withdrawal_rec = []
while option != 'f':
    print('''

x=====================================x
       Bem vindo ao Soprana Bank!
      
 Por favor, digite a opção desejada:
    [D]epósitos
    [S]aques
    [E]xtratos
    [A]juda
    [F]echar
x=====================================x
'''      
)

    option = input('>>>: ').lower()

    if option == 'd':
        deposit = Decimal(input('Digite o valor que deseja depositar: ').replace(',', '.'))
        balance += deposit
        print(f'Seu novo saldo é de R$ {float(balance):2f}')
        deposit_rec.append(float(deposit))



    elif option == 's':
        if withdrawal_count != 3:
            withdrawal = Decimal(input('Digite o valor que deseja sacar: ').replace(',', '.'))
            if withdrawal > balance:
                print('Saldo insuficiente!')
                continue
            if withdrawal > MAXWITHDRAWAL:
                print('O valor é acima do máximo permitido. Escolha valor até:', MAXWITHDRAWAL)
            else:
                withdrawal_count += 1
                balance -= withdrawal
                print('Seu novo saldo é:', balance)
                withdrawal_rec.append(float(withdrawal))
        else:
            print('Você já fez 3 saques diários. Tente novamente amanhã.')
            continue
      

    elif option == 'e':
        print('''
        x=======EXTRATO========x
        
        '''
        )
        print(f'Seu saldo atual é de R$ {balance:2f}')
        if withdrawal_rec == []:
            print('Você não fez saques ainda.')
        else:
            print(f'Você já fez estes saques hoje: {withdrawal_rec}')
            print(f'Você já fez {withdrawal_count} saques hoje')
        if deposit_rec == []:
            print('Você ainda não fez depósitos hoje.')
        else:
            print(f'Seus depósitos de hoje foram: {deposit_rec}')




    elif option == 'a':
        print('''
        x=======AJUDA========x
        - Para fazer um depósito, digite "D" no menu principal e informe o valor que deseja depositar.
        - Para fazer um saque, digite "S" no menu principal e informe o valor que deseja sacar. 
        Lembre-se que você só pode fazer 3 saques por dia e o valor máximo por saque é de R$ 500,00.
        - Para ver seu extrato, digite "E" no menu principal. Lá você verá seu saldo atual, seus depósitos e saques realizados no dia.
        - Para fechar o programa, digite "F" no menu principal.
        x=====================x
        ''')

    elif option == 'f':
        print('Obrigado por usar o Soprana Bank. Volte sempre!')
        break
    
    else:
        print('Você não digitou uma opção válida. por favor tente de novo!')
        error_count += 1
        if error_count == 3:
            print('Você excedeu suas tentativas por hoje. Por segurança encerraremos o acesso.')
            break

        

    

    


