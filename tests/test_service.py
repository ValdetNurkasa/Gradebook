import unittest
import os
from gradebook import service


class TestService(unittest.TestCase):

    def setUp(self):
        if os.path.exists("data/gradebook.json"):
            os.remove("data/gradebook.json")

    def test_add_student(self):
        sid = service.add_student("Test")
        self.assertEqual(sid, 1)

    def test_add_grade_invalid(self):
        with self.assertRaises(ValueError):
            service.add_grade(1, "EE414", 200)

    def test_compute_average(self):
        service.add_student("A")
        service.add_course("EE414", "Intro")
        service.enroll(1, "EE414")
        service.add_grade(1, "EE414", 100)

        avg = service.compute_average(1, "EE414")
        self.assertEqual(avg, 100)


if __name__ == "__main__":
    unittest.main()
