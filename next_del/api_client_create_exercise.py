from clients.courses.course_schema import CreateCourseRequestSchema
from clients.courses.courses_client import get_courses_client
from clients.exercises.exercises_client import get_exercise_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client, CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema

publish_user_create = get_public_users_client()

create_user_request = CreateUserRequestSchema()

create_user_response = publish_user_create.create_user(create_user_request)
print('Create user resp:', create_user_response)
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

file_client = get_files_client(authentication_user)
course_client = get_courses_client(authentication_user)
exercise_client = get_exercise_client(authentication_user)

create_file_request = CreateFileRequestSchema(upload_file='./testdata/files/image.jpg')
create_file_response = file_client.create_file(create_file_request)
print('Create File:', create_file_response)

create_course_request = CreateCourseRequestSchema(
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)

create_course_response = course_client.create_course(create_course_request)
print('Create course:', create_course_response)

create_exercise_request = CreateExerciseRequestSchema(
    title='Home work api Python',
    course_id=create_course_response.course.id
)

create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print('Create Exercise', create_exercise_response)

