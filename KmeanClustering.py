# Surpress warnings:
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import random 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans 
from sklearn.datasets import make_blobs 
from sklearn.preprocessing import StandardScaler

#%matplotlib inline

#import customer data 
cust_df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%204/data/Cust_Segmentation.csv")
cust_df.head()
#remove unusable column  
df = cust_df.drop('Address', axis=1)
df.head()

X = df.values[:,1:]
#convert nan to 0
X = np.nan_to_num(X)
#do fit then transform
Clus_dataSet = StandardScaler().fit_transform(X)
#Clus_dataSet

#set K=3
clusterNum = 4
k_means = KMeans(init = "k-means++", n_clusters = clusterNum, n_init = 12)
k_means.fit(X)
labels = k_means.labels_

df["Clus_km"] = labels
#df.head(5)
#df.groupby('Clus_km').mean()

area = np.pi * ( X[:, 1])**2  
plt.scatter(X[:, 0], X[:, 3], s=area, c=labels.astype(np.float), alpha=0.5)
plt.xlabel('Age', fontsize=18)
plt.ylabel('Income', fontsize=16)
plt.show(block=False)
plt.waitforbuttonpress(10)


from mpl_toolkits.mplot3d import Axes3D 
fig = plt.figure(1, figsize=(8, 6))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
#reset the axes for 3D plotting
plt.cla()
ax.set_xlabel('Education')
ax.set_ylabel('Age')
ax.set_zlabel('Income')
ax.scatter(X[:, 1], X[:, 0], X[:, 3], c= labels.astype(np.float))
plt.waitforbuttonpress(120)
plt.close()