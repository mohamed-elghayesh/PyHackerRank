import numpy as np
import pandas as pd

# A structured array
my_array = np.ones(3, dtype=([('foo', int), ('bar', float)]))
print(my_array['foo'])

# A record array
my_array2 = my_array.view(np.recarray)
print(my_array2.foo)

data = np.array([['','Col1','Col2'],
                 ['Row1',1,2],
                 ['Row2',3,4]])
                
print(pd.DataFrame(data=data[1:,1:],
                  index=data[1:,0],
                  columns=data[0,1:]))