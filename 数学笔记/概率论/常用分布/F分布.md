### F分布
##### 1.伽马分布
随机变量 $\xi$ 服从参数为 $(\alpha,\lambda)$ 的伽马分布, $\xi \thicksim \Gamma(\alpha,\lambda)$ ,其密度函数为

$$\begin{align}
    f_\xi(x) = \begin{cases}
        \displaystyle \frac{\lambda^{\alpha}}{\Gamma(\alpha)}x^{\alpha - 1}e^{-\lambda x},x\geq 0 \\
        0 , x <0
    \end{cases}
\end{align}$$

##### 2.卡方分布
自由度为 $n$ 的卡方分布, $\xi \thicksim \chi^2(n) \thicksim \Gamma(\frac{n}{2},\frac{1}{2})$ ,密度函数为:

$$\begin{align}
    f_\xi(x) \begin{cases}
        \displaystyle \frac{1}{2^{\frac{n}{2}}\Gamma(\frac{n}{2})} x^{\frac{n}{2} - 1}e^{-\frac{x}{2}},x \geq 0 \\
        0,x <0 
    \end{cases}
\end{align}$$

##### 3.已知 $\xi,\eta$ 相互独立,分别服从自由度为 $n$ 和 $m$ 的$\chi^2$ 分布,求 $\zeta = \frac{\xi / n}{ \eta / m}$ 的密度函数.  
解：
1.先求分子分母的密度函数:

$$\begin{align}
    P\left\{\frac{\xi}{n} \leq x\right\} &= P\left\{\xi \leq nx\right\} \\
    &= \int^{nx}_{-\infty} f_\xi(\tau) d\tau 
\end{align}$$

两边对 $x$ 求导得到分布函数为 $nf_{\xi}(nx)$ ,即为:

$$\begin{align}
    f_{\frac{\xi}{n}}(x) \begin{cases}
        \displaystyle \frac{n}{2^{\frac{n}{2}}\Gamma(\frac{n}{2})} (nx)^{\frac{n}{2} - 1}e^{-\frac{nx}{2}},x \geq 0 \\
        0,x <0 
    \end{cases}
\end{align}$$

同理有:

$$\begin{align}
    f_{\frac{\eta}{m}}(x) \begin{cases}
        \displaystyle \frac{m}{2^{\frac{m}{2}}\Gamma(\frac{m}{2})} (mx)^{\frac{m}{2} - 1}e^{-\frac{mx}{2}},x \geq 0 \\
        0,x <0 
    \end{cases}
\end{align}$$

商之间的密度函数为:

$$\begin{align}
    f_\zeta(y) &= \int^{+\infty}_0|x|p(yx,x)dx \\
    &= \int^{+\infty}_0|x| \frac{n}{2^{\frac{n}{2}}\Gamma(\frac{n}{2})} (nyx)^{\frac{n}{2} - 1}e^{-\frac{nyx}{2}}\frac{m}{2^{\frac{m}{2}}\Gamma(\frac{m}{2})} (mx)^{\frac{m}{2} - 1}e^{-\frac{mx}{2}}dx \\
    &=\frac{n^{\frac{n}{2}}m^{\frac{m}{2}}}{2^{\frac{n}{2} + \frac{m}{2}}\Gamma(\frac{n}{2})\Gamma(\frac{m}{2})}y^{\frac{n}{2} - 1}\int^{+\infty}_0x^{\frac{n}{2} + \frac{m}{2} - 1}e^{-\frac{mx + nxy}{2}} dx
\end{align}$$

令 $x(ny+m) = t \rightarrow dx = \frac{dt}{ny + m}$ ,得到:

$$\begin{align}
    \int^{+\infty}_0x^{\frac{n}{2} + \frac{m}{2} - 1}e^{-\frac{mx + nxy}{2}} dx &= \int^{{+\infty}}(\frac{t}{ny+m})^{\frac{n+m}{2} - 1} e^{-t} \frac{1}{ny + m} dt  \\
    &= \frac{1}{(ny+m)^{\frac{n+m}{2}}} \int^{+\infty}_0t^{\frac{n+m}{2}-1}e^{-t} dt
\end{align}$$

带回原式有:

$$\begin{align}
   &\frac{n^{\frac{n}{2}}m^{\frac{m}{2}}}{2^{\frac{n}{2} + \frac{m}{2}}\Gamma(\frac{n}{2})\Gamma(\frac{m}{2})}y^{\frac{n}{2} - 1}\int^{+\infty}_0x^{\frac{n}{2} + \frac{m}{2} - 1}e^{-\frac{mx + nxy}{2}} dx \\
   &=\frac{n^{\frac{n}{2}}m^{\frac{m}{2}}}{2^{\frac{n}{2} + \frac{m}{2}}\Gamma(\frac{n}{2})\Gamma(\frac{m}{2})}y^{\frac{n}{2} - 1}\frac{1}{(ny+m)^{\frac{n+m}{2}}} \int^{+\infty}_0t^{\frac{n+m-1}{2}}e^{-\frac{t}{2}} dt \\
   &= \frac{\Gamma(\frac{n+m}{2})}{\Gamma(\frac{n}{2})\Gamma(\frac{m}{2})} n^{\frac{n}{2}}m^{\frac{m}{2}}\frac{y^{\frac{n}{2} - 1}}{(ny+m)^{\frac{n+m}{2}}}\frac{1}{2^{\frac{m+n}{2}}\Gamma(\frac{n+m}{2})}\int^{+\infty}_0t^{\frac{n+m}{2}-1}e^{-\frac{t}{2}} dt \\
   &=\frac{\Gamma(\frac{n+m}{2})}{\Gamma(\frac{n}{2})\Gamma(\frac{m}{2})} n^{\frac{n}{2}}m^{\frac{m}{2}}\frac{y^{\frac{n}{2} - 1}}{(ny+m)^{\frac{n+m}{2}}}
\end{align}$$


注意:

$$\begin{align}
    \frac{1}{2^{\frac{m+n}{2}}\Gamma(\frac{n+m}{2})}\int^{+\infty}_0t^{\frac{n+m}{2}-1}e^{-\frac{t}{2}} dt = 1
\end{align}$$

因为它恰好为自由度为 $\frac{m+n}{2}$ 的 $\chi^2$ 分布的积分.

以 $(15)$ 式为密度函数的分布称为参数为 $n,m$ 的 $F$ 分布,记为 $F(n,m)$.$F$ 分布的本质是描述了两个正态分布的方差是否相等的问题.

$$\begin{align}
    f_\zeta(x) = \begin{cases}
        \displaystyle \frac{\Gamma(\frac{n+m}{2})}{\Gamma(\frac{n}{2})\Gamma(\frac{m}{2})} n^{\frac{n}{2}}m^{\frac{m}{2}}\frac{y^{\frac{n}{2} - 1}}{(ny+m)^{\frac{n+m}{2}}} , x\geq 0 \\
        0 , else
    \end{cases}
\end{align}$$

