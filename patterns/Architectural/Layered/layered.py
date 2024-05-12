# Data Access Layer
class UserDataAccess:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, user_info):
        self.users[user_id] = user_info

    def get_user(self, user_id):
        return self.users.get(user_id, None)

# Business Logic Layer
class UserManager:
    def __init__(self, data_access):
        self.data_access = data_access

    def create_user(self, user_id, user_info):
        if user_id not in self.data_access.users:
            self.data_access.add_user(user_id, user_info)
            return True
        return False

    def get_user_details(self, user_id):
        return self.data_access.get_user(user_id)

# Presentation Layer
class UserAPI:
    def __init__(self, user_manager):
        self.user_manager = user_manager

    def register_user(self, user_id, user_info):
        success = self.user_manager.create_user(user_id, user_info)
        return "User created" if success else "User already exists"

    def get_user_info(self, user_id):
        user = self.user_manager.get_user_details(user_id)
        return user if user else "User not found"

if __name__ == "__main__":
    data_access = UserDataAccess()
    user_manager = UserManager(data_access)
    user_api = UserAPI(user_manager)

    print(user_api.register_user("001", {"name": "John Doe", "email": "john@example.com"}))
    print(user_api.get_user_info("001"))
    print(user_api.register_user("001", {"name": "John Doe", "email": "john@example.com"}))
    print(user_api.get_user_info("002"))
