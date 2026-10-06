import streamlit as st
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches


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

# Função para desenhar a figura
def desenhar_figura():
    fig, ax = plt.subplots(figsize=(4, 3.5))
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#0e1117')
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_color('#333333')

    if figura == "Círculo":
        circ = patches.Circle((0, 0), raio, color='#3b82f6', alpha=0.6, ec='#60a5fa', lw=2)
        ax.add_patch(circ)
        ax.plot([0, raio], [0, 0], color='white', linestyle='--', linewidth=2)
        ax.text(raio/2, 0.5, f"r = {raio:.1f} cm", color='white', fontsize=10, fontweight='bold', ha='center')
        ax.set_xlim(-11, 11)
        ax.set_ylim(-11, 11)

    elif figura == "Retângulo":
        rect = patches.Rectangle((-largura/2, -altura/2), largura, altura, color='#1d4ed8', alpha=0.6, ec='#60a5fa', lw=2)
        ax.add_patch(rect)
        ax.text(0, -altura/2 - 1, f"b = {largura:.1f} cm", color='white', fontsize=10, fontweight='bold', ha='center')
        ax.text(largura/2 + 0.8, 0, f"h = {altura:.1f} cm", color='white', fontsize=10, fontweight='bold', va='center')
        ax.set_xlim(-11, 11)
        ax.set_ylim(-11, 11)

    elif figura == "Triângulo":
        pts = [[-largura/2, -altura/2], [largura/2, -altura/2], [-largura/2, altura/2]]
        tri = patches.Polygon(pts, color='#16a34a', alpha=0.6, ec='#4ade80', lw=2)
        ax.add_patch(tri)
        ax.text(0, -altura/2 - 1, f"b = {largura:.1f} cm", color='white', fontsize=10, fontweight='bold', ha='center')
        ax.text(-largura/2 - 1.2, 0, f"h = {altura:.1f} cm", color='white', fontsize=10, fontweight='bold', va='center')
        ax.set_xlim(-11, 11)
        ax.set_ylim(-11, 11)

    elif figura == "Esfera":
        circ = patches.Circle((0, 0), raio, color='#2563eb', alpha=0.6, ec='#60a5fa', lw=2)
        ellipse = patches.Ellipse((0, 0), raio*2, raio*0.6, color='#93c5fd', fill=False, lw=1.5, ls='--')
        ax.add_patch(circ)
        ax.add_patch(ellipse)
        ax.plot([0, raio], [0, 0], color='white', linestyle='--', linewidth=2)
        ax.text(raio/2, 0.5, f"r = {raio:.1f} cm", color='white', fontsize=10, fontweight='bold', ha='center')
        ax.set_xlim(-11, 11)
        ax.set_ylim(-11, 11)

    elif figura == "Cilindro":
        rect = patches.Rectangle((-raio, -altura/2), raio*2, altura, color='#2563eb', alpha=0.6, ec='none')
        top = patches.Ellipse((0, altura/2), raio*2, raio*0.5, color='#60a5fa', ec='#93c5fd', lw=1.5)
        bot = patches.Ellipse((0, -altura/2), raio*2, raio*0.5, color='#1d4ed8', ec='#60a5fa', lw=1.5)
        ax.add_patch(rect)
        ax.add_patch(bot)
        ax.add_patch(top)
        ax.text(0, altura/2 + 1, f"r = {raio:.1f} cm", color='white', fontsize=10, fontweight='bold', ha='center')
        ax.text(raio + 1.2, 0, f"h = {altura:.1f} cm", color='white', fontsize=10, fontweight='bold', va='center')
        ax.set_xlim(-11, 11)
        ax.set_ylim(-11, 11)

    ax.set_aspect('equal')
    ax.axis('off')
    return fig

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🖼️ Visualização Geométrica")
    st.pyplot(desenhar_figura())

    st.subheader("📊 Métricas")
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