
from src.parser import read_fasta, parse_gff
from src.analysis import strand_specific_composition

def main():
    fasta_path = "data/genome.fna"
    gff_path = "data/genome.gff"

    genome_seq = read_fasta(fasta_path)
    features = parse_gff(gff_path)

    result = strand_specific_composition(genome_seq, features)
    result.to_csv("output/strand_composition.csv")

    print(result)

if __name__ == "__main__":
    main()
