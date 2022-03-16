class AuthController:
    def __init__(self) -> None:
        pass

    def signup(self):
        return {"signup": "signup"}

    def signin(self):
        return {"signin": "signin"}


auth_controller = AuthController()
