# Curatorial Notes for Mouse `Accs` (`UniProtKB:A2AIG8`)

## 1. Identity, Phylogeny, and Isoforms
- **Gene symbol / IDs**: `Accs` (`MGI:1919717`, `NCBIGene:329470`, `ENSMUSG00000040272`), located on mouse chromosome 2 immediately adjacent to paralog `Accsl` (`MGI:3584519`), syntenic with human 11p11.2 (`ACCS`–`ACCSL`) [PMID:39876065].
- **UniProtKB**: `A2AIG8` (`1A1L1_MOUSE`, sequence version 1, 502 aa), assigned to **`PANTHER:PTHR43795:SF17`** (*1-AMINOCYCLOPROPANE-1-CARBOXYLATE SYNTHASE-LIKE PROTEIN 1*).
- **Isoforms**:
  - `A2AIG8-1`: Canonical 502-residue full-length polypeptide containing the complete fold-type I PLP-dependent catalytic domain.
  - `A2AIG8-2` (`VSP_052669`): 479-residue splice variant missing disordered N-terminal residues 1..23 while retaining the entire catalytic domain and all active-site residues.

## 2. Literature Search Log (Supporting `ND` Curation)
- Systematic PubMed and Europe PMC searches executed for `("Accs" OR "1-aminocyclopropane-1-carboxylate synthase-like protein 1" OR "A2AIG8" OR "Q8CHS6" OR "MGI:1919717" OR "329470") AND ("mouse" OR "Mus musculus" OR "murine")`:
  - Zero mouse-specific experimental publications characterize purified mouse `Accs` enzymatic activity, endogenous in vivo metabolic substrates, knockout phenotypes, or native subcellular localization (`GO:0005575` `ND` is verified as `TRUE_GAP`).
  - Only genome/cDNA sequencing papers (`PMID:19468303`, `PMID:15489334`) and comparative active-site conservation analyses in Gao et al. 2025 (`PMID:39876065`, Figure 7) mention mammalian `Accs` orthologs.

## 3. Active-Site Residue Conservation (`A2AIG8` sv 1 vs Human `Q96QU6` sv 1)
- `Tyr133` (`Q96QU6` `Tyr132`): Retained — inter-subunit PLP H-bond donor; in AlphaFold2 homology modeling and AutoDock Vina docking on human `ACCS`, partner-subunit `Tyr132(B)` is hypothesized to sterically impede productive S-adenosyl-L-methionine (`SAM`) binding (`PMID:39876065`).
- `Trp136` (`Q96QU6` `Trp135`): Retained — inter-subunit aromatic wall of the cysteine S-conjugate side-chain pocket (`PMID:39876065`, `"Notably, both W135 and R351 are highly conserved in mammalian ACCS orthologues (Figure 7)."`).
- `Asp287` (`Q96QU6` `Asp286`): Retained — canonical fold-type I aspartate salt-bridging the protonated PLP pyridinium nitrogen.
- `Lys324` (`Q96QU6` `Lys323`): Retained (`FT MOD_RES 324 N6-(pyridoxal phosphate)lysine`) — covalent internal-aldimine Schiff-base lysine and general base for C-beta-S elimination.
- `Arg352` (`Q96QU6` `Arg351`): Retained — inter-subunit cationic pocket arginine essential for C-beta-S lyase catalysis.
- `Arg458` (`Q96QU6` `Arg457`): Retained — conserved arginine salt-bridging the amino-acid substrate alpha-carboxylate group.

## 4. Annotation Decisions
- `GO:0005575` (`ND`, `GO_REF:0000015`): `ACCEPT` (`nd_case: TRUE_GAP`), paired with `[BIOLOGY]` `CC_DARK` knowledge gap.
- `GO:0006520` (`IBA`, `PTN002887088`) & `GO:0008483` (`IBA`, `PTN002887088`): `REMOVE` — stale propagations from retired plant aminotransferase PAINT node `PTN002887088` (resting on *Arabidopsis* PAT transamination; cleavage of L-cysteine S-conjugates/S-sulfoxides falls under `GO:0006575` *modified amino acid metabolic process*, not `GO:0006520`, and no `NEW` `GO:0006575` BP row is asserted while the endogenous in vivo substrate remains unidentified).
- `GO:0030170` (`IEA`, `InterPro:IPR004839`): `ACCEPT` — supported by complete conservation of `Lys324` and `Asp287` and stoichiometric PLP binding in direct human ortholog `Q96QU6`.
- `GO:0042802` (`IEA` `GO_REF:0000107` & `ISO` `GO_REF:0000119` from `UniProtKB:Q96QU6`): `ACCEPT` — obligate fold-type I homodimer conserving inter-subunit pocket residues `Trp136`, `Tyr133`, and `Arg352`.
- `NEW` `GO:0047804` (`cysteine-S-conjugate beta-lyase activity`, `ISS`, `with: UniProtKB:Q96QU6`, `PMID:39876065`): Proposed based on 1:1 orthology (~86% identity), 100% conservation of all catalytic and substrate-binding pocket residues (`K324`, `D287`, `R458`, `W136`, `Y133`, `R352`), and full Michaelis–Menten saturation kinetics of `Q96QU6` on `S-phenyl-L-cysteine` (substrate 4, EC 4.4.1.13) alongside cysteine S-sulfoxides.
- `UniProtKB:A2AIG8` `CC:FUNCTION`: Record `OUTDATED_STATEMENT` `source_defects` because it projects only the 2001 L-vinylglycine side reaction from `Q96QU6` and omits cysteine S-conjugate sulfoxide beta-lyase activity (`PMID:39876065`).
