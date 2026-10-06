# app_Matematica

---

### 💻 Como criar e atualizar o `README.md` pelo terminal:

1. Executa o comando abaixo na pasta do teu projeto para sobrescrever/criar o ficheiro:

```bash
cat << 'EOF' > README.md
# 📐 Calculadora Geométrica Interativa

Uma aplicação desktop desenvolvida em **Python** com **CustomTkinter** para exploração de figuras geométricas, visualização dinâmica de fórmulas e verificação de cálculos manuais em tempo real (prova real).

---

## 🚀 Funcionalidades

- 🔵 **Geometria Plana e Espacial:** Suporte para Círculo, Retângulo, Triângulo, Esfera e Cilindro.
- 🎛️ **Ajuste Dinâmico:** Barras deslizantes (sliders) para alterar dimensões com atualização imediata da figura e das métricas.
- 🖼️ **Visualização Gráfica:** Renderização vetorial no Canvas com cotas e medidas em centímetros.
- 🧮 **Bloco de Cálculo Livre (Prova Real):** Digita expressões matemáticas completas (usando `pi`, `sqrt()`, `**`, etc.) para testar e validar os teus cálculos.
- 🎨 **Interface Moderna:** Tema escuro (*Dark Mode*) desenvolvido com CustomTkinter.

---

## 🛠️ Tecnologias Utilizadas

- **[Python 3.x](https://www.python.org/)**
- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** (Interface Gráfica)
- **Math** (Módulo nativo para operações matemáticas)

---

## 📦 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone [https://github.com/lucianorviana75/app_Matematica.git](https://github.com/lucianorviana75/app_Matematica.git)
cd app_Matematica
2. Criar e ativar um ambiente virtual
Bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
3. Instalar as dependências
Bash
pip install customtkinter
4. Executar a aplicação
Bash
python interface.py
📜 Licença
Este projeto é de uso livre para fins educacionais e de aprendizagem.
EOF
