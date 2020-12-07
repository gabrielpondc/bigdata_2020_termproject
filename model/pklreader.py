# -*- coding: UTF8 -*-
import sys
sys.getdefaultencoding()
import pickle
import numpy as np
np.set_printoptions(threshold=1000000000000000)
path = 'ml-100k-testsize0.8-movie_popular.pkl'
file = open(path,'rb')
inf = pickle.load(file)       #读取pkl文件的内容
#fr.close()
inf=str(inf)
obj_path = 'test.txt'
ft = open(obj_path, 'w')
ft.write(str(inf))
print("Done")
