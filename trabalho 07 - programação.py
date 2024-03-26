def soma_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return soma, media

def substituir_palavra(lista, palavra_antiga, palavra_nova):
    return [palavra_nova if palavra == palavra_antiga else palavra for palavra in lista]

def gerar_triangulo(num_linhas):
    for i in range(1, num_linhas + 1):
        print('*' * i)

# Testando as funções
if __name__ == "__main__":
    # Teste da função soma_media
    lista_numeros = [1, 2, 3, 4]
    soma, media = soma_media(lista_numeros)
    print("Soma:", soma)
    print("Média:", media)

    # Teste da função substituir_palavra
    lista_palavras = ["banana", "morango", "limão"]
    palavra_antiga = "limão"
    palavra_nova = "laranja"
    nova_lista = substituir_palavra(lista_palavras, palavra_antiga, palavra_nova)
    print("Lista alterada:", nova_lista)

    # Teste da função gerar_triangulo
    num_linhas = 5
    print("Triângulo:")
    gerar_triangulo(num_linhas)
