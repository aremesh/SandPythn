# Read excel 
import pandas as pd
import os
cwd=os.getcwd()
input1=("%s\inputs\input1.xlsx" %cwd)
data1=pd.read_excel(input1)
print(data1)