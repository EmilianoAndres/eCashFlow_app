from onboarding.presentation.api.serializers import OrderSerializer
from onboarding.usecases.get_customer import GetCustomerUseCase
from onboarding.usecases.create_order import CreateOrderUseCase
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render
from ...handlers import *
from rest_framework.exceptions import APIException

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


class CreateOrderView(APIView):
    # this makes the response be able to render templates. Otherwise it displays messages in a swagger like ui.
    renderer_classes = [TemplateHTMLRenderer]

    def post(self, request):
        data = request.data
        use_case = CreateOrderUseCase()
        result = use_case.execute(data['customer_id'], data['total_amount'])

        if type(result) == APIException:
            return Response(status=result.status_code, template_name='errorpage.html')

        return Response(status=status.HTTP_201_CREATED, template_name='secondpage.html')


class GetCustomerView(APIView):
    def get(self, request, customer_id):
        use_case = GetCustomerUseCase()
        customer = use_case.execute(customer_id)
        serializer = OrderSerializer(customer)
        return Response(serializer.data)
