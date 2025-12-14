# CS50P Lecture 0 函数、变量

# 官方课程地址
https://cs50.harvard.edu/python/weeks/0/

## 创建代码
在 VS Code 终端中，执行 `code hello.py` 开始编写代码，输入：
```python
print("hello, world")
```
运行程序：
```bash
python hello.py
```
程序结果：
```
hello, world
```

## 函数 (Functions)
- 函数是计算机或计算机语言已经知道如何执行的动词或动作
- 在 `hello.py` 程序中，`print` 函数接受参数 `"hello, world"` 向终端窗口打印内容

## Bugs
- 代码错误是编程过程中不可避免的一部分
- 错误信息通常可以告知犯的错误，并提供改正方法的线索

## 改进你的第一个 Python 程序
在 `hello.py` 的文本编辑器中，添加另一个函数：
```python
input("What's your name? ")
print("hello, world")
```

## 变量 (Variables)
- 变量是程序中用于存储值的容器
- `name = input("What's your name? ")` 中的等号 `=` 起着赋值的作用
- `input("What's your name? ")` 返回的值被赋给了 `name`

```python
name = input("What's your name? ")
print("hello,")
print(name)
```

## 注释 (Comments)
- 注释是程序员追踪程序运行情况的一种方式
- 用于告知其他人代码的意图

```python
# Ask the user for their name
name = input("What's your name? ")
print("hello,")
print(name)
```

## 伪代码 (Pseudocode)
- 伪代码是一种重要的注释，是特殊的待办事项清单

```python
# Ask the user for their name
name = input("What's your name? ")
# Print hello
print("hello,")
# Print the name inputted
print(name)
```

## 进一步改进你的第一个 Python 程序
```python
# Ask the user for their name
name = input("What's your name? ")
# Print hello and the inputted name
print("hello, " + name)
print("hello,", name)
```

## 字符串和参数 (Strings and Parameters)
- 字符串（在 Python 中称为 `str`）是一段文本序列
- `print` 函数接收参数，这些参数会影响函数的行为

[print 函数文档](https://docs.python.org/3/library/functions.html#print)

`print(*objects, sep=' ', end='\n', file=None, flush=False)`

- `print` 函数自动包含参数 `end='\n'`，表示自动创建换行符

```python
# Ask the user for their name
name = input("What's your name? ")
print("hello,", end="")
print(name)
```

## 字符串引号问题
- `print("hello,"friend"")` 无法正常工作，解释器会抛出错误
- 解决方法：
  1. 将双引号改为单引号：`print('hello,"friend"')`
  2. 使用转义字符：`print("hello, \"friend\"")`

## 格式化字符串 (Formatting Strings)
```python
# Ask the user for their name
name = input("What's your name? ")
print(f"hello, {name}")
```

## 更多字符串处理
- 移除用户输入内容左右两侧的空格：`name = name.strip()`
- 首字母大写：`name = name.title()`

```python
# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()
# Print the output
print(f"hello, {name}")
```

[字符串文档](https://docs.python.org/3/library/stdtypes.html#str)

## 整数 (Integers or int)
- 在 Python 中，整数被称为 `int`
- 错误示例：
  ```python
  x = input("What's x? ")
  y = input("What's y? ")
  z = x + y
  print(z)
  ```
  输出结果为 `12`（字符串拼接）

- 正确写法：
  ```python
  x = int(input("What's x? "))
  y = int(input("What's y? "))
  print(x + y)
  ```

[整型文档](https://docs.python.org/3/library/functions.html#int)

## 可读性 (Readability Wins)
- 代码必须易于阅读
- 使用注释帮助理解和维护

## 浮点数基础 (Float Basics)
- 浮点值是指带有小数点的实数，例如 `0.52`
- 四舍五入到最接近的整数：
  ```python
  x = float(input("What's x? "))
  y = float(input("What's y? "))
  z = round(x + y)
  print(z)
  ```

- 格式化输出（千位分隔符）：
  ```python
  print(f"{z:,}")
  ```

[浮点数文档](https://docs.python.org/3/library/functions.html#float)

## 浮点数更多内容
- 四舍五入到小数点后两位：
  ```python
  x = float(input("What's x? "))
  y = float(input("What's y? "))
  z = x / y
  print(round(z, 2))
  print(f"{z:.2f}")
  ```

## Def
```python
def main():
    # Output using our own function
    name = input("What's your name? ")
    hello(name)
    # Output without passing the expected arguments
    hello()
# Create our own function
def hello(to="world"):
    print("hello,", to)
main()
```

## 返回值 (Returning Values)
- 函数不仅执行操作，还能将值返回给主函数

```python
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
def square(n):
    return n * n
main()
```