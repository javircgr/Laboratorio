class Alumno():
    def __init__(self, matricula, nombre, nota1, nota2, nota3):
        self.matricula  = matricula
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def dime_matricula(self):
        return self.matricula

    def dime_nombre(self):
        return self.nombre

    def dime_nota(self):
        nota_final = (self.nota1 + self.nota2 + self.nota3) / 3
        if 4.8 < nota_final or nota_final == 4.8:
            return 'APROBADO', nota_final
        else:
            return 'SUSPENSO', nota_final

alumno = Alumno(445, 'Alvaro', 2.7, 4, 5.2)
print('Numero de matricula: ', alumno.dime_matricula())
print('Nombre de alumno: ', alumno.dime_nombre())
print('Curso: ', alumno.dime_nota())
