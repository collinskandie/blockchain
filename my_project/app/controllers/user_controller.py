from app.models.user import User

class UserController:
    def create_user(self, user_id, username, email, role):
        # Create and return a new User object
        return User(user_id, username, email, role)

    def get_user_info(self, user):
        # Return user information as a string
        return str(user)
