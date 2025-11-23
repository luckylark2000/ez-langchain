# uv 核心知识学习

官方文档：<https://docs.astral.sh/uv/>

中文文档地址：<https://uv.doczh.com/>

## 核心操作

`uv init` 项目初始化 类似于 `npm init`

`uv add <package>` 添加包 类似于 `npm install <package>`

`uv sync` 项目统一安装所有包 类似于 `npm install`

`uv run <instruction>` 运行指定的命令 类似于 `npm run <script/instruction>` 或者 `node filename.js`

## 设置镜像源

### 临时使用

```bash
uv add <package> --index mirror-address
```

例如安装`request`库：

```bash
uv add request --index https://pypi.tuna.tsinghua.edu.cn/simple
```

### 在项目中设置镜像源

在 pyproject.toml中添加如下内容

```patch
+[[tool.uv.index]]
+url = "https://pypi.tuna.tsinghua.edu.cn/simple"
+default = true
```

### windows中统一设置镜像源(推荐)

参考：pypi 清华镜像官网：<https://mirrors.tuna.tsinghua.edu.cn/help/pypi/>

在 ~/.config/uv/uv.toml 或者 /etc/uv/uv.toml 填写下面的内容：

```toml
[[index]]
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
default = true
```
