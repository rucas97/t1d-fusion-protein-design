import math

# Standard amino acids to filter out (so we only look at sugar atoms)
standard_aa = {'ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL'}

# 1. Load receptor atoms from the docked complex (Chain R)
receptor_atoms = []
with open("structures/hdock_full_complex.pdb", "r") as f:
    for line in f:
        if line.startswith("ATOM") and line[21] == "R":
            x, y, z = float(line[30:38]), float(line[38:46]), float(line[46:54])
            receptor_atoms.append((x, y, z))

print(f"Loaded {len(receptor_atoms)} receptor atoms.")

# 2. Load glycan atoms from the newly glycosylated PDB
glycan_atoms = []
with open("structures/v2.0_full_alphafold-site_build-output.pdb", "r") as f:
    for line in f:
        if line.startswith("ATOM") or line.startswith("HETATM"):
            res_name = line[17:20].strip()
            # If it's not a standard amino acid, it's a sugar!
            if res_name not in standard_aa:
                x, y, z = float(line[30:38]), float(line[38:46]), float(line[46:54])
                res_num = line[22:26].strip()
                glycan_atoms.append((x, y, z, res_name, res_num))

print(f"Loaded {len(glycan_atoms)} glycan atoms.")

# 3. Calculate the minimum distance from ANY sugar atom to the receptor
if not glycan_atoms:
    print("❌ No glycan atoms found. Did GlycoShape output HETATM records?")
else:
    min_dist = float('inf')
    closest_glycan = None
    
    for (gx, gy, gz, res_name, res_num) in glycan_atoms:
        for (rx, ry, rz) in receptor_atoms:
            dist = math.sqrt((gx-rx)**2 + (gy-ry)**2 + (gz-rz)**2)
            if dist < min_dist:
                min_dist = dist
                closest_glycan = f"{res_name}{res_num}"
                
    print("-" * 50)
    print(f"Minimum distance from ANY glycan atom to the receptor: {min_dist:.2f} Å")
    print(f"Closest glycan residue: {closest_glycan}")
    print("-" * 50)
    
    if min_dist < 4.0:
        print("🚨 WARNING: SEVERE STERIC CLASH. The sugars physically crash into the receptor.")
    elif min_dist < 8.0:
        print("⚠️ CAUTION: Potential steric clash. Sugars are very close to the receptor surface.")
    else:
        print("✅ SAFE: Glycans are far enough away to not interfere with binding.")
