### t分布
##### 1.正态分布
##### 2.卡方分布

##### 3.t分布
设 $\xi \sim N(0,1) , \eta \sim \chi^2(n)$ ,且相互独立,求 $\zeta = \frac{\xi}{\sqrt{n/n}}$ 的分布.
解:
1.
设 $\varphi = \sqrt{\eta / n}$ ,则:

$$\begin{align}
    P\{\varphi \leq y\}  =  P\{\sqrt{\eta / n} \leq y\}
\end{align}$$

讨论:
1.$x<0$ ,$F_\varphi(y) = 0$
2.$x\geq 0$ 时

$$\begin{align}
    P\{\varphi \leq y\}  &=  P\{\sqrt{\eta / n} \leq y\}\\
    &=P\{\eta  \leq ny^2\} \\
    &=\int^{ny^2}_0 \frac{x^{\frac{n}{2}-1}}{\Gamma(\frac{n}{2})2^{\frac{n}{2}}} e^{-\frac{x}{2}} dx
\end{align}$$

两边对 $y$ 求导,得到密度函数则有:

$$\begin{align}
    f_\varphi(y) &= 2ny\frac{(ny^2)^{\frac{n}{2}-1}}{\Gamma(\frac{n}{2})2^{\frac{n}{2}}} e^{-\frac{ny^2}{2}} \\
    &=\frac{2(\frac{n}{2})^{\frac{n}{2}}}{\Gamma(\frac{n}{2})} y^{n-1}e^{-\frac{ny^2}{2}}
\end{align}$$

得到:

$$\begin{align}
    f_\varphi(y) = \begin{cases}
        \displaystyle \frac{2(\frac{n}{2})^{\frac{n}{2}}}{\Gamma(\frac{n}{2})} y^{n-1}e^{-\frac{ny^2}{2}} , y\geq 0\\
        0,else
    \end{cases}
\end{align}$$

2.已知 $\xi , \eta$ 相互独立,则 $\xi ,\varphi$ 相互独立 $f_{\xi,\varphi}(x,y) = f_\xi(x)f_\varphi(y)$ 则有:

$$\begin{align}
    f_{\xi,\varphi}(x,y) = \begin{cases}
        \displaystyle \frac{2(\frac{n}{2})^{\frac{n}{2}}}{\Gamma(\frac{n}{2})} y^{n-1}e^{-\frac{ny^2}{2}} \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}, y\geq 0\\
        0,else
    \end{cases}
\end{align}$$


因为 $\zeta = \frac{\xi}{\eta}$ ,则有

$$\begin{align}
    f_\zeta(z) &= \int^{+\infty}_{-\infty} |x| f_{\xi,\varphi}(zx,x) dx \\
    &=\int^{+\infty}_{-\infty} |x|\frac{2(\frac{n}{2})^{\frac{n}{2}}}{\Gamma(\frac{n}{2})} x^{n-1}e^{-\frac{nx^2}{2}} \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2x^2}{2}}dx \\
    &=\int^{+\infty}_{0} \frac{2(\frac{n}{2})^{\frac{n}{2}}}{\sqrt{2\pi}\Gamma(\frac{n}{2})} x^ne^{-\frac{(y^2 + n)x^2}{2}}  dx
\end{align}$$

令 $x^2(y^2 + n) = t$ ,则

$$\begin{cases}
    x = \sqrt{\frac{t}{y^2 + n}} \\
    dx = \frac{1}{2\sqrt{y^2+n}} \frac{1}{\sqrt{t}} dt
\end{cases}$$

则

$$\begin{align}
    f_\zeta(z) &=\int^{+\infty}_{0} \frac{2(\frac{n}{2})^{\frac{n}{2}}}{\sqrt{2\pi}\Gamma(\frac{n}{2})} (\sqrt{\frac{t}{y^2 + n}})^ne^{-\frac{t}{2}}  \frac{1}{2\sqrt{y^2+n}} \frac{1}{\sqrt{t}} dt \\
    &=\frac{(\frac{n}{2})^{\frac{n}{2}}}{\sqrt{2\pi}\Gamma(\frac{n}{2})}  (y^2 + n)^{\frac{-n-1}{2}} \int^{+\infty}_{0} t^{\frac{n-1}{2}}e^{-\frac{t}{2}}dt \\
    &=\frac{(\frac{n}{2})^{\frac{n}{2}}}{\sqrt{2\pi}\Gamma(\frac{n}{2})}  (y^2 + n)^{-\frac{n+1}{2}} \int^{+\infty}_{0} t^{\frac{n+1}{2} - 1}e^{-\frac{t}{2}}dt \\
    &=\frac{\Gamma(\frac{n+1}{2})}{\sqrt{n\pi}\Gamma(\frac{n}{2})}  (\frac{y^2}{n} + 1)^{-\frac{n+1}{2}}
\end{align}$$

分布函数服从 $(15)$ 式的随机变量被称为服从自由度为 $n$ 的 $t$ 分布随机变量.

##### 4. $t$ 分布与 $F$ 分布
设随机变量 $\eta \thicksim N(0,1) , \chi \thicksim \chi^2(n)$ ,则有

$$\begin{align}
    \xi = \frac{\eta}{\sqrt{\chi/n}} \thicksim t(n) 
\end{align}$$

同时上式蕴含着

$$\begin{align}
    t^2 = \frac{\eta^2}{\chi/n} \thicksim F(1,n)
\end{align}$$
