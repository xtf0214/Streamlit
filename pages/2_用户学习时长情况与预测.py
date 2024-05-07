import json

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="用户学习时长情况与预测", page_icon="📈")
st.markdown("# 用户学习时长情况与预测")


@st.cache_data
def load_data(path):
    return json.load(open(path, "r"))


# 用户列表
data = load_data("./out/用户学习时长情况与预测.json")
# 输入用户Id
userId = st.selectbox(label="请输入要查询的用户编号", options=data["userId_list"])
userId = str(userId)

pie, bar = st.tabs(["用户学习类型", "用户学习记录"])

pie.markdown("## 用户学习类型")
total = sum(data["user_learning_type"][userId].values())
if total > 0:
    df = pd.Series(data["user_learning_type"][userId], name="percentage")
    df = df / total * 100
    pie.bar_chart(df)
else:
    pie.markdown("### record not found")


record, predict = bar.columns(2)
record.markdown('### 学习时长记录')
record.line_chart(data["user_learning_record"][userId])
predict.markdown('### 学习时长预测')
predict.line_chart(data["user_learning_predict"][userId])
