def residuo_abs(fx,x0):
    return abs(fx(x0))

def bissecao(fx,xl,xu,tol,maxit=100):
    fl = fx(xl)
    fu = fx(xu)

    if abs(fl) < tol:
        return xl
    if abs(fu) < tol:
        return xu
    
    if (fl*fu) > 0:
        print("Sem Garantia de Zeros na Função")
        return

    xm = (xl+xu)/2
    fm = fx(xm)
    i = 0 
    residuo = residuo_abs(fx,xm)
    print("Residuo: ",residuo)

    while (residuo > tol and i < maxit):
        if fl * fm > 0:
            xl = xm
            fl = fm
        else: 
            xu = xm
            fu = fm
        xm = (xl+xu)/2
        fm = fx(xm)
        residuo = residuo_abs(fx,xm)
        i += 1
        print("Residuo: ",residuo)

    print("Quantidade de Iterações: ",i+1)
    return xm   

x = bissecao(fx=lambda x: x**3 + 2,xl=-2,xu=1,tol=0.2)
print("Valor de x: ",x)