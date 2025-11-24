"""_summary_
学习 Python 基础: 变量、数据类型、列表、字典、元组
对应文档:docs\\quick-start-python\\basic-grammar\\变量和数据类型.md
"""

# 变量声明
from types import NoneType


num = 3 # 不用用类似 let, const 之类的，python 自动识别

## 带类型的（3.9版本开始支持）,类型提示需要安装pyright插件
a:bool = True

print(num)
print(a)

# 数据类型
i=3
b = 1.2
c = True
n = None

print(type(i)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'bool'>
print(type(c)==bool) # True
print(type(n)==NoneType) # True
#


