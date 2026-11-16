# Curatorial Notes for Rat `Accs` (`UniProtKB:A0A8J8YIP6`)

## 1. Identity, Gene-Model Cross-Reference Note, and Phylogeny
- **Gene symbol / IDs**: `Accs` (`RGD:1309314`), located on rat chromosome 3 adjacent to paralog `Accsl` (`RGD:1596039`).
- **UniProtKB**: `A0A8J8YIP6` (`A0A8J8YIP6_RAT`, unreviewed TrEMBL entry, sequence version 2, 502 aa, `PE 1: Evidence at protein level` via PeptideAtlas), assigned to **`PANTHER:PTHR43795:SF17`** (*1-AMINOCYCLOPROPANE-1-CARBOXYLATE SYNTHASE-LIKE PROTEIN 1*).
- **Upstream Ensembl / UniProt cross-reference note**: In GRCr8 Ensembl annotation, neighboring tandem paralogs `Accs` (`ENSRNOT00000012214.9` -> `A0A8J8YIP6`, 502 aa, `SF17`) and `Accsl` (`ENSRNOT00000068585.3` -> `D3ZUW2`, 617 aa, `SF1`) were merged as alternative transcripts under a single Ensembl gene identifier (`ENSRNOG00000042533.3`), causing `A0A8J8YIP6` to inherit spurious `GN Synonyms=Accsl` and `DR RGD; 1596039; Accsl.` cross-references alongside its true identity `RGD:1309314` (`Accs`), as well as the misleading TrEMBL `SubName: Full=1-aminocyclopropane-1-carboxylate synthase`. At the protein sequence level, `A0A8J8YIP6` (502 aa) is the clean, full-length 1:1 rat `Accs` ortholog (~93% identical to mouse `A2AIG8` and ~86% identical to human `Q96QU6`).

## 2. Literature Search Log
- Targeted PubMed and Europe PMC searches for `("Accs" OR "A0A8J8YIP6" OR "RGD:1309314") AND ("rat" OR "Rattus norvegicus")`:
  - Zero rat-specific publications biochemically purify or genetically perturb rat `Accs` directly; functional inference rests on 1:1 orthology and active-site identity with human `ACCS` (`PMID:11470512`, `PMID:39876065`).

## 3. Active-Site Residue Conservation (`A0A8J8YIP6` sv 2 vs Human `Q96QU6` sv 1)
- `Tyr133` (`Q96QU6` `Tyr132`): **Retained** — partner-subunit PLP H-bond donor; AlphaFold2 modeling and AutoDock Vina docking on human `ACCS` hypothesize that `Tyr132(B)` sterically impedes productive SAM binding (`PMID:39876065`).
- `Trp136` (`Q96QU6` `Trp135`): **Retained** — partner-subunit aromatic pocket residue (`PMID:39876065` Figure 7).
- `Asp287` (`Q96QU6` `Asp286`): **Retained** — fold-type I pyridinium-stabilizing aspartate.
- `Lys324` (`Q96QU6` `Lys323`): **Retained** — covalent PLP Schiff-base lysine and general base.
- `Arg352` (`Q96QU6` `Arg351`): **Retained** — partner-subunit cationic pocket arginine (`PMID:39876065` Figure 7).
- `Arg458` (`Q96QU6` `Arg457`): **Retained** — substrate alpha-carboxylate-anchoring arginine.

## 4. Annotation Decisions
- `GO:0006520` (`IBA`, `PTN002887088`) & `GO:0008483` (`IBA`, `PTN002887088`): `REMOVE` — stale propagations from retired plant aminotransferase PAINT node `PTN002887088` (resting on *Arabidopsis* PAT transamination; cleavage of L-cysteine S-conjugates/S-sulfoxides falls under `GO:0006575` *modified amino acid metabolic process*, not `GO:0006520`, and no `NEW` `GO:0006575` BP row is asserted while the endogenous in vivo substrate remains unidentified).
- `GO:0030170` (`IEA`, `InterPro:IPR004839`): `ACCEPT` — supported by complete conservation of `Lys324` and `Asp287` and stoichiometric PLP binding in 1:1 human ortholog `Q96QU6`.
- `NEW` `GO:0047804` (`cysteine-S-conjugate beta-lyase activity`, `ISS`, `with: UniProtKB:Q96QU6`, `PMID:39876065`): Proposed based on 1:1 orthology, strict conservation of `K324`, `D287`, `R458`, `W136`, `Y133`, and `R352`, and full Michaelis–Menten saturation kinetics of `Q96QU6` on `S-phenyl-L-cysteine` (substrate 4, EC 4.4.1.13) alongside cysteine S-sulfoxides.
