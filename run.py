from locallm import AIChatbot
from locallm.config import DefaultConfig

class Llama2Config(DefaultConfig):
    model = "llama2"


if __name__ == "__main__":

    ai = AIChatbot(Llama2Config)
    print(ai.ask("What is the capital of Philippines"))
