class Resturante:
    nome = ""
    categoria = ""
    ativo = True    

restaurante_praca = Resturante()
restaurante_pizza = Resturante()

restaurantes = [restaurante_praca, restaurante_pizza]
print(dir(restaurante_praca))