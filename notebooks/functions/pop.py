import numpy as np 


#%% Projeção aritmética
def pa(t,p0,p2,t0,t2):
    ka = (p2-p0)/(t2-t0)
    return p0 + ka*(t-t0)


#%% Projeção geométrica
def pg(p0,p2,t,t0,t2):
    kg = (np.log(p2)-np.log(p0))/(t2-t0)
    return p0*np.exp(1)**(kg*(t-t0))
 
# %% Taxa decrescente de crescimento
def pt(p0,p1,p2,t,t0,t2):
    ps = (2*p0*p1*p2-p1**2*(p0+p2))/(p0*p2-p1**2)
    kd = (-np.log((ps-p2)/(ps-p0))/(t2-t0))
    return p0 + (ps-p0)*(1-np.exp(1)**(-kd*(t-t0)))

#%% Crecimento logístico
def cl(p0,p1,p2,t,t0,t1,t2):
    ps = (2*p0*p1*p2-p1**2*(p0+p2))/(p0*p2-p1**2)
    c = (ps-p0)/p0
    k1 = (1/(t2-t1))*(np.log((p0*(ps-p1)/(p1*(ps-p0)))))
    return ps/(1+c*np.exp(1)**(k1*(t-t0)))


