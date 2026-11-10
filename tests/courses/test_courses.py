from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.courses.course_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, \
    GetCourseIdResponseSchema, CreateCourseResponseSchema, GetCoursesQuerySchema, GetCoursesResponseSchema, \
    CreateCourseRequestSchema
from clients.courses.courses_client import CoursesClient
from fixtures.courses import CoursesFixture
from fixtures.files import FileFixture
from fixtures.user import UserFixture, function_user
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_get_course_id_response, \
    assert_get_courses_response, assert_create_course_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.suite(AllureFeature.COURSES)
class TestCourses:

    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.title('Create course')
    @allure.severity(Severity.BLOCKER)
    def test_create_course(
            self,
            courses_client: CoursesClient,
            function_files: FileFixture,
            function_user: UserFixture):

        request = CreateCourseRequestSchema(
            previewFileId=function_files.file_id, createdByUserId=function_user.user_id)
        response = courses_client.create_course_api(request)
        response_data = CreateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_course_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    @allure.title('Update course')
    @allure.severity(Severity.CRITICAL)
    def test_update_course(self, courses_client: CoursesClient, function_course: CoursesFixture):
        request = UpdateCourseRequestSchema()
        response = courses_client.update_course_api(course_id=function_course.course_id, request=request)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

        response_get_course_id = courses_client.get_course_api(response_data.course.id)
        response_get_course_id_data = GetCourseIdResponseSchema.model_validate_json(response_get_course_id.text)

        assert_status_code(response_get_course_id.status_code, HTTPStatus.OK)
        assert_get_course_id_response(response_data, response_get_course_id_data)

    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.sub_suite(AllureStory.GET_ENTITIES)
    @allure.title('Get courses')
    @allure.severity(Severity.BLOCKER)
    def test_get_courses(
            self, courses_client: CoursesClient,
            function_course: CoursesFixture,
            function_user: UserFixture
    ):

        query = GetCoursesQuerySchema(userId=function_user.user_id)
        response = courses_client.get_courses_api(query)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)

        assert_get_courses_response(response_data, [function_course.response])
        validate_json_schema(response.json(), response_data.model_json_schema())
