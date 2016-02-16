class Money:

    def __init__(self, amount, denomination):
        self.amount = amount
        self.denomination = denomination

    def __add__(self, other):
        if self.denomination == other.denomination:
            return self.amount + other.amount
        return self.amount + other.convert_currency()

    def __sub__(self, other):
        if self.denomination == other.denomination:
            return self.amount - other.amount
        return self.amount - other.convert_currency()

    def __gt__(self, other):
        if self.denomination == other.denomination:
            return self.amount > other.amount
        return self.amount > other.convert_currency()

    def __lt__(self, other):
        if self.denomination == other.denomination:
            return self.amount < other.amount
        return self.amount < other.convert_currency()

    def convert_currency(self):
        if type(self.amount) == type([]) and self.denomination == "USD":
            return self.usd_to_euro_list(self.amount)
        elif type(self.amount) == type([]) and self.denomination == "EUR":
            return self.euro_to_usd_list(self.amount)
        elif self.denomination == "USD":
            return self.usd_to_euro(self.amount)
        elif self.denomination == "EUR":
            return self.euro_to_usd(self.amount)

    def usd_to_euro(self, amount):
        return round((amount * .9), 2)

    def usd_to_euro_list(self, usd_list):
        return [self.usd_to_euro(usd_amount) for usd_amount in usd_list]

    def euro_to_usd(self, amount):
        return round((amount * 1.11), 2)

    def euro_to_usd_list(self, euro_list):
        return [self.euro_to_usd(euro_amount) for euro_amount in euro_list]
