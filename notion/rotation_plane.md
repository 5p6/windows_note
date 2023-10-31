## 旋转曲面面积

假设有一条曲线 $y = f(x)$ ,求:
1. 绕x轴旋转后的旋转体体积
2. 绕y轴旋转后的旋转体体积
3. 绕x轴旋转后的曲面的面积.
4. 绕y轴旋转后的曲面的面积.

### 问题1，3
!["fx"](4.1)
可以看到这个曲线绕x轴旋转后的旋转体,这里在 $[x,x + dx]$ ➗取微分量，做一个曲型圆柱体.
!["dV或者dS](4.2)

$f(x)$在问题**1**中有使用;$f(x),ds$在问题**3**中有使用

#### 1
取体积微元为柱体积微元,则

$$\begin{equation}
    \begin{aligned}
        dV = S(h)dh
    \end{aligned}
\end{equation}$$

如果以$x$为高,那么有

$$\begin{equation}
    \begin{aligned}
        dV &= \pi f^{2}(x)dx 
    \end{aligned}
\end{equation}$$


$$\begin{equation}
    \begin{aligned}
         V &= \int_{\alpha}^{\beta} \pi f^{2}(x) dx
    \end{aligned}
\end{equation}$$

#### 3.
由于曲面在 $x$ 处有倾斜,所以我们这里采用弧长微元来算面积,同样也取柱形

$$\begin{equation}
    \begin{aligned}
        dS &= 2 \pi |f(x)|ds 
    \end{aligned}
\end{equation}$$

积分

$$\begin{equation}
    \begin{aligned}
        S &= \int_{\alpha}^{\beta} 2 \pi |f(x)|ds 
    \end{aligned}
\end{equation}$$

因为

$$\begin{equation}
    \begin{aligned}
        ds = \sqrt{(dx)^2 + (dy)^2}
    \end{aligned}
\end{equation}$$

则

$$\begin{equation}
    \begin{aligned}
        S &= \int_{\alpha}^{\beta} 2 \pi |f(x)|\sqrt{(dx)^2 + (dy)^2}
    \end{aligned}
\end{equation}$$

附注:
>问题2，4其实也是和问题1,3一样的处理,只是绕x周的旋转体变为了绕y旋转的旋转体而已.
