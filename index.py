from math import pi, sqrt
from typing import Dict, List, Union


class FormaGeometrica:
    """Classe base para todas as formas geométricas."""
    
    def __init__(self, nome: str):
        self.nome = nome

    def obter_informacoes(self) -> Dict[str, Union[str, float, Dict[str, str]]]:
        raise NotImplementedError("Método deve ser implementado pelas subclasses.")


# ==========================================
# FIGURAS GEOMÉTRICAS PLANAS (2D)
# ==========================================

class Forma2D(FormaGeometrica):
    """Classe base para figuras bidimensionais."""
    
    def calcular_area(self) -> float:
        raise NotImplementedError

    def calcular_perimetro(self) -> float:
        raise NotImplementedError


class Circulo(Forma2D):
    def __init__(self, raio: float):
        super().__init__("Círculo")
        if raio <= 0:
            raise ValueError("O raio deve ser um número positivo.")
        self.raio = raio

    def calcular_area(self) -> float:
        return pi * (self.raio ** 2)

    def calcular_perimetro(self) -> float:
        return 2 * pi * self.raio

    def obter_informacoes(self) -> dict:
        return {
            "nome": self.nome,
            "propriedades": {"Raio": self.raio},
            "formulas": {
                "Área": "π * r²",
                "Perímetro": "2 * π * r"
            },
            "resultados": {
                "Área": round(self.calcular_area(), 2),
                "Perímetro": round(self.calcular_perimetro(), 2)
            }
        }


class Retangulo(Forma2D):
    def __init__(self, largura: float, altura: float):
        super().__init__("Retângulo")
        if largura <= 0 or altura <= 0:
            raise ValueError("Largura e altura devem ser positivas.")
        self.largura = largura
        self.altura = altura

    def calcular_area(self) -> float:
        return self.largura * self.altura

    def calcular_perimetro(self) -> float:
        return 2 * (self.largura + self.altura)

    def obter_informacoes(self) -> dict:
        return {
            "nome": self.nome,
            "propriedades": {"Largura": self.largura, "Altura": self.altura},
            "formulas": {
                "Área": "base * altura",
                "Perímetro": "2 * (base + altura)"
            },
            "resultados": {
                "Área": round(self.calcular_area(), 2),
                "Perímetro": round(self.calcular_perimetro(), 2)
            }
        }


class TrianguloRetangulo(Forma2D):
    def __init__(self, base: float, altura: float):
        super().__init__("Triângulo Retângulo")
        if base <= 0 or altura <= 0:
            raise ValueError("Base e altura devem ser positivas.")
        self.base = base
        self.altura = altura

    def calcular_hipotenusa(self) -> float:
        return sqrt(self.base**2 + self.altura**2)

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

    def calcular_perimetro(self) -> float:
        return self.base + self.altura + self.calcular_hipotenusa()

    def obter_informacoes(self) -> dict:
        return {
            "nome": self.nome,
            "propriedades": {
                "Base": self.base, 
                "Altura": self.altura,
                "Hipotenusa": round(self.calcular_hipotenusa(), 2)
            },
            "formulas": {
                "Área": "(base * altura) / 2",
                "Perímetro": "base + altura + hipotenusa",
                "Hipotenusa": "√(base² + altura²)"
            },
            "resultados": {
                "Área": round(self.calcular_area(), 2),
                "Perímetro": round(self.calcular_perimetro(), 2)
            }
        }


# ==========================================
# FIGURAS GEOMÉTRICAS ESPACIAIS (3D)
# ==========================================

class Forma3D(FormaGeometrica):
    """Classe base para figuras tridimensionais."""
    
    def calcular_volume(self) -> float:
        raise NotImplementedError

    def calcular_area_superficial(self) -> float:
        raise NotImplementedError


class Esfera(Forma3D):
    def __init__(self, raio: float):
        super().__init__("Esfera")
        if raio <= 0:
            raise ValueError("O raio deve ser um número positivo.")
        self.raio = raio

    def calcular_volume(self) -> float:
        return (4 / 3) * pi * (self.raio ** 3)

    def calcular_area_superficial(self) -> float:
        return 4 * pi * (self.raio ** 2)

    def obter_informacoes(self) -> dict:
        return {
            "nome": self.nome,
            "propriedades": {"Raio": self.raio},
            "formulas": {
                "Volume": "(4/3) * π * r³",
                "Área Superficial": "4 * π * r²"
            },
            "resultados": {
                "Volume": round(self.calcular_volume(), 2),
                "Área Superficial": round(self.calcular_area_superficial(), 2)
            }
        }


class Cilindro(Forma3D):
    def __init__(self, raio: float, altura: float):
        super().__init__("Cilindro")
        if raio <= 0 or altura <= 0:
            raise ValueError("Raio e altura devem ser positivos.")
        self.raio = raio
        self.altura = altura

    def calcular_volume(self) -> float:
        return pi * (self.raio ** 2) * self.altura

    def calcular_area_superficial(self) -> float:
        area_base = pi * (self.raio ** 2)
        area_lateral = 2 * pi * self.raio * self.altura
        return 2 * area_base + area_lateral

    def obter_informacoes(self) -> dict:
        return {
            "nome": self.nome,
            "propriedades": {"Raio": self.raio, "Altura": self.altura},
            "formulas": {
                "Volume": "π * r² * h",
                "Área Superficial": "2 * π * r * (r + h)"
            },
            "resultados": {
                "Volume": round(self.calcular_volume(), 2),
                "Área Superficial": round(self.calcular_area_superficial(), 2)
            }
        }


# ==========================================
# GERENCIADOR DO SISTEMA DE ESTUDOS
# ==========================================

class GerenciadorDeEstudos:
    """Gerencia o histórico de cálculos do aluno e relatórios."""
    
    def __init__(self, nome_aluno: str):
        self.nome_aluno = nome_aluno
        self.historico_consultas: List[FormaGeometrica] = []

    def calcular_e_registrar(self, forma: FormaGeometrica) -> dict:
        self.historico_consultas.append(forma)
        return forma.obter_informacoes()

    def gerar_relatorio_estudo(self) -> None:
        print(f"\n==========================================")
        print(f" RELATÓRIO DE ESTUDOS - ALUNO: {self.nome_aluno.upper()}")
        print(f" Total de formas calculadas: {len(self.historico_consultas)}")
        print(f"==========================================\n")
        
        for idx, forma in enumerate(self.historico_consultas, 1):
            info = forma.obter_informacoes()
            print(f"--- Formato {idx}: {info['nome']} ---")
            print("Propriedades:", info['propriedades'])
            print("Fórmulas:", info['formulas'])
            print("Resultados:", info['resultados'])
            print("-" * 40)


# ==========================================
# EXEMPLO DE USO / EXECUÇÃO
# ==========================================

if __name__ == "__main__":
    # Inicializando o sistema para um aluno
    sistema = GerenciadorDeEstudos("Lucas Santos")

    # Criando objetos geométricos
    circulo = Circulo(raio=5.0)
    retangulo = Retangulo(largura=4.0, altura=8.0)
    triangulo = TrianguloRetangulo(base=3.0, altura=4.0)
    esfera = Esfera(raio=3.0)
    cilindro = Cilindro(raio=2.0, altura=6.0)

    # Registrando cálculos no sistema
    sistema.calcular_e_registrar(circulo)
    sistema.calcular_e_registrar(retangulo)
    sistema.calcular_e_registrar(triangulo)
    sistema.calcular_e_registrar(esfera)
    sistema.calcular_e_registrar(cilindro)

    # Exibindo o relatório consolidado
    sistema.gerar_relatorio_estudo()