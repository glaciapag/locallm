import requests
import json
from .config import DefaultConfig


class AIChatbot:

    def __init__(self, config = None):
        self._config = config if config else DefaultConfig 
        self.endpoint = self._config.endpoint
        self.model = self._config.model
        
    def ask(self, question, stream: bool = False, **kwargs):

        payload = {"model": self.model, "prompt": question, "stream": stream}
        if kwargs:
            payload.update(kwargs)
        
        response = requests.post(
            url=self.endpoint,
            json=payload
        )

        if stream:
            response_text = []
            for resp in response:
                response_text.append(resp.decode("utf-8"))
            response_text = ''.join(response_text).strip().split('\n')
            response_json = [json.loads(resp) for resp in response_text]
            return response_json
        else:
            return response.json()
