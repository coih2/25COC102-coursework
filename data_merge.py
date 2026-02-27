### Imports
import pandas as pd
import numpy as np


### Datasets
patients = pd.read_csv("/Users/isabellehunt/Desktop/uniuni/YR 3 MODULES/COC102_adv-AI/COC102 cw/data_MIMIC-3/mimic3-10k/ADMISSIONS_sorted.csv")


### Dataset characteristics
print(patients["ETHNICITY"].value_counts())