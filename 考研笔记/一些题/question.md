
$$\begin{align}
    \int^{\frac{1}{2}}_{-\frac{1}{2}} 2\cos (2\pi t + \theta) e^{-j2\pi nt} dt
\end{align}$$

因为:

$$\begin{align}
    \cos (2\pi t + \theta) = \frac{e^{j(2\pi t + \theta)} + e^{-j(2\pi t + \theta)}}{2}
\end{align}$$

所以式 $(1)$ 转换为:

$$\begin{align}
    \int^{\frac{1}{2}}_{-\frac{1}{2}} 2\cos (2\pi t + \theta) e^{-j2\pi nt} dt &= \int^{\frac{1}{2}}_{-\frac{1}{2}} [e^{j(2\pi t + \theta)} + e^{-j(2\pi t + \theta)}] e^{-j2\pi nt} dt \\
    &= \int^{\frac{1}{2}}_{-\frac{1}{2}} e^{j(2\pi t + \theta - 2\pi nt)} + e^{-j(2\pi t + \theta + 2\pi nt)} dt \\
    &= e^{j\theta}\int^{\frac{1}{2}}_{-\frac{1}{2}} e^{j2\pi t(1 - n)} dt + e^{-j\theta} \int^{\frac{1}{2}}_{-\frac{1}{2}} e^{-j2\pi t(1 + n)} dt \\
    &= e^{j\theta}\frac{1}{j2\pi(1-n)} \int^{\frac{1}{2}}_{-\frac{1}{2}}e^{j2\pi t(1 - n)} d[j2\pi t(1 - n)] + e^{-j\theta}\frac{1}{-j2\pi(1+n)} \int^{\frac{1}{2}}_{-\frac{1}{2}}e^{-j2\pi t(1 + n)} d[-j2\pi t(1 + n)] \\
    &= \frac{e^{j\th eta}}{j2\pi(1-n)} e^{j2\pi t(1 - n)}|^{\frac{1}{2}}_{-\frac{1}{2}} + \frac{e^{-j\theta}}{-j2\pi(1+n)}e^{-j2\pi t(1 + n)}|^{\frac{1}{2}}_{-\frac{1}{2}} \\
    &=\frac{e^{j\theta}}{j2\pi(1-n)} (e^{j\pi (1-n)} - e^{-j\pi(1-n)}) + \frac{e^{-j\theta}}{-j2\pi(1+n)} (e^{-j\pi (1+n)} - e^{j\pi(1+n) }) \\
\end{align}$$


因为 

$$\begin{align}
    \sin \theta  = \frac{1}{2j}(e^{j\theta} - e^{-j\theta})  \rightarrow e^{j\theta} - e^{-j\theta} = 2j \sin \theta
\end{align}$$

所以式 $(8)$ 有:

$$\begin{align}
    &= \frac{e^{j\theta}}{j2\pi(1-n)} * 2j\sin(\pi(1-n)) + \frac{e^{-j\theta}}{-j2\pi(1+n)}*(-2j \sin(\pi(1+n))) \\
    &= \frac{e^{j\theta}\sin(\pi(1-n))}{\pi(1 - n)} + \frac{e^{-j\theta} \sin(\pi(1+n))}{\pi(1+n)}
\end{align}$$







