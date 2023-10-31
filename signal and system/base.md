
$$\begin{align}
    a_k &= \frac{1}{T} \int_{T} x(t) e^{-jkw_0t} dt \\
    x(t) &= \sum_{k = -\infty}^{+\infty} a_ke^{jkw_0t}
\end{align}$$

一些重要的性质

$$\begin{align}
    x(t) &\rightarrow a_k \\
    x(t - t_0) &\rightarrow a_ke^{-jkw_0t_0}\\
    x(t)e^{-jk_0w_0t} &\rightarrow a_{k + k_0}\\
    x(-t) &\rightarrow a_{-k} \\
    x^{*}(t) &\rightarrow a^{*}_{-k} \\
    \frac{1}{T}\int_T |x(t)|^2 dt &= \sum_{k = -\infty}^{+\infty} |a_k|^2 \\
    x(t) = x(-t) &\rightarrow a_k = a_{-k},且为纯实数 \\
    x(t) = -x(-t) &\rightarrow a_k = -a_{-k},且为纯虚数 , a_0 = 0
\end{align}$$

例题:假设 $x(t)$ 满足以下条件
* $x(t)$ 为实信号
* $x(t)$ 的周期为 $T = 4$ ,其傅里叶级数为 $a_k$
* $a_k = 0 ,|k| \geq 2$
* $b_k = e^{-j\pi k /2}a_{-k}$ 为奇信号
* $\frac{1}{4} \displaystyle\int_{4} |x(t)|^2 dt = \frac{1}{2}$

解:
&emsp;&emsp; $a_k = 0 ,|k| \geq 2$ 可知除了 $a_0,a_1,a_{-1}$ 非零其余的系数都是0;
&emsp;&emsp;因为 $b_k = e^{-j\pi k /2}a_k$ 为奇信号,那么 $b_k$ 为纯虚数,且之列分量为零,以及对称

$$\begin{align}
    b_0 &= 0 \rightarrow a_0 = 0 \\ 
    b_1 &= - b_{-1} \\
    |b_1| &= |a_{-1}| \\
    |b_{-1}| &= |a_{1}|
\end{align}$$

而 $\frac{1}{4} \displaystyle\int_{4} |x(t)|^2 dt = \frac{1}{2}$ 告诉我们:

$$\begin{align}
    |a_{-1}|^2 + |a_{0}|^2 +|a_{1}|^2 = \frac{1}{2}
\end{align}$$

得到:

$$\begin{align}
    |b_{-1}|^2 + |b_{0}|^2 + |b_{1}|^2 &= \frac{1}{2} \\
    2|b_1|^2 &= \frac{1}{2} \\
    |b_1| = \frac{1}{2}
\end{align}$$

由于 $b_k$ 为纯虚数,则有 $b_1 = j\frac{1}{2}$ 或者 $b_1 = -j\frac{1}{2}$,挑选一种记录答案: $b_1 = j\frac{1}{2}$ 得到

$$\begin{align}
    a_0 &= 0 \\
    a_1 &= e^{-j\pi \frac{1}{2}}b_{-1} = -\frac{1}{2}\\
    a_{-1} &=  e^{j\pi \frac{1}{2}}b_{1} = -\frac{1}{2}
\end{align}$$

得到:

$$\begin{align}
    x(t) &= -\frac{1}{2}(e^{j\pi t /2} + e^{-j\pi t /2}) \\
    &= -cos(\frac{\pi t}{2})
\end{align}$$


这里其实有一个技巧: $x(t)$ 为实信号,那么 $a_k = a^{*}_{-k}$

$$\begin{align}
    x(t) &= a_0 + a_1e^{j\pi t /2} + a_{-1}e^{-j\pi t /2} \\
    &= a_0 + a_1e^{j\pi t /2} + (a_1e^{j\pi t /2})^{*}
\end{align}$$

如果一个复数 $z = a+jb$ ,那有:

$$\begin{align}
    z + z^{*} &= a + jb + a -jb \\
    &= 2a \\
    &= 2Re\left\{z\right\}
\end{align}$$

那就有

$$\begin{align}
    x(t) 
    &= a_0 + a_1e^{j\pi t /2} + (a_1e^{j\pi t /2})^{*} \\
    &= a_0 + 2Re\left\{ a_1e^{j\pi t /2} \right\}
\end{align}$$

这样我们只需要求两个值就可以了