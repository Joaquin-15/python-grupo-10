from modules.auth_functions import login
from modules.email_functions import send_email
from modules.user_functions import create_user, get_user, get_users


user = get_user(4)

if user:
    print(f"User found: {user['name']}")
else:
    print("User not found")
    
if(login(user.get('email'), user.get('password'))):
    send_email(user.get('email'), 'Welcome', 'Hello, welcome to our app')
    
users = get_users()
print(users)
create_user({'id': 10, 'name': 'Israel', 'email': 'Israel@example.com', 'password': 'Israel1234'})

users = get_users()
print(users)