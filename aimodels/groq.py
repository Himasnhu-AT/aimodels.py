class Grok:
    def __init__(self, api_key: str):
        """
        Initialize the GrokAPI class with the API key
        
        Args:
            api_key (str): The API key for the Grok API
            
        Returns:
            None
        """

        self.api_key = api_key

    def generate_text(self, prompt: str, **kwargs) -> str:
        """
        Generate text using the Grok API

        Args:
            prompt (str): The prompt for text generation
            **kwargs: Additional keyword arguments for the API

        Returns:
            str: The generated text
        """
        
        return "Generated text from Grok"
