def conta_palavra_a(frase):
    # Converte a frase para minúsculas para garantir que "a" e "A" sejam tratados igualmente
    minusculas = frase.lower()
    # Conta quantas vezes a palavra "a" aparece
    count = minusculas.count('a')
    return count

# Chamando a função
frase = input("Digite o nome: ")
quantidade = conta_palavra_a(frase)
print(f'A palavra "a" aparece {quantidade} vezes na frase.')