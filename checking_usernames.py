current_users= ['Yemi','john','wale','george','light','nifemi']
new_users=['yemi','niFemi','daniella','olamide','kindness','foluke']
current_users_lower=[user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('Username already in use, Please select a different username\n')
    else:
        print('Username is available\n')