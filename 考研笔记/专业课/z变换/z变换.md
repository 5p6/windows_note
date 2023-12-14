### 1.Z变换
由于
$$\begin{align}
    X(e^{jw}) = \sum x[n]e^{-jwn}
\end{align}$$

在有时时不满足可积条件,我们可以引入 $z = r^{n}e^{jwn}$ ,则
$$\begin{align}
    X(z) &= \sum x[n]z^{-n} \\
    &=\sum (x[n]r^{-n} )e^{-jwn}
\end{align}$$

就是在算 $y[n] = x[n]r^{-n}$ 的离散傅里叶变换,则我们可以调节 $r$ 使得 $y[n]$ 满足可积条件,而满足可积条件的所有 $r$ 组成的集合,就称为 $X(z)$ 的收敛域.

### 2.性质
1.线性
$$\begin{align}
    Z\{a_1x_1[n] + a_2x_2[n]\} = a_1X_1(x) + a_2X_2(z)
\end{align}$$

2.时移
$$\begin{align}
    Z\{x[n - n_0]\} = X(z)z^{-n_0} 
\end{align}$$

3.伸缩
$$\begin{align}
    Z\{z_0^{n}x[n]\} = X(\frac{z}{z_0})
\end{align}$$

该性质在计算 $r^nx[n]$ 时非常有用,例如 $r^n\cos w_0 n \varepsilon[n]$ .

4.线性加权
$$\begin{align}
    Z\{nx[n]\} = -z\frac{dX(z)}{dz}
\end{align}$$

5.初值定理
因为
$$\begin{align}
    X(z) = x[0] + x[1]z^{-1} + \cdots
\end{align}$$

则
$$\begin{align}
    x[0] = \lim_{z\rightarrow\infty} X(z)
\end{align}$$

6.终值定理
$$\begin{align}
    x(\infty) = \lim_{z\rightarrow 1} (z - 1)X(z)
\end{align}$$

7.反折
$$\begin{align}
    Z\{x[n]\} = X(\frac{1}{z})
\end{align}$$

8.共轭
$$\begin{align}
    Z\{x^{*}[n]\} = X^{*}(z^{*})
\end{align}$$


其中 $x[n]$ 必须是一个收敛的序列,也就是 $X(z)$ 的收敛域包括单位圆.

在上述性质中,并没有讨论他们的收敛域的变化,在做题的时候是要注意的.