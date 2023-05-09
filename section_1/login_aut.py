import hashlib


def generate_token(username, password):
    
    token = hashlib.sha256((username + password).encode('utf-8')).hexdigest()
    return token


def login(username, password, token):
    
    if token == generate_token(username, password):
        return True
    else:
        return False
