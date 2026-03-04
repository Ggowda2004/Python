#same method name, behaving differently depending on the object that calls it
#types: compile time polymorphism(not supported in python) -> method overloading, runtime -> child overrides a method in parent


#following example does not use init because it does not store any values, it only performs actions
class PaymentMethod:
    def pay(self, amount):
        print(f"Paying {amount}")

class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Card")

class CryptoPayment(PaymentMethod):
    pass

#uses Design guarantee, Future safety(crypto payment), 

payments = [UPIPayment(), CardPayment(), CryptoPayment()]
for p in payments:
    p.pay(500)

#this example also implemented hierarchial inheritance
#better understood with abstraction



#simpler example
class Vehical:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print(f'{self.brand} is stating....')
class car(Vehical):
    def start(self):
        print(f'{self.brand} started')
v1=Vehical("generic")
v2=car("tesla")
v1.start()
v2.start()