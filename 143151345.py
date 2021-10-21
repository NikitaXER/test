class MoneyBox:
    def __init__(self, capacity=10):
        self.count = 0
    
    def can_add (self, v=0):
        if self.v < (self.capacity - self.count):
            return True
        else:
            return False

    def add (self, v):
        self.count += v

x= MoneyBox ()
print (x.count)
x.add(5)
print (x.can_add(5))
print (x.count)
