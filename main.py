import streamlit as st
from requests import *


st.set_page_config(layout="wide")
logo_path = "img/logo_cap.png"

# CSS pour positionner le logo en haut à droite
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        margin-top: 0px;
    }
    .sidebar .sidebar-content .sidebar-collapse-control {
        margin-top: 0px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.image(logo_path, width=100, use_column_width=False)
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


with st.container():

    def afficher_impacts(impacts):
        st.markdown(
            """
            <p><strong>Impact(s) lié(s) à cet enjeu:</strong></p> """
            , unsafe_allow_html=True

        )
        for impact, source in impacts:
            st.markdown(
                """
                <div style='border: 1px solid #fcac64; border-radius: 5px; padding: 10px;'>
                <br>
                <p>{}</p>
                <p style='font-size: 0.8em; color: gray;'>Source: {}</p>
                </div>
                <br>
                """.format(impact, source),
                unsafe_allow_html=True
            )

# Utilisation de la fonction pour afficher les impacts sur Streamlit
    impacts = get_impact(topic_ID)
    afficher_impacts(impacts)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


with st.container():

    def afficher_risques(risques):
        st.markdown(
            """
            <p><strong>Risque(s) lié(s) à cet enjeu:</strong></p> """
            , unsafe_allow_html=True

        )
        for impact, source in risques:
            st.markdown(
                """
                <div style='border: 1px solid #91f3fa; border-radius: 5px; padding: 10px;'>
                <br>
                <p>{}</p>
                <p style='font-size: 0.8em; color: gray;'>Source: {}</p>
                </div>
                <br>
                """.format(impact, source),
                unsafe_allow_html=True
            )

# Utilisation de la fonction pour afficher les impacts sur Streamlit
    risques = get_risk(topic_ID)
    afficher_risques(risques)


with st.container():

    def afficher_opp(opps):
        st.markdown(
            """
            <p><strong>Opportunités(s) liée(s) à cet enjeu:</strong></p> """
            , unsafe_allow_html=True

        )
        for opp, source in opps:
            st.markdown(
                """
                <div style='border: 1px solid #607c7b; border-radius: 5px; padding: 10px;'>
                <br>
                <p>{}</p>
                <p style='font-size: 0.8em; color: gray;'>Source: {}</p>
                </div>
                <br>
                """.format(opp, source),
                unsafe_allow_html=True
            )

# Utilisation de la fonction pour afficher les impacts sur Streamlit
    opps = get_opportunity(topic_ID)
    afficher_opp(opps)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

with st.container():
    c1, c2, c3 = st.columns([1, 1, 1])

    with c2:
        img_1_path = "img/illus_1.png"
        st.image(img_1_path, width=150, use_column_width=False)
