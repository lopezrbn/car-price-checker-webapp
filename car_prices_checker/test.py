import os
import pandas as pd


absolute_path = os.path.dirname(__file__)
relative_path = "data/csv"
file_path = "Abarth_500.csv"
full_path = os.path.join(absolute_path, relative_path, file_path)

print(absolute_path)
print(full_path)
print(os.path.isfile(full_path))

df = pd.read_csv(full_path, index_col=0)
print(df)