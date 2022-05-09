import streamlit as st


st.set_page_config( page_title='Susu Index', page_icon="💦")

st.title("Susu Index")
st.subheader("Calcul de l'index de susu en fonction de la température, de l'humidité et de votre sensibilité au soleil")

# Orgine 
origin_dict = {"J'ai pas d'origine":1,"Breton":1.5, "Dromadaire":0.9, "Irlandais":1.8}

col1, col2 = st.columns(2)

with col1:

    tempC = st.slider("Température", -10,50,20)
    temp = (tempC * (9/5))+32

    hum = st.slider('Humidité', 0,100,70)


with col2:
    origine = st.radio("Quelle est votre sensibilté au soleil ?",options=origin_dict.keys())


HIf = -42.379 + (2.04901523*temp) + (10.14333127*hum) + (-0.22475541*temp*hum) + (-0.00683783*temp**2) + (-0.05481717*hum**2) + (0.00122874*hum*temp**2) + (0.00085282*temp*hum**2) + (-0.00000199*temp**2 * hum**2)

HI = (HIf - 32)*(5/9)


def conversion_origin(origine):
    coeff = origin_dict.get(origine)

    HI_corr = HI*coeff
    return(HI_corr)

truc = conversion_origin(origine)
truc



