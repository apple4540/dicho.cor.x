import pandas as pd
import scipy 
import numpy as np
from mclustpy import mclustpy
from rpy2.robjects import r, pandas2ri

X1=list(np.random.normal(loc = 1, scale = 1, size = 100))
X2=list(np.random.normal(loc = -1, scale = 1, size = 100))
X=X1+X2

dicho_output=np.zeros([1,6])
rho=np.zeros([1,5])
N=len(X)
xx=pd.DataFrame(X)
BIC=mclustpy(xx)
y=mclustpy(xx, G=2, modelNames='VVE', random_seed=2020)
print(y)
