#"The process of hiding internal implementation details and showing only the essential features of an object to the user. It focuses on what an object does rather than how it does it."

from abc import ABC, abstractmethod
class SmartDevice(ABC):

    @abstractmethod
    def turn_on(self):
         #Every device must have a turn_on method.
         pass
    @abstractmethod
    def turn_off(self):
        #Every device must have a turn_off method.
        pass
class SonyTV(SmartDevice):
    def turn_on(self):
        print("Sony TV: Connecting to Wi-Fi... Displaying Logo... Power ON.")
    def turn_off(self):
        print("Sony TV:Power OFF.")

tv1=SonyTV()# Testing the Abstraction
tv1.turn_on()# The user doesn't care HOW it turns on, just that it DOES.
tv1.turn_off()

#You cannot do device = SmartDevice(). Python prevents this because a "generic" smart device doesn't exist in reality