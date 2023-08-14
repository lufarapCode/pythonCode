import pandas as pd

url = "imports-85.data"
url2 = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(url, sep=',')
df2 = pd.read_csv(url, header='none')
print (df)

# df prints the entire dataframe, not recommended for large dataset
# we can just use dataframe.head() to show the first n rows of the data frame.
# Similarly, dataframe.tail(n) shows the bottom n rows of data frame.
# Here, we printed out the first 5 rows of data.