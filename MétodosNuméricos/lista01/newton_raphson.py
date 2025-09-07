import math

def residuo_abs(fx):
    return abs(fx)



def desvio_abs(x,x0):
    return (abs(x-x0))


def newton_raphson(f, dx, x0, tol=1e-09, maxit=1000):
    x = x0
    fx = f(x)
    i = 0

    #if (abs(fx) < tol):
        #return x
    #print("Iteração= ", i, " x= ", x, " fx= ", fx)
    print(f"d)Residuo {residuo_abs(fx)}")
    while (abs(fx) > tol and i < maxit):
        fdx = dx(x)
        x_0 = x
        x = x - (fx/fdx)
        fx = f(x)
        i += 1
        if abs(fx) < tol:
            break
        print("\nIteração= ", i, "; x= ", x, " fx= ", fx, " dx= ", fdx)
        print(f"d)Residuo {residuo_abs(fx)}, Desvio: {desvio_abs(x,x_0)}")

    return x


f = lambda x: x + 3 * (math.e **(-x**2)) - 2 
dx = lambda x: 1 - 6 * x * (math.e**(-x**2))
print("3a)Para x = -1:")
xa = newton_raphson(f=f,dx=dx,x0=-1)

print("-"*80,"\n\n3b)Para x = 0.3:")
xb = newton_raphson(f=f,dx=dx,x0=0.3)
