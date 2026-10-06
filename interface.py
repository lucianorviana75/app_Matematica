import customtkinter as ctk
import math

# Configuração de tema
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class CalculadoraGeometrica(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora Geométrica + Bloco de Cálculo Manual")
        self.geometry("900x680")
        self.resizable(False, False)

        # Variáveis de entrada
        self.figura_atual = "Círculo"
        self.raio = 5.0
        self.largura = 6.0
        self.altura = 4.0

        self.criar_interface()

    def criar_interface(self):
        # Título
        self.lbl_titulo = ctk.CTkLabel(self, text="Calculadora Geométrica", font=("Arial", 24, "bold"))
        self.lbl_titulo.pack(anchor="w", padx=20, pady=(15, 2))

        self.lbl_subtitulo = ctk.CTkLabel(self, text="Explore dimensões, faça contas passo a passo e tire a prova real.", text_color="gray")
        self.lbl_subtitulo.pack(anchor="w", padx=20, pady=(0, 10))

        # Botões das Figuras
        self.frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_botoes.pack(fill="x", padx=20, pady=5)

        figuras = ["Círculo", "Retângulo", "Triângulo", "Esfera", "Cilindro"]
        for fig in figuras:
            btn = ctk.CTkButton(self.frame_botoes, text=fig, width=110, corner_radius=20,
                                command=lambda f=fig: self.trocar_figura(f))
            btn.pack(side="left", padx=5)

        # Painel Central (Visualizador + Métricas)
        self.frame_main = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_main.pack(fill="both", expand=True, padx=20, pady=10)

        # Tela de Desenho (Canvas)
        self.canvas = ctk.CTkCanvas(self.frame_main, width=400, height=250, bg="#18181b", highlightthickness=0)
        self.canvas.pack(side="left", padx=(0, 10))

        # Painel Lateral de Resultados
        self.frame_stats = ctk.CTkFrame(self.frame_main, fg_color="transparent")
        self.frame_stats.pack(side="right", fill="both", expand=True)

        self.lbl_m1 = ctk.CTkLabel(self.frame_stats, text="", font=("Arial", 15, "bold"), fg_color="#18181b", corner_radius=8, height=55)
        self.lbl_m1.pack(fill="x", pady=(0, 8))

        self.lbl_m2 = ctk.CTkLabel(self.frame_stats, text="", font=("Arial", 15, "bold"), fg_color="#18181b", corner_radius=8, height=55)
        self.lbl_m2.pack(fill="x", pady=(0, 8))

        self.txt_formulas = ctk.CTkTextbox(self.frame_stats, height=115, fg_color="#18181b", font=("Consolas", 12))
        self.txt_formulas.pack(fill="both", expand=True)

        # --- PAINEL INFERIOR DUPLO (Controles + Quadro de Cálculo Manual) ---
        self.frame_inferior = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_inferior.pack(fill="x", padx=20, pady=(0, 15))

        # 1. Quadro de Controles (Sliders)
        self.frame_controles = ctk.CTkFrame(self.frame_inferior, fg_color="#18181b", corner_radius=12)
        self.frame_controles.pack(side="left", fill="both", expand=True, padx=(0, 10))

        # 2. Quadro de Cálculo e Prova Real (Rascunho Livre)
        self.frame_prova_real = ctk.CTkFrame(self.frame_inferior, fg_color="#18181b", corner_radius=12, width=340)
        self.frame_prova_real.pack(side="right", fill="both", expand=True)

        self.montar_quadro_prova_real()
        self.montar_sliders()
        self.atualizar_calculos()

    def montar_quadro_prova_real(self):
        lbl_pr_titulo = ctk.CTkLabel(self.frame_prova_real, text="🧮 Bloco de Cálculo (Prova Real)", font=("Arial", 13, "bold"), text_color="#60a5fa")
        lbl_pr_titulo.pack(padx=10, pady=(8, 2))

        # Campo de entrada para expressões inteiras
        self.entry_expressao = ctk.CTkEntry(
            self.frame_prova_real, 
            placeholder_text="Digita o cálculo. Ex: 2 * pi * 5", 
            height=30,
            font=("Consolas", 12)
        )
        self.entry_expressao.pack(fill="x", padx=10, pady=5)

        btn_calcular = ctk.CTkButton(
            self.frame_prova_real, 
            text="Calcular & Provar", 
            fg_color="#2563eb", 
            hover_color="#1d4ed8",
            height=28, 
            command=self.verificar_calculo_manual
        )
        btn_calcular.pack(padx=10, pady=2)

        self.lbl_resultado_pr = ctk.CTkLabel(self.frame_prova_real, text="Dica: podes usar pi, sqrt(), +, -, *, /, **", font=("Arial", 10), text_color="gray")
        self.lbl_resultado_pr.pack(padx=10, pady=(4, 8))

    def verificar_calculo_manual(self):
        expressao = self.entry_expressao.get().strip()
        if not expressao:
            self.lbl_resultado_pr.configure(text="⚠️️ Digita uma expressão matemática", text_color="#fbbf24")
            return

        try:
            ambiente_seguro = {
                "pi": math.pi,
                "sqrt": math.sqrt,
                "pow": math.pow,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "abs": abs
            }
            expressao_formatada = expressao.replace(",", ".")
            resultado_user = float(eval(expressao_formatada, {"__builtins__": None}, ambiente_seguro))

            # Lista de valores aceites para a figura selecionada
            valores_aceitos = []

            if self.figura_atual == "Círculo":
                valores_aceitos = [math.pi * (self.raio ** 2), 2 * math.pi * self.raio]
            elif self.figura_atual == "Retângulo":
                valores_aceitos = [self.largura * self.altura, 2 * (self.largura + self.altura)]
            elif self.figura_atual == "Triângulo":
                valores_aceitos = [(self.largura * self.altura) / 2, math.sqrt(self.largura**2 + self.altura**2)]
            elif self.figura_atual == "Esfera":
                valores_aceitos = [(4/3) * math.pi * (self.raio ** 3), 4 * math.pi * (self.raio ** 2)]
            elif self.figura_atual == "Cilindro":
                valores_aceitos = [math.pi * (self.raio ** 2) * self.altura, 2 * math.pi * self.raio * (self.raio + self.altura)]

            correto = any(abs(resultado_user - val) < 0.5 for val in valores_aceitos)

            if correto:
                self.lbl_resultado_pr.configure(
                    text=f"✅ Teu cálculo: {resultado_user:.2f} (Correto!)", 
                    text_color="#4ade80"
                )
            else:
                self.lbl_resultado_pr.configure(
                    text=f"❌ Teu cálculo: {resultado_user:.2f} (Verifica as fórmulas)", 
                    text_color="#f87171"
                )

        except Exception:
            self.lbl_resultado_pr.configure(text="⚠️ Expressão inválida!", text_color="#fbbf24")

    def trocar_figura(self, figura):
        self.figura_atual = figura
        self.lbl_resultado_pr.configure(text="Dica: podes usar pi, sqrt(), +, -, *, /, **", text_color="gray")
        self.entry_expressao.delete(0, "end")
        self.montar_sliders()
        self.atualizar_calculos()

    def montar_sliders(self):
        for widget in self.frame_controles.winfo_children():
            widget.destroy()

        if self.figura_atual in ["Círculo", "Esfera"]:
            self.add_slider("Raio (r)", self.raio, 1, 10, self.update_raio)
        elif self.figura_atual in ["Retângulo", "Triângulo"]:
            self.add_slider("Base (b)", self.largura, 1, 10, self.update_largura)
            self.add_slider("Altura (h)", self.altura, 1, 10, self.update_altura)
        elif self.figura_atual == "Cilindro":
            self.add_slider("Raio (r)", self.raio, 1, 10, self.update_raio)
            self.add_slider("Altura (h)", self.altura, 1, 10, self.update_altura)

    def add_slider(self, label_text, initial_val, min_v, max_v, callback):
        row = ctk.CTkFrame(self.frame_controles, fg_color="transparent")
        row.pack(fill="x", padx=15, pady=6)

        lbl = ctk.CTkLabel(row, text=label_text, width=70, anchor="w")
        lbl.pack(side="left")

        slider = ctk.CTkSlider(row, from_=min_v, to=max_v, number_of_steps=90, command=lambda v: callback(v, val_lbl))
        slider.set(initial_val)
        slider.pack(side="left", fill="x", expand=True, padx=8)

        val_lbl = ctk.CTkLabel(row, text=f"{initial_val:.1f} cm", width=55)
        val_lbl.pack(side="right")

    def update_raio(self, val, val_lbl):
        self.raio = float(val)
        val_lbl.configure(text=f"{self.raio:.1f} cm")
        self.atualizar_calculos()

    def update_largura(self, val, val_lbl):
        self.largura = float(val)
        val_lbl.configure(text=f"{self.largura:.1f} cm")
        self.atualizar_calculos()

    def update_altura(self, val, val_lbl):
        self.altura = float(val)
        val_lbl.configure(text=f"{self.altura:.1f} cm")
        self.atualizar_calculos()

    def atualizar_calculos(self):
        self.canvas.delete("all")
        cx, cy = 200, 125

        self.txt_formulas.configure(state="normal")
        self.txt_formulas.delete("1.0", "end")

        if self.figura_atual == "Círculo":
            area = math.pi * (self.raio ** 2)
            circ = 2 * math.pi * self.raio

            self.lbl_m1.configure(text=f"Área (A)\n{area:.2f} cm²")
            self.lbl_m2.configure(text=f"Circunferência (C)\n{circ:.2f} cm")
            self.txt_formulas.insert("end", f"FÓRMULAS E CÁLCULO:\n\nA = π · r² = π · {self.raio:.1f}² ≈ {area:.2f} cm²\nC = 2 · π · r = 2 · π · {self.raio:.1f} ≈ {circ:.2f} cm")

            r_px = self.raio * 11
            self.canvas.create_oval(cx - r_px, cy - r_px, cx + r_px, cy + r_px, fill="#000000", outline="#3b82f6", width=2)
            self.canvas.create_oval(cx - 3, cy - 3, cx + 3, cy + 3, fill="#60a5fa", outline="")
            self.canvas.create_line(cx, cy, cx + r_px, cy, fill="#60a5fa", width=2, dash=(4, 2))
            self.canvas.create_text(cx + r_px/2, cy - 12, text=f"r = {self.raio:.1f} cm", fill="#ffffff", font=("Arial", 11, "bold"))

        elif self.figura_atual == "Retângulo":
            area = self.largura * self.altura
            perim = 2 * (self.largura + self.altura)

            self.lbl_m1.configure(text=f"Área (A)\n{area:.2f} cm²")
            self.lbl_m2.configure(text=f"Perímetro (P)\n{perim:.2f} cm")
            self.txt_formulas.insert("end", f"FÓRMULAS E CÁLCULO:\n\nA = b · h = {self.largura:.1f} · {self.altura:.1f} = {area:.2f} cm²\nP = 2·(b + h) = 2·({self.largura:.1f} + {self.altura:.1f}) = {perim:.2f} cm")

            w_px, h_px = self.largura * 10, self.altura * 10
            x1, y1 = cx - w_px, cy - h_px
            x2, y2 = cx + w_px, cy + h_px
            
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="#1d4ed8", outline="#60a5fa", width=2)
            self.canvas.create_text(cx, y2 + 14, text=f"b = {self.largura:.1f} cm", fill="#ffffff", font=("Arial", 11, "bold"))
            self.canvas.create_text(x2 + 35, cy, text=f"h = {self.altura:.1f} cm", fill="#ffffff", font=("Arial", 11, "bold"))

        elif self.figura_atual == "Triângulo":
            area = (self.largura * self.altura) / 2
            hip = math.sqrt(self.largura**2 + self.altura**2)

            self.lbl_m1.configure(text=f"Área (A)\n{area:.2f} cm²")
            self.lbl_m2.configure(text=f"Hipotenusa (c)\n{hip:.2f} cm")
            self.txt_formulas.insert("end", f"FÓRMULAS E CÁLCULO:\n\nA = (b · h) / 2 = ({self.largura:.1f} · {self.altura:.1f}) / 2 = {area:.2f} cm²\nc = √(b² + h²) = √({self.largura:.1f}² + {self.altura:.1f}²) ≈ {hip:.2f} cm")

            w_px, h_px = self.largura * 12, self.altura * 12
            x_left, x_right = cx - w_px/2, cx + w_px/2
            y_bottom, y_top = cy + h_px/2, cy - h_px/2
            
            pts = [x_left, y_bottom, x_right, y_bottom, x_left, y_top]
            self.canvas.create_polygon(pts, fill="#16a34a", outline="#4ade80", width=2)
            self.canvas.create_text(cx, y_bottom + 14, text=f"b = {self.largura:.1f} cm", fill="#ffffff", font=("Arial", 11, "bold"))
            self.canvas.create_text(x_left - 30, cy, text=f"h = {self.altura:.1f} cm", fill="#ffffff", font=("Arial", 11, "bold"))
            self.canvas.create_text(cx + 10, cy - 10, text=f"c = {hip:.1f} cm", fill="#a7f3d0", font=("Arial", 10, "italic"))

        elif self.figura_atual == "Esfera":
            vol = (4/3) * math.pi * (self.raio ** 3)
            area_sup = 4 * math.pi * (self.raio ** 2)

            self.lbl_m1.configure(text=f"Volume (V)\n{vol:.2f} cm³")
            self.lbl_m2.configure(text=f"Área Sup.\n{area_sup:.2f} cm²")
            self.txt_formulas.insert("end", f"FÓRMULAS E CÁLCULO:\n\nV = (4/3)·π·r³ = (4/3)·π·{self.raio:.1f}³ ≈ {vol:.2f} cm³\nA = 4·π·r² = 4·π·{self.raio:.1f}² ≈ {area_sup:.2f} cm²")

            r_px = self.raio * 11
            self.canvas.create_oval(cx - r_px, cy - r_px, cx + r_px, cy + r_px, fill="#2563eb", outline="#60a5fa", width=2)
            self.canvas.create_oval(cx - r_px, cy - r_px/3, cx + r_px, cy + r_px/3, outline="#93c5fd", width=1)
            self.canvas.create_line(cx, cy, cx + r_px, cy, fill="#ffffff", width=2, dash=(4, 2))
            self.canvas.create_text(cx + r_px/2, cy - 12, text=f"r = {self.raio:.1f} cm", fill="#ffffff", font=("Arial", 11, "bold"))

        elif self.figura_atual == "Cilindro":
            vol = math.pi * (self.raio ** 2) * self.altura
            area_sup = 2 * math.pi * self.raio * (self.raio + self.altura)

            self.lbl_m1.configure(text=f"Volume (V)\n{vol:.2f} cm³")
            self.lbl_m2.configure(text=f"Área Sup.\n{area_sup:.2f} cm²")
            self.txt_formulas.insert("end", f"FÓRMULAS E CÁLCULO:\n\nV = π·r²·h = π·{self.raio:.1f}²·{self.altura:.1f} ≈ {vol:.2f} cm³\nA = 2·π·r·(r+h) = 2·π·{self.raio:.1f}·({self.raio:.1f}+{self.altura:.1f}) ≈ {area_sup:.2f} cm²")

            r_px, h_px = self.raio * 9, self.altura * 8
            self.canvas.create_rectangle(cx - r_px, cy - h_px/2, cx + r_px, cy + h_px/2, fill="#2563eb", outline="")
            self.canvas.create_oval(cx - r_px, cy - h_px/2 - r_px/3, cx + r_px, cy - h_px/2 + r_px/3, fill="#60a5fa", outline="#93c5fd")
            self.canvas.create_oval(cx - r_px, cy + h_px/2 - r_px/3, cx + r_px, cy + h_px/2 + r_px/3, fill="#1d4ed8", outline="#60a5fa")
            self.canvas.create_line(cx, cy - h_px/2, cx + r_px, cy - h_px/2, fill="#ffffff", width=2, dash=(3, 2))
            self.canvas.create_text(cx + r_px/2, cy - h_px/2 - 12, text=f"r = {self.raio:.1f} cm", fill="#ffffff", font=("Arial", 10, "bold"))
            self.canvas.create_text(cx + r_px + 35, cy, text=f"h = {self.altura:.1f} cm", fill="#ffffff", font=("Arial", 11, "bold"))

        self.txt_formulas.configure(state="disabled")

if __name__ == "__main__":
    app = CalculadoraGeometrica()
    app.mainloop()