#  IMPORTNING THE LIBRARY

import numpy as np 	#Array		

import matplotlib.pyplot as plt		

import pandas as pd		
#--------------------------------------------
# import the dataset & divided my dataset into independe & dependent

dataset = pd.read_csv(r"D:\NIT\7 NOV   (ML... BASIC)\8th- ML\5. Data preprocessing\Data.csv")

X=dataset.iloc[:,0:3].values

Y=dataset.iloc[:,3].values
#--------------------------------------------
from sklearn.impute import SimpleImputer

imputer=SimpleImputer()
#-----------------------------------------------------------------------------
imputer=imputer.fit(X[:,1:3])
(X[:,1:3])=imputer.transform(X[:,1:3])

#  HOW TO ENCODE CATEGORICAL DATA & CREATE A DUMMY VARIABLE

from sklearn.preprocessing import LabelEncoder

labelencoder_X = LabelEncoder()

labelencoder_X=labelencoder_X.fit(X[:,0])
(X[:,0])=labelencoder_X.transform((X[:,0]))
#-------------------------------------------------------------------------------
labelencoder_y = LabelEncoder()

Y = labelencoder_y.fit_transform(Y)
#-----------------------------------------------------------------------
#SPLITING THE DATASET IN TRAINING SET & TESTING SET

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test =train_test_split(X,Y,test_size=0.2)
# if you remove random_stat then your model not behave as accurate 
