import streamlit as st
import pandas as pd
import plotly.express as px 

st.set_page_config(layout="wide")

abertura = pd.read_csv('jucepe_abertura.csv', sep=";")

## preenchimento de sidebar com ano 
ano = st.sidebar.selectbox("Ano", abertura["ANO"].unique()) 

## Filtro 
abertura_filtro = abertura[abertura["ANO"] == ano] 
abertura_filtro

## Determinação de colunas para layout 
col1, col2 = st.columns(2) 
col3, col4, col5 = st.columns(3)

## Faturamento total por ano de Abertura 
ano_total = abertura_filtro.groupby("ANO")[["TOTAL"]].sum().reset_index() 
fig_ano = px.bar(ano_total, x="ANO", y="TOTAL", title="Abertura por Ano") 
col1.plotly_chart(fig_ano)

## Faturamento total por mês de Abertura 
mes_total = abertura_filtro.groupby("MES")[["TOTAL"]].sum().reset_index() 
fig_mes = px.bar(mes_total, x="MES", y="TOTAL", title="Abertura por Mês") 
col2.plotly_chart(fig_mes, use_container_width=True)

