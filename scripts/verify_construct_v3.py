# Build the exact v2.0 sequence from verified UniProt components to avoid typos
glp1 = "HAEGTFTSDVSSYLEGQAAKEFIAWLVKGRG"
linker1 = "GSGKRGGGGSGGGGS"
manf = "LRPGDCEVCISYLGRFYQDLKDRDVTFSPATIENELIKFCREARGKENRLCYYIGATDDAATKIINEVSKPLAHHIPVEKICEKLKKKDSQICELKYDKQIDLSTVDLKKLRVKELKKILDDWGETCKGCAEKSDYIRKINELMPKYAPKAASARTDL"
linker2 = "GGGGSGGGGSGGGGS"
# Fcµ sequence from UniProt P01871, containing the FVQWMQR motif
fcmu = "GSASAPTLFPLVSCENSPSDTSSVAVGCLAQDFLPDSITFSWKYKNNSDISSTRGFPSVLRGGKYAATSQVLLPSKDVMQGTDEHVVCKVQHPNGNKEKNVPLPVIAELPPKVSVFVPPRDGFFGNPRKSKLICQATGFSPRQIQVSWLREGKQVGSGVTTDQVQAEAKESGPTTYKVTSTLTIKESDWLSQSMFTCRVDHRGLTFQQNASSMCVPDQDTAIRVFAIPPSFASIFLTKSTKLTCLVTDLTTYDSVTISWTRQNGEAVKTHTNISESHPNATFSAVGEASICEDDWNSGERFTCTVTHTDLPSPLKQTISRPKGVALHRPDVYLLPPAREQLNLRESATITCLVTGFSPADVFVQWMQRGQPLSPEKYVTSAPMPEPQAPGRYFAHSILTVSEEEWNTGETYTCVVAHEALPNRVTERTVDKSTGKPTLYNVSLVMSDTAGTCY"

# Find the target motif and mutate R to A
target_motif = "FVQWMQR"
replacement = "FVQWMQA"
if target_motif in fcmu:
    fcmu_mutated = fcmu.replace(target_motif, replacement)
    print("✅ Mutation applied: R to A in FVQWMQR motif.")
else:
    fcmu_mutated = fcmu
    print("❌ Target motif not found in Fcµ sequence.")

# Assemble the full sequence
full_seq = glp1 + linker1 + manf + linker2 + fcmu_mutated

print(f"\nTotal length: {len(full_seq)}")
print(f"GLP-1 (1-31): {len(glp1)} aa")
print(f"Linker 1 (32-46): {len(linker1)} aa")
print(f"MANF (47-204): {len(manf)} aa")
print(f"Linker 2 (205-219): {len(linker2)} aa")
print(f"Fcµ (220-end): {len(fcmu_mutated)} aa")

# Find the exact index of the mutated Alanine
mut_idx = full_seq.find(replacement)
print(f"\nThe mutated Alanine (A) is at 1-indexed position: {mut_idx + len('FVQWMQ') + 1}")
