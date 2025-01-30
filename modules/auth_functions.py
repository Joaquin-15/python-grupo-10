from modules.user_functions import users


def login(email: str, password: str) -> bool:
    user = next((user for user in users if user['email'] == email), None)
    if user:
        return user['password'] == password
    else:
        return False
    

    
