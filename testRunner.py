import unittest
import  main

class logChunktest(unittest.TestCase):

    def test_main(self):
        temp = main.testFunction()
        self.assertTrue(temp=="wroom")
