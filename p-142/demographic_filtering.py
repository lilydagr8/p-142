import pandas as pd
import numpy as np

df = pd.read_csv('/Users/lilydalmia/Downloads/classes and projects/p-142/articles.csv')

df = df.sort_values(['total_events'], ascending=[False])

output = df[["url", "title", "text", "lang", "total_events"]].head(20)