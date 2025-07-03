class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    ## returns a string representation of the object
    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    def from_sum(self, value1, value2):
        return FixedFloat(value1 + value2)

number = FixedFloat(18.5746)
new_number = number.from_sum(19.575, 0.789)
print(new_number)