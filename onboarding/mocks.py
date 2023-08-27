from onboarding import services

# Create your tests here.


class MockLoginService(services.LoginService):
    def Login(self):
        print("This is mock login!")
