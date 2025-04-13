import streamlit as st
import pygsheets
import json

st.title("Page : Collecte des Données")

creds = st.secrets["GOOGLE_SHEETS_CREDS"]
gc = pygsheets.authorize(service_account_info=json.loads(creds))
# sh = gc.open('NomDeVotreFichierGoogleSheets')
sh = gc.open('str1')
wks = sh[0]

nom = st.text_input("Nom")
email = st.text_input("Email")

if st.button("Ajouter"):
    if nom and email:
        wks.append_table([nom, email])
        st.success("Les données ont été ajoutées avec succès !")
    else:
        st.warning("Veuillez remplir tous les champs.")

