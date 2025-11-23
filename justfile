# Set the shell for all recipes
set shell := ["pwsh", "-c"]

doc:
    uv run mkdocs serve

main:
    uv run main.py