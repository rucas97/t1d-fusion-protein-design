from Bio import SeqIO

# Load v3 sequence
record = SeqIO.read("constructs/full_construct_v3.0.fasta", "fasta")
seq = str(record.seq)

print("=== LOCAL CLEAVAGE MOTIF SCANNER ===")
print(f"Query Length: {len(seq)} aa\n")

# 1. Granzyme B (Target)
gzB_motif = "IEPD"
gzB_hits = [i+1 for i in range(len(seq)) if seq.startswith(gzB_motif, i)]
print(f"[Target] Granzyme B motif ({gzB_motif}):")
if gzB_hits:
    for pos in gzB_hits:
        print(f"  -> PASS: Found at position {pos} (cleaves after the D)")
else:
    print("  -> FAIL: Motif missing!")

# 2. Furin (Off-target) - Motif: R-X-[K/R]-R
print(f"\n[Off-Target] Furin motif (R-X-[K/R]-R):")
furin_hits = []
for i in range(len(seq)-3):
    motif = seq[i:i+4]
    if motif[0] == 'R' and motif[3] == 'R' and motif[1] != 'P' and motif[2] in ['K', 'R']:
        furin_hits.append(f"{motif} at pos {i+1}")
if furin_hits:
    for hit in furin_hits: print(f"  -> WARNING: {hit}")
else:
    print("  -> PASS: No Furin sites found.")

# 3. Thrombin (Off-target) - Motif: L-V-P-R | G-S
print(f"\n[Off-Target] Thrombin motif (L-V-P-R / G-S):")
thrombin_hits = []
for i in range(len(seq)-5):
    motif = seq[i:i+6]
    if motif.startswith("LVPR") and motif[4] in ['G', 'S']:
        thrombin_hits.append(f"{motif} at pos {i+1}")
if thrombin_hits:
    for hit in thrombin_hits: print(f"  -> WARNING: {hit}")
else:
    print("  -> PASS: No Thrombin sites found.")

print("\n=== END OF SCAN ===")
