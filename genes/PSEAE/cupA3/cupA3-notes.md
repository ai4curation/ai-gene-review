# cupA3 (PA2130, Q9I1Y5) review notes

Outer-membrane usher of the CupA chaperone-usher fimbrial system (fimbrial
export usher family; InterPro IPR000015). Unreviewed UniProt entry. Cluster
cupA1 (pilin), cupA2 (chaperone), cupA3 (usher), cupA4, cupA5.

## Literature (no deep-research provider available; own reading)

- Vallet et al. 2001 (full text read). Tn5 screen for attachment-defective
  mutants of a non-piliated strain identified the cupA cluster. CupA3 is the
  usher [PMID:11381121 "CupA3 appears to be the usher component of the system,
  based on its high similarity to FocD"]. A cupA3 insertion mutant attaches at
  10% of parent [PMID:11381121 "This strain, carrying a disrupted cupA3 gene,
  showed an adhesion-deficient phenotype, with only 10% of the bacteria
  adhering relative to the parental PAK-NP"]. The usher's role is assembly
  [PMID:11381121 "called usher, that forms a channel into the outer membrane
  through which the pilin subunits are sequentially assembled"].
- Vallet et al. 2004 (abstract only; PMC387821 gave no full text). MvaT
  represses cupA; restates that cupA is needed for biofilm formation
  [PMID:15090530 "The cupA gene cluster, but not the cupB or cupC cluster, is
  required for biofilm formation on abiotic surfaces."].
- Alvarez-Ortega and Harwood 2007 (abstract only): low-O2 transcriptome; cup
  genes not mentioned in the abstract. IEP row left UNDECIDED.
- Klebensberger et al. 2009 (abstract only): cupA operon needed for SDS-induced
  aggregation [PMID:19638175 "the cupA-operon and the co-transcribed genes siaA
  (PA0172) and siaD (PA0169) were essential for SDS-induced aggregation."].

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001252526 | GO:0007155 cell adhesion | 2 | 36 (5 taxa) | GO:0007155, IMP, PMID:11381121 (PseudoCAP) | INDIRECT-PHENOTYPE | Full text: real attachment defect of the cupA3 mutant, but CupA3 is the assembly pore; adhesion is done by the fimbria. Upstream role, not participation. | E. coli HtrE P33129 (EcoCyc IMP PMID:27696649, qualifier acts_upstream_of_or_within) | No. The only other seed is itself an upstream-qualified usher phenotype; the node term does not suit an usher clade |
| PTN001252526 | GO:0007155 cell adhesion | 2 | 36 (5 taxa) | GO:0007155, IMP, PMID:15090530 (PseudoCAP) | INDIRECT-PHENOTYPE (UNVERIFIABLE for cupA3) | Abstract only; MvaT paper restating the cupA biofilm requirement. | as above | as above |

Defects:
- PSEUDOCAP WRONG_QUALIFIER on the PMID:11381121 row (PROBABLE; full text read,
  call rests on the participation/upstream judgement) and on the PMID:15090530
  row (SUSPECTED, CHECK; abstract only). Requested: acts_upstream_of_or_within,
  or repoint to GO:0009297.
- GO_CENTRAL WRONG_TERM on PTN001252526 (PROBABLE, CHECK): withdraw the cell
  adhesion IBD; the clade's role is GO:0015473 fimbrial usher porin activity and
  GO:0009297 pilus assembly. The sibling IBDs at this node (GO:0015473 and
  GO:0009279, seeded by E. coli FimD IDA) are sound.

### Other PseudoCAP rows (not seeds)

| term | verdict | defect |
|---|---|---|
| GO:0098743 cell aggregation (IMP, PMID:19638175) | INDIRECT-PHENOTYPE | none recorded (abstract does not name the gene mutated); MARK_AS_OVER_ANNOTATED |
| GO:0071453 cellular response to oxygen levels (IEP, PMID:17581126) | UNVERIFIABLE | none; UNDECIDED |
