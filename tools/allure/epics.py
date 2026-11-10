from enum import Enum


class AllureEpic(str, Enum):
    LMS = 'LMS service'
    STUDENT = 'Student service'
    ADMINISTRATOR = 'Administrator service'