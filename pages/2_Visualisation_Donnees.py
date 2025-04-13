import streamlit as st
import pygsheets
import json
import pandas as pd

st.title("Page : Visualisation des Données")

creds = st.secrets["GOOGLE_SHEETS_CREDS"]
gc = pygsheets.authorize(service_account_info=json.loads(creds))
sh = gc.open('str1')
wks = sh[0]

df = wks.get_as_df()

st.subheader("Données enregistrées")
st.dataframe(df)

