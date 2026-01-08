import sys

def parse_multifasta(fasta_file):
    sequences = {}
    current_header = None
    current_seq = []

    with open(fasta_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if line.startswith(">"):
                if current_header is not None:
                    sequences[current_header] = "".join(current_seq)
                current_header = line[1:]   # remove '>'
                current_seq = []
            else:
                current_seq.append(line)

        # save last record
        if current_header is not None:
            sequences[current_header] = "".join(current_seq)

    return sequences

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_multifasta.py <seq.mfa>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    sequences = parse_multifasta(fasta_file)

    for header, seq in sequences.items():
        print(f"{header}\tLength: {len(seq)}")
