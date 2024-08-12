import google.generativeai as genai

class Gemini:
    def __init__(self, api_key: str, model: str = "gemini-1.5-flash"):
        """
        Initialize the GeminiAI class with the API key

        Args:
            api_key (str): The API key for the Gemini API

        Returns:
            None
        """

        self.model = model
        self.api_key = api_key

    def generate_text(self, prompt: str, **kwargs):
        """
        Generate text using the Gemini API

        Args:
            prompt (str): The prompt for text generation
            **kwargs: Additional keyword arguments for the API

        Returns:
            str: The generated text
        """

        genai.configure(self.api_key)
        model = genai.GenerativeModel(self.model)
        response = model.generate_content(prompt)
        return response.text
