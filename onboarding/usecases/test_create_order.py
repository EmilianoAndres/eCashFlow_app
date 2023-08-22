import pytest
from onboarding.infrastructure.models import OrderPersistence
from onboarding.infrastructure.models import CustomerPersistence
from onboarding.usecases.create_order import CreateOrderUseCase


@pytest.mark.django_db
def test_create_order():
    # Dummy data
    customer = CustomerPersistence.objects.create(id=5, name="juan")
    order = OrderPersistence.objects.create(
        id=10, customer=customer, total_amount=5.23)

    usecase = CreateOrderUseCase()

    result = usecase.execute(customer.id, order.total_amount)

    assert result.total_amount == order.total_amount
    assert result.customer.id == customer.id
