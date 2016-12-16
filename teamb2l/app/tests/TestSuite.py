import unittest

from ..classes.StudentAcct import StudentAcct
from ..classes.TeacherAcct import TeacherAcct
from ..classes.Course import Course
from ..classes.User import User
from ..classes.StudentCourse import StudentCourse

from Test_Course import Test_Course
from Test_Student_Course import Test_Student_Course
from Test_User import Test_User
from Test_FAQ import Test_FAQ

courseSuite = unittest.TestLoader().loadTestsFromTestCase(Test_Course)
studentCourseSuite = unittest.TestLoader().loadTestsFromTestCase(Test_Student_Course)
userSuite = unittest.TestLoader().loadTestsFromTestCase(Test_User)
faqSuite = unittest.TestLoader().loadTestsFromTestCase(Test_FAQ)
alltests = unittest.TestSuite([
    courseSuite,
    studentCourseSuite,
    userSuite,
    faqSuite
])
unittest.TextTestRunner(verbosity=2).run(alltests)
