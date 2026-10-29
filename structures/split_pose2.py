from Bio.PDB import PDBParser, PDBIO, Select

class ChainSplitter(Select):
    def __init__(self, split_resnum, target_chain):
        self.split_resnum = split_resnum
        self.target_chain = target_chain
    
    def accept_residue(self, residue):
        resnum = residue.get_id()[1]
        if self.target_chain == "R":
            return resnum <= self.split_resnum
        else:
            return resnum > self.split_resnum

# Load the merged model
parser = PDBParser(QUIET=True)
structure = parser.get_structure("pose2", "hdock_pose2.pdb")
model = structure[0]

# The receptor has 393 residues (from the earlier chain analysis)
# The drug has 650 residues. Total = 1043.
# We split at residue 393.
split_point = 393

# Write the receptor (first 393 residues)
io = PDBIO()
io.set_structure(model)
io.save("pose2_receptor.pdb", ChainSplitter(split_point, "R"))

# Write the drug (remaining residues)
io = PDBIO()
io.set_structure(model)
io.save("pose2_drug.pdb", ChainSplitter(split_point, "A"))

print("Split complete.")
