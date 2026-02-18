
from src.parser import read_fasta, parse_gff
from src.analysis import strand_specific_composition
from src.analysis import strand_specific_composition, plot_strand_composition

def main():
    fasta_path = "C:\Genomics\Genome_TE_annotation_pipeline\data\GCF_000005845.2_ASM584v2_genomic.fna"
    gff_path = "C:\Genomics\Genome_TE_annotation_pipeline\data\genomic.gff"

    genome_seq = read_fasta(fasta_path)
    features = parse_gff(gff_path)

    result = strand_specific_composition(genome_seq, features)
    result.to_csv("output/strand_composition.csv")
    plot_strand_composition(result)

    print(result)

if __name__ == "__main__":
    main()
