# Extract MANF (47-204) and Fcµ (220-672) from the AlphaFold model
with open("v2.0_full_alphafold.pdb", "r") as f_in, \
     open("isolated_manf.pdb", "w") as f_manf, \
     open("isolated_fcmu.pdb", "w") as f_fcmu:
    
    for line in f_in:
        if line.startswith("ATOM"):
            res_num = int(line[22:26])
            if 47 <= res_num <= 204:
                f_manf.write(line)
            elif 220 <= res_num <= 672:
                f_fcmu.write(line)
                
    f_manf.write("END\n")
    f_fcmu.write("END\n")

print("Successfully extracted isolated_manf.pdb and isolated_fcmu.pdb")
