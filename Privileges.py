from user import Admin


admin = Admin('adeyemi', 'banire', 21, 'male')
admin.describe_user()
admin.privilege.privileges = [
    'can delete posts',
    'can ban user',
    'can add post',
    'can warn user',
    ]
admin.privilege.show_privileges()