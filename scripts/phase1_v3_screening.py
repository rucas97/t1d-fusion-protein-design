import os
from Bio import SeqIO

os.makedirs("validation/v3", exist_ok=True)

# Load the sequence
seq_path = "constructs/full_construct_v3.0.fasta"
record = SeqIO.read(seq_path, "fasta")
seq = str(record.seq)

# Domain boundaries for v3.0
domains = {
    "GLP1": (1, 31),
    "Linker1_GzB": (32, 43),
    "MANF": (44, 201),
    "Linker2_Whitlow": (202, 219),
    "IgG1_Fc_LALA": (220, 451)
}

print("\n=== V3.0 Domain Map ===")
for name, (start, end) in domains.items():
    domain_seq = seq[start-1:end]
    print(f"{name:15} [{start:3d}-{end:3d}] Length: {len(domain_seq):3d} | Seq: {domain_seq[:15]}...")
    
    # Save each domain to its own FASTA for downstream analysis
    with open(f"validation/v3/{name}.fasta", "w") as f:
        f.write(f">{name}\n{domain_seq}\n")

# Verify Critical Motifs
print("\n=== Critical Motif Verification ===")
gzB_site = "IEPD"
if gzB_site in seq:
    print(f"[PASS] Granzyme B cleavage motif ({gzB_site}) found at position {seq.find(gzB_site)+1}")
else:
    print("[FAIL] Granzyme B motif missing!")

print("\n=== Off-Target Cleavage Scan ===")
furin_count = 0
for i in range(len(seq)-3):
    motif = seq[i:i+4]
    if motif[0] == 'R' and motif[3] == 'R' and motif[1] != 'P' and (motif[2] == 'K' or motif[2] == 'R'):
        print(f"[WARN] Potential Furin site found: {motif} at position {i+1}")
        furin_count += 1
if furin_count == 0:
    print("[PASS] No obvious Furin cleavage sites (R-X-K/R-R) found in sequence.")

# Save full sequence for BLAST
with open("validation/v3/v3_full_for_blast.fasta", "w") as f:
    f.write(f">v3.0_full_construct\n{seq}\n")
print("\nSaved domains and full sequence to validation/v3/")
