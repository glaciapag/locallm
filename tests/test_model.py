import unittest
from locallm import AIChatbot
from locallm.config import DefaultConfig

class TestModel(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """This method is run once before any test in the class."""
        cls.chat_bot_instance =  AIChatbot()

    
    

if __name__ == '__main__':
    unittest.main()
