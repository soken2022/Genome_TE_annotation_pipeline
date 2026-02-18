
# parser.py
# Functions for reading FASTA and GFF files

from Bio import SeqIO

def read_fasta(fasta_path):
    """
    Reads a FASTA file and returns sequence as a string.
    """
    record = next(SeqIO.parse(fasta_path, "fasta"))
    return str(record.seq)

