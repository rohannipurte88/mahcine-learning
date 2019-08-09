# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 00:43:01 2019
@author: Saurabh Mangaonkar
"""

import pandas as pd

phy = list(map(int,input().split()))
his = list(map(int,input().split()))

x=pd.Series(phy)
y=pd.Series(his)

r=x.cov(y)/(x.std()*y.std())

beta1 = (r*y.std())/x.std()
print("Slope :",round(beta1,3))
