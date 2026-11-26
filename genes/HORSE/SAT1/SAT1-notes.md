# SAT1 (horse, A0A5F5PNJ9) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was opened or used.

### Identity: this is APOO/MIC26, not SAT1
- UniProt A0A5F5PNJ9 (TrEMBL, PE 3, 198 aa) has `GN Name=SAT1 {ECO:0000313|VGNC:VGNC:22698}`,
  but its DE line, InterPro (IPR019166, IPR033182), Pfam (PF09769 ApoO) and PANTHER (PTHR14564)
  cross-references, and `CTD; 79135` (the human APOO gene id) all point to MIC26/APOO.
- Ensembl maps it to APOO-201 (ENSECAT00000077118) of gene ENSECAG00000013441, which Ensembl
  names APOO (VGNC:15425), on chrX. NCBI Gene 100060141 (from the KEGG xref) is horse APOO.
  Ensembl Compara: ortholog_one2one with human APOO.
- PANTHER v19: PTHR14564:SF2 (MICOS complex subunit MIC26), the same subfamily as human Q9BUR5.
  MIC27/APOOL is in SF3.
- 91.4% identical to human MIC26 over the full 198 aa, 36.4% to MIC27, 21.7% to human SAT1
  (unrelated). See `SAT1-bioinformatics/RESULTS.md`.
- It is a full-length product, not a fragment or isoform: the length matches human and mouse
  MIC26 (198 aa) and the transmembrane helix is at the same place. It is one of nine Ensembl
  transcripts and not the Ensembl canonical one (241 aa). The other horse entry F7AGU3 (200 aa,
  named APOO) differs only at the N-terminus.
- Probable cause: an overlapping-locus mix-up. In EquCab3.0 (Ensembl REST, checked 2026-10-21)
  horse SAT1 (ENSECAG00000021968, X:19,065,531-19,068,529, + strand) lies within the span of
  APOO (ENSECAG00000013441, X:19,065,057-19,157,721, - strand), and transcript APOO-201 has the
  same span. A0A5F5PNJ9 carries SAT1's identifiers: `VGNC; VGNC:22698; SAT1` (the same VGNC xref
  as the real horse SAT1 entry F6X9A1) and `Bgee; ENSECAG00000021968`, the SAT1 gene id. Its
  sequence, though, is APOO's. Horse SAT1 proper is F6X9A1 / A0A5F5PK54. The folder name
  follows the campaign and keeps SAT1.

### Deep research
- `just deep-research HORSE SAT1 --provider falcon` failed with "Exception: Failed to
  authenticate" (falcon credentials). No deep-research file exists. Running it under the
  symbol SAT1 would also have steered the search to the wrong gene. The review relies instead
  on the cached primary literature for human MIC26, which was already read for
  `genes/human/APOO` (status COMPLETE).

### Evolutionary basis for transfer
- PAINT (interpro/panther/PTHR14564/PTHR14564-paint.tsv) has one node, PTN001803267, with IBDs
  for GO:0061617 MICOS complex (seeds FB:FBgn0038400, Q6UXV4, Q9BUR5) and GO:0042407 cristae
  formation (seed Q9BUR5). The horse protein is in SF2 with the human seed, so both IBAs apply.
  PAINT asserted only these two terms. No MF, lipid-binding or cardiolipin term was placed, and
  none is added here.
- Human MIC26 evidence used (cached publications): MICOS subunit in the inner membrane
  [PMID:25764979]; recovered in the MIB complex after import [PMID:25781180]; single knockout
  lowers crista junction number [PMID:32788226]; pathogenic variants disrupt cristae
  [PMID:32439808, PMID:37649161]; the secreted "apolipoprotein" species is not MIC26
  [PMID:37279200]. Cardiolipin binding was shown for MIC27, not MIC26 [PMID:23704930].

### Decisions
- mitochondrial inner membrane (SubCell IEA): ACCEPT.
- mitochondrion (ARBA IEA) and mitochondrial membrane (SubCell IEA): MODIFY to mitochondrial
  inner membrane. Both are correct but less specific than the location supported by the
  orthologue and by the predicted TM helix.
- cristae formation (IBA, IEA) and MICOS complex (IBA, IEA): ACCEPT, core.
- No NEW annotations. Phenotypes downstream of cristae (cardiolipin levels, OXPHOS supercomplex
  stability, adipose and atherosclerosis phenotypes in mice) are not annotated on horse.

### Relative
- Human APOO (Q9BUR5), genes/human/APOO, review COMPLETE. Same PANTHER subfamily (SF2), seed of
  the PAINT node, Compara one-to-one orthologue.
- Modules: no ModuleReview covers mammalian MICOS. `modules/dmel_micos_complex.yaml` is the
  Drosophila MICOS module (includes Mic26-27) and is the closest. `modules/mitochondrion_lifecycle.yaml`
  mentions MICOS only in its scope prose.
