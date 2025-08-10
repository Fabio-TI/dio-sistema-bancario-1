class Veiculo:
    def __init__(self, cor, placa, n_rodas):
        self.cor = cor
        self.placa = placa
        self.n_rodas = n_rodas

    def ligar_motor(self):
        print("Motor ligado")

class Carro(Veiculo):
    pass


class Motocicleta(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, n_rodas, carregado):
        self.carregado = carregado

    def estado_carregado(self):
        print(f"{"Sim" if self.carregado else "Não"} estou carregado")
        

moto = Motocicleta("preta", "ABC-1234", 2)
moto.ligar_motor()

carro = Carro("branco", "XYZ-5678", 4)
carro.ligar_motor()

caminhao = Caminhao("azul", "LMN-9012", 8, True)
caminhao.ligar_motor()
caminhao.estado_carregado()