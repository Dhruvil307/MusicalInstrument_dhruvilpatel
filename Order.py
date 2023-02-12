class Order:

    def __init__(self, o_id, customer_name, orders) -> None:
        self.instruments = []
        self.o_id = o_id
        self.customer_name = customer_name
        self.orders = orders

    def add_instrument(self, instrument):
        self.instruments.append(instrument)

    def get_total(self):
        total = 0
        for i in self.instruments:
            total += i.value
        return total
