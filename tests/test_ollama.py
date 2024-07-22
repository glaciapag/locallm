import unittest
from locallm import AIChatbot
from locallm.config import DefaultConfig

class TestOllama(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """This method is run once before any test in the class."""
        cls.chat_bot_instance =  AIChatbot()

    def test_ollama_connection(self):
        """Tests the connection for Ollama server"""
        self.assertEqual(TestOllama.chat_bot_instance.health_check(), 200)

    def test_ollama_default_config(self):
        """Tests the default configuration"""
        self.assertEqual(TestOllama.chat_bot_instance.endpoint, "http://localhost:11434/api/generate")
        self.assertEqual(TestOllama.chat_bot_instance.model, "llama3")

    def test_ollama_custom_config(self):
        """Tests the custom configuration"""
        class CustomConfig(DefaultConfig):
            model = "custom_model"
            endpoint = "http://customendpoint::8000"
        
        custom_chat_bot_instance = AIChatbot(CustomConfig)

        self.assertEqual(custom_chat_bot_instance.endpoint, "http://customendpoint::8000")
        self.assertEqual(custom_chat_bot_instance.model, "custom_model")


if __name__ == '__main__':
    unittest.main()
