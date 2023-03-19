"""CSC110 Fall 2021 Assignment 2, Part 3: Programming Tests

Instructions (READ THIS FIRST!)
===============================
This Python module contains example tests you can run for Part 3 of this assignment. Please note
that passing all these tests does NOT mean you have a 100% correct solution.

Some of the tests are empty, consider completing them. Also consider adding more of your own tests.
"""
import pytest
import datetime

import a2_part3 as a
import a2_part4

###################################################################################################
# Sample Meeting Times
###################################################################################################
MON_9_TO_11 = ('Monday', datetime.time(9), datetime.time(11))
MON_12_TO_1 = ('Monday', datetime.time(12), datetime.time(13))

TUE_9_TO_11 = ('Tuesday', datetime.time(9), datetime.time(11))
TUE_10_TO_12 = ('Tuesday', datetime.time(10), datetime.time(12))

WED_9_TO_11 = ('Wednesday', datetime.time(9), datetime.time(11))
WED_12_TO_1 = ('Wednesday', datetime.time(12), datetime.time(13))

THU_3_TO_4 = ('Thursday', datetime.time(15), datetime.time(16))
THU_1_TO_2_30 = ('Thursday', datetime.time(13), datetime.time(14, 30))

FRI_9_TO_11 = ('Friday', datetime.time(9), datetime.time(11))
FRI_12_TO_1 = ('Friday', datetime.time(12), datetime.time(13))
FRI_1_TO_2 = ('Friday', datetime.time(13), datetime.time(14))

SAT_1_TO_2 = ('Saturday', datetime.time(13), datetime.time(14))

###################################################################################################
# Sample Sections
###################################################################################################
MAT137_LEC0101 = ('LEC0101', 'Y', (MON_9_TO_11, TUE_9_TO_11, WED_9_TO_11))
MAT137_LEC0201 = ('LEC0201', 'Y', (MON_12_TO_1, WED_12_TO_1, FRI_12_TO_1))

CSC110_LEC0101 = ('LEC0101', 'F', (MON_9_TO_11, TUE_9_TO_11, WED_9_TO_11))
CSC111_LEC0301 = ('LEC0301', 'S', (MON_9_TO_11, TUE_9_TO_11, FRI_1_TO_2))

CON123_LEC0123 = ('LEC0123', 'F', (FRI_1_TO_2,))
CON123_LEC0321 = ('LEC0321', 'S', (TUE_10_TO_12, FRI_1_TO_2))

CON333_LEC1337 = ('LEC1337', 'F', (WED_9_TO_11,))
CON333_LEC2001 = ('LEC2001', 'F', (MON_9_TO_11,))

STA130_LEC0101 = ('LEC0101', 'F', (THU_3_TO_4,))
STA130_LEC0201 = ('LEC0201', 'F', (THU_1_TO_2_30,))

LOL100_LEC0101 = ('LEC0101', 'F', (SAT_1_TO_2,))
AAA100_LEC0101 = ('a', 'S', (FRI_1_TO_2,))

###################################################################################################
# Sample Courses
###################################################################################################
CSC110 = ('CSC110', 'Foundations of Computer Science I', {CSC110_LEC0101})
CSC111 = ('CSC111', 'Foundations of Computer Science II', {CSC111_LEC0301})

CON123 = ('CON123', 'Foundation Construction', {CON123_LEC0123, CON123_LEC0321})
CON333 = ('CON333', 'Advanced Brick Laying', {CON333_LEC1337, CON333_LEC2001})

MAT137 = ('MAT137', 'Calculus!', {MAT137_LEC0101, MAT137_LEC0201})

STA130 = ('STA130', 'Introduction to Statistical Reasoning',
          {STA130_LEC0101, STA130_LEC0201})

LOL100 = ('LOL100', 'test', {LOL100_LEC0101})
AAA100 = ('a', 'a', {AAA100_LEC0101})

###################################################################################################
# Sample Schedule
###################################################################################################
SCHEDULE_1 = {
    'CSC110': CSC110_LEC0101,
    'CSC111': CSC111_LEC0301
}

SCHEDULE_2 = {
    'CON123': CON123_LEC0123,
    'CSC111': CSC111_LEC0301,
    'CON333': CON333_LEC1337
}

SCHEDULE_3 = {
    'CSC110': CSC110_LEC0101,
    'CSC111': CSC111_LEC0301,
    'MAT137': MAT137_LEC0201,
    'CON123': CON123_LEC0321
}

# Note that this is SCHEDULE_1 but with CON123 added
SCHEDULE_4 = {
    'CSC110': CSC110_LEC0101,
    'CSC111': CSC111_LEC0301,
    'CON123': CON123_LEC0123
}

###################################################################################################
# Sample Raw Data
###################################################################################################
WED_9_TO_11_RAW = {'day': 'Wednesday', 'startTime': '09:00', 'endTime': '11:00'}
MON_9_TO_11_RAW = {'day': 'Monday', 'startTime': '09:00', 'endTime': '11:00'}
CON333_LEC1337_RAW = {'sectionCode': 'LEC1337', 'term': 'F', 'meetingTimes': [WED_9_TO_11_RAW]}
CON333_LEC2001_RAW = {'sectionCode': 'LEC2001', 'term': 'F', 'meetingTimes': [MON_9_TO_11_RAW]}
CON333_RAW = {'courseCode': 'CON333', 'courseTitle': 'Advanced Brick Laying',
              'sections': [CON333_LEC1337_RAW, CON333_LEC2001_RAW]}


###################################################################################################
# Part 3 Question 1
###################################################################################################
def test_num_sections() -> None:
    """
    Test num_sections with 1 section from CSC110
    """
    assert a.num_sections(CSC110) == 1


def test_num_lecture_hours() -> None:
    """
    Test num_lecture_hours with MAT137
    """
    assert a.num_lecture_hours(MAT137_LEC0101) == 6


###################################################################################################
# Part 3 Question 2
###################################################################################################
def test_times_conflict() -> None:
    """
        Test times_conflict with conflicting meetings times that overlap
    """
    m1 = TUE_9_TO_11
    m2 = TUE_10_TO_12
    expected = True
    actual = a.times_conflict(m1, m2)
    assert actual == expected


def test_times_no_conflict() -> None:
    """
    Test times_conflict with non-conflicting meetings times
    """
    # TODO: Create a test


def test_sections_conflict() -> None:
    """
    Test sections_conflict with conflicting sections
    """
    s1 = CSC110_LEC0101
    s2 = MAT137_LEC0101
    expected = True
    actual = a.sections_conflict(s1, s2)
    assert actual == expected


def test_sections_conflict2() -> None:
    """
    Test sections_conflict with conflicting sections
    """
    s1 = CSC110_LEC0101
    s2 = MAT137_LEC0201
    expected = False
    actual = a.sections_conflict(s1, s2)
    assert actual == expected


def test_sections_no_conflict() -> None:
    """
    Test sections_conflict with non-conflicting sections
    """
    s1 = CON123_LEC0123
    s2 = CON123_LEC0321
    expected = False
    actual = a.sections_conflict(s1, s2)
    assert actual == expected


def test_is_valid() -> None:
    """
    Test is_valid with valid schedule
    """
    expected = True
    actual = a.is_valid(SCHEDULE_1)
    assert actual == expected


def test_is_valid2() -> None:
    """
    Test is_valid with valid schedule
    """
    expected = True
    actual = a.is_valid(SCHEDULE_2)
    assert actual == expected


def test_is_valid3() -> None:
    """
    Test is_valid with valid schedule
    """
    expected = True
    actual = a.is_valid(SCHEDULE_4)
    assert actual == expected


def test_not_valid() -> None:
    """
    Test is_valid with invalid schedule
    """
    expected = False
    actual = a.is_valid(SCHEDULE_3)
    assert actual == expected


def test_2_possible_schedule_combinations() -> None:
    """
    Test possible_schedule_combinations with 2 possible combinations
    """
    c1 = MAT137
    c2 = CSC111
    expected = 2
    actual = a.possible_schedules(c1, c2)
    assert len(actual) == expected


def test_4_possible_schedule_combinations() -> None:
    """
    Test possible_schedule_combinations with 4 possible combinations
    """
    c1 = MAT137
    c2 = STA130
    expected = 4
    actual = a.possible_schedules(c1, c2)
    assert len(actual) == expected


def test_1_valid_schedule_combinations() -> None:
    """
    Test valid_schedule_combinations with valid schedule combination, bounds of 1
    """
    c1 = MAT137
    c2 = CSC111
    expected = 1
    actual = a.valid_schedules(c1, c2)
    assert len(actual) == expected


def test_4_valid_schedule_combinations() -> None:
    """
    Test valid_schedule_combinations with 4 valid schedule combinations
    """
    # TODO: Create a test


def test_possible_five_course_schedules() -> None:
    """
    Test possible_five_course_schedules with five possible course schedules
    """
    c1 = CSC110
    c2 = CSC111
    c3 = CON123
    c4 = CON333
    c5 = MAT137
    expected = 8
    actual = a.possible_five_course_schedules(c1, c2, c3, c4, c5)
    assert len(actual) == expected


def test_invalid_five_course_schedules() -> None:
    """
    Test valid_five_course_schedules with invalid five course schedule
    """
    c1 = CSC110
    c2 = CSC111
    c3 = CON123
    c4 = MAT137
    c5 = AAA100
    expected = 0
    actual = a.valid_five_course_schedules(c1, c2, c3, c4, c5)
    assert len(actual) == expected


###################################################################################################
# Part 3 Question 3
###################################################################################################
def test_section_compatible() -> None:
    """
    Test is_section_compatible with compatible sections
    """
    expected = True
    actual = a.is_section_compatible(SCHEDULE_1, LOL100_LEC0101)
    assert actual == expected


def test_section_not_compatible() -> None:
    """
    Test is_section_compatible with incompatible sections
    """
    expected = False
    actual = a.is_section_compatible(SCHEDULE_1, AAA100_LEC0101)
    assert actual == expected


def test_course_compatible() -> None:
    """
    Test is_course_compatible with compatible course
    """
    expected = True
    actual = a.is_course_compatible(SCHEDULE_1, LOL100)
    assert actual == expected


def test_course_not_compatible() -> None:
    """
    Test is_course_compatible with incompatible course
    """
    expected = False
    actual = a.is_course_compatible(SCHEDULE_1, AAA100)
    assert actual == expected


def test_compatible_sections() -> None:
    """
    Test compatible_sections with compatible sections
    """
    actual = a.compatible_sections(SCHEDULE_1, CON123) == {CON123_LEC0123}
    expected = True
    assert actual == expected


###################################################################################################
# Part 4
###################################################################################################
def test_transform_course_data() -> None:
    """
    Test transform_course_data
    """
    expected = CON333
    actual = a2_part4.transform_course_data(CON333_RAW)
    assert actual == expected


def test_transform_section_data() -> None:
    """
    Test transform_section_data
    """
    expected = CON333_LEC2001
    actual = a2_part4.transform_section_data(CON333_LEC2001_RAW)
    assert actual == expected


def test_transform_meeting_time_data() -> None:
    """
    Test transform_meeting_time_data
    """
    expected = MON_9_TO_11
    actual = a2_part4.transform_meeting_time_data(MON_9_TO_11_RAW)
    assert actual == expected


if __name__ == "__main__":
    pytest.main(['a2_example_tests.py'])
