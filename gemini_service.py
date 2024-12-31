"""The hello_world gemini module"""

import os
from typing import Optional
from dotenv import load_dotenv
import google.generativeai as genai  # type: ignore

class GeminiService:
    def __init__(self) -> None:
        self.model: Optional[genai.GenerativeModel] = None
        
    def initialize(self) -> None:
        """Initialize the Gemini service with API key and model configuration"""
        if self.model is not None:
            return  # Already initialized
            
        load_dotenv()
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        
    def get_response(self, query: str) -> str:
        """Get a response from Gemini for the given query"""
        if self.model is None:
            self.initialize()
        assert self.model is not None  # for type checker
        response = self.model.generate_content(query)
        return response.text

# Create a singleton instance
gemini_service = GeminiService()
