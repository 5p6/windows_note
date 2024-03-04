### 1.残留边带调制
其定义式为
$$\begin{align}
    S_{VSB}(f) &= S_{DSB}(f)H_{VSB}(f) \\
    &=\frac{1}{2}[M(f + f_c) + M(f - f_c)]H_{VSB}(f)
\end{align}$$

通过解调器的乘法输出后有
$$\begin{align}
    Y_{VSB}(f) &= S_{VSB}(f + f_c) + S_{VSB}(f - f_c) \\
    &=\frac{1}{2}[M(f + 2f_c) + M(f )]H_{VSB}(f + f_c) + \frac{1}{2}[M(f ) + M(f - 2f_c)]H_{VSB}(f - f_c) \\
    &=\frac{1}{2}M(f)[H_{VSB}(f + f_c) + H_{VSB}(f - f_c)] +\\ 
    & \{\frac{1}{2}M(f + 2f_c)H_{VSB}(f + f_c) + M(f - 2f_c)H_{VSB}(f - f_c)\} 
\end{align}$$

通过低通滤波器滤除高频分量,得到信号
$$\begin{align}
    Y_{VSB}(f) &= \frac{1}{2}M(f)[H_{VSB}(f + f_c) + H_{VSB}(f - f_c)]
\end{align}$$

只要 $H_{VSB}(f + f_c) + H_{VSB}(f - f_c) = C, |f| \leq f_H$ ,那么输出将是一个完整的波形. 