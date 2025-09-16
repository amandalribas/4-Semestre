import numpy as np
from matplotlib import pyplot as plt

def my_f(x):
    x = np.float64(x)
    #y = -np.power(x,2.) + 4.
    y = 5. / (x+1.) + 2.*np.exp(x-3.)-4.
    return y

def bissec(f,xl,xu,tol=1e-06,maxit=1000):
    if (np.abs(f(xl))<=tol):
        return xl
    if (np.abs(f(xu))<=tol):
        return xu
    xm = 0.5*(xl+xu)
    fx = np.array([f(xl),f(xm),f(xu)],dtype='float64')
    delta = np.abs(fx[1])
    ii=1
    print(f'iter {ii}, xm={xm:.8e}, f(xm)={fx[1]:.8e}')
    while (delta > tol and ii<maxit):
        if (fx[0]*fx[1] < 0):
            xu=xm
            fx[2]=fx[1]
        else: # (fx[1]*fx[2] < 0):
            xl=xm
            fx[0]=fx[1]
        xm = 0.5*(xl+xu)
        fx[1] = f(xm)
        delta = np.abs(fx[1])
        ii+=1
        print(f'iter {ii}, xm={xm:.8e}, f(xm)={fx[1]:.8e}')
    return xm

def bissec_desvio(f,xl,xu,tol=1e-06,maxit=1000):
    fl = f(xl)
    if (np.abs(fl)<=tol):
        return xl
    fu = f(xu)
    if (np.abs(fu)<=tol):
        return xu
    xm = 0.5*(xl+xu)
    fm = f(xm)
    if (np.abs(fm)<=tol):
        return xm
    delta = tol*10.
    ii=1
    print(f'iter {ii}, xm={xm:.8e}, f(xm)={fm:.8e}')
    while (delta > tol and ii<maxit):
        if (fl*fm < 0):
            xu=xm
            fu=fm
        else: # (fm*fu < 0):
            xl=xm
            fl=fm
        xprev=xm
        xm = 0.5*(xl+xu)
        fm = f(xm)
        delta = np.abs(xm-xprev) / ( np.abs(xm) if xm!=0. else 1. )
        ii+=1
        print(f'iter {ii}, xm={xm:.8e}, f(xm)={fm:.8e}, e={delta:.8e}')
    return xm
    
def bissec_desvio_absoluto(f,xl,xu,tol=1e-06,maxit=1000):
    fl = f(xl)
    if (np.abs(fl)<=tol):
        return xl
    fu = f(xu)
    if (np.abs(fu)<=tol):
        return xu
    xm = 0.5*(xl+xu)
    fm = f(xm)
    if (np.abs(fm)<=tol):
        return xm
    delta = tol*10.
    ii=1
    print(f'iter {ii}, xm={xm:.8e}, f(xm)={fm:.8e}')
    while (delta > tol and ii<maxit):
        if (fl*fm < 0):
            xu=xm
            fu=fm
        else: # (fm*fu < 0):
            xl=xm
            fl=fm
        xprev=xm
        xm = 0.5*(xl+xu)
        fm = f(xm)
        delta = np.abs(xm-xprev)
        ii+=1
        print(f'iter {ii}, xm={xm:.8e}, f(xm)={fm:.8e}, e={delta:.8e}')
    return xm
    
def bissec_graphic(f,xl,xu,tol=1e-06,maxit=1000):
    plt.ion()
    fig, (ax1, ax2) = plt.subplots(2,1)
    x = np.linspace(xl,xu,10001,dtype='float64')
    y = f(x)
    ax1.plot(x,y,'b-')
    if (np.abs(f(xl))<=tol):
        return xl
    if (np.abs(f(xu))<=tol):
        return xu
    xm = 0.5*(xl+xu)
    fx = np.array([f(xl),f(xm),f(xu)],dtype='float64')
    delta = np.abs(fx[1])
    ii=1
    print(f'iter {ii}, xm={xm:.8e}, f(xm)={fx[1]:.8e}')
    m_plt, = ax1.plot(xm,fx[1],'g.', markersize=20)
    x = np.array([xl,xu],dtype='float64')
    y = np.zeros((2),dtype='float64')
    lu_plt, = ax1.plot(x,y,'r+', markersize=10)
    iter_x = np.linspace(1,maxit,maxit)
    residuo = np.zeros(np.shape(iter_x))
    residuo[0] = delta
    res_plt, = ax2.plot(iter_x[:ii],residuo[:ii])
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax2.set_xlim([0,2])
    ax2.set_ylim([tol*1e-01,1e+01])
    ax2.set_yscale('log')
    ax2.set_xlabel('iter')
    ax2.set_ylabel('|f(x)|')
    _ = input('')
    while (delta > tol and ii<maxit):
        if (fx[0]*fx[1] < 0):
            xu=xm
            fx[2]=f(xu)
        else: # (fx[1]*fx[2] < 0):
            xl=xm
            fx[0]=f(xl)
        xm = 0.5*(xl+xu)
        fx[1] = f(xm)
        delta = np.abs(fx[1])
        ii+=1
        print(f'iter {ii}, xm={xm:.8e}, f(xm)={fx[1]:.8e}')
        m_plt.set_data([xm],[fx[1]])
        x[0]=xu
        x[1]=xl
        lu_plt.set_data(x,y)
        residuo[ii-1]=delta
        res_plt.set_data(iter_x[:ii],residuo[:ii])
        ax2.set_xlim([0,ii+1])
        _ = input('')
    return xm

if __name__ == '__main__':
    #bissec(my_f,np.float64(0.0),np.float64(5.0))
    #bissec_desvio(my_f,np.float64(0.5),np.float64(4.5))
    #bissec_desvio_absoluto(my_f,np.float64(0.5),np.float64(8.5))
    bissec_graphic(my_f,np.float64(-0.5),np.float64(5.5))
    _ = input('')