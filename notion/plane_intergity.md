

### 1.曲面面积

$$\begin{equation}
\begin{aligned}
        r = r(u,v)
\end{aligned}
\end{equation}$$

在点 $(u_0,v_0)$上的曲面面积微分为

$$\begin{equation}
\begin{aligned}
   dS =  \Vert r_u \times r_v \Vert du dv
\end{aligned}
\end{equation}$$

则曲面面积为

$$\begin{equation}
\begin{aligned}
    S = \iint_{ D } \Vert r_u \times r_v \Vert du dv
\end{aligned}
\end{equation}$$

(1)因为

$$\begin{equation}
\begin{aligned}
        r_u \times r_v = A\bm{i} +B\bm{j} + C \bm{k} 
\end{aligned}
\end{equation}$$


$$\begin{equation}
\begin{aligned}
        A = \frac{\partial(y,z)}{\partial(u,v)}
\end{aligned}
\end{equation}$$


$$\begin{equation}
\begin{aligned}
        B = \frac{\partial(z,x)}{\partial(u,v)}
\end{aligned}
\end{equation}$$


$$\begin{equation}
\begin{aligned}
        C = \frac{\partial(x,y)}{\partial(u,v)}
\end{aligned}
\end{equation}$$

所以


$$\begin{equation}
\begin{aligned}
    S = \iint_{ D } \sqrt{A^2 + B^2 + C^2} du dv
\end{aligned}
\end{equation}$$

(2)
有因为


$$\begin{equation}
\begin{aligned}
    \Vert r_u \times r_v \Vert^2 = \Vert r_u \Vert^2 \Vert r_v \Vert^2 - < r_u , r_v >^2
\end{aligned}
\end{equation}$$

令 $E = \Vert r_u \Vert^2 ,G = \Vert r_v \Vert^2 ,F =  \Vert r_u \Vert \Vert r_v \Vert $,则有


$$\begin{equation}
\begin{aligned}
    S = \iint_{ D } \sqrt{EG -F^2} du dv
\end{aligned}
\end{equation}$$


