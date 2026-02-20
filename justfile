set allow-duplicate-recipes := true


entry := "main.py"
app_name := "gemini-cli"

# List just
default:
    just --list

# Clean build for windows
[windows]
build:
    pyinstaller {{entry}} --onefile --name {{app_name}}.exe

# Clean build for linux/unix
[linux]
build:
    pyinstaller {{entry}} --onefile --name {{app_name}}

# Clean then rebuild
rebuild: clean build

# Cleanup redundancy
clean:
    rm -rv ./dist/
    rm -rv ./build/
    rm -rv ./*.spec

# Run python
run *ARGS:
    python3 {{entry}} {{ARGS}}