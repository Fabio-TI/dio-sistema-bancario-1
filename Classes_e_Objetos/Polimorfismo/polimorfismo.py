class Passaro:
    def voar(self):
        print("voando....")


class Pardal(Passaro):
    def voar(self):
        super().voar()      

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa, corre rápido!")


class Aviao(Passaro):
    def voar(self):
        print("Avião decolando!")


def plano_de_voo(obj):
    obj.voar()


plano_de_voo(Pardal())  # Saída: voando....
plano_de_voo(Avestruz())  # Saída: Não voa, corre rápido!
plano_de_voo(Aviao())