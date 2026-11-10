from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from pydantic_create_user import CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password='test1',
    last_name='ushakov',
    first_name='vova',
    middleName='ivanovich'
)

create_user_response = public_users_client.create_user_api(create_user_request)

create_user_response_json_schema = CreateUserResponseSchema.model_json_schema()

validate_json_schema(instance=create_user_response.json(), schema=create_user_response_json_schema)
print(create_user_response_json_schema)

