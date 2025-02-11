class Resturante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = True    

restaurante_praca = Resturante('Cadu', 'sushi')
restaurante_pizza = Resturante('Vitoria', 'Poke')

restaurantes = [restaurante_praca, restaurante_pizza]
print(vars(restaurante_praca))