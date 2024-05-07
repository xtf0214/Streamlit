import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="课程内容查询", page_icon="📈")
st.markdown("# 课程内容查询")

course_chapter = pd.read_csv("./out/course_chapter.csv")[["courseId", "type", "number", "seq", "title"]]

courseId_list = sorted(course_chapter["courseId"].unique())

course_chapter = course_chapter.sort_values(by=["seq"]).set_index(keys="courseId")

courseId = st.selectbox(label="请输入要查询的课程编号", options=courseId_list, format_func=int)
df = course_chapter.loc[courseId]

st.dataframe(df)

