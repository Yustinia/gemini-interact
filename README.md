# Gemini Interact

A lightweight command-line interface for interacting with Google's Gemini API using your personal API key.

## Overview

`gemini-cli` allows you to:

- Send prompts directly from the terminal
- Store and update your API key
- Manage persistent AI instructions
- Quickly access built-in help

## Usage

Before using any other command, set your API key:

```bash
./gemini-cli -k <api_key>
```

The api key is saved on the same directory as `gemini-cli`.

| **Argument**             | **Description**                 | **Usage**                       |
| ------------------------ | ------------------------------- | ------------------------------- |
| -h / --help              | Show help message               | `./gemini-cli -h`               |
| -a / --ask               | Ask a question                  | `./gemini-cli -a <question>`    |
| -k / --keyfile           | Set or Update the API key       | `./gemini-cli -k <api_key>`     |
| -s / --show-instructions | Display current AI instructions | `./gemini-cli -s`               |
| -i / --add-instruction   | Add additional AI instruction   | `./gemini-cli -i <instruction>` |

You then can use `./gemini-cli` with the following available arguments:

```bash
# asking a question
./gemini-cli -a "What is sleep?"
./gemini-cli -a "Help, I can't sleep"

# adding additional instructions
./gemini-cli -i "Respond like an anime catgirl"
```

## Requirements

- Python 3.13+
- pip
- A valid Gemini API Key
- Optional: `just` (building from source)
- Optional: `pyinstaller` (building from source)

## Build

Clone the repository:

```bash
git clone https://github.com/Yustinia/gemini-interact.git
```

Build the project:

```bash
just build
```

The compiled executable will be available as:

```bash
./gemini-cli
```

You can find the file inside `./dist/`.

Otherwise, you can also directly run using:

```bash
just run <*arg>

# example
just run -a <question>
just run -i <instruction>
```

Clean the directory:

```bash
just clean
```
