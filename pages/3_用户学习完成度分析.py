import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="", page_icon="📈")
st.markdown("# 用户学习完成度分析")


@st.cache_data
def load_data(path):
    return json.load(open(path, "r"))


# 用户列表
data = load_data("./out/用户学习完成度分析.json")


@st.cache_resource
def plot():
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    (pd.Series(data["sort_by_time"]) / 3600).plot(ax=ax1)
    ax1.set_xlabel("userId")
    ax1.set_ylabel("learnedTime / h")

    fig2, ax2 = plt.subplots(figsize=(10, 6))
    pd.Series(data["sort_by_num"]).plot(ax=ax2)
    ax2.set_xlabel("userId")
    ax2.set_ylabel("finishedTaskNum")
    return fig1, fig2

# 输入用户Id
userId = st.selectbox(label="请输入要查询的用户编号", options=data["userId"])
userId = str(userId)

c1, c2, c3, c4 = st.columns(4)
c1.metric(label="学习时长", value=f'{data["sort_by_time"][userId] / 3600:.1f} h')
c2.metric(
    label="学习时长排名",
    value=f'{np.ceil(list(data["sort_by_time"].keys()).index(userId) / len(data["sort_by_time"]) * 100):.0f}%',
)
c3.metric(label="完成任务数", value=data["sort_by_num"][userId])
c4.metric(
    label="完成任务数排名",
    value=f'{np.ceil(list(data["sort_by_num"].keys()).index(userId) / len(data["sort_by_num"]) * 100):.0f}%',
)

fig1, fig2 = plot()
st.markdown("## 用户学习时长曲线图")
st.pyplot(fig1)
st.markdown("## 用户完成任务数曲线图")
st.pyplot(fig2)
