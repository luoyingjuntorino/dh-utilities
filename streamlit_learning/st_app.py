import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import requests
st.set_page_config(layout="wide")
st.header("GLHF")
##################################################
st.title("Welcome to API station")
url_publicIP = "https://get.geojs.io/v1/ip/geo.json"
r = requests.get(url=url_publicIP).json()
st.write("This is your Public IP address:")
st.write(r["ip"])
##################################################
st.title("Randomly generate a yes or no image")
r = requests.get(url="https://yesno.wtf/api").json()
ans = r["answer"]
image_url = r["image"]
st.write("Your image is generated with:")
st.markdown(ans)
st.image(image_url)




