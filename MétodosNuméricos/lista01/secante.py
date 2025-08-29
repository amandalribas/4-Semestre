import math


def residuo_abs(fx):
    return abs(fx)

def desvio_abs(x,x0):
    return (abs(x-x0))

def dx_convencional(xl,xu,f):
    return (f(xl)-f(xu))/(xl-xu)

def dx_centrada(x,delta,f):
    return (f(x+delta)-f(x-delta))/(2*delta)

def metodo_secante(x0,x1,f,tol=1e-06,maxit=1000):
    xl = x0
    fl = f(xl)
    if (abs(fl) < tol):
        return xl
    
    xu = x1
    fu = f(xu)
    if (abs(fu) < tol): 
        return xu
    
    x = (xu+xl)/2
    fx = f(x)

    i = 0
    print(f"Iteração={i}, x={x}, fx={fx}")
    
    print(f"Residuo {residuo_abs(fx)}, Desvio: {desvio_abs(xu,xl)}")

    while (abs(fx) > tol and i < maxit):
        dx = dx_convencional(xl,xu,f)
        x = x - (fx/dx)
        fx = f(x)
        i += 1
        print(f"\nIteração={i}, x={x}, fx={fx}")
        print(f"Residuo {residuo_abs(fx)}, Desvio: {desvio_abs(xu,xl)}")
        xl, xu = xu, x 
    return x



def metodo_secante_centrada(x0,delta,f,tol=1e-06,maxit=1000):
    x = x0
    fx = f(x)
    if (abs(fx) < tol):
        return x

    i = 0
    print("Iteração= ", i, " x= ", x, " fx= ", fx)
    print(f"Residuo {residuo_abs(fx)}")

    while (abs(fx) > tol and i < maxit):
        dx = dx_centrada(x,delta,f)
        x_0 = x
        x = x - (fx/dx)
        fx = f(x)
        i += 1
        print("\nIteração= ", i, " x= ", x, " fx= ", fx)
        print(f"Residuo {residuo_abs(fx)}, Desvio: {desvio_abs(x,x0)}")

    return x




f = lambda x: x - 5 * (math.e**(-x**2)) + 4 
print("a)Empregando a aproximação da derivada 'convencional':")
x = metodo_secante(x0=-1.4,x1=1.5,f=f)

print("\nb)Empregando a aproximação da derivada baseada em diferenças centradas:")
x = metodo_secante_centrada(x0=2.0,delta=0.01,f=f)