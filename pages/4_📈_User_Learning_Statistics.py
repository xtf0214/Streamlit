import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json


st.set_page_config(page_title="User Learning Statistics", page_icon="📈")
st.markdown("# User Learning Statistics")
st.sidebar.header("User Learning Statistics")


@st.cache_data
def load_data(path):
    return json.load(open(path, "r"))


# 用户列表
data = load_data("./out/user_learning_statistics.json")
# 输入用户Id
userId = st.selectbox(label="Please input userId", options=data["userId_list"])
userId = str(userId)

pie, bar = st.tabs(['pie', 'bar'])

pie.markdown('## learning type')
total = sum(data['user_learning_type'][userId].values())
if total > 0:
    fig, ax = plt.subplots()
    ax.pie(
        data["user_learning_type"][userId].values(),
        labels=data["user_learning_type"][userId].keys(),
        autopct=lambda p: f"{p:.1f}%  ({p * total / 100:.0f})"
    )
    ax.legend()
    pie.pyplot(fig)
else:
    pie.markdown('### record not found')

bar.markdown('## learning record')
df = pd.DataFrame(data['user_learning_record'][userId], columns=['LearnedTime'])
bar.bar_chart(df)
