from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Restaurante da Praça', 'Tradicional')
#restaurante_mexicano = Restaurante('Mexican', 'Mexicano')
#restaurante_japa = Restaurante('Sushi House', 'Japonesa')
restaurante_praca.receber_avaliacao('João', 5)
restaurante_praca.receber_avaliacao('Maria', 10)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()