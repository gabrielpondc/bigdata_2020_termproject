# -*- coding: UTF8 -*-
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import json
from collections import defaultdict
from numpy import random
import pandas as pd
import matplotlib.pyplot as mp, seaborn
import pickle
import seaborn as sns
import os
np.set_printoptions(threshold=1000000000000000)
sns.set()
sys.getdefaultencoding()
i=0
msg=[]
for root, dirs, files in os.walk("./model"):
    msg=files
    for file in files:
        i+=1
        print(str(i)+':'+file)
n=int(input("Please select the file you need to draw:"))-1
try:
    pa=msg[n]
except IndexError:
    n=int(input("(Wrong index)Please select the file you need to draw:"))-1
    pa=msg[n]
path = './model/'+pa
print("Open"+path.replace(".pkl","")+" Done!Waiting for drawing")
file = open(path,'rb')
inf = pickle.load(file)
c=str(inf)
#读取pkl文件的内容
jsObj = json.dumps(inf)
b=json.loads(jsObj)
f=pd.DataFrame(b)
df_corr = f.corr()
ax = sns.heatmap(df_corr,vmax=0.8,cmap='RdBu_r',square=True,center=0,cbar=False)
cb=ax.figure.colorbar(ax.collections[0]) #显示colorbar
cb.ax.tick_params(labelsize=5) #设置colorbar刻度字体大小。
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
plt.savefig(pa.replace(".pkl","")+'.png', dpi=600)
print("Done")
