# Mup42 (Q9T1V6) — Probable tape measure protein gp42 (gpY)

## Summary
- **UniProt**: `Q9T1V6` (`TMP_BPMU`), 690 aa, locus tag `Mup42`, synonym `Y`.
- **Function**: Tail tape measure protein (TMP) of bacteriophage Mu (`PF06791` / `IPR010626`, `TIGR01760` / `IPR010150`). Assembles onto the baseplate hub prior to tail tube polymerization, serves as the scaffold/template that determines the exact length of the tail tube and sheath, and is probably ejected ahead of the viral genome during infection ([PMID:27555589](../../../publications/PMID_27555589.md); [PMID:22297511](../../../publications/PMID_22297511.md); [file:BPMU/Mup42/Mup42-uniprot.txt](Mup42-uniprot.txt)).
- **Disruption Phenotype & Structure**: Disruption of `Mup42` (`Y`) abolishes tail synthesis (`DISRUPTION PHENOTYPE: No tail is synthesized. {ECO:0000269|PubMed:3904174}.`). Cryo-EM of the phage Mu tail (`PDB:9KI1`, chains `g/h/i=1-690`) resolves three copies of gp42 occupying the lumen of the tail tube/baseplate complex ([file:BPMU/Mup42/Mup42-uniprot.txt](Mup42-uniprot.txt)).

## Key References
- **PMID:27555589**: Büttner et al. (2016), *PNAS* — "Baseplate assembly of phage Mu: Defining the conserved core components of contractile-tailed phages and related bacterial systems." Discusses recruitment of the tape-measure protein to the baseplate prior to tail tube polymerization.
- **PMID:22297511**: Leiman & Shneider (2012), *Adv. Exp. Med. Biol.* — Review of contractile phage tail machines and the role of the tape measure protein in tail assembly and length determination.
- **file:BPMU/Mup42/Mup42-uniprot.txt**: Swiss-Prot record documenting template role in tail tube polymerization and tail length determination, null phenotype (`No tail is synthesized.`), and cryo-EM structure (`PDB:9KI1`).

## Annotation Decisions
- `GO:0098003` (`viral tail assembly`, IEA, `GO_REF:0000043`): **ACCEPT** — core role as the length-determining scaffold required for tail tube polymerization (`No tail is synthesized.` when disrupted).
- `GO:0030430` (`host cell cytoplasm`, IEA, `GO_REF:0000044`): **KEEP_AS_NON_CORE** — synthesized and assembled into the developing tail in the host cytoplasm, whereas its mature residence is inside the virus tail lumen.
- `GO:0039660` (`structural constituent of virion`, `enables`): **NEW** — forms the central internal tape-measure filament (`PDB:9KI1`) of the mature phage tail.
- `GO:0098015` (`virus tail`, `located_in`): **NEW** — occupies the central lumen of the phage tail (`PDB:9KI1`).
