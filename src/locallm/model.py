import json
import requests
import uuid
import chromadb
from .config import DefaultModelConfig
from .embedding import AIEmbedding


class ModelNotFoundError(FileNotFoundError):
    pass


class AIChatbot:

    def __init__(self, config=None):
        self._config = config if config else DefaultModelConfig 
        self.endpoint = self._config.endpoint
        self.model = self._config.model
        
    def ask(self, question, stream: bool = False, documents: list = None, **kwargs):

        if documents:
            if isinstance(documents, str):
                documents = [documents]

            client = chromadb.Client()
            collection = client.create_collection(name=f"document-{uuid.uuid1().hex}")
            emb = AIEmbedding() 
            
            for i, d in enumerate(documents):

                res = emb.embed(d)
                if "error" in res.keys():
                    raise ModelNotFoundError(res)
                
                embedding = res.get("embedding")
                collection.add(
                    ids=[str(i)],
                    embeddings=[embedding],
                    documents=[d]
                )
            response = emb.embed(d)
            results = collection.query(
                query_embeddings=[response["embedding"]],
                n_results=len(documents)
            )
            data = results["documents"]
            payload = {
                "model": self.model, 
                "prompt": f"using this data: {data}, answer the following question: {question}", 
                "stream": stream
            }
        else:
            payload = {"model": self.model, "prompt": question, "stream": stream}

        if kwargs:
            payload.update(kwargs)
        
        response = requests.post(url=self.endpoint, json=payload)

        if stream:
            response_text = []
            for resp in response:
                response_text.append(resp.decode("utf-8"))
            response_text = ''.join(response_text).strip().split('\n')
            response_json = [json.loads(resp) for resp in response_text]
            return response_json
        else:
            return response.json()
        
    def health_check(self):

        payload = {"model": self.model}
        response = requests.post(url=self.endpoint, json=payload)
        return response.status_code
    
