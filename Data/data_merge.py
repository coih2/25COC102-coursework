### Imports
import pandas as pd
import numpy as np


### Datasets
patients = pd.read_csv("ADMISSIONS_sorted.csv")


### Dataset characteristics
print(patients["ETHNICITY"].value_counts())