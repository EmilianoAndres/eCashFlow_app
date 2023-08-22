from django.test import TestCase
from abc import ABC, abstractmethod
from onboarding import mocks

# Create your tests here.


class TestLoginService(TestCase):
    def test_login(self):
        mockLoginService = mocks.MockLoginService()
        mockLoginService.Login()
