import unittest

from ..tests.Test_Course import Test_Course
from ..tests.Test_Student_Course import Test_Student_Course
from ..tests.Test_User import Test_User
from ..tests.Test_FAQ import Test_FAQ
from ..tests.Test_Question import Test_Question

courseSuite = unittest.TestLoader().loadTestsFromTestCase(Test_Course)
studentCourseSuite = unittest.TestLoader().loadTestsFromTestCase(Test_Student_Course)
userSuite = unittest.TestLoader().loadTestsFromTestCase(Test_User)
faqSuite = unittest.TestLoader().loadTestsFromTestCase(Test_FAQ)
questionSuite = unittest.TestLoader().loadTestsFromTestCase(Test_Question)
alltests = unittest.TestSuite([
    courseSuite,
    studentCourseSuite,
    userSuite,
    faqSuite,
    questionSuite
])
unittest.TextTestRunner(verbosity=2).run(alltests)
