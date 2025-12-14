# CS50P Lecture 1 Problem Set 1

# GitHub仓库地址

[https://github.com/m1ngxiao/AI-Infra-Courses/tree/main/CS50P/Lecture_1_Problem_Set_1](https://github.com/m1ngxiao/AI-Infra-Courses/tree/main/CS50P/Lecture_1_Problem_Set_1)

---

## Deep Thought

> "All right," said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
> 
> "You're really not going to like it," observed Deep Thought.
> 
> "Tell us!"
> 
> "All right," said Deep Thought. "The Answer to the Great Question..."
> 
> "Yes…!"
> 
> "Of Life, the Universe and Everything..." said Deep Thought.
> 
> "Yes…!"
> 
> "Is..." said Deep Thought, and paused.
> 
> "Yes…!"
> 
> "Is..."
> 
> "Yes…!!!…?"
> 
> "Forty-two," said Deep Thought, with infinite majesty and calm."
> — The Hitchhiker's Guide to the Galaxy, Douglas Adams

在 `deep.py` 中，实现一个程序，提示用户回答关于生命、宇宙和一切的伟大问题，如果用户输入 `42` 或（不区分大小写） `forty-two` 或 `forty two`，则输出 `Yes`。否则输出 `No`。

**提示：**
如果检查是否与字符串 `"42"` `str` 一样，而不是与 `int` `42` 相等，则无需将用户输入转换为 `int`！

如果你的输出或用户输入的内容换行显示，也没关系。

```python
# deep.py
def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    print(deep(answer))

def deep(answer):
    if answer in ["42", "forty-two", "forty two"]:
        return "Yes"
    else:
        return "No"

main()
```

---

## Home Federal Savings Bank

在《宋飞正传》第七季第 24 集中，克莱默去了一家银行，这家银行承诺，只要有人没听到"你好"（hello）的问候，就奖励 100 美元。结果克莱默听到的是"嘿"（hey），他坚持认为这不是"你好"，于是要求银行奖励 100 美元。银行经理提出了一个折衷方案："既然你听到的问候是以'h'开头的，那 20 美元怎么样？"克莱默接受了。

在名为 `bank.py` 的文件中，实现一个程序，提示用户输入问候语。如果问候语以"hello"开头，则输出 `$0`。如果问候语以"h"（但不是"hello"）开头，则输出 `$20`。否则，输出 `$100`。忽略用户问候语中的任何前导空格，并将用户的问候语视为 case-insensitively。

**提示：**
str 有很多方法 [https://docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
不仅 "hello"，而且 "hello there", "hello, Newman" 等等，都应该支付 0 美元。

```python
# bank.py
def main():
    greeting = input("Greeting: ").strip().lower()
    print(bank(greeting))

def bank(greeting):
    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"

main()
```

---

## File Extensions

尽管 Windows 和 macOS 有时会隐藏文件扩展名，但大多数文件都有扩展名，即文件名末尾以句点 (.) 开头的后缀。例如，GIF 文件的文件名以 `.gif` 结尾，JPEG 文件的文件名以 `.jpg` 或 `.jpeg` 结尾。当您双击文件打开它时，计算机会使用文件扩展名来确定要启动哪个程序。

相比之下，网页浏览器依赖于媒体类型（以前称为 MIME 类型）来确定如何显示网络上的文件。当您从 Web 服务器下载文件时，服务器会发送一个 HTTP 标头以及文件本身，该标头指示文件的媒体类型。例如，GIF 的媒体类型是 `image/gif`，JPEG 的媒体类型是 `image/jpeg`。为了确定文件的媒体类型，Web 服务器通常会查看文件的扩展名，并将两者进行映射。

有关常用类型，请参阅 [https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types/Common_types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types/Common_types)

在名为 `extensions.py` 的文件中，实现一个程序，该程序提示用户输入文件名，然后输出该文件的媒体类型（如果文件名以以下任何后缀结尾，则不区分大小写）：
- `.gif`
- `.jpg`
- `.jpeg`
- `.png`
- `.pdf`
- `.txt`
- `.zip`

如果文件名以其他后缀结尾或根本没有后缀，则输出 `application/octet-stream`，这是一个常见的默认值。

**提示：**
str 有很多方法 [https://docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

```python
# extensions.py
EXTENSIONS_DICT = {
    "gif": "image/gif", 
    "jpg": "image/jpeg", 
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

def main():
    fileName = input("File name: ").strip().lower()
    print(get_extension(fileName))

def get_extension(fileName):
    file_ex = fileName.split(".")[-1]
    if file_ex in EXTENSIONS_DICT:
        return EXTENSIONS_DICT[file_ex]
    else:
        return "application/octet-stream"

main()
```

---

## Math Interpreter

Python 已经支持数学运算，你可以编写代码来对数值甚至变量进行加、减、乘、除运算。但是，让我们编写一个程序，让用户即使不懂 Python 也能进行数学运算。

在名为 `interpreter.py` 的文件中，实现一个程序，该程序提示用户输入一个算术表达式，然后计算并输出结果，结果以一位小数的浮点数形式表示。假设用户的输入格式为 `x y z`，其中 `x` 和 `y` 之间以及 `y` 和 `z` 之间各有一个空格。

- `x` 是一个整数
- `y` 可以是 `+`、`-`、`*` 或 `/`
- `z` 是一个整数

例如，如果用户输入 `1 + 1`，你的程序应该输出 `2.0`。假设，如果 `y` 是 `/`，那么 `z` 将不为 `0`。

请注意，正如 `python` 本身是 Python 的解释器一样，您的 `interpreter.py` 也将是数学的解释器！

**提示：**
str 提供了相当多的方法 [https://docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods)，包括 split，它可以将 str 分割成一系列值，这些值可以一次性赋值给变量。例如，如果 expression 是一个类似 1 + 1 的 str，那么 `x, y, z = expression.split(" ")` 将 `x` 赋值为 `1`，`y` 赋值为 `+`，`z` 赋值为 `1`。

```python
# interpreter.py
def main():
    x, y, z = input("Expression: ").split()
    result= interpreter(x, y, z)
    print(f"{result:.1f}")

def interpreter(x, y, z):
    x = float(x)
    z = float(z)
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z

main()
```

---

## Meal Time

假设你身处一个习惯于早餐在 7:00 到 8:00 之间、午餐在 12:00 到 13:00 之间、晚餐在 18:00 到 19:00 之间的国家。如果有一个程序可以告诉你什么时候该吃什么，那岂不是很好吗？

在 `meal.py` 中，实现一个程序，提示用户输入时间，并输出当前是 `breakfast time`、`lunch time` 还是 `dinner time`。如果不是用餐时间，则不输出任何内容。假设用户输入的时间格式为 24 小时制，格式为 `#:##` 或 `##:##`。并且假设每餐的时间范围都包含该时间。例如，无论是 7:00、7:01、7:59 还是 8:00，或者介于这些时间之间的任何时间，都表示是早餐时间。

请按照以下结构编写程序，其中 `convert` 是一个函数（可由 `main` 调用），它将 `time`（一个 24 小时制 `str`）转换为相应的小时数（`float`）。例如，给定 `time` `"7:30"`（即 7 小时 30 分钟），`convert` 应返回 `7.5`（即 7.5 小时）。

```python
def main():
    ...
def convert(time):
    ...
if __name__ == "__main__":
    main()
```

**提示：**
str 提供了相当多的方法 [https://docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods)，包括 split，它可以将 str 分割成一系列值，这些值可以一次性赋值给变量。例如，如果 time 是一个类似 "7:30" 的 str，那么 `hours, minutes = time.split(":")` 将 "7" 分配给 hours，将 "30" 分配给 minutes。

请记住，1 小时有 60 分钟。

```python
# meal.py
def main():
    time = input("What time is it? ")
    result = convert(time)
    if result:
        print(result)

def convert(time):
    hour, minute = time.split(":")
    time = float(hour) + float(minute) / 60
    if 7 <= time <= 8:
        return "breakfast time"
    elif 12 <= time <= 13:
        return "lunch time"
    elif 18 <= time <= 19:
        return "dinner time"

if __name__ == "__main__":
    main()
```

---

## 挑战：添加对 12 小时制时间的支持

挑战一下，可以选择添加对 12 小时制时间的支持，允许用户以这种格式输入时间：
- `#:## a.m.` 和 `##:## a.m.`
- `#:## p.m.` 和 `##:## p.m.`

```python
# meal_challenge.py
def main():
    time = input("What time is it? ").strip().lower()
    result = convert(time)
    if result:
        print(result)

def convert(time):
    end = None
    if time.endswith("a.m."):
        end = "a.m."
        time = time[:-4]
    elif time.endswith("am"):
        end = "a.m."
        time = time[:-2]        
    elif time.endswith("p.m."):
        end = "p.m."
        time = time[:-4]
    elif time.endswith("pm"):
        end = "p.m."
        time = time[:-2]
    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)
    if end == "a.m." and hour == 12:
        hour = 0
    elif end == "p.m." and hour != 12:
        hour += 12

    time = hour + minute / 60.0
    if 7 <= time <= 8:
        return "breakfast time"
    elif 12 <= time <= 13:
        return "lunch time"
    elif 18 <= time <= 19:
        return "dinner time"

if __name__ == "__main__":
    main()
```