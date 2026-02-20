from google import genai
from google.genai import types
from pathlib import Path
import time
import sys


class GeminiInteract:
    def __init__(self, api_key: str) -> None:
        self.client = genai.Client(api_key=api_key)
        self.instruct = [
            "Response must be factual and correct, regardless if response takes longer to generate.",
            "Ensure accuracy than baseless assumptions or opinions; unless, the user prompts for opinionated answers.",
            "Provide the entire hyperlink in the response when sourcing answers from other websites.",
            "Adopt a friendly and casual tone. Adjust based on user request.",
            "Clarification will not be provided, ensure on the first response that it tackles most possible questions or clarifications.",
            "In regards to code handling. Write clear, non-complex code with comments on confusing parts and provide concise explanations.",
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


def validate_api_key() -> str:
    api_path = Path.cwd() / "api_key.txt"

    if not api_path.exists():
        api_path.touch()
        raise Exception(f"File created. Allocate '{api_path.name}' with your key")

    if api_path.stat().st_size == 0:
        raise Exception(f"File is empty. Add your api key inside '{api_path.name}'")

    api_key = api_path.read_text().strip()
    return api_key


def main():
    try:
        validate_api_key()
    except Exception as e:
        print(e)

    api_key = validate_api_key()
    gemini = GeminiInteract(api_key)

    question = sys.stdin.read().strip()
    gemini.ask_question(question)


if __name__ == "__main__":
    main()
