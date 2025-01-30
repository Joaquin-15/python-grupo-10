users = [
    {'id': 1, 'name': 'Douglas', 'email': 'douglas@example.com', 'password': 'prueba123'},
    {'id': 2, 'name': 'Adrian', 'email': 'adrian@example.com', 'password': 'prueba123'},
    {'id': 3, 'name': 'Gilmar', 'email': 'gilmar@example.com', 'password': 'prueba123'},
    {'id': 4, 'name': 'Deiber', 'email': 'deiber@example.com', 'password': 'prueba123'}
]

def get_user(id: int):
    return next((user for user in users if user['id'] == id), None)

def create_user(user: dict) -> None:
    users.append(user)
    
def get_users():
    return users