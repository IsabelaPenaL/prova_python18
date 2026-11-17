import pandas as pd
import openpyxl
import streamlit as st
df= pd.read_excel("dados-educacao.xlsx")  

from dados-educacao.xlxs import escolaridade_filtrado

st.set_page_config(page_title="Dados Educação", layout="wide")
st.title("Dados Educação")