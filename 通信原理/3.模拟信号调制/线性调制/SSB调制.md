### 1.调制原理
双边带调制的频谱是对称的,是否可以通过去除一个边带,仅用单个边带传输,单边带传输信号可以写为
$$\begin{align}
    S_{SSB}(f) &= S_{DSB}(f)H_{SSB}(f) \\
    &=\frac{1}{2}[M(f + f_c) + M(f - f_c)]H_{SSB}(f)
\end{align}$$

其中 $H_{SSB}(f)$ 是一个低通滤波器(下边带 $H_{LSB}(f)$ )或者高通滤波器(上边带 $H_{USB}(f)$),两者的分析方式是一致的,这里我们仅仅讨论上边带调制方法
$$\begin{align}
    H_{USB}(f) = u(f - f_c) + u(-f - f_c)
\end{align}$$

其中 $u(*)$ 是一个阶跃函数,上边带的傅里叶变换为
$$\begin{align}
    S_{USB}(f) &= \frac{1}{2}[M(f + f_c) + M(f - f_c)][u(f - f_c) + u(-f - f_c)] \\
    &=\frac{1}{2}M(f + f_c)u(-f - f_c) + \frac{1}{2}M(f - f_c)u(f - f_c)
\end{align}$$

因为时频对称原理有
$$\begin{align}
    u(f) \rightarrow \frac{1}{2}\delta(t) + \frac{j}{2\pi t},u(-f) \rightarrow \frac{1}{2}\delta(t) + \frac{1}{j2\pi t}
\end{align}$$

已知希尔伯特变换有
$$\begin{align}
    \hat{m}(t) &= \frac{1}{\pi}\int^{+\infty}_{-\infty} \frac{m(\tau)}{t - \tau} d\tau = m(t) * \frac{1}{\pi t}
\end{align}$$

则
$$\begin{align}
    s_{USB}(t) &= \frac{1}{2}[m(t) * [\frac{1}{2}\delta(t) + \frac{1}{j2\pi t}]]e^{-j2\pi f_ct} + \frac{1}{2}[m(t) * [\frac{1}{2}\delta(f) + \frac{j}{2\pi f}]] e^{j2\pi f_ct} \\
    &=\frac{1}{4}[m(t) + \frac{\hat{m}(t)}{j}]e^{-j2\pi f_ct} + \frac{1}{4}[m(t) + j\hat{m}(t)]e^{j2\pi f_ct} \\
    &=\frac{m(t)(e^{j2\pi f_ct} + e^{-j2\pi f_c})}{4} - \frac{\hat{m}(t)(e^{j2\pi f_ct} - e^{-j2\pi f_ct}))}{4j} \\
    &=\frac{1}{2}[m(t) \cos(2\pi f_c t) - \hat{m}(t)\sin(2\pi f_c t)]
\end{align}$$

由于 $s_{DSB}(t) = s_{USB}(t) + s_{LSB}(t)$ ,则
$$\begin{align}
    s_{LSB}(t) = \frac{1}{2}[m(t) \cos(2\pi f_c t) + \hat{m}(t)\sin(2\pi f_c t)]
\end{align}$$

单边带的带宽为 $B_{SSB} = \frac{1}{2}B_{DSB} = f_H$ , 最后有功率为
$$\begin{align}
    P_{SSB} = \frac{1}{2}P_{DSB} = \frac{\bar{m^2(t)}}{4}
\end{align}$$