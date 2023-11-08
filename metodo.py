import math

def f(x):
    return math.exp(x) - x - 2

def bissecao(f, a, b, epsilon):
    if f(a) * f(b) > 0:
        raise ValueError("A função não muda de sinal no intervalo dado.")
    
    iteracoes = 0  # Inicialize a contagem de iterações
    
    while (b - a) / 2 > epsilon:
        c = (a + b) / 2
        iteracoes += 1  # Incrementar a contagem de iterações
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    
    raiz = (a + b) / 2
    return raiz, iteracoes

# Defina o intervalo e a tolerância
a = -2
b = 0
epsilon = 1e-3

# Encontre a raiz e obtenha o número de iterações
raiz, num_iteracoes = bissecao(f, a, b, epsilon)

print(f"A raiz da função é aproximadamente {raiz:.6f}")
print(f"Foram necessárias {num_iteracoes} iterações para encontrar a raiz.")
