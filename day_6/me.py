import numpy as np
import pandas as pd

batch = pd.read_csv("batch.csv")

np.random.seed(99)
test_items = batch.sample(5, replace=False)

print(test_items.sort_values("item_id"))
