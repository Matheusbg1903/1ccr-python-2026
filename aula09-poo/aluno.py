from disciplina import Disciplina
class aluno:
    def __init__(self, nome, rm, curso):
        self.nome = nome
        self.rm = rm
        self.curso = curso
        self.disciplinas = [] # array  [Disciplina, Disciplina, ....]
        self.notas_por_diciplinas = {}

    def matricular(self, disciplina: Disciplina):
        self.disciplinas.append(disciplina)
        self.notas_por_diciplinas.setdefault(disciplina.nome,[])

    def adicionar_nota(self, d: Disciplina, nota: float):
        self.notas_por_diciplinas[d.nome].append(nota)

    def calcular_media_d(self, d: Disciplina) -> float:
        notas = self.notas_por_diciplinas.get(d.nome, [])
        return sum(notas) / len(notas)