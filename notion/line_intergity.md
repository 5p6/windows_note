## 1.弧长

$$\begin{equation}
\begin{aligned}
        ds &= \Vert dr \Vert
    &=\sqrt{(dx)^2 + (dy)^2 + (dz)^2}
\end{aligned}
\end{equation}$$


$$\begin{equation}
\begin{aligned}
        s = \int_{\Gamma}\sqrt{(dx)^2 + (dy)^2 + (dz)^2} 
\end{aligned}
\end{equation}$$
如果 $x = x(t), y= y(t) ,z =z(t)$ ,则:

$$\begin{equation}
\begin{aligned}
    s(t) = s_0 + \int_{t_0}^{t} \sqrt{x^{'2}(t) + y^{'2}(t)  + z^{'2}(t)} dt
\end{aligned}
\end{equation}$$

## 2.弧长质量
假设在点 $p$ 处的质量为 $\rho(p)$,这里的 $p$ 可以是三维点或者二维点,可以定义第一类曲面积分

$$\begin{equation}
\begin{aligned}
        m = \int_{\Gamma}\rho(p) ds
\end{aligned}
\end{equation}$$


$$\begin{equation}
\begin{aligned}
        m = \int_{\Gamma} \rho(x(t),y(t))\sqrt{x^{'2}(t) + y^{'2}(t)} dt
\end{aligned}
\end{equation}$$

或者

$$\begin{equation}
\begin{aligned}
        m = \int_{\Gamma} \rho(x(t),y(t),z(t))\sqrt{x^{'2}(t) + y^{'2}(t) + z^{'2}(t)} dt
\end{aligned}
\end{equation}$$

例如:
(1)设曲线 $L:x^2+y^2=2x$下半周,求$\int_{L} \sqrt{x^2 + y^2} ds$


$$\begin{align}
    x &= 1 + \cos t \\
    y &= \sin t
\end{align}$$

则

$$\begin{align}
    \int_{L} \sqrt{x^2 + y^2} ds &= \int_{L} \sqrt{2x(t)} dt \\
    &= \int_{\pi}^{2\pi} \sqrt{2 + 2\cos t} dt \\
    & = \int_{\pi}^{2\pi} \sqrt{2(1 + 2 \cos^2 \frac{t}{2} - 1)} dt \\
    &= \int_{\pi}^{2\pi} 2 \cos \frac{t}{2} dt\\
    &=4 | \sin \frac{t}{2} |_{\pi}^{2\pi} |\\
    &= 4
\end{align}$$


(2)设曲线 $\Gamma: x^2 +y^2 +z^2 = 4,x+y+z=2$,求积分$\oint_{\Gamma} x^2 + z ds$


(2)设曲线 $\Gamma: x^2 +y^2 +z^2 = 4,x+y+z=2$,求积分$\oint_{\Gamma} x^2 + z ds$


(2)设曲线 $\Gamma: x^2 +y^2 +z^2 = 4,x+y+z=2$,求积分$\oint_{\Gamma} x^2 + z ds$

(2)设曲线 $\Gamma: x^2 +y^2 +z^2 = 4,x+y+z=2$,求积分 $\oint_{\Gamma} x^2 + z ds$



解:

$$\begin{align} 
    \oint_{\Gamma} x^2 + z ds &= \frac{1}{3} \oint_{\Gamma} x^2 +y^2 +z^2+x+y+z ds\\
    &= 2 \oint_{\Gamma} ds \\
    &= 4 \pi \sqrt{\frac{8}{3}}
\end{align}$$


## 3.场论曲线积分

假设有高维力场 $\vec{F} =\sum_{i=1}^{n} F_i\vec{e_{i}} $，沿着一条高维曲线路径 $\gamma$做功,其积分表达式可以写为

$$\begin{align}
    dW &= \vec{F} \cdot \vec{dx} \\
\end{align}$$

其中

$$\begin{align}
    \vec{dx} &= \sum_{i=1}^{n} \vec{e_i}dx_i 
\end{align}$$

对其积分得到

$$\begin{align}
    W &= \int_{\gamma} \vec{F} \cdot \vec{dx} \\
    &= \int_{\gamma} \sum_{i=1}^{n}F_i dx_i 
\end{align}$$

如果曲线是闭合的,那么情况比较特殊,把积分写为:

$$\begin{align}
    W &= \oint_{\gamma} \vec{F} \cdot \vec{dx}
\end{align}$$

上式就是广义第二型曲线积分,一般都是在二维平面或者三维空间讨论它:

$$\begin{align}
    W &= \int_{\gamma} F_1dx + F_2dy \\
    W &= \int_{\gamma} F_1dx + F_2dy + F_3dz
\end{align}$$

利用广义斯托克斯定理有:

$$\begin{align}
    W &= \oint_{\gamma} F_1dx + F_2dy \\
    &=\iint_{D} (\frac{\partial F_2}{\partial x} - \frac{\partial F_1}{\partial y} )dxdy \\
    W &= \oint_{\gamma} F_1dx + F_2dy + F_3dz \\
    &= \iint_{D} (\frac{\partial F_2}{\partial x} -\frac{\partial F_1}{\partial y})dxdy +(\frac{\partial F_3}{\partial y} -\frac{\partial F_2}{\partial z})dydz +(\frac{\partial F_1}{\partial z} -\frac{\partial F_3}{\partial y})dzdx 
\end{align}$$

例题:
1.设曲线为$\Gamma:x^2+y^2 = 1$的正向圆周,求积分$\oint_{\Gamma} (2xy - 2y)dx + (x^2 - 4x)dy$
解:
直接使用斯托克斯公式,得到积分区域 $D:x^2+y^2 \leq 1$

$$\begin{align}
    \oint_{\Gamma} (2xy - 2y)dx + (x^2 - 4x)dy  &= \iint_{D} (2x - 4  + 2 -2x) dxdy \\
    &= -2\iint_{D}dxdy \\
    &=-2\pi
\end{align}$$

2.设曲线为$\Gamma:(x-1)^2+y^2 = 4$的正向圆周,求积分$\oint_{\Gamma} \frac{ydx - xdy}{x^2 + 4y^2}$
解:
这里使用挖洞法，再使用斯托克斯公式,令

$$\begin{align}
    x = \xi \cos t , y = \frac{\xi}{2} \sin t
    ,(\xi \rightarrow 0)
\end{align}$$


$(0,0)$处挖一个

$$\begin{align}
    x^2 + 4y^2 = \xi^2,\xi \rightarrow 0
\end{align}$$

同时令曲线 $\Gamma_1:x^2 + 4y^2 = \xi^2$沿顺时针方向,则有

$$\begin{align}
    \oint_{\Gamma} = \oint_{\Gamma + \Gamma_1} - \oint_{\Gamma_1}
\end{align}$$

即:

$$\begin{align}
    \oint_{\Gamma} \frac{ydx - xdy}{x^2 + 4y^2} = \oint_{\Gamma + \Gamma_1}\frac{ydx - xdy}{x^2 + 4y^2} - \oint_{\Gamma_1}\frac{ydx - xdy}{x^2 + 4y^2}
\end{align}$$

在$\Gamma + \Gamma_1$上可以使用斯托克斯公式,

$$\begin{align}
    \oint_{\Gamma + \Gamma_1}\frac{ydx - xdy}{x^2 + 4y^2} &= \iint_{D}[ \frac{x^2 - 4y^2}{(x^2 + 4y^2)^2} - \frac{x^2 - 4y^2}{(x^2 + 4y^2)^2} ]dxdy \\
    &=0
\end{align}$$

在第二条积分上为:

$$\begin{align}
    \oint_{\Gamma_1} \frac{ydx - xdy}{x^2 + 4y^2} &= \oint_{\Gamma_1} \frac{ydx - xdy}{\xi^2} \\
    &= \frac{1}{\xi^{2}} \iint_{D} -2dxdy
\end{align}$$

其中 $D:x^2+4y^2\leq \xi^2$,那么(39)式变为

$$\begin{align}
    &=\frac{1}{\xi^{2}} \iint_{D} -2dxdy \\
    &=\frac{1}{\xi^{2}} * -2*\pi ab \\
    &(\frac{x^2}{\xi^2} + \frac{y^2}{(\frac{\xi}{2})^2} =1 \rightsquigarrow a = \xi , b= \frac{\xi}{2}) \\
    &= -\pi
\end{align}$$


