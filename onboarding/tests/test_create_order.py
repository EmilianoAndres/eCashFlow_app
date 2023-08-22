import pytest
from onboarding.infrastructure.models import OrderPersistence
from onboarding.infrastructure.models import CustomerPersistence
from onboarding.infrastructure.repositories import OrderRepository
from onboarding.infrastructure.repositories import CustomerRepository
from onboarding.usecases.create_order import CreateOrderUseCase
from unittest.mock import MagicMock


@pytest.mark.django_db
def test_create_order_success():

    # Dummy data
    customer = CustomerPersistence(id=1, name="juan")
    order = OrderPersistence(
        id=10, customer=customer, total_amount=5.23)

    # dependencies
    orderRepo = OrderRepository()
    customerRepo = CustomerRepository()

    # manipulate methods with magic mock implementation
    orderRepo.save = MagicMock(return_value=order)
    customerRepo.get_customer_by_id = MagicMock(return_value=customer)

    # instantiate class to test
    usecase = CreateOrderUseCase(
        orderRepo, customerRepo)

    # test the method
    result = usecase.execute(customer.id, order.total_amount)

    # assert results
    assert result.total_amount == order.total_amount
    assert result.customer.id == customer.id


@pytest.mark.django_db
def test_create_order_no_customer():

    # Dummy data
    customer = CustomerPersistence(id=1, name="juan")
    order = OrderPersistence(
        id=10, customer=customer, total_amount=5.23)

    # dependencies
    orderRepo = OrderRepository()
    # manipulate methods with magic mock implementation
    orderRepo.save = MagicMock(return_value=order)
    customerRepo = CustomerRepository()
    customerRepo.get_customer_by_id = MagicMock(return_value=None)

    orderRepoInstance = OrderRepository()
    customerRepoInstance = CustomerRepository()

    usecase = CreateOrderUseCase(
        orderRepo, customerRepo)

    result = usecase.execute(customer.id, order.total_amount)

    assert result.detail == 'user not found'
