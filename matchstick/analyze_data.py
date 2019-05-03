"""
用pandas对数据进行处理,由于对航天术语不了解,这里只得到数据,没有对数据做进一步处理.
"""

import pandas as pd

data = pd.read_json('./data1.json', orient="records", lines=True)
print(data)