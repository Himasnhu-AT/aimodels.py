import openai

class OpenAI:
    def __init__(self, api_key: str, model: str = "text-davinci-003"):
        """
        Initialize the OpenAIAI class with the API key

        Args:
            api_key (str): The API key for the OpenAI API

        Returns:
            None
        """

        self.model = model
        openai.api_key = api_key

    def generate_text(self, prompt: str, **kwargs) -> str:
        """
        Generate text using the OpenAI API

        Args:
            prompt (str): The prompt for text generation
            **kwargs: Additional keyword arguments for the API

        Returns:
            str: The generated text
        """

        # response = openai.Completion.create(
        #     engine=self.model,
        #     prompt=prompt,
        #     **kwargs
        # )
        # return response['choices'][0]['text']

        return "Generated text from OpenAI"
