def has_permission(user, permission):
    user_permissions = user.role.get_all_permissions()
    return permission in user_permissions
