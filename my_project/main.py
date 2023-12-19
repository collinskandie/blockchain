from app.controllers.user_controller import UserController
from app.views.user_view import UserView
from app.models.user import Role

def main():
    # Create a UserController instance
    user_controller = UserController()

    # Create a Role with permissions
    admin_role = Role(role_id=1, name="Administrator", permissions=["Read", "Write", "Execute"])
    
    # Get user input
    username = UserView().input_username()
    email = UserView().input_email()
    
    # Create a new user
    new_user = user_controller.create_user(user_id=1, username=username, email=email, role=admin_role)

    # Display user information
    user_info = user_controller.get_user_info(new_user)
    UserView().display_user_info(user_info)

if __name__ == "__main__":
    main()
