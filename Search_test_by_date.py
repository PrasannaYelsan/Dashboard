import ast
import time
import streamlit as st
from datetime import datetime
import time
from PIL import Image
import threading
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# dashboard title
st.set_page_config(
    page_title="Generic Automation Dashboard",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.subheader("Search test case(s) by name or date")


@st.cache
def load_excel():
    pass
container1 = st.container()
with container1:
    mcol1, mcol2, mcol3, mcol4 = st.columns(4)
    with mcol1:
       st.metric(label="Passed", value="100")

    with mcol2:
       st.metric(label="Failed", value="10")

    with mcol3:
       st.metric(label="Error", value="20")

    with mcol4:
       st.metric(label="Skipped", value="10")
