import numpy as np
import pandas as pd
import scipy

# Example for using numpy
array_1 = np.array([2, 3, 6, 5])
print(array_1)

# Example for using pandas
data = {
    'Name' : ['Lulu', 'Lala', 'Lili'],
    'Age': [23, 45, 46],
}

df = pd.DataFrame(data)
print(df)

#Example for using SciPy
print(f'SciPy version is {scipy.__version__}')