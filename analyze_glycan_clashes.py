import math

# The 4 predicted N-glycosylation sites (Asn residues)
glyco_sites = [265, 428, 491, 659]

# Load the docked complex (Chain R is Receptor, Chain A is Drug)
# We use the hdock_full_complex.pdb we analyzed earlier
receptor_atoms = []
glyco_atoms = []

with open("structures/hdock_full_complex.pdb", "r") as f:
    for line in f:
        if line.startswith("ATOM"):
            chain = line[21]
            res_num = int(line[22:26])
            res_name = line[17:20].strip()
            x, y, z = float(line[30:38]), float(line[38:46]), float(line[46:54])
            
            if chain == "R":
                # Store all receptor atoms for distance calculation
                receptor_atoms.append((x, y, z))
            elif chain == "A" and res_num in glyco_sites and res_name == "ASN":
                # Store the coordinates of the glyco-site Asn sidechain (CB, CG, OD1, ND2)
                # For simplicity, we just grab all atoms of that residue
                glyco_atoms.append((res_num, x, y, z))

print(f"Loaded {len(receptor_atoms)} receptor atoms and {len(glyco_atoms)} glyco-site atoms.\n")

# Calculate the minimum distance from each glyco site to the receptor
for res_num in glyco_sites:
    site_coords = [atom[1:] for atom in glyco_atoms if atom[0] == res_num]
    
    if not site_coords:
        print(f"Residue {res_num}: Not found in docked complex.")
        continue
        
    min_dist = float('inf')
    
    # Find the closest receptor atom to any atom in this glyco site
    for (sx, sy, sz) in site_coords:
        for (rx, ry, rz) in receptor_atoms:
            dist = math.sqrt((sx-rx)**2 + (sy-ry)**2 + (sz-rz)**2)
            if dist < min_dist:
                min_dist = dist
                
    print(f"Glycosylation Site N{res_num}: Minimum distance to Receptor = {min_dist:.2f} Å")
