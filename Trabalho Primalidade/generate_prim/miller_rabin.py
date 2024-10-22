import random
rand = random.SystemRandom() # A single dice.
import time

def single_test(n, a):
    """
    Realiza um único teste de primalidade de Miller-Rabin para um número n com uma base a.

    Args:
        n (int): O número a ser testado.
        a (int): A base aleatória escolhida para o teste.

    Returns:
        bool: Retorna True se n passar no teste de Miller-Rabin para a base a, indicando que n é provavelmente primo. 
        Retorna False se n for composto.
    """

    exp = n - 1
    # Divide n - 1 por 2 até que exp seja ímpar
    # Isso encontra a maior potência de 2 que divide n - 1, ou seja, escreve n - 1 como 2^r * d
    while not exp & 1: # Enquanto exp for par (último bit 0)
        exp >>= 1       # Divide exp por 2 
        
    # Se a^exp ≡ 1 (mod n), n passa no teste de Miller-Rabin para a base a
    if pow(a, exp, n) == 1:
        return True
    
    # Testa sucessivas potências de 2 * exp para ver se alguma é congruente a n - 1 (mod n)
    while exp < n - 1:
        if pow(a, exp, n) == n - 1:
            return True  # Se alguma potência atingir n - 1, n passa no teste para essa base a
            
        exp <<= 1 # Multiplica exp por 2 (bit shift para esquerda)
    
    # Se nenhuma das condições acima foi satisfeita, n é composto para essa base a
    return False
    
def miller_rabin(n, k=40):
    """
    Implementa o teste probabilístico de Miller-Rabin para determinar se um número n é primo.

    Args:
        n (int): O número a ser testado.
        k (int): O número de iterações para aumentar a confiança no resultado. 
                 Quanto maior k, maior a certeza do resultado (padrão é 40).

    Returns:
        bool: Retorna True se n é provavelmente primo, ou False se for composto.
    """
    # Casos iniciais
    if (n<= 2):
        return False # 0, 1, 2 e números negativos não são considerados primos
    if not (n & 1):
        return False # Não pode ser par

    for i in range(k):
        a = rand.randrange(2, n - 1)  # Escolhe uma base a aleatória no intervalo [2, n-2]
        if not single_test(n, a):
            return False
            
    return True
    


            
