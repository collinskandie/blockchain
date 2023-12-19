class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def change_role(self, new_role):
        self.role = new_role
