# L (P79678) — Tail sheath protein L (Mup39 / gpL)

## Summary
- **UniProt**: `P79678` (`TSHP_BPMU`), 495 aa, locus tag `Mup39`, gene `L`.
- **Function**: Major contractile tail sheath protein of bacteriophage Mu (`PF04984` / `IPR007067`). Polymerizes into an extended helical outer sheath around the baseplate-tail tube complex; upon host cell attachment, sheath contraction drives the inner tail tube through the host cell envelope for viral genome ejection ([PMID:9714755](../../../publications/PMID_9714755.md); [PMID:22297511](../../../publications/PMID_22297511.md); [PMID:27555589](../../../publications/PMID_27555589.md); [file:BPMU/L/L-uniprot.txt](L-uniprot.txt)).
- **Disruption Phenotype & Structure**: Disruption of gene *L* abolishes tail synthesis (`DISRUPTION PHENOTYPE: No tail is synthesized. {ECO:0000269|PubMed:3904174}.`). Cryo-EM structures (`PDB:9KHY`, `PDB:9KI0`, `PDB:9KI1`) resolve the hexameric ring layers of gpL in the tail sheath.

## Key References
- **PMID:9714755**:iliopoulos et al. / Takeda et al. (1998), *J. Biochem.* — "Discovery of the tail tube gene of bacteriophage Mu and sequence analysis of the sheath and tube genes." Sequenced gene *L* and confirmed by N-terminal protein sequencing that gpL is the contractile tail sheath subunit.
- **PMID:22297511**: Leiman & Shneider (2012), *Adv. Exp. Med. Biol.* — Review of bacteriophage contractile tail machines and sheath-contraction mechanism.
- **PMID:27555589**: Büttner et al. (2016), *PNAS* — Describes phage Mu contractile tail architecture in which the outer sheath contracts to drive the central tail tube through the host cell envelope.
- **file:BPMU/L/L-uniprot.txt**: Swiss-Prot entry documenting helical sheath polymerization, contraction during genome ejection, disruption phenotype, and cryo-EM structures.

## Annotation Decisions
- `GO:0098027` (`virus tail, sheath`, IDA `PMID:9714755` and IEA `GO_REF:0000043`): **ACCEPT** — both experimental and keyword-backed annotations accurately capture the core localization of gpL.
- `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`, IEA, `GO_REF:0000043`): **ACCEPT** — accurately captures sheath contraction driving tail tube penetration and DNA ejection.
- `GO:0046718` (`symbiont entry into host cell`, IEA, `GO_REF:0000043`): **TOO_GENERAL** — entailed by the retained specific descendant `GO:0099000`.
- `GO:0098015` (`virus tail`, IEA, `GO_REF:0000043`): **TOO_GENERAL** — entailed by the retained `part_of` child `GO:0098027` (`virus tail, sheath`).
- `GO:0030430` (`host cell cytoplasm`, IEA, `GO_REF:0000044`): **KEEP_AS_NON_CORE** — site of synthesis and tail assembly prior to cell lysis.
- `GO:0039660` (`structural constituent of virion`, `enables`): **NEW** — core structural role forming the contractile tail sheath.
- `GO:0098003` (`viral tail assembly`, `involved_in`): **NEW** — supported by sheath polymerization around the baseplate-tube complex and the null phenotype (`No tail is synthesized.`).
