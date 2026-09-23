class User:
    def __init__(self, username):
        self.username = username


class Admin(User):
    def __init__(self, username, permissions):
        super().__init__(username)
        self.permissions = permissions

    def has_permission(self, permission):
        return permission in self.permissions


user = Admin("user", ["ban", "mute"])
print(user.has_permission("ban"))
