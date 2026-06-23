from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercise_client, CreateExercisesRequestDict, QueryExercisesDict, \
    UpdateExercisesRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import generate_fake_email

publish_user_create = get_public_users_client()


create_user_request = CreateUserRequestDict(
    email=generate_fake_email(),
    password='test1',
    lastName='Marin',
    firstName='Pedro',
    middleName='Pedrovich'
)

create_user_response = publish_user_create.create_user(create_user_request)

authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

file_client = get_files_client(authentication_user)
course_client = get_courses_client(authentication_user)
exercise_client = get_exercise_client(authentication_user)

create_file_request = CreateFileRequestDict(
    filename='image.jpg',
    directory='courses',
    upload_file='./testdata/files/image.jpg'

)
create_file_response = file_client.create_file(create_file_request)
print('Create File:', create_file_response)


create_course_request = CreateCourseRequestDict(
    title='Python',
    maxScore=100,
    minScore=30,
    description='Homework',
    estimatedTime='2 days',
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = course_client.create_course(create_course_request)
print('Create course:', create_course_response)


create_exercise_request = CreateExercisesRequestDict(
    title='Home work API clients',
    courseId=create_course_response['course']['id'],
    maxScore=100,
    minScore=30,
    orderIndex=1,
    description='Api clients',
    estimatedTime='2 weeks'
)

create_exercise_request_2 = CreateExercisesRequestDict(
    title='Home work API clients №2',
    courseId=create_course_response['course']['id'],
    maxScore=100,
    minScore=30,
    orderIndex=2,
    description='Api clients №2',
    estimatedTime='4 weeks'
)

create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print('Create Exercise', create_exercise_response)

create_exercise_response_2 = exercise_client.create_exercise(create_exercise_request_2)
print('Create Exercise №2', create_exercise_response)


get_exercise_response =  exercise_client.get_exercise(exercise_id=create_exercise_response['exercise']['id'])
print('Exercise:', get_exercise_response)

get_all_exercises_request = QueryExercisesDict(
    courseId=create_course_response['course']['id']
)

get_all_exercises_response = exercise_client.get_exercises(query=get_all_exercises_request)
print('Exercises:', get_all_exercises_response)

update_exercise_request = UpdateExercisesRequestDict(
    title='New title NOT HOMEWORK GO TO CHILLL',
    maxScore=0,
    minScore=0,
    description='CHIIIIL'
)

update_exercise_response = exercise_client.update_exercise(
    exercise_id=create_exercise_response_2['exercise']['id'],
    request=update_exercise_request
)

get_update_exercise_response = exercise_client.get_exercise(exercise_id=update_exercise_response['exercise']['id'])
print('Exercise update:', get_update_exercise_response)
