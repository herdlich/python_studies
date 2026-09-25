class User:
    count_id = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.user_id = User.count_id

        User.count_id += 1

    def __repr__(self):
        return f"{self.username}, {self.email}"


class UserRepository:
    def __init__(self):
        self.users = {}

    def create(self, user):
        self.users[user.user_id] = user

    def delete(self, user):
        self.users.pop(user.user_id)

    def get_by_id(self, user_id):
        return self.users[user_id]

    def get_all(self):
        return self.users


class UserService:
    def __init__(self, repository):
        self.repository = repository

    def create_user(self, user):
        self.repository.create(user)

    def delete_user(self, user):
        self.repository.delete(user)

    def get_user_by_id(self, user_id):
        if not self.repository.get_by_id(user_id):
            raise RuntimeError(f"User id {user_id} does not exist")

        return self.repository.get_by_id(user_id)

    def get_all_users(self):
        return self.repository.get_all()
