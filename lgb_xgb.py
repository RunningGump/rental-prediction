# -*- coding: utf-8 -*-
import pandas as pd
from copy import deepcopy

lgb_df = pd.read_csv("./result/lgb.csv")
xgb_df = pd.read_csv("./result/xgb.csv")
res = pd.DataFrame()
res['id'] = lgb_df['id']
# 比例按照线上比分计算出来
# 0.62/0.38 1.82066
# 0.65/0.35 1.82041
# 0.66/0.34 1.82039
# 0.7/0.3 下降
res['price'] = lgb_df['price'] * 0.34 + xgb_df['price'] * 0.66
res.to_csv('./result/new.csv', index=False)


