class Role:
    def __init__(self, name, permissions=None, inherited_roles=None):
        self.name = name
        self.permissions = permissions or []
        self.inherited_roles = inherited_roles or []

    def add_permission(self, permission):
        self.permissions.append(permission)

    def add_inherited_role(self, role):
        self.inherited_roles.append(role)

    def get_all_permissions(self):
        all_permissions = set(self.permissions)
        for role in self.inherited_roles:
            all_permissions.update(role.get_all_permissions())
        return all_permissions
