import jwt
import datetime

# Chave secreta para assinar os tokens
SECRET_KEY = "sua_chave_secreta_super_segura"

# Tempo padrão de validade dos tokens em minutos
TOKEN_EXPIRATION_MINUTES = 30

#Desenvolvimento do Módulo de Geração de Tokens:

def generate_jwt(user_id, secret_key, expiration_minutes):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_minutes)
    payload = {
        'user_id': user_id,
        'exp': expiration_time
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

# Exemplo de uso:
user_id = "colocar nome aqui"
token = generate_jwt(user_id, SECRET_KEY, TOKEN_EXPIRATION_MINUTES)
print(f"Token gerado: {token}")
