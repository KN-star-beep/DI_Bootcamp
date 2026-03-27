class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        # Returns a readable string for print()
        # Adding an 's' for pluralization if you want it to look like '5 dollars'
        suffix = 's' if self.amount != 1 else ''
        return f"{self.amount} {self.currency}{suffix}"

    def __repr__(self):
        # For this exercise, repr is expected to match the str output
        suffix = 's' if self.amount != 1 else ''
        return f"{self.amount} {self.currency}{suffix}"

    def __int__(self):
        # Casts the amount to an integer
        return int(self.amount)

    def __add__(self, other):
        # Check if we are adding another Currency object
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        # Handle adding a simple number (int/float)
        return self.amount + other

    def __iadd__(self, other):
        # Handles the += operator
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        else:
            self.amount += other
        return self # Must return self for in-place operators