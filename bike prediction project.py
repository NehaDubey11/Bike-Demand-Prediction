# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 03:13:42 2021

@author: 91639
"""
# bike prediction projects

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

bike=pd.read_csv("hour.csv")

#step 2- premilinary analysis
bike_prep=bike.copy()


print(bike_prep.isnull().sum(axis=0))

bike_prep=bike_prep.drop(['index','date','casual','registered'])
























