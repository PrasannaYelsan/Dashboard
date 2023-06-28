import ast
import time
import pandas as pd
import streamlit as st
from datetime import datetime
import time
from PIL import Image
import threading
import streamlit as st
import streamlit.components.v1 as components
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
st.title("Automation Tracker")
st.subheader("Dashboard")

def ColourWidgetText(wgt_txt, wch_colour = '#000000'):
    htmlstr = """<script>var elements = window.parent.document.querySelectorAll('*'), i;
                    for (i = 0; i < elements.length; ++i) { if (elements[i].innerText == |wgt_txt|) 
                        elements[i].style.color = ' """ + wch_colour + """ '; } </script>  """

    htmlstr = htmlstr.replace('|wgt_txt|', "'" + wgt_txt + "'")
    components.html(f"{htmlstr}", height=0, width=0)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style/style.css")
#
# with st.sidebar.title("Welcome..."):
#     pass


#Load excel
def load_excel():
    pass

container1 = st.container()
with container1:
    mcol1, mcol2, mcol3, mcol4 = st.columns(4)
    with mcol1:
       mcol1.metric(label="Passed", value="100")
       ColourWidgetText("Passed", '#0251CA')  # colour only metric text
       #ColourWidgetText(va, '#FF0000')

    with mcol2:
       st.metric(label="Failed", value="10")
       ColourWidgetText("Failed", '#FF2B2B')

    with mcol3:
       st.metric(label="Error", value="20")
       ColourWidgetText("Error", "#83C9FF")

    with mcol4:
       st.metric(label="Skipped", value="10")
       ColourWidgetText("Skipped", "#E78F6F")


container2 = st.container()
with container2:

    chart_col1, chart_col2 = st.columns([1,3])

    with chart_col1:
        import numpy

        # Random Data
        data = [100, 10, 20, 10]
        names = ['Passed', 'Failed', 'Error', 'Skipped']

        fig = px.pie(values=data, title='Overall', names=names)
        fig.update_layout(width=295)

        st.plotly_chart(fig, width=295)

    with chart_col2:

        data ={"Test cases": [100, 90, 85, 89, 50, 74, 60, 89],
         'Date':['21-6-2023', '22-6-2023', '23-6-2023', '24-6-2023', '25-6-2023','26-6-2023','27-6-2023','28-6-2023']}
        df = pd.DataFrame(data)
        fig = px.line(df,x="Date",
                      y= "Test cases",
                      title='Statistics')
        fig.update_layout(width=700)
        st.plotly_chart(fig, theme="streamlit", width=700)







