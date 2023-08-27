from abc import ABC, abstractmethod
from onboarding import models


class OrderService(ABC):
    @abstractmethod
    def create_order(self, customer, order_data):
        pass


class DefaultOrderService(OrderService):
    def create_order(self, customer, order_data):
        order = models.Order(customer=customer,
                             total_amount=order_data['total_amount'])
        # Perform additional business logic and validations
        order.save()
        return order


class LoginService(ABC):
    @abstractmethod
    def Login(self):
        pass


class DefaultLoginService(LoginService):
    def Login(self):
        print("you have logged in!")
