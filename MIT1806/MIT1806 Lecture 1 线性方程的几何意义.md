# MIT1806 Lecture 1 线性方程的几何意义

# 官方课程地址
https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-1-the-geometry-of-linear-equations/

### 一、知识概要

本节课将带领我们深入探讨线性代数的核心概念，我们从方程求解入手，了解线性代数在解决复杂方程系统中的广泛应用。我们通过“行图像”和“列图像”两种方法来求解方程，这为理解矩阵与向量之间的关系奠定了基础。

### 二．方程组的几何解释

#### 2.1 二维行图像

首先，我们通过一个例子来理解如何利用行图像求解方程：

**例 1**

求解方程：\(
\begin{cases}
2x - y = 0 \\
-x + 2y = 3
\end{cases}
\)

将方程写为矩阵形式：

\[
\begin{bmatrix}
2 & -1 \\
-1 & 2
\end{bmatrix}
\underset{\text{系数矩阵}}{} 
\quad
\begin{bmatrix}
x \\
y
\end{bmatrix}
\underset{\text{未知系数}}{}
\quad
=
\quad
\begin{bmatrix}
0 \\
3
\end{bmatrix}
\underset{\text{向量}}{}
\]


- 系数矩阵 \( A \)：将方程的系数按行排列，构成矩阵。
- 未知向量 \( x \)：将方程中的未知数按列排列，构成向量。
- 向量 \( b \)：将等式右侧的结果提取出来，构成向量。

接下来，我们使用行图像来解这个方程：行图像是指在系数矩阵上每次取一行来构成方程，并在坐标系中绘制图像。与初等数学中通过图像求解方程的方式类似。


![](https://fastly.jsdelivr.net/gh/bucketio/img13@main/2025/12/14/1765711535556-e8c9bda6-59b4-4098-9ce8-25eb6aaea8b5.png)

方程：\[
\begin{cases}
2x - y = 0 \\
-x + 2y = 3
\end{cases}
\]

解得：\(x = 1, \quad y = 2\)



---

#### 2.2 二维列图像

接下来，从列图像的角度来求解同一个方程：
\[
\begin{cases}
2x - y = 0 \\
-x + 2y = 3
\end{cases}
\]

这次，我们将方程按列提取系数，得到的矩阵为：
\[
x \begin{bmatrix} 2 \\ -1 \end{bmatrix} + y \begin{bmatrix} -1 \\ 2 \end{bmatrix} = \begin{bmatrix} 0 \\ 3 \end{bmatrix}
\]

如上，我们使用列向量构成系数矩阵，将问题化为：将向量\(\begin{bmatrix} 2 \\ -1 \end{bmatrix}\)与\(\begin{bmatrix} -1 \\ 2 \end{bmatrix}\)正确组合，使得其结果构成\(
\begin{bmatrix} 0 \\ 3 \end{bmatrix}
\)。

接下来我们使用列图像求解此方程：

![](https://fastly.jsdelivr.net/gh/bucketio/img10@main/2025/12/14/1765712589413-df6ca02e-214d-402a-9a18-16e92a4fb89c.png)


在这种方法下，我们的目标是找到合适的 \( x \)和 \( y \) ，使得 \( x \) 倍的 \( (2,-1) \) 和 \( y \) 倍的 \( (-1,2) \) 的线性组合恰好等于 \( (0,3) \)。如图所示，\( 1 \) 倍 \( (2,-1) \) 加上 \( 2 \) 倍 \( (-1,2) \) 满足条件。从图像中也能清晰地看出结果的正确性。

如果我们随意选择 \( x \) 和 \( y \)，会得到不同方向的向量，这些向量将覆盖整个平面。我们暂时不展开讨论，保持这种初步的印象即可。

---

### 三. 方程组的几何解释推广

#### 3.1 高维行图像

如果我们将方程推广到更高维度，例如三维空间：
\[
\begin{cases}
2x - y = 0 \\
-x + 2y - z = -1 \\
-3y + 4z = 4
\end{cases}
\]

对应的矩阵为：
\[
A = \begin{bmatrix}
-2 & -1 & 0 \\
1 & 0 & 2 \\
-3 & -1 & 4
\end{bmatrix}, \quad b = \begin{bmatrix} 0 \\ -1 \\ 4 \end{bmatrix}
\]
方程：\[
Ax = b
\]

此时，若通过行图像求解，得到的是三个平面相交的情况，然而直接通过图像来观察交点较为复杂。常见的做法是先联立两个平面，求出交线，再研究这条线与第三个平面交于何处，最终得到交点坐标。对于三维问题，这种方法尚可行，但在四维或更高维时，图像的直观性则极大受限，行图像方法的局限性也逐渐显现。

---

#### 3.2 高维列图像

对于同样的方程，我们改用列图像方法来解决：
\[
\begin{cases}
2x - y = 0 \\
-x + 2y - z = -1 \\
-3y + 4z = 4
\end{cases}
\]

使用列图像时，矩阵形式为：
\[
x \begin{bmatrix} 2 \\ -1 \\ 0 \end{bmatrix} + y \begin{bmatrix} -1 \\ 2 \\ -3 \end{bmatrix} + z \begin{bmatrix} 0 \\ -1 \\ 4 \end{bmatrix} = \begin{bmatrix} 0 \\ -1 \\ 4 \end{bmatrix}
\]

通过这种方法，解题的思路变得清晰：寻找合适的线性组合使得左边的向量和右边的结果一致。这种方式比行图像更加系统化。



![](https://fastly.jsdelivr.net/gh/bucketio/img14@main/2025/12/14/1765712784981-cecd1cd1-da38-4aa9-80c3-86f402c8a1bf.png)



显然，对于这个特定例子，我们只需取 \( x = 0 \)，\( y = 0 \)，\( z = 1 \) ，就能得到正确结果，而在行图像中这一点并不明显。列图像方法的另一个优点是其简便性：当我们修改右侧向量 \( b \)后，依然可以通过重新求解线性组合得到新的解，而行图像则需要重新绘制图像。

此外，我们还要考虑：对于任意的 \( b \) 是否都能找到解 \( Ax = b \) ？于像本例这样的矩阵，列空间可以覆盖整个三维空间，解是存在的。然而，某些矩阵的列向量只构成一个平面，这种情况下，无法覆盖整个空间，进而不能对任意 \( b \) 求解 \( Ax = b \) 这个方程。

---

#### 3.3 矩阵乘法

假设已知矩阵 \( A \) 和向量 \( x \)，如何计算它们的乘积？例如， \( A = \begin{bmatrix} 2 & 5 \\ 1 & 3 \end{bmatrix}, x = \begin{bmatrix} 1 \\ 2 \end{bmatrix} \)，我们有两种方法：

- **方法 1**：将矩阵 \( A \) 看做列向量的组合：
\[
\begin{bmatrix} 2 & 5 \\ 1 & 3 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \end{bmatrix} = 1 \begin{bmatrix} 2 \\ 1 \end{bmatrix} + 2 \begin{bmatrix} 5 \\ 3 \end{bmatrix} = \begin{bmatrix} 12 \\ 7 \end{bmatrix}
\]

- **方法 2**：将矩阵 \( A \) 看做行向量的组合：
\[
\begin{bmatrix} 2 & 5 \\ 1 & 3 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} (2,5) \cdot (1,2) \\ (1,3) \cdot (1,2) \end{bmatrix} = \begin{bmatrix} 12 \\ 7 \end{bmatrix}
\]
通过这种方式，矩阵乘法的计算变得更加直观。

![](https://fastly.jsdelivr.net/gh/bucketio/img4@main/2025/12/14/1765715236855-763e19bb-6727-4692-826d-119b49bb5e1b.png)



---

### 四、学习感悟

这部分内容帮助我们初步理解了线性代数的核心概念，通过从解方程入手，逐步引入列空间的概念，发现从列空间角度将求解方程转化为求列向量的线性组合，这一思路更加系统和科学。
