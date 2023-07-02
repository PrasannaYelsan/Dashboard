import ast
import time
from fpdf import FPDF
import base64
import pandas as pd
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
    layout="centered",
    initial_sidebar_state="expanded",
)

report_header= st.subheader("HTML Test Report")
hr = st.markdown("""---""")
summary_text = '<p style="font-family:sans-serif; color:Green; font-size: 22px;">Summary : </p>'
st.markdown(summary_text, unsafe_allow_html=True)
st.markdown("Please go through Total test start, end date and also time taken to execute ~100 test cases for the Project iOS")
data  = {"First Date of Testing":["Jan 25-01-2023"],
         "Last Date of Testing":["Jun 25-06-2023"],
         "Total execution hours for running 100 test cases":["30:11:22"],
         "Total number of issue(s) found during test run entire automation team reported":["100"],
         "Total number of issue(s) fixed by Development team":["10"],
         "Total number of issue(s) still inprogress to fix by other teams":["10"]}

df = pd.DataFrame(data)
df= df.set_index('First Date of Testing').transpose() # Tricky code
st.markdown(df.style.to_html(), unsafe_allow_html=True)

st.write("\n\n")
st.write("\n\n")
overall_text = '<p style="font-family:sans-serif; color:Green; font-size: 18px;">Overall Statistics : </p>'
st.markdown(overall_text, unsafe_allow_html=True)
st.markdown("Please go through overall statistics report for ~100 test cases for the project iOS")
# Read specific excel sheet
df = pd.read_excel('./db/Automation_Report.xlsx', sheet_name='test_data')
print(df)
#st.write(df)

total_dataframe = pd.DataFrame({
'Status':['Pass', 'Fail', 'Error','Skip'],
'Number of cases':(df['count'][0],df['count'][1],df['count'][2],df['count'][3])})
#st.write(total_dataframe)
col1, col2 = st.columns(2)

with col1:
    total_summary_graph = px.bar(
            df,
            x='Status',
            y='count',
            title= "Overall Status Report",
            color='Status', color_discrete_map={'Pass':'green','Fail':'red','Error':'coral','Skip':'purple'})
    total_summary_graph.update_layout(width=360)
    st.plotly_chart(total_summary_graph, width=360)

with col2:
    st.write("\n\n")
    st.write("\n\n")
    st.write("\n\n")
    st.write("\n\n")
    st.write("\n\n")
    st.write("\n\n")
    st.write("\n\n")

    test_data_issues = pd.DataFrame({
    'Failure reason':['Test failure', 'other Misc. isues'],
    'count':[10,10]})
    st.markdown(test_data_issues.style.to_html(), unsafe_allow_html=True)
convert_pdf = st.button("Genrate Report")


def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'


if convert_pdf:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(100, 10, report_header)
    pdf.cell(100, 20, hr)

    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")

    st.markdown(html, unsafe_allow_html=True)

st.markdown("""---""")


