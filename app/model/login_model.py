

class LoginModel:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # simple check for empty fields
    def is_valid(self):
        if self.username == " " or self.password == "":
            return False
        else:
            return True



