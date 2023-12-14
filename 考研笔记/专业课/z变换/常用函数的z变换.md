1.冲击函数和阶跃函数
$$\begin{align}
    x[n] = \delta[n] \rightarrow X(z) = 1 \\
    y[n] = \varepsilon[n] \rightarrow Y(z) = \frac{z}{z - 1}
\end{align}$$

2.幂函数
$$\begin{align}
    x[n] = a^n\varepsilon[n] \rightarrow X(z) = \frac{z}{z - a}
\end{align}$$


3.反幂函数
$$\begin{align}
    x[n] = -a^n\varepsilon[- n- 1] \rightarrow X(z) = \frac{z}{z - a}
\end{align}$$

4.正余弦信号
$$\begin{align}
    x[n] = \cos w_0n \varepsilon[n] \rightarrow X(z) = \frac{z(z - \cos w_0)}{z^2 - 2z\cos w_0 + 1} \\
    y[n] = \sin w_0n \varepsilon \rightarrow Y(z) = \frac{z\sin w_0}{z^2 - 2z\cos w_0 + 1}
\end{align}$$

常用:
$$\begin{align}
    \cos \frac{\pi}{2}n \varepsilon[n] \rightarrow \frac{z^2}{z^2 + 1} \\
    \sin \frac{\pi}{2}n \varepsilon [n] \rightarrow \frac{z}{z^2 + 1}
\end{align}$$


5.幂函数与正余弦信号
因为 $a^nx[n] \rightarrow X(\frac{z}{a})$ ,则
$$\begin{align}
    x[n] = r^n\cos w_0n \varepsilon[n] \rightarrow X(z) = \frac{z(z - r\cos w_0)}{z^2 - 2zr\cos w_0 + r^2} \\
    y[n] = r^n\sin w_0n \varepsilon \rightarrow Y(z) = \frac{zr\sin w_0}{z^2 - 2zr\cos w_0 + r^2}
\end{align}$$

常用:
$$\begin{align}
    r^n\cos \frac{\pi}{2}n \varepsilon[n] \rightarrow \frac{z^2}{z^2 + r^2} \\
    r^n\sin \frac{\pi}{2}n \varepsilon[n] \rightarrow \frac{rz}{z^2 + r^2}
\end{align}$$