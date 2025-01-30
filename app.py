from modules.auth_functions import login
from modules.email_functions import send_email
from modules.user_functions import get_user


user = get_user(4)

if user:
    print(f"User found: {user['name']}")
else:
    print("User not found")
    
if(login(user.get('email'), user.get('password'))):
    send_email(user.get('email'), 'Welcome', 'Hello, welcome to our app')
