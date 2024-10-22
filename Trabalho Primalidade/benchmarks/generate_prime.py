import perfplot
import os, sys
import pandas as pd
#import random
#rand = random.SystemRandom() # A single dice.

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/generate_prim")
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/generate_random")

from fermat import fermat_primality_test
from miller_rabin import miller_rabin
from xorshift import Xorshift

dict_primes_miller_rabin = dict()
dict_primes_fermat = dict()

def fermat_test(nbits):
        rand = Xorshift(seed = 2**32 - 1) # Como tem a mesma semente, os números gerados serão os mesmos para os dois testes
        while True:
            # Guarantees that a is odd.
            num = (rand.random_number(nbits) << 1) + 1
            if fermat_primality_test(num):
                dict_primes_fermat[nbits] = num
                return num

def miller_rabin_test(nbits):
        rand = Xorshift(seed = 2**32 - 1) # Como tem a mesma semente, os números gerados serão os mesmos para os dois testes
        while True:
            # Guarantees that a is odd.
            num = (rand.random_number(nbits) << 1) + 1
            if miller_rabin(num):
                dict_primes_miller_rabin[nbits] = num
                return num
    
def benchmark():
    
    # Criação dos gráficos comparativos
    bench = perfplot.bench(
        setup=lambda n: n, # Número de bits,
        kernels=[
            lambda bits: miller_rabin_test(bits),
            lambda bits: fermat_test(bits)
        ],
        labels=["Miller Rabin", "Fermat"],
        n_range=[40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096],
        xlabel="Número de bits",
        title="Comparação de desempenho: Xorshift vs LFSR",
        equality_check=None  # Desativa a verificação de igualdade
    )

    # Executa o benchmark e captura os resultados
    result = bench  # Aqui chamamos o bench diretamente

    # Extraindo os dados
    times = result.timings_s
    n_values = result.n_range
    labels = ["Xorshift", "LFSR"]
    primes_miller_rabin = []
    for (nbits, prime) in dict_primes_miller_rabin.items():
        primes_miller_rabin.append(prime)

    primes_fermat = []
    for (nbits, prime) in dict_primes_fermat.items():
        primes_fermat.append(prime)
         

    # Criando um DataFrame para armazenar os resultados
    #results = pd.DataFrame(zip(*times), columns=labels, index=n_values)

    results = pd.DataFrame({
        "Número de Bits": n_values,
        "Tempo Miller Rabin (s)": times[0],
        "Tempo Fermat (s)": times[1],
        "Primo Miller Rabin": primes_miller_rabin,
        "Primo Fermat": primes_fermat
    })

    # Mostrando a tabela
    print(results)

    # Opcional: Salvando a tabela em um arquivo CSV
    results.to_csv("prim_generations.csv", index_label="Número de Bits")

    # Gerando e mostrando o gráfico
    result.save("prim_generations.png")  # Salva o gráfico em um arquivo
    result.show()  # Mostra o gráfico na tela

if __name__ == "__main__":  
    benchmark()
