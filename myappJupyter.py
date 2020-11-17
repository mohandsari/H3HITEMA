from pathlib import Path
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
@st.cache
def load_data(dataname):
   data = pd.read_csv("csv/"+dataname+".csv")
   return data

def start(x):
    df = load_data(x)
    if st.button("Show DataSet "):
        
        number = st.number_input("Number of Rows to View")
        st.dataframe(df.head(int(number)))
        
    if st.button("Columns Names "):
        st.write(df.columns.tolist())
        
    if st.button("Columns Type "):
        st.write(df.dtypes)
    if st.button("Shape "):
        st.write(df.shape)
    if st.button("Statistique "):
        st.write(df.describe)
    if st.button("Graphique "):
        if st.checkbox("heatmap "):
            st.write(sns.heatmap(df.corr(),annot=True))
            st.pyplot()
        if st.checkbox("barplot "):
            st.write(sns.barplot(data=df.shape))
            st.pyplot()
            
database=["vintage","felonies"]
for x in database :
    if st.checkbox(x):
        start(x)
    
       
    