class User:
    def __init__(self, username, email, is_active=True):
        self.username = username
        self.email = email
        self.is_active = is_active

    def activate(self):
        if self.is_active:
            print("Already active")
            return

        self.is_active = True

    def deactivate(self):
        if not self.is_active:
            print("Already deactive")
            return

        self.is_active = False


user = User("User", "example@test.py")

print(f"""
||| USERNAME: {user.username}
||| EMAIL: {user.email}
||| ACTIVE STATUS: {user.is_active}
""")

# homemade pytest xd
print("[Expected: True] ---", user.is_active)

print("[Expected: Already active] --- ", end="")
user.activate()

user.deactivate()
print("[Expected: False] ---", user.is_active)

print("[Expected: Already deactive] --- ", end="")
user.deactivate()
