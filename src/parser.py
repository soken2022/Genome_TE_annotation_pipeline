
# parser.py
# Functions for reading FASTA and GFF files

from Bio import SeqIO

def read_fasta(fasta_path):
    """
    Reads a FASTA file and returns sequence as a string.
    """
    record = next(SeqIO.parse(fasta_path, "fasta"))
    return str(record.seq)




def parse_gff(gff_path):
    """
    Parses GFF file and extracts gene coordinates with strand info.
    Returns a list of dictionaries.
    """
    features = []

    with open(gff_path, "r") as file:
        for line in file:
            if line.startswith("#"):
                continue

            parts = line.strip().split("\t")
            if len(parts) < 9:
                continue

            feature_type = parts[2]
            start = int(parts[3])
            end = int(parts[4])
            strand = parts[6]

            if feature_type == "gene":
                features.append({
                    "start": start,
                    "end": end,
                    "strand": strand
                })

    return features


