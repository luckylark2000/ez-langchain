# LangChain 学习路线 TODO

## 第一阶段：Python 快速入门 (预计: 1-2周)

### 基础语法学习

- [x] 安装 Python 3.8+ 和配置开发环境 (VS Code + Python 插件)
- [ ] 学习 Python 基础: 变量、数据类型、列表、字典、元组
- [ ] 掌握函数定义 (`def`)、参数传递 (`*args`, `**kwargs`)
- [ ] 学习流程控制: 条件语句、循环 (`for`, `while`)
- [ ] 理解列表推导式和字典推导式
- [ ] 学习文件操作 (读写 txt、json 文件)
- [ ] 掌握异常处理 (`try-except`)
- [ ] 理解 `async/await` 异步编程基础

### 环境与工具

- [x] 学习使用 `uv/pip` 包管理器
- [x] 掌握虚拟环境创建和使用 (`python -m venv venv`或者uv自带的)
- [x] 学习创建和管理 `requirements.txt/pyproject.toml`

**实践项目**: 编写一个 Python 脚本，爬取网页内容并保存为结构化 JSON 数据

---

## 第二阶段：Python 项目工程化与 FastAPI (预计: 1-2周)

### FastAPI 基础

- [ ] 创建第一个 FastAPI 应用 (`app = FastAPI()`)
- [ ] 学习定义路由和 HTTP 方法 (`@app.get`, `@app.post`)
- [ ] 掌握 Pydantic 模型定义请求/响应体
- [ ] 学习使用 FastAPI 的自动 API 文档 (`/docs`, `/redoc`)
- [ ] 理解依赖注入基础概念

### 项目结构

- [ ] 建立标准的 Python 项目目录结构
- [ ] 学习模块化组织代码 (routers, models, services)
- [ ] 配置 CORS 中间件 (为前端连接做准备)

**实践项目**: 构建一个完整的 TODO API，包含:

- [ ] 添加、删除、更新、查询任务
- [ ] 使用 Pydantic 验证输入数据
- [ ] 通过 `/docs` 测试所有接口

---

## 第三阶段：AI 应用开发生态库 (预计: 1周)

### 必要库学习

- [ ] 学习 `httpx` 或 `aiohttp` 进行 HTTP 请求
- [ ] 掌握 `python-dotenv` 管理环境变量和 API 密钥
- [ ] 了解 `chromadb` 向量数据库的基本操作
- [ ] (可选) 学习 `pandas` 基础数据操作

### 集成实践

- [ ] 在 FastAPI 项目中集成环境变量管理
- [ ] 创建调用外部 API 的服务层

---

## 第四阶段：LangChain 核心概念 (预计: 2-3周)

### Model I/O 模块

- [ ] 配置 LangChain 和 OpenAI API 密钥
- [ ] 学习使用 `ChatOpenAI` 和 `ChatOllama` (本地模型)
- [ ] 掌握 `PromptTemplate` 创建动态提示词
- [ ] 学习 `OutputParsers` 将 LLM 输出转为结构化数据
- [ ] 实践: 创建返回 JSON 格式的聊天接口

### Retrieval 模块

- [ ] 学习使用 `DocumentLoaders` 加载各种文档格式
- [ ] 掌握 `TextSplitters` 进行文本分块
- [ ] 学习向量数据库集成 (`ChromaDB`)
- [ ] 理解嵌入模型 (`OpenAIEmbeddings`)
- [ ] 实践: 构建个人文档问答系统

### Chains 模块

- [ ] 学习 LCEL (LangChain Expression Language) 使用 `|` 操作符
- [ ] 掌握 `create_stuff_documents_chain` 创建文档链
- [ ] 学习 `create_retrieval_chain` 创建检索链
- [ ] 实践: 将检索和生成组合成完整流程

### Agents 模块

- [ ] 理解 Agent 和 Tools 的概念
- [ ] 学习创建自定义 Tools
- [ ] 掌握 `AgentExecutor` 运行代理
- [ ] 实践: 创建能够使用工具的智能助手

### Memory 模块

- [ ] 学习 `ConversationBufferMemory` 管理对话历史
- [ ] 实践: 为聊天应用添加记忆功能

---

## 第五阶段：综合项目实践 (预计: 1-2周)

### 项目选择 (二选一)

**选项 A: 个人知识库问答助手**

- [ ] 后端: 文档上传、向量存储、智能问答 API
- [ ] 前端: 文件上传界面 + 聊天界面
- [ ] 集成: 前后端联调测试

**选项 B: AI 客服助手**

- [ ] 后端: Agent + Tools (搜索、查询等)
- [ ] 前端: 聊天界面
- [ ] 集成: 实时对话功能

### 部署准备

- [ ] 学习基本的 Python 应用部署 (可选: Docker)
- [ ] 测试生产环境配置

---

## 学习资源

- [ ] LangChain 官方文档: <https://python.langchain.com/>
- [ ] FastAPI 官方文档: <https://fastapi.tiangolo.com/>
- [ ] Python 官方教程: <https://docs.python.org/3/tutorial/>

## 检查点

- [ ] 完成第一阶段: 能编写基础 Python 脚本
- [ ] 完成第二阶段: 能创建完整的 FastAPI 应用
- [ ] 完成第三阶段: 熟悉 AI 开发常用库
- [ ] 完成第四阶段: 掌握 LangChain 核心功能
- [ ] 完成第五阶段: 成功构建全栈 AI 应用

**预计总时间**: 6-10 周 (根据个人学习进度调整)

---
*每完成一个任务就在框内打勾 [x]，保持动力！*
