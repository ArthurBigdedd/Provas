class Veiculo:
    def movimentar(self):
        print("Veículo está em movimento.")

class Carro(Veiculo):
    def movimentar(self):
        print("Carro está dirigindo.")

class Moto(Veiculo):
    def movimentar(self):
        print("Moto está acelerando.")

meu_carro = Carro()
minha_moto = Moto()
veiculo_generico = Veiculo()

veiculo_generico.movimentar()
meu_carro.movimentar()
minha_moto.movimentar()