import unittest

from mycode import *

class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world(), "hello world")  # fonction à tester et résultat attendu

    def testScoreCalculator1(self):
        self.assertEqual(ScoreCalculator("Joseph", 15), "0.66")

    def testScoreCalculator2(self):
        self.assertEqual(ScoreCalculator("Marie", 33), "0.5")

    def testScoreCalculator3(self):
        self.assertEqual(ScoreCalculator("Marc", 60), "0.43")

    def testScoreCalculator4(self):
        self.assertEqual(ScoreCalculator("Ely", 28), "0.75")

    def testScoreCalculator5 (self, dico):
        dico = {('Joseph', 15): 0.66, ('Marie', 33): 33, ('Marc', 60): 0.43, ('Ely', 28): 0.75}
        self.assertEqual(ScoreCalculator1(dico,("Joseph", 15), "0.66"))
# comment pour test



