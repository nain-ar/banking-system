class Bank:
    Bankname='Billionaire bank'
    def __init__(self,balance,name):
        self.balance=balance
        self.name=name
    def __str__(self):
        return f"Name: {self.name}, Balance: {self.balance}"
    
class pay_mode(Bank):
       
    def __init__(self, balance,name):
        super().__init__(balance,name)
        self.payment_method=input('enter type(cash,upi,other)')
    
        
        if self.payment_method=='cash':
            print('0.1% charges')
        elif self.payment_method=='upi':
            print('no charges')
        else:
            print('2% charge fee')
            # return 'thanks'
class deposit(pay_mode):
    def __init__(self,amount,balance,name):
        super(). __init__(balance,name)
        self.amount=amount
        if 0<amount:
            self.balance += amount
            print('payment successfully deposited')
        else:
            print('access failed,invalid amount')
class pay_mode(Bank):
       
    def __init__(self, balance,name):
        super().__init__(balance,name)
        self.payment_method=input('enter withdraw type(cash,upi,other)')
    
        
        if self.payment_method=='cash':
            print('0.1% charges ')
        elif self.payment_method=='upi':
            print('no charges')
        else:
            print('2% charge fee is applicable')


class withdraw(pay_mode):
    def __init__(self,amount, balance, name):
        super().__init__(balance, name)
        self.amount=amount
        
        if amount>0 and amount<balance:
            self.balance-=amount
            print('withdraw successfull')
            print('balance remaining',self.balance)
        else:
            print('invalid amount')


# sample

print(Bank.Bankname)    
a1 = deposit(200, 90000, 'meer')
print(a1)
print(Bank.Bankname)
a1=withdraw(5000,90200,'meer')

