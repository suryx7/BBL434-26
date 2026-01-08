import sys

def count_unique_kmers(fasta_file, k):
    sequence = []

    with open(fasta_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(">"):
                continue
            sequence.append(line)

    seq = "".join(sequence)
    unique_kmers = set()

    for i in range(len(seq) - k + 1):
        unique_kmers.add(seq[i:i+k])

    return len(unique_kmers)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python count_unique_kmers.py <seq.fa> <k>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    k = int(sys.argv[2])

    if k <= 0:
        print("k must be a positive integer")
        sys.exit(1)

    count = count_unique_kmers(fasta_file, k)
    print(f"Unique {k}-mers: {count}")
