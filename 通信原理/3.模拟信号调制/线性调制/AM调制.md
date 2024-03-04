### 幅度调制原理
AM调制信号的原理是将 $c(t)$ 设置为
$$\begin{align}
    c(t) = A\cos(2\pi ft)
\end{align}$$

其调制后的信号为
$$\begin{align}
    s_{AM}(t) = [A + m(t)]\cos(2\pi f_ct)
\end{align}$$

它的信号频谱为
$$\begin{align}
    S_{AM}(jw) = \frac{A}{2}[\delta(f -  f_c) + \delta(f + f_c) ] + \frac{1}{2}[M(f -  f_c) + M(f + f_c)]
\end{align}$$

其中 $m(t)$ 时直流分量为 $0$ 的信号,其中
$$\begin{align}
    \beta_{AM} = \frac{max|m(t)|}{A}
\end{align}$$

称为调频指数.载波功率
$$\begin{align}
    P_{AM} = \frac{A^2}{2} + \frac{\bar{m^2(t)}}{2}
\end{align}$$

其中 $\frac{A^2}{2}$ 为载波功率, $\frac{\bar{m^2(t)}}{2}$ 为边带功率.调频效率为
$$\begin{align}
    \eta_{AM} = \frac{\bar{m^2(t)}}{A^2 + \bar{m^2(t)}} < 1
\end{align}$$