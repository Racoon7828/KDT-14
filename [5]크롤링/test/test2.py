#%%
import json
import pandas as pd
data = json.load(open('lotto.json'))
# %%
pd.Series(data['data']['list'][0])

# %%
lotto = pd.Series(data['data']['list'])
lotto