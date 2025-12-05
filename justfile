# Set the shell for all recipes
set shell := ["pwsh", "-c"]

# 本地运行文档
doc:
    uv run mkdocs serve

# 执行 main.py
main:
    uv run main.py

# 启动 fastapi 的 http 服务
api:
    uv run fastapi dev .\app\main.py --port 3324