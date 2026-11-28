# M (P79679) — Tail tube protein M (Mup40 / gpM)

## Summary
- **UniProt**: `P79679` (`TTUB_BPMU`), 118 aa, locus tag `Mup40`, gene `M`.
- **Function**: Major tail tube protein (TTP) of bacteriophage Mu (`PF09691` / `IPR019154`). Polymerizes as a stacked hexameric ring cylinder around the tape measure protein (gp42) to form the central tail tube surrounded by the contractile tail sheath (gpL). Upon sheath contraction, the tail tube penetrates the host cell envelope and serves as the conduit for viral genome delivery ([PMID:9714755](../../../publications/PMID_9714755.md); [PMID:27555589](../../../publications/PMID_27555589.md); [file:BPMU/M/M-uniprot.txt](M-uniprot.txt)).
- **Disruption Phenotype & Structure**: Mutants in gene *M* fail to synthesize tails (`DISRUPTION PHENOTYPE: No tail is synthesized. {ECO:0000269|PubMed:3904174}.`). Cryo-EM structures (`PDB:9KHY`, `PDB:9KI0`, `PDB:9KI1`) resolve the central tail tube rings.

## Key References
- **PMID:9714755**: (1998), *J. Biochem.* — "Discovery of the tail tube gene of bacteriophage Mu and sequence analysis of the sheath and tube genes." Identified the ORF immediately downstream of *L* (`M` / `Mup40`) as the phage Mu tail tube gene by N-terminal amino acid sequencing of purified tail tubes.
- **PMID:22297511**: Leiman & Shneider (2012), *Adv. Exp. Med. Biol.* — Review of contractile phage tail machines.
- **PMID:27555589**: Büttner et al. (2016), *PNAS* — Details how the tail tube attaches to the baseplate and penetrates the host cell envelope upon sheath contraction.
- **file:BPMU/M/M-uniprot.txt**: Swiss-Prot entry documenting tail tube polymerization around the tape measure protein, host envelope penetration during genome ejection, and disruption phenotype.

## Annotation Decisions
- `GO:0098026` (`virus tail, tube`, IDA `PMID:9714755` and IEA `GO_REF:0000043`): **ACCEPT** — both experimental and keyword-derived rows accurately capture the core localization of gpM.
- `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`, IEA, `GO_REF:0000043`): **ACCEPT** — gpM forms the central conduit pushed across the host envelope during contractile genome ejection.
- `GO:0046718` (`symbiont entry into host cell`, IEA, `GO_REF:0000043`): **TOO_GENERAL** — entailed by the retained specific descendant `GO:0099000`.
- `GO:0098015` (`virus tail`, IEA, `GO_REF:0000043`): **TOO_GENERAL** — entailed by the retained `part_of` child `GO:0098026` (`virus tail, tube`).
- `GO:0030430` (`host cell cytoplasm`, IEA, `GO_REF:0000044`): **KEEP_AS_NON_CORE** — site of tail synthesis and assembly inside the infected bacterium.
- `GO:0039660` (`structural constituent of virion`, `enables`): **NEW** — core structural activity of the tail tube subunit.
- `GO:0098003` (`viral tail assembly`, `involved_in`): **NEW** — supported by tail tube polymerization around the tape measure protein and the complete absence of tails in *M* mutants (`No tail is synthesized.`).
