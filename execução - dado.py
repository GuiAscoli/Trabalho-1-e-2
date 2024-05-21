import random

def lancamento_dado():
    resultado = random.randint(1, 6)
    return resultado

# Testando a função
resultado_lancamento = lancamento_dado()
print("O resultado do lançamento do dado é:", resultado_lancamento)