#inheritance :-> one class use the properties and methods of another class (derived class)
#4 types-> single, multi level(don't use), hiearchial (1 to many), multiple (many to one)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print (f"My name is {self.name} and I am {self.age} years old")
    
#super keyword is used to call parent class methods/ constructors inside it

class Customer(Person):
    def __init__(self, name, age, customer_id):
        super().__init__(name,age)
        self.customer_id=customer_id

    def get_role(self):
        print(f"I am customer {self.name} with id {self.customer_id}")

person1=Person("Mahesh",25)
person1.introduce()

customer1=Customer("Pratham",30,123)
customer1.get_role()
customer1.introduce()