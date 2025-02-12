class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = True    #colocar o _ faz com que seja um atributo provado e as pessoas não conseguem acessar ele direto
        Restaurante.restaurantes.append(self)    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes(self):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | Ativo')
        for r in Restaurante.restaurantes:
            print(f'{r.nome.ljust(25)} | {r.categoria.ljust(25)} | {r.ativo}')

    @property
    def ativo(self):
        return '☑' if self._ativo else   '☐'

restaurante_praca = Restaurante('Cadu', 'sushi')
restaurante_pizza = Restaurante('Vitoria', 'Poke')

Restaurante.listar_restaurantes(Restaurante)