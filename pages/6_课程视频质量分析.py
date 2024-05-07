import json

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="课程视频质量分析", page_icon="📈")
st.markdown("# 课程视频质量分析")


@st.cache_data
def load_data(path):
    return json.load(open(path, "r"))


# 用户列表
data = load_data("./out/课程视频质量分析.json")
# 输入用户Id
userId = st.selectbox(label="请输入要查询的用户编号", options=data["userId_list"])
userId = str(userId)

pie, bar = st.tabs(["用户学习类型", "bar"])

pie.markdown("## 用户学习类型")
total = sum(data["user_learning_type"][userId].values())
if total > 0:
    df = pd.Series(data["user_learning_type"][userId], name="percentage")
    df = df / total * 100
    pie.bar_chart(df)
else:
    pie.markdown("### record not found")
