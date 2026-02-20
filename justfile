default:
    just --list

build:
    pyinstaller --onefile --name "gen" main.py

clean:
    rm -rv ./dist/
    rm -rv ./build/
    rm -rv ./gen.spec