
import pandas as pd

def calculate_nucleotide_composition(sequence):
    length = len(sequence)
    return {
        "A": sequence.count("A") / length,
        "T": sequence.count("T") / length,
        "G": sequence.count("G") / length,
        "C": sequence.count("C") / length
    }


def strand_specific_composition(genome_seq, features):
    plus_seq = ""
    minus_seq = ""

    for feature in features:
        start = feature["start"] - 1
        end = feature["end"]

        if feature["strand"] == "+":
            plus_seq += genome_seq[start:end]
        elif feature["strand"] == "-":
            minus_seq += genome_seq[start:end]

    plus_comp = calculate_nucleotide_composition(plus_seq)
    minus_comp = calculate_nucleotide_composition(minus_seq)

    return pd.DataFrame({
        "Plus": plus_comp,
        "Minus": minus_comp
    })


import matplotlib.pyplot as plt

def plot_strand_composition(df, output_path="output/strand_composition_plot.png"):
    """
    Generates a bar plot comparing nucleotide composition in + and - strands.
    """
    df.T.plot(kind="bar")
    plt.ylabel("Proportion")
    plt.title("Strand-Specific Nucleotide Composition")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


