from clients.courses.course_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from clients.courses.courses_client import get_courses_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

public_api_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password='test123',
    lastName='1',
    middleName='2',
    firstName='3'
)

create_user_response = public_api_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)




course_client = get_courses_client(authentication_user)
create_course_request = CreateCourseRequestSchema(
    title="Python",
    max_score=100,
    min_score=10,
    description="Python API course",
    estimated_time="2 weeks",
    created_by_user_id=create_user_response.user.id
)

create_course_response = course_client.create_course_api(create_course_request)
create_course_response_schema = CreateCourseResponseSchema.model_json_schema()

validate_json_schema(instance=create_course_response.json(), schema=create_course_response_schema)