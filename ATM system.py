#ATM System
from datetime import date
from datetime import datetime

#Get password
def password(attempt):
  pass_word=int(input('            Please enter your password\n                      '))
  attempt+=1

  #Check password
  if pass_word==5604:

    balance=500
    min_remain=10

    while True:

      #Get Date
      # dd/mm/YY
      today = date.today()
      d1 = today.strftime("%d/%m/%Y")

      #Get Time
      #%H:%M:%S
      now = datetime.now()
      time = now.strftime("%H:%M:%S")

      #Get service from user
      print('\n-----------Please choose your service--------------\n')
      print('          1.Withdraw','\t','   2.Deposit','\n','         3.Get balance','    4.Quit')
      c=int(input('\n                      '))
      

      if c==1:
        amount=int(input(' How many dollars you want to withdraw:'))
        if amount<balance and balance-amount>min_remain:
          balance-=amount
          print('---------------------------------------------------')
          print(' Amount:',amount,'$ -','\n','---Withdraw---','\n','Balance:',balance,'$','\n','Date:',d1,'\n','Time:',time)
          print('---------------------------------------------------')
          print(' 1.Get your card','\t','2.Choose an other service')
          d=int(input('\n                      '))
        else:
          print('---------------------------------------------------')
          print(' The balance is not enough')  
          print('---------------------------------------------------')
          print(' 1.Get your card','\t','2.Choose an other service')
          d=int(input('\n                      '))

      elif c==2:
        amount=int(input(' How many dollars you want to deposit:'))
        balance+=amount
        print('---------------------------------------------------')
        print(' Amount:',amount,'$ +','\n','---Deposit---','\n','Balance:',balance,'$','\n','Date:',d1,'\n','Time:',time)
        print('---------------------------------------------------')
        print(' 1.Get your card','\t','2.Choose an other service')
        d=int(input('\n                      '))

      elif c==3:
        print('---------------------------------------------------')
        print(' Balance:',balance,'$','\n','Date:',d1,'\n','Time:',time)
        print('---------------------------------------------------')
        print(' 1.Get your card','\t','2.Choose an other service')
        d=int(input('\n                      '))

      elif c==4:
        print('---------------------------------------------------')
        print(' Have nice day \n Dont forget your credit card!!')
        print('---------------------------------------------------')
        break

      if d==1:
        print('---------------------------------------------------')
        print(' Have nice day \n Dont forget your credit card!!')
        print('---------------------------------------------------')
        break
      elif d==2:
        continue 
  else:
    
    if attempt==3:
      print('\n_________________Your card blocked_________________\n')
      exit()

    print('\n------------------Wrong password-------------------\n')
    password(attempt)


print('\n--------------Welcome to ATM system----------------\n')
password(attempt=0)
