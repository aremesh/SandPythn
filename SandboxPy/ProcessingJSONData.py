#Read the file path
import os
jsonpath=("%s/inputs/input.json"%os.getcwd())
csvpath=("%s/inputs/input.csv"%os.getcwd())
# read the Json files now

import pandas as pd

data=pd.read_json(jsonpath)
print(data)

# read the specific rows and columns

import pandas as pd
data=pd.read_json(jsonpath)
print (data.loc[[1,3,5],['Salary','Name']])


# Read the rows and cols as Records

import pandas as pd
data=pd.read_json(csvpath)
print (data.to_json(orient="records",lines=True))