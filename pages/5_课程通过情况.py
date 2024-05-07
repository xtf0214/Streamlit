import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="课程通过情况", page_icon="📈")
st.markdown("# 课程通过情况")


@st.cache_data
def load_data(path):
    return json.load(open(path, "r"))


# 用户列表
data = load_data("./out/课程通过情况.json")


@st.cache_resource
def plot():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(pd.Series(data["course_pass_rate"]).values)
    ax.set_ylabel("course pass rate / %")
    return fig


# 输入用户Id
courseId = st.selectbox(label="请输入要查询的课程编号", options=data["courseId_list"])
courseId = str(courseId)

c1, c2 = st.columns(2)
c1.metric(label="通过率", value=f'{data["course_pass_rate"][courseId]:.1f}%')
c2.metric(
    label="通过率排名",
    value=f'{np.ceil(list(data["course_pass_rate"].keys()).index(courseId) / len(data["course_pass_rate"]) * 100):.0f}%',
)

fig = plot()
st.markdown("## 课程通过率曲线")
st.pyplot(fig)
