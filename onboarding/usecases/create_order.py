from onboarding.domain.entities import Customer
from onboarding.domain.entities import Order
from onboarding.infrastructure.repositories import OrderRepository
from onboarding.infrastructure.repositories import CustomerRepository
from rest_framework.exceptions import APIException
import uuid


class CreateOrderUseCase:
    def __init__(self, orderRepository: OrderRepository, customerRepository: CustomerRepository):
        self.OrderRepository = orderRepository
        self.CustomerRepository = customerRepository

    def execute(self, customer_id, total_amount):
        # Fetch the customer using an external service or repository
        customer = self.CustomerRepository.get_customer_by_id(customer_id)
        if customer == None:
            return APIException(detail="user not found", code=404)

        # Create the order
        ref = "OR-" + str(uuid.uuid4())
        order = Order(order_id=None, customer=customer,
                      total_amount=total_amount, reference=ref)

        # Save the order using the repository
        order = self.OrderRepository.save(order)

        return order
