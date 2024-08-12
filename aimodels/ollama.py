import requests

class Ollama:
    def __init__(self, url: str, model: str):
        """
        Initialize the OllamaAPI class with the URL and model

        Args:
            url (str): The URL for the Ollama API
            model (str): The model for the Ollama API

        Returns:
            None
        """

        self.model = model
        self.url = url

    def generate_text(self, prompt: str, **kwargs) -> str:
        """
        Generate text using the Ollama API

        Args:
            prompt (str): The prompt for text generation
            **kwargs: Additional keyword arguments for the API

        Returns:
            str: The generated text
        """

        body = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.url, json=body)
        response.raise_for_status() # Raise an exception for 4xx/5xx status codes
        return response.json()['response']
