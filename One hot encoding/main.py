import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10

random.shuffle(lst)
data = pd.DataFrame(lst)

data = data.replace(["robot", "human"], ["[1, 0]", "[0, 1]"])

print(data)
