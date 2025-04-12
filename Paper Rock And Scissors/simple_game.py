import random 


#make  a list of paper rock and scissors
lst=['paper' , 'rock' , 'scissors']

computer = random.choice(lst)


neil = input('enter your choice:')
print(f'Neil chose {neil}')



print(f'computer chose {computer}')



if computer == 'rock' and neil =='paper':
    print('neil won')
if computer == 'paper' and neil == 'scissors':
    print('Nel Won')
    
if computer == 'scissors' and neil == 'rocl':
    print('Nel Won')



if neil == 'rock' and computer =='paper':
    print('compu won')
if neil == 'paper' and computer == 'scissors':
    print('computer Won')
    
if neil == 'scissors' and computer == 'rocl':
    print('computer Won')
if neil==computer:
    print('draw')





