class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    ## returns a string representation of the object
    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    @staticmethod
    def from_sum(value1, value2):
        return FixedFloat(value1 + value2)

new_number = FixedFloat.from_sum(19.575, 0.789)
print(new_number)