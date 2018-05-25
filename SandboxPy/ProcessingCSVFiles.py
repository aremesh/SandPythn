#Python - Processing CSV Dat
import pandas as PD

data=PD.read_csv('c:/users/rarumugam/desktop/input.csv')
print(data)

#Reading a specific value
import pandas as pd
data=pd.read_csv('c:/users/rarumugam/desktop/input.csv')
print(data[0:5]["salary"])



#Reading a specific value
import pandas as pd
data=pd.read_csv('c:/users/rarumugam/desktop/input.csv')
print(data["salary"])
print (data.loc[:,['salary','name']])

import pandas as pd
data = pd.read_csv('path/input.csv')

# Use the multi-axes indexing funtion
print (data.loc[2:6,['salary','name']])
