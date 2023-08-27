from abc import ABC, abstractmethod
from onboarding import models
from onboarding import services


class OrderHandler(ABC):
    @abstractmethod
    def create_order(self, customer_id, order_data):
        pass


class DefaultOrderHandler(OrderHandler):

    def __init__(self, orderService: services.OrderService) -> None:
        self.orderService = orderService

    def create_order(self, customer_id, order_data):
        customer = models.Customer.objects.get(id=customer_id)
        return self.orderservice.create_order(customer, order_data)
