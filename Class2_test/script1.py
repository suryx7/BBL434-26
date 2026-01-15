import sys
from collections import defaultdict

def read_fasta(fasta):
    seq = []
    with open(fasta) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith(">"):
                seq.append(line.upper())
    return "".join(seq)

def count_kmers(seq, k):
    d = defaultdict(int)
    for i in range(len(seq) - k + 1):
        d[seq[i:i+k]] += 1
    return d

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ori_finder.py genome.fa")
        sys.exit(1)

    seq = read_fasta(sys.argv[1])

    k = 8
    window = 5000
    step = 500

    # GC skew ORI
    min_skew = float("inf")
    ori_gc = 0

    for i in range(0, len(seq) - window + 1, step):
        wseq = seq[i:i+window]
        g = wseq.count("G")
        c = wseq.count("C")
        skew = (g - c) / (g + c) if (g + c) > 0 else 0
        if skew < min_skew:
            min_skew = skew
            ori_gc = i

    # k-mer enrichment ORI
    max_enrich = 0
    ori_kmer = 0

    for i in range(0, len(seq) - window + 1, step):
        wseq = seq[i:i+window]
        counts = count_kmers(wseq, k)
        val = max(counts.values())
        if val > max_enrich:
            max_enrich = val
            ori_kmer = i

    print("ORI (GC skew minimum):", ori_gc)
    print("ORI (k-mer enrichment):", ori_kmer)
