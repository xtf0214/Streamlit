import streamlit as st
import pandas as pd
import numpy as np
import json


st.set_page_config(page_title="个性化课程推荐", page_icon="📈")
st.markdown("# 个性化课程推荐")


@st.cache_data
def load_data(path):
    return json.load(open(path, "r"))


# 用户列表
data = load_data("./out/个性化课程推荐.json")
# 输入用户Id
userId = st.selectbox(label="请输入要查询的用户编号", options=data["userId_list"])
userId = str(userId)

by_score, by_rating = st.tabs(["按分数", "按等级"])

# 根据分数推荐
similar_course , popular_course = by_score.columns(2)
similar_course.markdown("## 推荐课程")
similar_course.table(
    pd.DataFrame(
        {
            "课程编号": data["courseId_by_score"][userId].keys(),
            "预测分数": data["courseId_by_score"][userId].values(),
        }
    )
)
popular_course.markdown("## 热门课程")
popular_course.table(pd.DataFrame({"课程编号": data["hot_courseId_by_score"]}))

# 根据等级推荐
similar_course , popular_course = by_rating.columns(2)
similar_course.markdown("## 推荐课程")
similar_course.table(
    pd.DataFrame(
        {
            "课程编号": data["courseId_by_rating"][userId].keys(),
            "预测等级": data["courseId_by_rating"][userId].values(),
        }
    )
)
popular_course.markdown("## 热门课程")
popular_course.table(pd.DataFrame({"课程编号": data["hot_courseId_by_rating"]}))