from aluno import aluno # PascalCase
from disciplina import Disciplina

# criar / instanciar 1 aluno
aluno1 = aluno ("João", "1234566", "Ciência da Computação")
#print(aluno1.notas_por_disciplina)

#criar / instanciar 2 disciplinas
model_mat = Disciplina("Modelagem Mat.", "Roberto")
model_lin = Disciplina("Modelagem Lin.", "Rodolpho")
# print(model_lin.professor)
# model_lin.exibir_infos()

# matricular o aluno nas disciplinas
aluno1.matricular(model_mat)
aluno1.matricular(model_lin)
#print(aluno1.disciplinas[0].professor)
#aluno1.disciplinas[0].exibir_infos()

#adicionar notas referentes às disciplinas
aluno1.adicionar_nota(model_mat, 10)
aluno1.adicionar_nota(model_mat, 8)
aluno1.adicionar_nota(model_lin, 5)
aluno1.adicionar_nota(model_lin, 3)
#print(aluno1.notas_por_diciplinas)

print(aluno1.calcular_media_d(model_lin))