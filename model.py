import pandas as pd
import numpy as np
import pickle
import os
import sys
import json

input_params = (sys.stdin.readline())
input_params1 = (sys.stdin.readline())
input_params2 = (sys.stdin.readline())
input_params3 = (sys.stdin.readline())


current_dir = os.path.dirname(os.path.realpath(__file__))

import pickle
import pandas as pd
df = pickle.load(open('utils/columns.csv', 'rb'))
model = pickle.load(open("utils/xgboostmodel2.sav",'rb'))
# sys.stdout.write(input_params)
# sys.stdout.write(input_params[2])

state_name = input_params.strip()
season = input_params1.strip()
crop = input_params2.strip()
area = float(input_params3)
df2 = pd.DataFrame(0,index = range(1), columns=df.columns)
df2['State_Name_'+state_name] = 1
df2['Season_'+season] = 1
df2['Crop_'+crop] = 1
df2['Area'] = area
# print(df2.shape)
Production = model.predict(df2)
output = Production * area
sys.stdout.write(str(output))
sys.stdout.flush()
