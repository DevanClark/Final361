from django.test import TestCase
from Final.models import User
from Final.models import Course
from django.test import Client


class TestCourseInfo(TestCase):
    def test_view_course_info_page_is_accessible(self):
        response = self.client.get('/viewcourseinfo/')
        self.assertEqual(response.status_code, 200)

   def test_view_course_info(self):
