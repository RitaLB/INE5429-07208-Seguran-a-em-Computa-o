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
