import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Course Analyze", page_icon="📈")
st.markdown("# Course Analyze")
st.sidebar.header("Course Analyze")
random_data = np.random.rand(100, 10)
# df = pd.DataFrame(random_data, columns=[f'Col{i}' for i in range(1, 11)])

course_chapter = pd.read_csv("./out/course_chapter.csv")[
    ["courseId", "type", "number", "seq", "title"]
]

courseId_list = sorted(course_chapter["courseId"].unique())

course_chapter = course_chapter.sort_values(by=["seq"]).set_index(keys="courseId")

courseId = st.selectbox(
    label="请输入要查询的课程编号",
    options=courseId_list,  
    format_func=int
)
df = course_chapter.loc[courseId]

# st.dataframe(df)
st.table(df)
