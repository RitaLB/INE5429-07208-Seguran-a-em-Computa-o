import perfplot
import os, sys
import pandas as pd
import logging
#import random
#rand = random.SystemRandom() # A single dice.

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/generate_prim")
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/generate_random")

from fermat import fermat_primality_test
from miller_rabin import miller_rabin
from xorshift import Xorshift

# Configuração do logging para salvar a saída no arquivo
logging.basicConfig(filename='benchmark_agreement.txt', level=logging.INFO, format='%(message)s')


def compare_prim_generators(nbits, n_samples = 10000):
    rand = Xorshift(seed = 2**32 - 1) # Como tem a mesma semente, os números gerados serão os mesmos para os dois testes
    disagreed_primes = {"fermat" : [], "miller_rabin" : []}
    disagreements = 0
    agreements = 0
    founded_primes = 0

    for _ in range(n_samples):
        while True:
            num = (rand.random_number(nbits) << 1) + 1
            result_fermat = fermat_primality_test(num)
            result_miller_rabin = miller_rabin(num)

            if result_fermat | result_miller_rabin:
                founded_primes +=1 
                if result_fermat != result_miller_rabin:
                    if result_fermat:
                        disagreed_primes["fermat"].append(num)
                    else:
                        disagreed_primes["miller_rabin"].append(num)
                    disagreements += 1
                    break
                else:
                    agreements += 1
                    break
            else: 
                agreements += 1

    return (disagreements, agreements, disagreed_primes, founded_primes)
     
def benchmark():
    nbits = [(40, 1000), (56, 1000), (80, 1000), (128, 1000), (168, 1000), (224, 1000), (256, 100), (512, 100), (1024, 10), (2048, 10), (4096, 5)]
    for (nbit, nprim) in nbits:
        disagreements, agreements, disagreed_primes, founded_primes = compare_prim_generators(nbit, nprim)
        logging.info(f"Founds for {nbit} bits: {founded_primes}")
        logging.info(f"Disagreements for {nbit} bits: {disagreements}")
        logging.info(f"Agreements for {nbit} bits: {agreements}")
        logging.info(f"Disagreed primes for {nbit} bits: {disagreed_primes}")
        logging.info("Total tested numbers: " + str(agreements + disagreements))
        logging.info("\n")
    
if __name__ == "__main__":
    benchmark()