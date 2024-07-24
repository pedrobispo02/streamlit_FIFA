import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = (df_data["Club"].unique())
clube = st.sidebar.selectbox("Clube", clubes)

df_jogadores = df_data[(df_data["Club"] == clube)]
jogadores = df_jogadores["Name"].unique()
jogador = st.sidebar.selectbox("Jogador", jogadores)

jogador_selecionado = df_data[df_data["Name"] == jogador].iloc[0]

st.image(jogador_selecionado["Photo"])
st.title(jogador_selecionado["Name"])
st.divider()

coluna1, coluna2, coluna3 = st.columns(3)
coluna1.markdown(f"**Clube**: {jogador_selecionado['Club']}")
coluna2.image(jogador_selecionado["Club Logo"])
coluna1.markdown(f"**Posição**: {jogador_selecionado['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade**: {jogador_selecionado['Age']}")
col2.markdown(f"**Altura**: {jogador_selecionado['Height(cm.)'] / 100}m")
col3.markdown(f"**Peso**: {jogador_selecionado['Weight(lbs.)']*0.453:.2f}kg")
st.divider()

st.subheader(f"**Overall**: {jogador_selecionado['Overall']}")
st.progress(int(jogador_selecionado['Overall']) )

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {jogador_selecionado['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {jogador_selecionado['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {jogador_selecionado['Release Clause(£)']:,}")