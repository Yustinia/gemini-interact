from pathlib import Path
import argparse


class ArgumentParse:
    def __init__(self, description: str = "Gemini AI CLI") -> None:
        self.description = description
        self.parser = argparse.ArgumentParser(description=self.description)
        self._setup_arguments()

    def _setup_arguments(self):
        self.parser.add_argument(
            "-a", "--ask", nargs="+", type=str, help="Ask question to Gemini"
        )
        self.parser.add_argument("-k", "--keyfile", help="Set or update API key")
        self.parser.add_argument(
            "-s",
            "--show-instructions",
            action="store_true",
            help="Display AI instructions",
        )
        self.parser.add_argument(
            "-i", "--add-instruction", nargs="+", help="Add additional AI instructions"
        )

    def parse_args(self) -> argparse.Namespace:
        return self.parser.parse_args()

    def write_api_key(self, keyfile_path: Path, key: str):
        keyfile_path.write_text(key)

    def read_api_key(self, keyfile_path: Path) -> str:
        try:
            if not keyfile_path.exists():
                raise FileNotFoundError(
                    "API file not found. Please create it first using -k or --keyfile"
                )

            if keyfile_path.stat().st_size == 0:
                raise ValueError("API file is empty")

            return keyfile_path.read_text().strip()

        except Exception as e:
            raise e
