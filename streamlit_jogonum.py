import streamlit as st
import random as rd

st.markdown("""
<style>
.stApp {
    background-color: #141A2A;
    color: #a29bfe;
label {
    color: #a29bfe !important;
    font-size: 19px;
.stButton > button {
    background-color: #141A2A;
    color: #141A2A;
    border-radius: 10px;
    border: none;
    padding: 8px 16px;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(layout="wide")

st.title("🎲 Jogo: Acerte o número entre 1 e 15!")

# Inicializa variáveis
if "numsorteado" not in st.session_state:
    st.session_state["numsorteado"] = rd.randint(1, 15)
    st.session_state["tentativas"] = 0
    st.session_state["resultado"] = ""
    st.session_state["fim_jogo"] = False

# Campo de input
numusuario = st.number_input(
    "Digite um número entre 1 e 15:",
    min_value=1,
    max_value=15,
    key="tentativa_input",
    disabled=st.session_state["fim_jogo"]
)

# Botão
if st.button("Testar", disabled=st.session_state["fim_jogo"]):

    st.session_state["tentativas"] += 1

    if st.session_state["numsorteado"] < numusuario:
        st.session_state["resultado"] = f"O número sorteado é menor que {numusuario}!"

    elif st.session_state["numsorteado"] > numusuario:
        st.session_state["resultado"] = f"O número sorteado é maior que {numusuario}!"

    else:
        st.session_state["resultado"] = f"🎉 GANHOU!!! {numusuario} = {st.session_state['numsorteado']}!"
        st.session_state["fim_jogo"] = True

    # perdeu por tentativas
    if st.session_state["tentativas"] >= 3 and numusuario != st.session_state["numsorteado"]:
        st.session_state["resultado"] = f"❌ Perdeu! O número sorteado era {st.session_state['numsorteado']}."
        st.session_state["fim_jogo"] = True

# Mostrar resultado
st.write(st.session_state["resultado"])
st.write(f"Tentativas usadas: {st.session_state['tentativas']} de 3")