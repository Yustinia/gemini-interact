from google import genai
from google.genai import types
import time


class GeminiInteract:
    def __init__(self, api_key: str) -> None:
        self.client = genai.Client(api_key=api_key)
        self.instruct = [
            "Response must be factual and correct, regardless if response takes longer to generate.",
            "Ensure accuracy rather than baseless assumptions or opinions; unless the user prompts for opinionated answers.",
            "Provide the entire hyperlink in the response when sourcing answers from other websites.",
            "Adopt a friendly and casual tone. Adjust based on user request.",
            "Clarification will not be provided; ensure the first response tackles most possible questions or clarifications.",
            "Regarding code handling: write clear, non-complex code with comments on confusing parts and provide concise explanations.",
            "The refusal structure must reference the exact ToS line and briefly explain why.",
        ]

    def ask_question(self, question: str) -> None:
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question,
            config=types.GenerateContentConfig(
                system_instruction=self.instruct, temperature=0.2
            ),
        )
        response = str(response.text)
        self._animate_text(response)

    def _animate_text(self, response: str) -> None:
        for char in response:
            print(char, end="", flush=True)
            time.sleep(0.02)
