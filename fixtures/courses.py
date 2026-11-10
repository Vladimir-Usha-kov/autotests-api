import pytest
from pydantic import BaseModel

from clients.courses.course_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from clients.courses.courses_client import get_courses_client, CoursesClient
from fixtures.files import FileFixture
from fixtures.user import UserFixture


class CoursesFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

    @property
    def course_id(self) -> str:
        return self.response.course.id

@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user)

@pytest.fixture
def function_course(
        courses_client: CoursesClient,
        function_files: FileFixture,
        function_user: UserFixture
) -> CoursesFixture:

    request = CreateCourseRequestSchema(
        preview_file_id=function_files.file_id,
        created_by_user_id=function_user.user_id
    )

    response = courses_client.create_course(request)
    return CoursesFixture(request=request, response=response)