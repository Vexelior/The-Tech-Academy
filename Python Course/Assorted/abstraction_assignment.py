from abc import ABC, abstractmethod
class Blocks(ABC):
    def current_blocks(self, amount):
        print("Your have currently walked this many blocks: ",amount)
# This function is telling us to pass in an argument, but we won't tell you how or what kind
# of data it will be.
    @abstractmethod
    def total_blocks(self, amount):
        pass

class Walking(Blocks):
# Here we've defined how to implement the payment function from its parent 'Blocks' class.
    def total_blocks(self, amount):
        print("Your have walked a total of {} blocks.".format(amount))

obj = Walking()
obj.current_blocks("5")
obj.total_blocks("10")
