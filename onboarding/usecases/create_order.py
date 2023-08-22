from onboarding.domain.entities import Customer
from onboarding.domain.entities import Order
from onboarding.infrastructure.repositories import OrderRepository
from onboarding.infrastructure.repositories import CustomerRepository


class CreateOrderUseCase:
    def __init__(self):
        self.OrderRepository = OrderRepository()
        self.CustomerRepository = CustomerRepository()

    def execute(self, customer_id, total_amount):
        print(customer_id)
        # Fetch the customer using an external service or repository
        customer = self.CustomerRepository.get_customer_by_id(customer_id)

        # Create the order
        order = Order(order_id=None, customer=customer,
                      total_amount=total_amount)

        # Save the order using the repository
        self.OrderRepository.save(order)

        return order
