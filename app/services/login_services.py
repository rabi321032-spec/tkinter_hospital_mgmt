from app.model.login_model import LoginModel

class LoginService:
    def authenticate(self, model):
        # first check if fields are empty
        if model.is_valid() == False:
            return False

        # simple hardcoded login for now
        if model.username == "admin" and model.password == "123":
            return True
        else:
            return False
