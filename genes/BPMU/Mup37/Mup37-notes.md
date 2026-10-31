# Mup37 (Q9T1V8) — Probable tail terminator protein gp37 (gpK)

## Summary
- **UniProt**: `Q9T1V8` (`VPK_BPMU`), 182 aa, locus tag `Mup37`, synonym `K`.
- **Function**: Tail terminator protein (TrP) of bacteriophage Mu (`PF09684` / `IPR019147`). Capping the growing tail tube once it reaches the length dictated by the tape measure protein, it stops tail tube polymerization, prevents depolymerization, and provides the interaction surface for head attachment ([file:BPMU/Mup37/Mup37-uniprot.txt](Mup37-uniprot.txt); [PMID:19426744](../../../publications/PMID_19426744.md)).
- **Disruption Phenotype & Structure**: Mutants accumulate free heads and abnormally long, variable-length free tails (`DISRUPTION PHENOTYPE: Accumulation of free heads as well as free tails longer than normal and variable in length. {ECO:0000269|PubMed:3904174}.`). Cryo-EM (`PDB:9KHY`, chains `1–6`, residues 1–182) confirms a hexameric ring capping the tail tube ([file:BPMU/Mup37/Mup37-uniprot.txt](Mup37-uniprot.txt)).

## Key References
- **PMID:19426744**: Pell et al. (2009), *J. Mol. Biol.* — Demonstrates that tail terminator proteins of long-tailed phages (including contractile-tailed phages P2 and Mu) form conserved hexameric rings that cap the polymerizing tail tube and serve as the head-binding interface.
- **file:BPMU/Mup37/Mup37-uniprot.txt**: Swiss-Prot record documenting tail tube capping function, disruption phenotype (`PubMed:3904174`), virion tail localization, and hexameric cryo-EM structure (`PDB:9KHY`).

## Annotation Decisions
- `GO:0098003` (`viral tail assembly`, IEA, `GO_REF:0000043`): **ACCEPT** — core biological process; gp37 terminates tail tube polymerization at the proper length.
- `GO:0098015` (`virus tail`, IEA, `GO_REF:0000043`): **ACCEPT** — forms the distal hexameric cap of the virus tail.
- `GO:0030430` (`host cell cytoplasm`, IEA, `GO_REF:0000044`): **KEEP_AS_NON_CORE** — tail assembly occurs in the host cytoplasm, whereas the mature protein is a structural component of the virus tail.
- `GO:0039660` (`structural constituent of virion`, `enables`): **NEW** — structural hexameric ring subunit (`PDB:9KHY`) of the phage tail.
