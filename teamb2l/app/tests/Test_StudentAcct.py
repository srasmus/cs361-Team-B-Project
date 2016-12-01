'''
Created on Nov 8, 2016

@author: Eric
'''
import unittest

from ..classes.StudentAcct import StudentAcct

class StudentTest(unittest.TestCase):
    def setUp(self):
        self.StudentAcct = StudentAcct()

    def tear(self):
        del self.StudentAcct
        
    def test_initial(self):
        self.assertEqual(self.StudentAcct.firstName, "")
        self.assertEqual(self.StudentAcct.lastName, "")       
        self.assertEqual(self.StudentAcct.email, "")  
        self.assertTrue(len(self.StudentAcct.courses) == 0)
        
    def test_makeStudent(self):
        self.setUp()
        self.StudentAcct.makeStudent("John", "Smith", "jsmith@uwm.edu", "12345")
        self.assertEqual(self.StudentAcct.name, "Smith, John")
        self.assertEqual(self.StudentAcct.email, "jsmith@uwm.edu")
        self.assertEqual(self.StudentAcct.courses[0], "12345")
        self.tear()
              
suite = unittest.TestLoader().loadTestsFromTestCase(StudentTest)
unittest.TextTestRunner(verbosity=2).run(suite)

