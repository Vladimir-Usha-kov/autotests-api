from clients.private_http_builder import AuthenticationUserDict
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import generate_fake_email

public_users_client = get_public_users_client()
create_user_request = CreateUserRequestDict(
    email=generate_fake_email(),
    password='test1',
    lastName='string',
    firstName='string',
    middleName='string'
)

create_user_response = public_users_client.create_user(create_user_request)
print('create user:', create_user_response)


authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)


private_users_client = get_private_users_client(authentication_user)

get_users_response = private_users_client.get_user(user_id=create_user_response['user']['id'])
print('info user:', get_users_response)
