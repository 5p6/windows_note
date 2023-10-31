### 解
16.

$$\begin{align}
    F(s) &= \frac{s^2(1 - e^{-s})}{s + 3} \\
    &=  \frac{[(s+3)^2 - 6s  - 9]](1 - e^{-s})}{s + 3} \\
    &=(s + 3)(1 - e^{-s})  - \frac{(6s + 9)(1 - e^{-s})}{s + 3} \\
    &=(s + 3)(1 - e^{-s})  -6(1 - e^{-s}) + \frac{ 9(1 - e^{-s})}{s + 3}
\end{align}$$

那么

$$\begin{align}
    f(0_+) &= \lim_{s\rightarrow \infty}sF'(s)
\end{align}$$

注意其中 $F'(s)$ 是 $F(s)$ 的真分式,则

$$\begin{align}
    f(0_+) &= \lim_{s\rightarrow \infty}sF'(s) \\
    &=\lim_{s\rightarrow \infty}\frac{ 9s(1 - e^{-s})}{s + 3} \\
    &= 9
\end{align}$$



解:
已知宽度为 $1$ 的门函数 $g_2(t)=\begin{cases} 1 ,|t|\leq 1  \\ 0,else\end{cases}$ ,两个该函数卷积就变为了三角波函数 $f(t) = 2\Delta_4(t) = g_2(t) * g_2(t) $ ,其中

$$\begin{align}
    \Delta_4(t)=\begin{cases}
        1 - \frac{|t|}{2} , |t| \leq 2 \\
        0, else
    \end{cases}
\end{align}$$

得到他的傅里叶变换为 $F(jw) = F[f(t)] = 4Sa^2(w)$ ,如图
<center>
<img src="./image2.png">
</center>

它的第一个零点,$w = \pi$ ,而图中的函数 $f_T(t)$ 是一个周期 $T = 8$ 的周期函数,$f_T(t) = \displaystyle \sum_{n=-+\infty}^{+\infty}f(t - 8n) =f(t) * \sum_{n=-+\infty}^{+\infty} \delta(t - 8n)$ ,那么它的傅里叶变换为

$$\begin{align}
    F_T(jw) &= F(jw) \frac{n\pi}{4}\sum_{n=-+\infty}^{+\infty} \delta(w - \frac{n\pi}{4}) \\
    &=\frac{n\pi}{4}\sum_{n=-+\infty}^{+\infty} F(j\frac{n\pi}{4})\delta(w - \frac{n\pi}{4})
\end{align}$$


$$\begin{align}
    \frac{\sin w}{w} = 0 \rightarrow \sin w = 0, w= n\pi \rightarrow first \; w_0 = \pi
\end{align}$$
