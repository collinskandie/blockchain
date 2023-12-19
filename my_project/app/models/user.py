class User:
    def __init__(self, user_id, username, email, role):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.role = role  # Reference to the user's role object

    def __str__(self):
        return f"User ID: {self.user_id}, Username: {self.username}, Email: {self.email}, Role: {self.role}"

class Role:
    def __init__(self, role_id, name, permissions):
        self.role_id = role_id
        self.name = name
        self.permissions = permissions

    def __str__(self):
        return f"Role ID: {self.role_id}, Name: {self.name}, Permissions: {self.permissions}"
