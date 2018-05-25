import os
cwd = os.getcwd()

filePath=("%s\inputs\input.csv" %cwd)

#Python - Processing CSV Dat
import pandas as PD

data=PD.read_csv(filePath)
print(data)

#Reading a specific value
import pandas as pd
data=pd.read_csv(filePath)
print(data[0:5]["salary"])



#Reading a specific value
import pandas as pd
data=pd.read_csv(filePath)
print(data["salary"])
print (data.loc[:,['salary','name']])

import pandas as pd
data = pd.read_csv(filePath)

# Use the multi-axes indexing funtion
print (data.loc[2:6,['salary','name']])
