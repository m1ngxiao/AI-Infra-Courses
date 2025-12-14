# CS50P Lecture 0 Problem Set 0

**GitHub 仓库地址**：  
[https://github.com/m1ngxiao/AI-Infra-Courses/tree/main/CS50P/Lecture_0_Problem_Set_0](https://github.com/m1ngxiao/AI-Infra-Courses/tree/main/CS50P/Lecture_0_Problem_Set_0)

---

## 📢 Indoor Voice

**题目描述**：  
全部用大写字母写作就像大喊大叫。有时候最好用“室内音量”说话，并且全部使用小写字母。  
在名为 `indoor.py` 的文件中，用 Python 编写一个程序，提示用户输入内容，然后将输入的内容转换为小写形式输出。标点符号和空格应保持不变。您可以选择（但并非必须）显式地提示用户输入内容，例如将自定义 `str` 作为参数传递给 `input`。

**提示**：
- `input` 返回的是一个 `str`：[https://docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input)
- `str` 有很多方法：[https://docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

```python
# indoor.py
def main():
    voice = input()
    print(indoor(voice))

def indoor(voice):
    return voice.lower()

main()
```

---

## 🎧 Playback Speed

**题目描述**：  
有些人习惯说话语速很快，最好能让他们慢下来，就像 YouTube 的 0.75 倍播放速度一样，或者让他们在单词之间停顿一下。  
在名为 `playback.py` 的文件中，用 Python 实现一个程序，提示用户输入，然后输出相同的输入，并将每个空格替换为 `...`（即三个句点）。

**提示**：
- `input` 返回的是一个 `str`：[https://docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input)
- `str` 有很多方法：[https://docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

```python
# playback.py
def main():
    speed = input()
    print(playback(speed))

def playback(speed):
    return speed.replace(" ", "...")

main()
```

---

## 😊 Making Faces

**题目描述**：  
在表情符号出现之前，人们使用表情符号，例如 `:)` 代表笑脸， `:(` 代表哭脸。如今，程序通常会自动将表情符号转换为表情符号！  
在名为 `faces.py` 的文件中，实现一个名为 `convert` 函数，该函数接受一个 `str` 作为输入，并返回该字符串，其中所有 `:)` 都转换为 🤗（即略带微笑的表情），所有 `:(` 都转换为 🙁（即略带皱眉的表情）。所有其他文本应保持不变。  
然后，在同一个文件中，实现一个名为 `main` 函数，该函数提示用户输入，对输入内容 `convert` 函数，并打印结果。你可以选择显式地提示用户输入，例如将你自己的 `str` 作为参数传递给 `input`。请务必在文件末尾调用 `main`。

**提示**：
- `input` 返回的是一个 `str`：[https://docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input)
- `str` 有很多方法：[https://docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- 表情符号实际上只是一个字符，所以你可以像引用任何 `str` 一样引用它，例如 `"🙂"`；您可以根据需要将此页面上的表情符号复制并粘贴到自己的代码中。

```python
# faces.py
def main():
    emotion = input()
    print(faces(emotion))

def faces(emotion):
    return emotion.replace(":)", "🙂").replace(":(", "🙁")

main()
```

---

## ⚡ Einstein

**题目描述**：  
即使你从未学过物理（或者最近没学过！），你也可能听说过 `E=mc^2`，其中 `E` 代表能量（以焦耳为单位），`m` 代表质量（以千克为单位），`c` 代表光速（大约为每秒 3000000000 米），这是阿尔伯特·爱因斯坦等人提出的公式。本质上，这个公式意味着质量和能量是等价的。  
在名为 `einstein.py` 的文件中，用 Python 编写一个程序，提示用户输入质量（以千克为单位，取整数），然后输出等效的焦耳数（取整数）。假设用户输入的是一个整数。

**提示**：
- `input` 返回 `str`：[https://docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input)
- `int` 可以将 `str` 转换为 `int`：[https://docs.python.org/3/library/functions.html#int](https://docs.python.org/3/library/functions.html#int)
- Python 附带了几个内置函数：[https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)

```python
# einstein.py
def main():
    n = int(input("m: "))
    E = einstein(n)
    print("E:", E)

def einstein(n):
    return n * 300000000**2

main()
```

---

## 💰 Tip Calculator

**题目描述**：  
在美国，在餐厅用餐后给服务员小费是一种惯例，金额通常为餐费的15%或更多。不过别担心，我们已经为您准备了一个小费计算器！  
```python
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # TODO

def percent_to_float(p):
    # TODO

main()
```

**需要实现的功能**：
- `dollars_to_float`：接受 `str`（格式为 `$##.##`），移除前导 `$`，返回 `float`（例如输入 `$50.00` → 返回 `50.0`）
- `percent_to_float`：接受 `str`（格式为 `##%`），移除末尾 `%`，返回 `float`（例如输入 `15%` → 返回 `0.15`）

**提示**：
- `input` 返回的是一个 `str`：[https://docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input)
- `float` 可以将 `str` 转换为 `float`：[https://docs.python.org/3/library/functions.html#float](https://docs.python.org/3/library/functions.html#float)
- `str` 有很多方法：[https://docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

```python
# tip.py
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d.removeprefix("$"))

def percent_to_float(p):
    return float(p.removesuffix("%")) / 100

main()
```

---

> ✨ **完整项目已托管在 GitHub**：  
> [https://github.com/m1ngxiao/AI-Infra-Courses/tree/main/CS50P/Lecture_0_Problem_Set_0](https://github.com/m1ngxiao/AI-Infra-Courses/tree/main/CS50P/Lecture_0_Problem_Set_0)  
> 所有题目描述、代码示例和提示链接均按原始要求完整保留，无任何删减！