import streamlit as st
import math

st.set_page_config(page_title="Calculadora Geométrica", page_icon="📐", layout="wide")

st.title("📐 Calculadora Geométrica Interativa")
st.write("Explore dimensões, consulte fórmulas e faça a prova real dos seus cálculos.")

# Menu Lateral (Seleção da Figura)
figura = st.sidebar.selectbox("Escolha a figura:", ["Círculo", "Retângulo", "Triângulo", "Esfera", "Cilindro"])

st.sidebar.subheader("🎛️ Parâmetros")
if figura in ["Círculo", "Esfera"]:
    raio = st.sidebar.slider("Raio (r)", 1.0, 10.0, 5.0, 0.1)
elif figura in ["Retângulo", "Triângulo"]:
    largura = st.sidebar.slider("Base (b)", 1.0, 10.0, 6.0, 0.1)
    altura = st.sidebar.slider("Altura (h)", 1.0, 10.0, 4.0, 0.1)
elif figura == "Cilindro":
    raio = st.sidebar.slider("Raio (r)", 1.0, 10.0, 3.9, 0.1)
    altura = st.sidebar.slider("Altura (h)", 1.0, 10.0, 5.0, 0.1)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Métricas da Figura")
    if figura == "Círculo":
        area = math.pi * (raio ** 2)
        circ = 2 * math.pi * raio
        st.metric("Área (A)", f"{area:.2f} cm²")
        st.metric("Circunferência (C)", f"{circ:.2f} cm")
        st.code(f"A = π · {raio:.1f}² ≈ {area:.2f} cm²\nC = 2 · π · {raio:.1f} ≈ {circ:.2f} cm")

    elif figura == "Retângulo":
        area = largura * altura
        perim = 2 * (largura + altura)
        st.metric("Área (A)", f"{area:.2f} cm²")
        st.metric("Perímetro (P)", f"{perim:.2f} cm")
        st.code(f"A = {largura:.1f} · {altura:.1f} = {area:.2f} cm²\nP = 2·({largura:.1f} + {altura:.1f}) = {perim:.2f} cm")

    elif figura == "Triângulo":
        area = (largura * altura) / 2
        hip = math.sqrt(largura**2 + altura**2)
        st.metric("Área (A)", f"{area:.2f} cm²")
        st.metric("Hipotenusa (c)", f"{hip:.2f} cm")
        st.code(f"A = ({largura:.1f} · {altura:.1f}) / 2 = {area:.2f} cm²\nc = √({largura:.1f}² + {altura:.1f}²) ≈ {hip:.2f} cm")

    elif figura == "Esfera":
        vol = (4/3) * math.pi * (raio ** 3)
        area_sup = 4 * math.pi * (raio ** 2)
        st.metric("Volume (V)", f"{vol:.2f} cm³")
        st.metric("Área Superficial", f"{area_sup:.2f} cm²")
        st.code(f"V = (4/3)·π·{raio:.1f}³ ≈ {vol:.2f} cm³\nA = 4·π·{raio:.1f}² ≈ {area_sup:.2f} cm²")

    elif figura == "Cilindro":
        vol = math.pi * (raio ** 2) * altura
        area_sup = 2 * math.pi * raio * (raio + altura)
        st.metric("Volume (V)", f"{vol:.2f} cm³")
        st.metric("Área Superficial", f"{area_sup:.2f} cm²")
        st.code(f"V = π·{raio:.1f}²·{altura:.1f} ≈ {vol:.2f} cm³\nA = 2·π·{raio:.1f}·({raio:.1f}+{altura:.1f}) ≈ {area_sup:.2f} cm²")

with col2:
    st.subheader("🧮 Bloco de Cálculo (Prova Real)")
    expressao = st.text_input("Digita a tua expressão (ex: pi * 5**2 ou 2 * pi * 5):")
    
    if st.button("Calcular & Provar"):
        if expressao.strip():
            try:
                ambiente = {
                    "pi": math.pi, "sqrt": math.sqrt, "pow": math.pow,
                    "sin": math.sin, "cos": math.cos, "tan": math.tan, "abs": abs
                }
                res = float(eval(expressao.replace(",", "."), {"__builtins__": None}, ambiente))
                st.info(f"Resultado calculado: **{res:.2f}**")
            except Exception:
                st.error("⚠️ Expressão matemática inválida.")
        else:
            st.warning("Digita um cálculo primeiro.")