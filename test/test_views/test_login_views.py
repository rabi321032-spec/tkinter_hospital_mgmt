from app.model.login_model import LoginModel
from app.services.login_services import LoginService

def test_login_flow_correct():
    model = LoginModel("admin", "123")
    service = LoginService()
    assert service.authenticate(model) == True

def test_login_flow_wrong():
    model = LoginModel("x", "y")
    service = LoginService()
    assert service.authenticate(model) == False
