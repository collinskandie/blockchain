class AdminView:
    def display_admin_menu(self):
        # Display the admin menu options
        print("Admin Menu:")
        print("1. Create User")
        print("2. Assign Role to User")
        print("3. View User Information")
        print("4. Exit")

    def input_user_id(self):
        # Prompt the admin for input (e.g., user ID)
        return input("Enter User ID: ")

    def input_role_name(self):
        # Prompt the admin for input (e.g., role name)
        return input("Enter Role Name: ")

    def display_user_info(self, user_info):
        # Display user information on the admin interface
        print(user_info)
