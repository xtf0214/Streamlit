import streamlit as st
import pandas as pd
import numpy as np
import json


st.set_page_config(page_title="Course Recommond", page_icon="📈")
st.markdown("# Course Recommond")
st.sidebar.header("Course Recommond")


@st.cache_data
def load_data(path):
    return json.load(open(path, "r"))


# 用户列表
data = load_data("./out/recommond_data.json")
# 输入用户Id
userId = st.selectbox(label="Please input userId", options=data["userId_list"])
userId = str(userId)

by_score, by_rating = st.tabs(["by score", "by rating"])

# 根据分数推荐
similar_course , popular_course = by_score.columns(2)
similar_course.markdown("## similar_course")
similar_course.table(
    pd.DataFrame(
        {
            "predit courseId": data["courseId_by_score"][userId].keys(),
            "predit score": data["courseId_by_score"][userId].values(),
        }
    )
)
popular_course.markdown("## popular_course")
popular_course.table(pd.DataFrame({"predit courseId": data["hot_courseId_by_score"]}))

# 根据等级推荐
similar_course , popular_course = by_rating.columns(2)
similar_course.markdown("## similar_course")
similar_course.table(
    pd.DataFrame(
        {
            "predit courseId": data["courseId_by_rating"][userId].keys(),
            "predit rating": data["courseId_by_rating"][userId].values(),
        }
    )
)
popular_course.markdown("## popular_course")
popular_course.table(pd.DataFrame({"predit courseId": data["hot_courseId_by_rating"]}))