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

# Exemplo de uso:
if __name__ == "__main__":
    # Semente inicial
    seed = 0x123456789ABCDEF123456789ABCDEF123456789ABCDEF123456789ABCDEF1234  # Exemplo de semente de 4096 bits
    
    # Taps selecionados com base em um polinômio primitivo (para garantir boa aleatoriedade)
    taps = [4095, 4093, 4089, 4080]  # Exemplo de taps (posições onde o XOR será aplicado)

    # Inicializa o LFSR com 4096 bits
    lfsr = LFSR(seed=seed, taps=taps)

    nbits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    # Gera números aleatórios de 64 bits

    for nbit in nbits:
        random_number = lfsr.get_random_bits(nbit)
        print(f"Número aleatório: {random_number:#0{18}x}")
        print(f"Bits: {random_number.bit_length()}")

    if len(sys.argv) != 1:
        print(f"Informe o numero de bits do numero aleatorio a ser gerado")
        sys.exit(1)


