import streamlit as st
import pandas as pd 

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].unique()
clube = st.sidebar.selectbox("Clube", clubes)

df_filtrado = df_data[(df_data['Club'] == clube)].set_index("Name")

st.image(df_filtrado.iloc[0]["Club Logo"])
st.markdown(f"## {clube}")

columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_filtrado[columns],
             column_config={
                "Overall": st.column_config.ProgressColumn(
                     "Overall", min_value=0, max_value=100, format="%d"
                     ),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country"),
                "Wage(£)": st.column_config.ProgressColumn(
                    "Wekly Wage", format="£%f", min_value=0, max_value=df_filtrado["Wage(£)"].max()
                ),

             })