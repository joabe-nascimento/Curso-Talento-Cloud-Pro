# Lista original de produtos
lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

# Atualização da lista de produtos
lista_produtos[1] = 'rímel'  # Substituindo 'batons' por 'rímel'
lista_produtos[4] = 'cremes hidratantes'  # Substituindo 'loções' por 'cremes hidratantes'
lista_produtos.remove('delineadores')  # Removendo 'delineadores'

# Adicionando dois novos produtos
lista_produtos.append('protetor solar')  # Adicionando 'protetor solar'
lista_produtos.append('perfume sólido')  # Adicionando 'perfume sólido'

# Imprimindo a nova lista de produtos
print(lista_produtos)
