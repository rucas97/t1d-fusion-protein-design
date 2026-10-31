import math, os, sys

def analyze_pose(pose_file):
    if not os.path.exists(pose_file): return None

    atoms = []
    for line in open(pose_file, errors="ignore"):
        if line.startswith("ATOM"):
            rn = int(line[22:26])
            rname = line[12:16].strip()
            if rname.startswith("H"): continue
            xyz = (float(line[30:38]), float(line[38:46]), float(line[46:54]))
            atoms.append((rn, rname, xyz))

    if not atoms:
        return {"error": "No atoms found"}

    # Get unique residue numbers in order
    unique_res = []
    seen = set()
    for rn, _, _ in atoms:
        if rn not in seen:
            unique_res.append(rn)
            seen.add(rn)

    total_res = len(unique_res)
    
    # We know the v9.0 payload is 211 residues. 
    # The receptor is everything before that.
    if total_res < 211:
        return {"error": f"Total residues ({total_res}) smaller than drug (211)"}
        
    lig_start_res = unique_res[-211] # The 211th residue from the end

    rec_atoms = [a for a in atoms if a[0] < lig_start_res]
    lig_atoms = [a for a in atoms if a[0] >= lig_start_res]

    contacts = {}
    clashes = 0
    min_dist = 999.0

    for rn, rname, rxyz in rec_atoms:
        for ln, lname, lxyz in lig_atoms:
            d = math.dist(rxyz, lxyz)
            if d < min_dist: min_dist = d
            if d < 2.0: clashes += 1
            if d <= 4.5:
                if ln not in contacts or d < contacts[ln]:
                    contacts[ln] = d

    # GLP-1 arm is the first 31 residues of the v9.0 payload
    glp_resids = unique_res[-211:][:31]
    glp_hits = [r for r in contacts if r in glp_resids]
    
    # Map back to v9.0 sequence numbering (1-31)
    glp_hits_relative = [glp_resids.index(r) + 1 for r in glp_hits]

    return {
        "min_dist": min_dist,
        "clashes": clashes,
        "glp_contacts": len(glp_hits),
        "glp_residues": sorted(glp_hits_relative)
    }

def batch(folder, label):
    print(f"\n{'='*60}")
    print(f" {label}")
    print(f"{'='*60}")
    print(f"{'Model':<10} | {'Clashes':<8} | {'Min Dist':<10} | {'GLP-1 Hits':<10} | {'GLP-1 Residues'}")
    print("-" * 80)
    
    for i in range(1, 11):
        file = os.path.join(folder, f"model_{i}.pdb")
        res = analyze_pose(file)
        
        if not res:
            print(f"model_{i:<4} | File not found")
        elif "error" in res:
            print(f"model_{i:<4} | ERROR: {res['error']}")
        else:
            print(f"model_{i:<4} | {res['clashes']:<8} | {res['min_dist']:<10.2f} | {res['glp_contacts']:<10} | {res['glp_residues']}")

if __name__ == "__main__":
    batch("structures/v9.0_target_poses", "TARGET: v9.0 vs GLP-1R (Therapeutic Target)")
    batch("structures/v9.0_offtarget_poses", "OFF-TARGET: v9.0 vs GCGR (Safety Check)")
