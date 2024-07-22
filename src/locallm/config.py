from dataclasses import dataclass


@dataclass
class DefaultConfig:
    endpoint: str = "http://localhost:11434/api/generate"
    model: str = "llama3"