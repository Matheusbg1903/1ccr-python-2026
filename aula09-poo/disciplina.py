class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def exibir_infos(self):
        print(f"disciplina: {self.nome} | Prof: {self.professor}")

#TEMPORÁRIO
# python = disciplina("PCP", "Russi")
# print(python.professor)
# python.exibir_infos()