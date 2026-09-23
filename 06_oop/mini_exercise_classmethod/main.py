class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["username"],
            data["email"],
        )


user_dict = {"username": "Test User", "email": "example@test.py"}
user = User.from_dict(user_dict)

print(user.username)  # Test User
print(user.email)     # example@test.py
