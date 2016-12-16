import unittest
from teamb2l.app.handlers import MessagerHandler


class MessagerTest(unittest.TestCase):

    def testMessage(self):
        messages = [["Student", "Test Message"], ["Teacher", "Test Message"]]
        self.assertEquals(MessagerHandler.refresh(messages), """<div class="personalMessage">
                                                                    Test message
                                                                </div>
                                                                <div class="otherMessage">
                                                                    Test message
                                                                </div>")""")
