import streamlit as st
import calculadora as calc

st.title("Calculadora (●'◡'●)")
st.image("https://tse3.mm.bing.net/th/id/OIP.h8fVyFA1E1KpRb1Lxt_T5gHaHa?r=0&rs=1&pid=ImgDetMain&o=7&rm=3")

numero1 = st.number_input("Digite o primeiro numero: ", step=0.1,value=None)
numero2 = st.number_input("Digite o segundo numero: ", step=0.1,value=None)
operacao = st.selectbox("Selecione a operação",{"+","-","*","/"})
if st.button ("Calcular"):
    resultado = calc.calcular(numero1, numero2,operacao)
    st.success(f"O resultado é: {resultado}") 