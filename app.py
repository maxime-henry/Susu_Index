import streamlit as st


st.set_page_config( page_title='Susu Index', page_icon="💦")
st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True )
st.title("Index de Transpiration")
st.subheader("Calcul de l'index de transpiration en fonction de la température, de l'humidité et de votre sensibilité au chaud")


# Orgine 
origin_dict = {"Je n'ai pas d'origine":1,"Breton":1.5, "Toulousain":0.8, "Espagnol":0.75, "Ukrainien":1.4,"Alaska":1.7}

col1, col2 = st.columns(2)

with col1:

    tempC = st.slider("Température", 20,50,20)
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

HI_corr = conversion_origin(origine)



st.markdown(f'<h2 style=" text-align:center">Température ressentie {round(HI,0)} °C, Vous êtes en </h2> ', unsafe_allow_html=True )

if HI_corr <25:
    bilan = "zone de confort"
    commentaire = 'Tout vas bien, detendez vous 😎'
    st.markdown(f'<h2 style="font-size: 2rem; text-align:center; font-family:verdana">{bilan}</h2>', unsafe_allow_html=True )
    
elif HI_corr >=25 and HI_corr < 32:
    bilan = "inconfort"
    commentaire = "Il commence à faire chaud, il faut boire de l'eau, beaucoup d'eau 🚰"
    st.markdown(f'<h2 style="font-size: 3rem; text-align:center; font-family:verdana; color:orange">{bilan}</h2>', unsafe_allow_html=True )
elif HI_corr >= 32 and HI_corr<40:
    bilan = "extreme inconfort"
    commentaire = "Phew, il fait vraiment chaud ici, trouvons un peu de fraicheur 💨"
    st.markdown(f'<h2 style="font-size: 4rem; text-align:center; font-family:verdana;color:orange">{bilan}</h2>', unsafe_allow_html=True )
elif HI_corr>=40 and HI_corr<50:
    bilan = "danger"
    commentaire = " 🥵🥵🥵🥵🥵🥵🥵🥵 "
    st.markdown(f'<h2 style="font-size: 4.5rem; text-align:center; font-family:verdana; color:IndianRed">{bilan}</h2>', unsafe_allow_html=True )
elif HI_corr>=50:
    bilan= "danger extreme"
    commentaire = "🔥🔥🔥🔥🔥🔥🔥"
    st.markdown(f'<h2 style="font-size: 5rem; text-align:center; font-family:verdana; color:red">{bilan}</h2>', unsafe_allow_html=True )



st.markdown(f'<p style="text-align:center">{commentaire}</p>', unsafe_allow_html=True)

st.caption("Cet index de transpiration est calculé de manière très précise et scientifique basé sur les travaux de Robert G. Steadman de 1979.")
st.caption("Слава Україні!")


