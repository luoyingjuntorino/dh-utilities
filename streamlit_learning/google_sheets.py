import streamlit as st
import pandas as pd
import numpy as np
import requests
from io import BytesIO

st.title('CN stcoks')

# load dataframe

# excel_file = "CNSTOCKS.xlsx"
# sheet_name = "工作表1"

# df = pd.read_excel(excel_file, 
#                    sheet_name=sheet_name)

# st.dataframe(df)

# 定义Excel文件的URL
excel_url = "https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD"

# 使用requests库从URL获取Excel文件内容
response = requests.get(excel_url)

# 检查请求是否成功
if response.status_code == 200:
    # 使用BytesIO将二进制数据包装成文件对象
    excel_file = BytesIO(response.content)

    # 使用pd.read_excel读取Excel文件
    df = pd.read_csv(excel_file)

    # 现在df包含了Excel文件的数据
st.dataframe(df)