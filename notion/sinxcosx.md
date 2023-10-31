## 1.R(-sinx,cosx) = -R(sinx,cosx)

方法 : 凑 $d\cos x,u=\cos x$ 
示例:

$$\begin{aligned}
    \int \frac{dx}{\sin 2x + 2 \sin x}  
    &= \int \frac{dx}{2\sin x \cos x + 2 \sin x} \\
    &= \int \frac{\sin x dx}{ 2 \sin^2 x (\cos x + 1)} \\
    & =\int \frac{-d\cos x}{ 2 (1 - \cos^2 x) (\cos x + 1)} \\
    &= -\int \frac{du}{ 2 (1 - u^2) (u + 1)} \\
    &= \int \frac{du}{ 2 (u - 1) (u + 1)^2} \\
    &= \frac{1}{4}\int \frac{1-u + 1+u}{(u - 1) (u + 1)^2} du \\
    &=\frac{1}{4}\int \frac{1}{u^2 - 1}  - \frac{1}{(u + 1)^2} du \\
    & = \frac{1}{8}[\ln \frac{u - 1}{u + 1} + \frac{2}{u+1}] + C
\end{aligned}$$

## 2.R(sinx,-cosx) = -R(sinx,cosx)
方法 : 凑 $d\sin x,u=\sin x$ 


## 3.R(-sinx,-cosx) = R(sinx,cosx)
方法 : 凑 $d\tan x,u=\tan x$ 

## 4.凑不出来了
万能代换

$$\begin{aligned}
    t = tan \frac{x}{2}
\end{aligned}$$

## 5.特殊类型

$$\begin{aligned}
    \int \frac{1}{1 + \sin x} dx
    &= \int \frac{1 - \sin x}{\cos^{2}x} dx \\
    &= \int \sec^2 x dx + \int \frac{d\cos x}{\cos^2 x} \\
    &=\tan x - \frac{1}{\cos x} +C
\end{aligned}$$





