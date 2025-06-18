import unittest

from project.student import Student


class TestsForStudent(unittest.TestCase):

    def setUp(self):
        pass



    def test_init_without_courses(self):
        s = Student("Ivan")

        expected_courses = {}
        result_courses =s.courses

        expected_name = "Ivan"
        result_name = s.name

        self.assertEqual(result_name, expected_name)

        self.assertEqual(result_courses, expected_courses)

    def test_init_with_courses(self):
        s = Student("Ivan",{"Java":["note", "note2"], "Python":["note3", "note4"]})

        expected_courses = {"Java":["note", "note2"], "Python":["note3", "note4"]}
        result_courses = s.courses

        expected_name = "Ivan"
        result_name = s.name

        self.assertEqual(result_name, expected_name)

        self.assertEqual(result_courses, expected_courses)

    def test_enroll_course_name_in_courses(self):
        s = Student("Ivan", {"Java": ["note", "note2"], "Python": ["note3", "note4"]})

        result= s.enroll("Java",["note5", "note6"],"Y")
        expected="Course already added. Notes have been updated."

        self.assertEqual(result, expected)
        self.assertEqual(s.courses,{"Java": ["note", "note2","note5", "note6"], "Python": ["note3", "note4"]})

        s = Student("Ivan", {"Java": ["note", "note2"], "Python": ["note3", "note4"]})

        result = s.enroll("Java", ["note5", "note6"], "n")
        expected = "Course already added. Notes have been updated."

        self.assertEqual(result, expected)
        self.assertEqual(s.courses, {"Java": ["note", "note2", "note5", "note6"], "Python": ["note3", "note4"]})


    def test_enroll_y(self):
        s = Student("Ivan", {"Java": ["note", "note2"], "Python": ["note3", "note4"]})

        result = s.enroll("C#", ["note7", "note8"], "Y")
        expected = "Course and course notes have been added."

        self.assertEqual(result, expected)
        self.assertEqual(s.courses, {"Java": ["note", "note2"], "Python": ["note3", "note4"], "C#":["note7", "note8"]})


    def test_enroll_nothing(self):
        s = Student("Ivan", {"Java": ["note", "note2"], "Python": ["note3", "note4"]})

        result = s.enroll("C#", ["note7", "note8"], "")
        expected = "Course and course notes have been added."

        self.assertEqual(result, expected)
        self.assertEqual(s.courses, {"Java": ["note", "note2"], "Python": ["note3", "note4"], "C#": ["note7", "note8"]})

    def test_enroll_course_name_in_courses_without_notes(self):
        s = Student("Ivan", {"Java": ["note", "note2"], "Python": ["note3", "note4"]})

        result = s.enroll("C#", ["note22", "note21"], "N")
        expected = "Course has been added."

        self.assertEqual(result, expected)

        self.assertEqual(s.courses,{"Java": ["note", "note2"], "Python": ["note3", "note4"], "C#":[]})



    def test_add_notes_course_in_courses(self):
        s = Student("Ivan", {"Java": ["note", "note2"], "Python": ["note3", "note4"]})

        result = s.add_notes("Java", "note9")
        expected = "Notes have been updated"

        self.assertEqual(result, expected)
        self.assertEqual(s.courses, {"Java": ["note", "note2", "note9"], "Python": ["note3", "note4"]})



    def test_add_notes_course_not_in_courses(self):
        s = Student("Ivan", {"Java": ["note", "note2"], "Python": ["note3", "note4"]})

        with self.assertRaises(Exception) as result:
            s.add_notes("C++", "note10")

        self.assertEqual(str(result.exception), "Cannot add notes. Course not found.")

    def test_leave_course_course_in_courses(self):
        s = Student("Ivan", {"Java": ["note", "note2"], "Python": ["note3", "note4"]})

        result = s.leave_course("Java")
        expected = "Course has been removed"

        self.assertEqual(result, expected)
        self.assertEqual(s.courses, {"Python": ["note3", "note4"]})

    def test_leave_course_course_not_in_courses(self):
        s = Student("Ivan", {"Java": ["note", "note2"], "Python": ["note3", "note4"]})

        with self.assertRaises(Exception) as result:
            s.leave_course("C++")

        self.assertEqual(str(result.exception), "Cannot remove course. Course not found.")


if __name__=="__main__":
    unittest.main()










