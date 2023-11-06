
$$\begin{align}
    &\int^{\infty}_{-\infty} \int^{\infty}_{-\infty} h_1^{*}(u)h_2(v) \frac{N_0}{2}\delta(u+\tau - v) dudv \\
    &= \frac{N_0}{2}\int^{\infty}_{-\infty} \int^{\infty}_{-\infty} h_1^{*}(u)h_2(v) \delta\left\{-[v-(u+\tau)]\right\} dudv \\
\end{align}$$

由于单位冲激函数是一个偶函数 $\delta(-t) = \delta(t)$,上式就变为:

$$\begin{align}
    &= \frac{N_0}{2}\int^{\infty}_{-\infty} \int^{\infty}_{-\infty} h_1^{*}(u)h_2(v) \delta[(v-(u+\tau)] dudv \\
    &= \frac{N_0}{2}\int^{\infty}_{-\infty} h_1^{*}(u)du \int^{\infty}_{-\infty} h_2(v) \delta[v-(u+\tau)] dv \\
    &= \frac{N_0}{2}\int^{\infty}_{-\infty} h_1^{*}(u)du \int^{\infty}_{-\infty} h_2(u+\tau) \delta[v-(u+\tau)] dv \\
    &= \frac{N_0}{2}\int^{\infty}_{-\infty} h_1^{*}(u)h_2(u+\tau)du \int^{\infty}_{-\infty}  \delta[v-(u+\tau)] dv \\ 
    &=\frac{N_0}{2}\int^{\infty}_{-\infty} h_1^{*}(u)h_2(u+\tau)du
\end{align}$$




$$\begin{align}
    \displaystyle \frac{s^{-2} + 3 s^{-1}}{1 + \frac{3}{4}s^{-1} + \frac{1}{8}s^{-2}}
\end{align}$$



如果 $F[f(t)] = F(jw)$

$$\begin{align}
    F[f(t)e^{jw_0t}] &= F(j(w - w_0)) \\
    F[f(t)e^{w_0t}] &= F[f(t)e^{j(-jw_0)t}] = F[j(w +jw_0)]
\end{align}$$



$$\begin{align}
    p^2 = (\frac{dy}{dx})^2 \\
    \frac{dp}{dx} =  \frac{d^2 y}{dx^2}
\end{align}$$







解:

$$\begin{align}
    sgn[n] = 2u[n] - 1 - \delta[n] =\begin{cases}
        1 , n=1,2,3\cdots \\
        0 , n = 0 \\
        -1,n=-1,-2,-3\cdots
    \end{cases}
\end{align}$$

则

$$\begin{align}
    \Delta sgn[n] &= sgn[n+1] - sgn[n] \\
    &=2u[n+1] - 1  - \delta[n+1]- \{2u[n +] - 1 - \delta[n+]\} \\
    &=2u[n+1] - 2u[n+]  - \delta[n+1] +   \delta[n] \\
    &=2 \delta[n+1]- \delta[n+1] +   \delta[n-1] \\
    &=\delta[n] + \delta[n+1]
\end{align}$$



$$\begin{align}
    \triangle x[n] = x[n + 1] - x[n] \\
    \triangledown x[n] = x[n] - x[n-1]
\end{align}$$

已知

$$\begin{align}
    H(S) = \frac{s + 3 - K}{2K} \rightarrow h(t) = -\frac{1}{2K} \delta'(t) + \frac{3 - K}{2K} \delta(t)
\end{align}$$

得到 $h(t)$ 的傅里叶变换为,则输出

$$\begin{align}
    y(t) &= x(t) * h(t) \\
    &=-\frac{1}{2K} x'(t) + \frac{3 - K}{2K} x(t)
\end{align}$$

在 $x'(t)$ 在输出时会出现无限的情况,所以不稳定.

$$\begin{align}
    Y(z) = F(Z)[1 + a^1z^{-1} + a^2 z^{-2} + \cdots a^{M-1}z^{M-1}] \rightarrow \\ H(z) = \frac{Y(z)}{F(z)} = [1 + a^1z^{-1} + a^2 z^{-2} + \cdots a^{M-1}z^{M-1}]
\end{align}$$

得到

$$\begin{align}
    h[n] = \delta[n] + \sum_{i=1}^{M-1}a^i\delta[n-i]
\end{align}$$



