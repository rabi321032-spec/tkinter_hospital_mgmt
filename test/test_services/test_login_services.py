from app.model.login_model import LoginModel
from app.services.login_services import LoginService

def test_correct_login():
    model = LoginModel("admin", "123")
    service = LoginService()
    assert service.authenticate(model) == True

def test_wrong_login():
    model = LoginModel("aaa", "bbb")
    service = LoginService()
    assert service.authenticate(model) == False
