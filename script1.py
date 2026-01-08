import sys

def fasta_length(fasta_file):
    seq_len = 0
    with open(fasta_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(">"):
                continue
            seq_len += len(line)
    return seq_len

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fasta_length.py <seq.fa>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    length = fasta_length(fasta_file)
    print(f"Sequence length: {length}")

