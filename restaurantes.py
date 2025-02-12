class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = True    
        Restaurante.restaurantes.append(self)    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes(self):
        for r in Restaurante.restaurantes:
            print(f'{r.nome} | {r.categoria} | {r.ativo}')

restaurante_praca = Restaurante('Cadu', 'sushi')
restaurante_pizza = Restaurante('Vitoria', 'Poke')

Restaurante.listar_restaurantes(Restaurante)