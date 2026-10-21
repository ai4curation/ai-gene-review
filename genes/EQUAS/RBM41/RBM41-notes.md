# RBM41 (donkey, A0A9L0IK51) - review notes

DONKEY40 cohort. 6 IEA GOA rows (4 TreeGrafter, 2 InterPro/combined). No cached RBM41 literature was available; NCBI E-utilities could not be reached from this session, so no primary RBM41 paper was consulted.

## Sequence
- [file:EQUAS/RBM41/RBM41-bioinformatics/RESULTS.md "95.83% identity over 408 paired residues"]; RRM: ["78 of 79 human residues in this span are identical"]. Donkey has a 24-residue insertion (175-198) in a non-domain region.

## Family
- [file:EQUAS/RBM41/RBM41-bioinformatics/interpro-IPR045164.md "It binds to the U11-associated 59K protein via its RRM1 and employs the RRM2 to bind hairpin III of the U12 small nuclear RNA (snRNA)."] (about RNPC3) and ["RBM41 contains only one RRM. Its biological function remains unclear."]
- Human UniProt: [file:EQUAS/RBM41/RBM41-bioinformatics/human-Q96IZ5-uniprot.txt "May bind RNA."]
- Human RBM41 carries the same IBAs (U12 snRNA binding, U12-type spliceosomal complex, mRNA splicing via spliceosome, pre-mRNA intronic binding) from PTN000413238.

## Decisions
- Accept U12 snRNA binding, U12-type spliceosomal complex, mRNA splicing via spliceosome as phylogenetic inference (PAINT node + RRM homology to RNPC3 RRM2). UNDECIDED pre-mRNA intronic binding (family's known contact is U12 snRNA). Nucleic acid binding and RNA binding marked TOO_GENERAL.
- ProtNLM2 GO:0003723 RNA binding: correct but less precise than GOA U12 snRNA binding (LSP).

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this section.

### Identity
- A0A9L0IK51 (432 aa, TrEMBL, PE 4) is the full-length donkey RBM41 gene model (Ensembl ENSEASP00005041268, chromosome X). It is not a fragment or isoform. Compared with human Q96IZ5 (413 aa) it has a 24-residue insertion (175-198) in the N-terminal non-domain region and lacks the last 5 human residues. The RRM (333-411) is 78/79 identical to human [file:EQUAS/RBM41/RBM41-bioinformatics/RESULTS.md "78 of 79 human residues in this span are identical"].

### Evolutionary grounding
- Donkey: PANTHER PTHR16105:SF2 "RNA-BINDING PROTEIN 41" [file:EQUAS/RBM41/RBM41-uniprot.txt]. Human RBM41 Q96IZ5 and mouse Rbm41 Q8JZV4 are in SF2. The RNPC3/U11-U12-65K paralogs (human Q96LT9, mouse, Arabidopsis SNRNP65) are in SF0 [file:interpro/panther/PTHR16105/PTHR16105-entries.csv]. Human RBM41 is therefore the characterized ortholog; RNPC3 is a paralog in a different subfamily.
- The human IBAs come from family node PTN000413238. Their donors are the 65K paralogs (AT1G09230, FBgn0265184, zebrafish rnpc3, Q96LT9), not RBM41, so they are paralog-level inferences. The donkey TreeGrafter rows (PTN009029508) inherit the same set. No PANTHER family review exists under interpro/panther/PTHR16105/ (only entries + metadata), so there is no placement disagreement to report.

### Literature
- Deep research: `just deep-research EQUAS RBM41 --provider falcon` failed with "Failed to authenticate" (Edison/falcon auth error), so no deep-research file exists. Literature was found by web search and cached: PMID:38499487 (Norppa et al. 2024 NAR, full text).
- Key findings for human RBM41 [PMID:38499487]:
  - The RRM binds U12 and U6atac 3' stem-loops ["the RBM41 RRM has a low micromolar affinity to both U12 (Kd= 2.14 μM) and U6atac hairpins (Kd= 3.78 μM; Figure 2D)"].
  - In cells it associates with U12/U4atac/U6atac but not U11 snRNA ["V5-RBM41 co-immunoprecipitated the U12 snRNA, U4atac and U6atac snRNAs, but not the U11 snRNA"], and these associations depend on the RRM.
  - It is in the U12 mono-snRNP ["RBM41 peak co-migrated with the U12 mono-snRNP"].
  - It co-precipitates U12-type intron lariats ["RBM41 preferentially co-immunoprecipitated U12-type but not U2-type intron lariats"] and binds DHX8 through its N-terminal region.
  - It localizes to Cajal bodies ["endogenous RBM41 localizes to Cajal bodies"].
  - Knockout cells are viable but show a weak U12-type 3' splice site defect.
  - Conclusion: ["RBM41 functions in post-splicing steps of the minor spliceosome assembly/disassembly cycle"].

### Decisions (changes from the previous version)
- GO:0030626 U12 snRNA binding, GO:0005689 U12-type spliceosomal complex, GO:0000398 mRNA splicing via spliceosome: still ACCEPT. Support is now direct experimental evidence on the SF2 ortholog. Previously it was InterPro text about RNPC3 plus "function unclear".
- GO:0097157 pre-mRNA intronic binding: still UNDECIDED. The lariat co-IP does not show direct intron contact, and the RRM is specific for snRNA hairpins.
- GO:0003676 and GO:0003723: TOO_GENERAL (unchanged).
- NEW (ISO from human, PMID:38499487): GO:0030624 U6atac snRNA binding, GO:0005693 U12 snRNP, GO:0015030 Cajal body. These are a molecular function and cellular components measured directly, not process terms, so the participation test does not apply. DHX8 association is not annotated, because the protein-binding policy applies and no more specific MF is supported.
- Description and core function rewritten: RBM41 acts in post-catalytic minor spliceosome steps, distinct from 65K's role in intron recognition; Cajal body added as a location.
- Old InterPro and human-UniProt file references are kept in the references list but are no longer used as support (see reference_review notes).

### Relative
- Next relative: human RBM41 (Q96IZ5), ortholog in PTHR16105:SF2. No review exists in the repo (no genes/human/RBM41).
- Modules: no minor-spliceosome module exists. modules/dmel_spliceosome.yaml explicitly excludes the minor spliceosome.
