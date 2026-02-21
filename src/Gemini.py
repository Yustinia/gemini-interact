from google import genai
from google.genai import types
from pathlib import Path
import time
import json


class GeminiInteract:
    def __init__(self, api_key: str) -> None:
        self.client = genai.Client(api_key=api_key)
        self.instruct = self._load_instructions()

    def _load_instructions(self) -> list[str]:
        project_root = Path(__file__).resolve().parent.parent
        instruct_config = project_root / "config" / "instructions.json"

        with instruct_config.open("r", encoding="utf-8") as f:
            data = json.load(f)

        instructions = data.get("instructions", [])

        return instructions

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
