import perfplot
import os, sys
import pandas as pd

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/generate_random")

from xorshift import Xorshift
from lfsr import LFSR


# Implementação de LFSR para a quantidade de bits
seed = 0x123456789ABCDEF123456789ABCDEF123456789ABCDEF123456789ABCDEF1234  # Exemplo de semente de 4096 bits
# Taps selecionados com base em um polinômio primitivo (para garantir boa aleatoriedade)
taps = [4095, 4093, 4089, 4080]  # Exemplo de taps (posições onde o XOR será aplicado)    

random_generator = Xorshift(seed = seed) # Tanto faz a semente
# Inicializa o LFSR com 4096 bits
lfsr = LFSR(seed=seed, taps=taps)

def xorshift_test(bits):
    number = random_generator.random_number(bits)
    return number

def lfsr_test(bits):
    random_number = lfsr.get_random_bits(bits)
    return random_number

def benchmark():
    # Criação dos gráficos comparativos
    bench = perfplot.bench(
        setup=lambda n: n,
        kernels=[
            lambda bits: xorshift_test(bits),
            lambda bits: lfsr_test(bits)
        ],
        labels=["Xorshift", "LFSR"],
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

    # Criando um DataFrame para armazenar os resultados
    results = pd.DataFrame(zip(*times), columns=labels, index=n_values)

    # Mostrando a tabela
    print(results)

    # Opcional: Salvando a tabela em um arquivo CSV
    results.to_csv("randoms_comparation.csv", index_label="Número de Bits")

    # Gerando e mostrando o gráfico
    result.save("ramdoms_comparation.png")  # Salva o gráfico em um arquivo
    result.show()  # Mostra o gráfico na tela

if __name__ == "__main__":
    benchmark()
