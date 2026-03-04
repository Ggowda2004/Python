class Car:
    def __init__(self,colour,model,drive,type):
        self.colour=colour
        self.model=model
        self.drive =drive
        self.type=type

    def start(self):
        print(f'The car {self.model} has started')
    def stop(self):
        print(f'The car {self.model} has stopped')

car1=Car("Red","Maruthi","4wd","suv")
car1.start()
car1.stop()