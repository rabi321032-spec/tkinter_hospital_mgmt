from app.model.login_model import LoginModel

def test_valid_data():
    model = LoginModel("abc", "123")
    assert model.is_valid() == True

def test_empty_data():
    model = LoginModel("", "")
    assert model.is_valid() == False
