import numpy as np
import pandas as pd
import math
import streamlit as st
from PIL import Image
# st.balloons()  #过场动画

st.set_page_config(
    initial_sidebar_state="auto",
    layout="centered"
)

# # # 侧边栏设置
st.sidebar.write("<h4 style='color: blue;'>本工具可以计算LCD新产品串色水平</h4>", unsafe_allow_html=True)


# # # 工具名称、版本号
st.write("# LCD新产品串色评估工具(非VR) #")
col1, col2 = st.columns([2, 1])
with col2:
    st.write("<h5 style='color: blue;'>版本号：V1.0</h5>", unsafe_allow_html=True)
    st.write("<h5 style='color: blue;'>发布时间：2023/11/17</h5>", unsafe_allow_html=True)


# # # 设置步骤1
final_click = st.button('***点击获取结果***', key=99)
if final_click is True:
    # 这是另一个页面
    if name in st.session_state:
        value_from_home = st.session_state[name]
        st.write(value_from_home)
        
