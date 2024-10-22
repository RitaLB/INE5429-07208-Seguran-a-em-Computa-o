import sys

class Xorshift:

    # Xorshift formula: 
    # X⊕=(X≫a),
    # X⊕=(X≪b),
    # X⊕=(X≫c) 
    # em que x é o estado atual
    def __init__(self, seed: int = 2**32 -1 , mod: int = 2** 32 -1):
        self.x = seed
        self.mod = mod # O mod vai determinar a quantidade de bits máxima dos números gerados

    def change_mod(self, mod: int = 2** 32 -1):
        self.mod = mod

    def random_number(self, bits = 2** 32 -1) -> int:
        self.change_mod(mod=2**bits)

        self.x ^= (self.x >> 13)
        self.x = self.x % self.mod # Aplicando aqui o mod pra deixar o número dentro do intervalo desejado
        self.x ^= (self.x << 17)
        self.x = self.x % self.mod
        self.x ^= (self.x >> 5)
        self.x = self.x % self.mod
        return self.x 

    # Exemplo de uso:

'''
if __name__ == '__main__':

    if len(sys.argv) != 1:
        print(f"Informe o numero de bits do numero aleatorio a ser gerado")
        sys.exit(1)

    # Pegando os valores dos argumentos
    nbit = sys.argv[1]

    #nbits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    random_generator = Xorshift(seed=12345) # Tanto faz a semente
    random_generator.change_mod(mod=2**nbit)
    number = random_generator.random_number()
    print(f"Numero aleatorio de até {nbit} bits: {number}")
    print(f"Numero de bits: {number.bit_length()}")
'''
def test_xorshift_40():
    random_generator = Xorshift(seed=12345) # Tanto faz a semente
    random_generator.change_mod(mod=2**40)
    number = random_generator.random_number()
    print(f"Numero aleatorio de até {40} bits: {number}")
    print(f"Numero de bits: {number.bit_length()}")

def test_xorshift_80():
    random_generator = Xorshift(seed=12345) # Tanto faz a semente
    random_generator.change_mod(mod=2**40)
    number = random_generator.random_number()
    print(f"Numero aleatorio de até {40} bits: {number}")
    print(f"Numero de bits: {number.bit_length()}")

#__benchmarks__ = [(test_xorshift_40, test_xorshift_80, "numero 40 bits / numero 80 bits")]

def sort_seven():
    """Sort a list of seven items"""
    for _ in range(10_000):
        sorted([3,2,4,5,1,5,3])

def sort_three():
    """Sort a list of three items"""
    for _ in range(10_000):
        sorted([3,2,4])

__benchmarks__ = [
    (sort_seven, sort_three, "Sorting 3 items instead of 7")
]