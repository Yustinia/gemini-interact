from src import GeminiInteract, ArgumentParse
from pathlib import Path
import argparse


def handle_ask_question(args: argparse.Namespace, gemini: GeminiInteract):
    question = " ".join(args.ask)
    print(f"Question: {question}")
    gemini.ask_question(question)


def handle_show_instructions(args: argparse.Namespace, gemini: GeminiInteract):
    for num, instruct in enumerate(gemini.instruct, start=1):
        print(f"{num}. {instruct}")


def handle_add_instructions(args: argparse.Namespace, gemini: GeminiInteract):
    instruction = " ".join(args.add_instruction)

    gemini.instruct.append(instruction)


def main():
    api_path = Path.cwd() / "api_key.txt"
    argument = ArgumentParse()
    args = argument.parse_args()

    if args.keyfile:
        argument.write_api_key(api_path, args.keyfile)

    try:
        api_key = argument.read_api_key(api_path)
        gemini = GeminiInteract(api_key)

        if args.ask:
            handle_ask_question(args, gemini)

        elif args.show_instructions:
            handle_show_instructions(args, gemini)

        elif args.add_instruction:
            handle_add_instructions(args, gemini)

    except (FileNotFoundError, ValueError, Exception) as e:
        print(e)


if __name__ == "__main__":
    main()
