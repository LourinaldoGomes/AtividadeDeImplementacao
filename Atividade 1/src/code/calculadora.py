print('MENU INICIAL\n1-ADIÇÃO\n2-SUBTRAÇÃO\n3-MULTIPLICAÇÃO\n4-DIVISÃO')
opc=int(input('Digite o valor da opção escolhida. '))

if opc == 1 :
   print('opção adição selecionada: ')
   num1=int(input('digite o primeiro valor: '))
   num2=int(input('digite o segundo valor: '))
   soma=num1+num2
   print('resultado: '+str(soma))
if opc == 2 :
   print('opção subtração selecionada: ')
   num1=int(input('digite o maior valor: '))
   num2=int(input('digite o menor valor: '))
   sub=num1-num2
   print('resultado: '+str(sub))
if opc == 3 :
   print('opção multiplicação selecionada: ')
   num1=int(input('digite o primeiro valor: '))
   num2=int(input('digite o segundo valor: '))
   mult=num1*num2
   print('resultado: '+str(mult))
if opc == 4 :
   print('opção divisão selecionada: ')
   num1=int(input('digite o primeiro valor: '))
   num2=int(input('digite o segundo valor: '))
   div=float(num1/num2)
   print('resultado: '+str(div))