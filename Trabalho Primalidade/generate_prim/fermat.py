import random
rand = random.SystemRandom() # A single dice.

def fermat_primality_test(n, k = 40):
    """
    Teste de primalidade de Fermat.

    Args:
        n (int): Número a ser testado.
        k (int): Número de iterações para aumentar a confiança no resultado.

    Returns:
        bool: Retorna True se o número é provavelmente primo, caso contrário False.
    """
    if n < 2:
        return False
    elif n < 4:
        return True
    
    if not( n & 1):
        return False

    # Executa o teste de Fermat k vezes
    a_list = set([rand.randrange(2, n - 1) for _ in range(k)]) # Escolhe k bases aleatórias no intervalo [2, n-2]. Agrupei em um set p/ evitar repetições.
    for a in a_list:
        # se a é primo, a^(n-1) % n = 1
        if pow(a, n - 1, n) != 1:
            return False

    return True

