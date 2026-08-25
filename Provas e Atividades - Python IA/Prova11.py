class Animal:
    def falar(self):
        print("Este animal faz um som genérico.")

class Cachorro:
    def falar(self):
        print("O cachorro está latindo.")

class Gato:
    def falar(self):
        print("O gato está miando.")
        
animal_generico = Animal()
meu_cachorro = Cachorro()
meu_gato = Gato()

animal_generico.falar()
meu_cachorro.falar()
meu_gato.falar()