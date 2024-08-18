from dataclasses import dataclass


@dataclass
class DefaultModelConfig:
    endpoint: str = "http://localhost:11434/api/generate"
    model: str = "llama3"


@dataclass
class DefaultEmbeddingConfig:
    endpoint: str = "http://localhost:11434/api/embeddings"
    model: str = "mxbai-embed-large"