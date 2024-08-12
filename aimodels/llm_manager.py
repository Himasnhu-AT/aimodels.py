from .openai import OpenAI
from .gemini import Gemini
from .ollama import Ollama
from .groq import Grok

# class LLMManager:
#     def setup_openai(self, api_key: str, model: str = "text-davinci-003"):
#         self.openai_api = OpenAI(api_key, model)
    
#     def setup_gemini(self, api_key: str, model: str = "gemini-1.5-flash"):
#         self.gemini_api = Gemini(api_key, model)
    
#     def setup_ollama(self, url: str, model: str = "llama3.1"):
#         self.ollama_api = Ollama(url, model)
    
#     def setup_grok(self, api_key: str):
#         self.grok_api = Grok(api_key)
    