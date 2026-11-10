# """{
#   "id": "string",
#   "title": "string",
#   "maxScore": 0,
#   "minScore": 0,
#   "description": "string",
#   "previewFile": {
#     "id": "string",
#     "filename": "string",
#     "directory": "string",
#     "http_client": "https://example.com/"
#   },
#   "estimatedTime": "string",
#   "createdByUser": {
#     "id": "string",
#     "email": "user@example.com",
#     "lastName": "string",
#     "firstName": "string",
#     "middleName": "string"
#   }
# }"""
# import uuid
#
# from pydantic import BaseModel, Field, ConfigDict, HttpUrl, EmailStr, ValidationError
# from pydantic.alias_generators import to_camel
# from pydantic.v1 import FilePath
#
# from tools.fakers import fake
#
# class FileSchema(BaseModel):
#     id: str
#     filename: str
#     directory: str
#     http_client: HttpUrl
#
# class UserSchema(BaseModel):
#     id: str
#     email: EmailStr
#     lastName: str
#     firstName: str
#     middleName: str
#
# class CourseSchema(BaseModel):
#     id: str
#     title: str = 'PLaywright'
#     max_score: int = Field(alias='maxScore', default=1000)
#     min_score: int = Field(alias='minScore', default=100)
#     description: str = 'Playwright course'
#     preview_file: FileSchema = Field(alias='previewFile')
#     estimated_time: str = Field(alias='estimatedTime', default='10 days')
#     created_by_user: UserSchema = Field(alias='createdByUser')
#
#
# # Инициализируем модель CourseSchema через передачу аргументов
# course_default_model = CourseSchema(
#     id="course-id",
#     title="Playwright",
#     maxScore=10,
#     minScore=1,
#     previewFile=FileSchema(
#         id='id',
#         filename='/.file',
#         directory='directory',
#         http_client='http://url'
#     ),
#     description="Playwright",
#     estimatedTime="1 week",
#     createdByUser=UserSchema(
#         id='id_user',
#         email='s@mail.ru',
#         lastName='lastName',
#         firstName='firstName',
#         middleName='midle_name'
#     )
# )
#
# print('CourseSchema default model:', course_default_model)
#
# print('====================================================dict====================================================')
# course_dict = {
#   "id": "string",
#   "title": "string",
#   "maxScore": 0,
#   "minScore": 0,
#   "description": "string",
#   "previewFile": {
#     "id": "string",
#     "filename": "string",
#     "directory": "string",
#     "http_client": "https://example.com/"
#   },
#   "estimatedTime": "string",
#   "createdByUser": {
#     "id": "string",
#     "email": "user@example.com",
#     "lastName": "string",
#     "firstName": "string",
#     "middleName": "string"
#   }
# }
#
# course_dict_model = CourseSchema(**course_dict)
# print('CourseSchema dict:', course_dict_model)
# print(course_dict_model.model_dump())
# print(course_dict_model.model_dump(by_alias=True))
# print('====================================================JSON====================================================')
#
# course_json = """{
#   "id": "string",
#   "title": "string",
#   "maxScore": 0,
#   "minScore": 0,
#   "description": "string",
#   "previewFile": {
#     "id": "string",
#     "filename": "string",
#     "directory": "string",
#     "http_client": "https://example.com/"
#   },
#   "estimatedTime": "string",
#   "createdByUser": {
#     "id": "string",
#     "email": "user@example.com",
#     "lastName": "string",
#     "firstName": "string",
#     "middleName": "string"
#   }
# }"""
#
# course_json_model = CourseSchema.model_validate_json(course_json)
# print('CourseSchema JSON:', course_json_model)
# print(course_json_model.model_dump_json())
# print(course_json_model.model_dump_json(by_alias=True))
#
#
# print('='*1000)
# try:
#     file = FileSchema(
#         id='id',
#         http_client='//s',
#         directory='s',
#         filename='s'
#     )
# except ValidationError as e:
#     print(f'Error: {e}')
#     print(e.errors())
#
# print('='*1000)