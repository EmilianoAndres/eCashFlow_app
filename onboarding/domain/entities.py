from onboarding.domain.aggregate import OrderLine


class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email


class Order:
    def __init__(self, order_id, customer: Customer, total_amount: float, reference: str):
        self.order_id = order_id
        self.customer = customer
        self.total_amount = total_amount
        self.reference = reference
        self._order_lines = []

    def add_order_line(self, product, quantity, unit_price):
        order_line = OrderLine(product, quantity, unit_price)
        self._order_lines.append(order_line)

    def get_order_lines(self):
        return self._order_lines.copy()
