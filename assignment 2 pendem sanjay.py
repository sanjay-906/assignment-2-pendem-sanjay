import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("D:\dataset\diabetes.csv")
df
df.head()
df.tail()
df.shape
df.info
df.describe()
df.columns # now, copy the output and create the next line and initialize it with df_features
df_features=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
x=df[df_features]
y=df.Insulin # choose any feature
