import numpy as np
import pandas as pd

whisky = pd.read_csv("whiskies.txt")

whisky["Region"] = pd.read_csv("regions.txt")

whisky.head()