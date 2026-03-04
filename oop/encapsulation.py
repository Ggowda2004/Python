#protecting data from direct access, and bundling data and method in a single unit(class)
#it uses access modifiers, variable(public), _variable(protected), __variable(private)

class BankAccount:
    def __init__(self, owner, acc_type, balance, pin):
        self.owner = owner
        self._balance = balance
        self.__pin=pin
        self.acc_type=acc_type

    
    def get_balance(self):
        return (self._balance)

    def deposit(self, amount):
        if amount>0:
            self._balance+=amount
            print(f"new balance: {self._balance}")
        else:
            print ("amount to deposite is too low")
    def withdraw(self, amount, pin):
        if pin==self.__pin:
            if amount>0 and self._balance>=amount:
                self._balance-=amount
                print(f"new balance: {self._balance}")
            else:
                print ("account balance low, or incorrect amount entered")
        else:
            print("incorrect pin entered")


user1=BankAccount("Suresh","savings",200,1900)
print(user1.get_balance())
user1.deposit(200)
user1.withdraw(300,1980)
print(user1.owner)
print(user1._balance) # this variable is for internal use. Please don’t touch it unless you know what you’re doing.”
#using single _ only changes naming

#actual use of encapsulation 
print(user1.__pin) #but still van be accesed using (user1._BankAccount__pin)