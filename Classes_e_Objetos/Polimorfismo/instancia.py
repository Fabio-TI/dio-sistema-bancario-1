class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula


    def __str__(self):
        return f"Nome: {self.nome} - Matrícula: {self.matricula} - Escola: {self.escola}"

def mostrar_valores(objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovana", 2)
mostrar_valores([aluno_1, aluno_2])


aluno_1.matricula = 3
mostrar_valores([aluno_1, aluno_2])

Estudante.escola = "Python"
aluno_3 = Estudante("Fabio", 4)
mostrar_valores([aluno_1, aluno_2, aluno_3])