class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    ## returns a string representation of the object
    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)

new_number = FixedFloat.from_sum(19.575, 0.789)
print(new_number)

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'


money = Euro(18.786)
print(money)

## This will use the from_sum method from the parent FixedFloat class inherited from the Euro class.
## But we don't want this.  We want an object of the type we called it with, which is Euro.
## In order to do that, we need to change the FixedFloat from_sum method to use a classmethod decorator
## instead of a staticmethod decorator.
money = Euro.from_sum(19.575, 0.789)
print(money)