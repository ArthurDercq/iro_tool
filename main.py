import sqlite3
import streamlit as st
from requests import *


st.set_page_config(layout="wide")
st.title('Cap Conseil - Exemples des IRO rencontrés lors de nos missions')
st.write('Bienvenue sur notre application de démonstration. Vous pouvez sélectionner un topic dans la barre latérale pour afficher les impacts, risques et opportunités associés.')

# Connexion à la base de données (créée si elle n'existe pas)
# conn = sqlite3.connect('data/iro.db')
# cursor = conn.cursor()

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)



# Sélection du topic dans la barre latérale
selected_topic = st.sidebar.selectbox("Sélectionnez un topic", get_topic_name())

# Affichage du topic sélectionné

st.markdown("""
            <p> Voici des exemples d'IRO pour l'enjeu <strong>{}</strong>  </p>

            """.format(selected_topic), unsafe_allow_html=True)


topic_ID = get_topicID(selected_topic)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)



c1,c2, c3 = st.columns([1, 1, 1])

with c1:
    st.markdown(
        """
        <div style='border: 1px solid #fcac64; border-radius: 5px; padding: 10px;'>
        <p>Impact lié:</p>
        <p>{}</p>
        </div>
        """.format(get_impact(topic_ID)[0]),
        unsafe_allow_html=True
    )


with c2:

    if get_risk(topic_ID)[0]:
        result = get_risk(topic_ID)[0]

    else:
        print("No risks found")

    st.markdown(
        """
        <div style='border: 1px solid #91f3fa; border-radius: 5px; padding: 10px;'>
        <p>Risque lié:</p>
        <p>{}</p>
        </div>
        """.format(result),
        unsafe_allow_html=True
    )

with c3:

    st.markdown(
        """
        <div style='border: 1px solid #607c7b; border-radius: 5px; padding: 10px;'>
        <p>Opportunité liée:</p>
        <p>{}</p>
        </div>
        """.format(get_opportunity(topic_ID)[0]),
        unsafe_allow_html=True
    )
