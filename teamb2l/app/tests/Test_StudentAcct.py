'''
Created on Nov 8, 2016

@author: Eric
'''
import unittest

from ..classes.User import User

class StudentTest(unittest.TestCase):
    def setUp(self):
        self.StudentAcct = User()

    def tear(self):
        del self.StudentAcct
        
    def test_initial(self):
        self.assertEqual(self.User.firstName, "")
        self.assertEqual(self.User.lastName, "")       
        self.assertEqual(self.User.email, "")  
        self.assertTrue(len(self.User.courses) == 0)
        
    def test_makeStudent(self):
        self.setUp()
        self.User.makeStudent("John", "Smith", "jsmith@uwm.edu", "12345")
        for i in User.query().fetch():
            if i.email == "jsmith@uwm.edu":
                tmp = i
        self.assertEqual(tmp.name, "Smith, John")
        self.assertEqual(tmp.email, "jsmith@uwm.edu")
        """self.assertEqual(tmp.courses[0], "12345")"""
        self.tear()
              
suite = unittest.TestLoader().loadTestsFromTestCase(StudentTest)
unittest.TextTestRunner(verbosity=2).run(suite)

