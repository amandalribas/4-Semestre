import math


def residuo_abs(fx):
    return abs(fx)

def desvio_abs(x,x0):
    return (abs(x-x0))

def dx_convencional(xl,xu,f):
    return (f(xl)-f(xu))/(xl-xu)

def dx_centrada(x,delta,f):
    return (f(x+delta)-f(x-delta))/(2*delta)


def secante_convencional(f, x_anterior,  x_atual, tol=1e-08, maxit=1000):
    x = x_atual
    x_ant = x_anterior
    
    fx = f(x)
    fx_ant = f(x_ant)
    
    if (fx < tol): 
        return x
    #dx = (fx-fx_ant)/(x-x_ant)
    i = 0

    #print("\nIteração= ", i, "; x= ", x, " fx= ", fx)
    print(f"Residuo {residuo_abs(fx)}")
    while (abs(fx) > tol and i < maxit):
        print(f"Iteração={i}; x={x}; fx={fx}")
        
        aux = x
        dx = (fx-fx_ant)/(x-x_ant)
        #x = x - ((fx*(x-x_ant))/(fx-fx_ant))
        x = x - (fx/dx)
        x_ant = aux

        fx = f(x)
        fx_ant = f(x_ant)
        i += 1

        #if abs(fx) < tol:
            #return x
        print(f"\nDesvio: {desvio_abs(x,x_ant)}; Residuo: {residuo_abs(fx)},")

    return x


def secante_dif_centrada(f, x, delta, tol=1e-03, maxit=1000):
    fx = f(x)
    if (fx < tol): 
        return x
    i = 0

    print(f"Residuo {residuo_abs(fx)}")
    while (abs(fx) > tol and i < maxit):
        print(f"Iteração={i}; x={x}; fx={fx}")
        x_ant = x
        dx = (f(x + delta) - f(x - delta))/(2*delta)
        x = x - (fx/dx)
        fx = f(x)

        i+= 1
        print(f"\nDesvio: {desvio_abs(x,x_ant)}; Residuo: {residuo_abs(fx)},")
    return x

f = lambda x: x - 5 * (math.e**(-x**2)) + 4 
print("\na)Empregando a aproximação da derivada 'convencional':\n")
#x = metodo_secante(x00=-1.4,x01=1.5,f=f)
x = secante_convencional(f=f,x_anterior=-1.5,x_atual=-1.4)
print(x)
print()
print("-"*80,"\nb)Empregando a aproximação da derivada baseada em diferenças centradas:")
x = secante_dif_centrada(f=f,x=2.0,delta=0.01)
print(x)
