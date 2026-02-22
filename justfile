set allow-duplicate-recipes := true

entry := "main.py"
app_name := "gemini-cli"

# List just
default:
    just --list

# Clean build for linux/unix
build:
    pyinstaller {{entry}} --onefile --add-data config:config --name {{app_name}}

# Clean then rebuild
rebuild: clean build

# Cleanup redundancy
clean:
    rm -rv ./dist/
    rm -rv ./build/
    rm -rv ./*.spec

# Run python
run *ARGS:
    python {{entry}} {{ARGS}}
