import requests
import json
from .config import DefaultEmbeddingConfig


class AIEmbedding:
    
    def __init__(self, config=None):
        self._config = config if config else DefaultEmbeddingConfig
        self.endpoint = self._config.endpoint
        self.model = self._config.model
    
    def embed(self, prompt, **kwargs):
        
        payload = {"model": self.model, "prompt": prompt}
        if kwargs:
            payload.update(**kwargs)
        
        response = requests.post(url=self.endpoint, json=payload)
        return response.json()