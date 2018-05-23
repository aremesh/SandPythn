#Data Operations in Numpy
#numby.array
#*********************************
# one dimentions
import numpy as np
x=np.array([1,2,3])
print(x)
#*********************************
# More than one dimentions
import numpy as np
x=np.array([[1,2,3],[3,2,4]])
print(x)
#*********************************
#minimum dimention array
import numpy as np
x=np.array([1,2,3,4,5],ndmin=2)
print(x)
#*********************************
#complex dtype parameter
#*********************************
import numpy as np
x=np.array([2,3,4],dtype=complex)
print(x)

#Data opeations of Pandas
#*********************************
#panda Series -- converts them array rep with index
#pandas.Series( data, index, dtype, copy)

import numpy as np
import pandas as pd
x=np.array([1,2,3])
ps=pd.Series(x)
print(ps)

#*********************************

#pandas data frame

import pandas as pd
data={'Name':['Tim','cook','sathya','sundar'],'Age':[50,65,34,34]}
df=pd.DataFrame(data,index=["rank1","rank2","rank3","rank4"])
print(df)

#*********************************
#panda panel

#pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)

import numpy as np
import pandas as pd
data={'item1':pd.DataFrame(np.random.randn(4,3)),
      'item2':pd.DataFrame(np.random.randn(4,2))}
p=pd.Panel(data)
print(p)