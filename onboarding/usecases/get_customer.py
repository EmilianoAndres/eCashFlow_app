# myapp/applications/get_customer.py
from onboarding.domain.entities import Customer
from onboarding.infrastructure.repositories import CustomerRepository


class GetCustomerUseCase:
    def __init__(self):
        self.repository = CustomerRepository()

    def execute(self, customer_id):
        return self.repository.get_customer_by_id(customer_id)
