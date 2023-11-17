import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Vishnu", {})
        self.test_student = Student('Ibrahim', {'JS': ['3 times a week',]})
        self.test_notes = ['junior developer',]
        self.update_notes = ["2 years", 'every day attendance']
        self.test_add_notes = 'Y'

    def test_proper_init_empty_or_None_courses(self):
        self.assertEqual(self.student.name, 'Vishnu')
        self.assertEqual(self.student.courses, {})
        self.student = Student("Vishnu", None)
        self.assertEqual(self.student.courses, {})

    def test_proper_init_with_a_course(self):
        self.assertEqual(self.test_student.name, 'Ibrahim')
        self.assertEqual(self.test_student.courses, {'JS': ['3 times a week',]})

    def test_enroll__if_existing_course_update_notes(self):
        self.student.courses['Python'] = self.test_notes
        self.result = self.student.enroll('Python', self.update_notes, self.test_add_notes)
        self.assertEqual(self.result, "Course already added. Notes have been updated.")
        self.assertEqual(self.student.courses['Python'], ['junior developer',"2 years", 'every day attendance'])

    def test_enroll__if_new_course_with_notes_Y(self):
        self.result = self.student.enroll('Python', self.update_notes, self.test_add_notes)
        self.assertEqual(self.result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses['Python'], self.update_notes)

    def test_enroll__if_new_course_with_notes_empty_string(self):
        self.result = self.student.enroll('Python', self.update_notes, )
        self.assertEqual(self.result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses['Python'], self.update_notes)

    def test_enroll__if_new_course_NO_notes_(self):
        self.result = self.student.enroll('Python', [], 'Later')
        self.assertEqual(self.result, "Course has been added.")
        self.assertEqual(self.student.courses['Python'], [])

    def test_enroll__if_new_course_with_notes_(self):
        self.result = self.student.enroll('Python', self.test_notes, 'No')
        self.assertEqual(self.result, "Course has been added.")
        self.assertEqual(self.student.courses['Python'], [])

    def test_add_notes__existing_course(self):
        self.student.courses['Python'] = self.test_notes
        self.result = self.student.add_notes('Python', self.update_notes)
        self.assertEqual(self.result, "Notes have been updated")

    def test_add_notes__NO_course(self):
        with self.assertRaises(Exception) as ex:
            self.result = self.student.add_notes('Python', self.update_notes)
        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

    def test_leave_course__existing_course(self):
        self.student.courses['Python'] = self.test_notes
        self.result = self.student.leave_course('Python')
        self.assertEqual(self.result, "Course has been removed")

    def test_leave_course__NO_course(self):
        with self.assertRaises(Exception) as ex:
            self.result = self.student.leave_course('Python')
        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")


if __name__ == '__main__':
    unittest.main()
