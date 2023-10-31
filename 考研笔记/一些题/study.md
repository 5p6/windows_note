
### 1

$$\begin{cases}
    1.a \leq f(x) \leq b ,x \in [a,b] \\
    2.\forall x,y \in [a,b] ,|f(x) - f(y)| \leq \frac{1}{2} |x - y| \\
    3. \left\{ x_n \right\} , a \leq x_1 \leq b , x_{n+1} = \frac{1}{2}[x_n + f(x_n)] 
\end{cases}$$

证明:
(1) $f(x) = x$ 有唯一解 $c$ ;
(2) $\lim \limits_{n \rightarrow +\infty} x_n = c $ 

(1) 证明思路:
a.先证明 $F(x) =  f(x) - x$ 在 $[a,b]$ 上有零点,b.然后证明这个零点的唯一性,证明:
先证明存在性,令 

$$\begin{align}
    F(x) = f(x) - x\\
\end{align}$$

则有

$$\begin{align}
    F(a) &= f(a) - a \geq 0 \\
    F(b) &= f(b) - b \leq 0 \\
\end{align}$$

讨论 $F(a) = 0$ 或者 $F(b) = 0$ 的情况下,$c = a $ 或者 $c = b$ , 如果都不是,则更具零点定理, $\exist \xi \in (a,b)$ 使得:

$$\begin{align}
    F(\xi) = f(\xi) - \xi = 0
\end{align}$$

再证唯一性:假设 $ c,d \in [a,b]$ 且 $c\not ={d}$ ,使得

$$\begin{align}
    f(c) - c  = f(d) - d = 0
\end{align}$$

则有:

$$\begin{align} 
   | f(c) - f(d) | = |c - d| \leq \frac{1}{2} |c - d| 
\end{align}$$

矛盾,所以只有 $c=d$

(2) 这里看到

$$\begin{align}
    x_{n+1} = \frac{1}{2} [x_n + f(x_n)]
\end{align}$$

如果

$$\begin{align}
    \lim\limits_{n\rightarrow + \infty} x_n = \lim\limits_{n\rightarrow + \infty} x_{n+1} = c
\end{align}$$

则 $\exist N \in Z^{+} , n>N $ 时存在每个 $\xi \geq 0$ 有: 

$$\begin{align}
    |x_{n+1} - c| \leq \xi
\end{align}$$


$$\begin{align}
    x_{n+1} - c = \frac{1}{2} [x_n + f(x_n)] - c
\end{align}$$

因为

$$\begin{align}
    c = f(c)
\end{align}$$

则有

$$\begin{align}
    x_{n+1} - c &= \frac{1}{2} [x_n + f(x_n)] - c \\
    &= \frac{1}{2} [x_n + f(x_n)] - \frac{1}{2}[c + f(c)]\\
    &= \frac{1}{2}[x_n - c] + \frac{1}{2}[f(x_n) - f(c)]
\end{align}$$

取绝对值:

$$\begin{align}
    |x_{n+1} - c |
    &= |\frac{1}{2}[x_n - c] + \frac{1}{2}[f(x_n) - f(c)]|\\ &\leq |\frac{1}{2}[x_n - c] + \frac{1}{2}*\frac{1}{2}[x_n - c]|=\frac{3}{4} |x_n - c|
\end{align}$$

则有

$$\begin{align}
    |x_{n+1} - c | &\leq \frac{3}{4} |x_n - c| \leq (\frac{3}{4})^2 |x_{n-1} - c| \leq (\frac{3}{4})^3 |x_{n-2} - c| \cdots \leq (\frac{3}{4})^{n} |x_{1} - c|  
\end{align}$$

两边取极限

$$\begin{align}
    \lim\limits_{n\rightarrow + \infty}|x_{n+1} - c | \leq \lim\limits_{n\rightarrow + \infty}(\frac{3}{4})^{n} |x_{1} - c|  \\
\end{align}$$

即可得 

$$\begin{align}
    \lim\limits_{n\rightarrow + \infty} x_n = c
\end{align}$$