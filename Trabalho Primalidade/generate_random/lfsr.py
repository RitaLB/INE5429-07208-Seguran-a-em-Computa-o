import sys

class LFSR:
    def __init__(self, seed: int, taps: list):
        """
        Inicializa o LFSR com uma semente inicial, pontos de realimentação (taps) e tamanho do registro.

        Args:
            seed (int): O valor inicial para o registro de deslocamento, deve ser até o tamanho de 4096 bits.
            taps (list): Lista de posições de realimentação, onde as operações XOR serão aplicadas.
            size (int): O número de bits no registro (por padrão, 4096 bits).
        """
        self.state = seed  # A semente inicial determina o estado inicial do LFSR.
        self.size = seed.bit_length()   # Define o tamanho do registro de deslocamento. Será o número de bits da seed fornecisa
        self.taps = taps   # Posições no registro onde as operações XOR serão aplicadas.

    def step(self):
        """
        Realiza um passo do LFSR, calculando o próximo estado com base nos taps.

        Returns:
            int: O próximo valor do estado após um passo.
        """
        # Aplica a operação XOR nas posições de realimentação (taps).
        feedback = self.state & 1 # O bit menos significativo do state é o bit de realimentação.
        for tap in self.taps:
            # Extrai o bit na posição 'tap' e faz XOR com 'feedback'.
            feedback ^= (self.state >> tap) & 1

        # Desloca o estado para a direita (shift), inserindo o bit de feedback à esquerda.
        self.state = (self.state >> 1) | (feedback << (self.size - 1))
 
        return self.state

    def get_random_bits(self, num_bits: int):
        """
        Gera um número aleatório de num_bits bits, realizando vários passos do LFSR.

        Args:
            num_bits (int): O número de bits aleatórios a gerar.

        Returns:
            int: Um número aleatório com o número de bits especificado.
        """
        result = 0
        for _ in range(num_bits):
            # Faz um passo do LFSR e adiciona o bit menos significativo ao resultado.
            result = (result << 1) | (self.step() & 1)
        return result



