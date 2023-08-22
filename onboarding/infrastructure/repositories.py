from .models import CustomerPersistence
from .models import OrderPersistence
from onboarding.domain.entities import Order


class CustomerRepository:
    def get_customer_by_id(self, customer_id):
        # Use Django's ORM to fetch a customer by ID
        try:
            return CustomerPersistence.objects.get(id=customer_id)
        except CustomerPersistence.DoesNotExist:
            return None


class OrderRepository:
    def save(self, order: Order):
        order_data = {
            'customer': order.customer,
            'total_amount': order.total_amount,
            # Add other fields as needed
        }
        new_order = OrderPersistence(**order_data)
        new_order.save()

        return new_order

    def get_by_id(self, order_id):
        try:
            return OrderPersistence.objects.get(order_id=order_id)
        except OrderPersistence.DoesNotExist:
            return None

    def list_all(self):
        return OrderPersistence.objects.all()
