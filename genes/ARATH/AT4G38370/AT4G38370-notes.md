# AT4G38370 (Q0WW53): evidence and exact-input prediction review

The fold-level name is reasonable. The only emitted GO term is generic catalytic activity; the TIGAR structural donor does not establish a particular phosphatase substrate or glycolytic role for AT4G38370.

## Input identity and functional boundary

Q0WW53 maps to AT4G38370 and PTHR47821:SF2. Its 225-residue sequence contains an N-terminal RHG motif. The emitted donor Q7ZVE3 is zebrafish TIGAR B. Exploratory global alignment preserves the donor catalytic histidine and proton-donor/acceptor residues, but is highly gapped and has low overall identity; the apparent mismatch at a transition-state contact is not reliable evidence of catalytic loss. No TIGAR-specific substrate assignment follows from this alignment.

## Biological evidence

- [PMID:19015259 — Structural and biochemical studies of TIGAR (TP53-induced glycolysis and apoptosis regulator).](https://pubmed.ncbi.nlm.nih.gov/19015259/): Direct TIGAR biochemistry establishes donor activity and substrate discrimination, not the substrate of the Arabidopsis protein.

> The
> recombinant human and zebra fish enzymes hydrolyze fructose-2,6-bisphosphate as
> well as fructose-1,6-bisphosphate but not fructose 6-phosphate in vitro.

## Exact non-GO claims

The complete emitted record is preserved in [AT4G38370-protnlm-source.json](AT4G38370-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Phosphoglycerate mutase-like protein

CNN (CS 2). “Phosphoglycerate mutase-like protein” is a qualified fold-level description consistent with the histidine-phosphatase domain assignment. The “-like” wording does not assert phosphoglycerate turnover or a glycolytic pathway role.

## Emitted GO claims

All 1 emitted GO claims are individually assessed in [AT4G38370-protnlm-predictions-review.yaml](AT4G38370-protnlm-predictions-review.yaml).

## Family integration

PTHR47821:SF2 places the target among phosphoglycerate-mutase-family proteins. The histidine-phosphatase fold encompasses different phosphosugar reactions, so a common RHG catalytic motif cannot identify a substrate. It also does not establish the specialized secreted phytase architecture of another histidine-phosphatase branch.

## Evidence limits

No target-specific biochemical study was located under AT4G38370 or Q0WW53. The TIGAR primary report is abstract-only and explicitly establishes donor enzymology. The genuine Falcon synthesis supplies family hypotheses but does not establish a target reaction. The sequence comparison is exploratory: sparse global alignments are not used to call residue loss or to identify an evolved pseudoenzyme.

Exact sequence mapping: [AT4G38370-bioinformatics/RESULTS.md](AT4G38370-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Done without opening any ProtNLM file or prediction-evidence folder.

### Entry identity

- Q0WW53 is the RIKEN full-length cDNA entry (EMBL BAE98645.1) for At4g38370. Its 225-residue
  sequence is identical to F4JTN4, the reference-proteome entry from the genome annotation (EMBL
  AEE86920.1, RefSeq NP_568040.1, Proteomes UP000006548). A third TrEMBL entry, Q8LCU4, is a cDNA
  variant differing only at K90E. See `AT4G38370-bioinformatics/RESULTS-rereview.md`.
- Q0WW53 is therefore not a fragment, isoform or alternative gene model. It is a redundant entry for
  the full canonical product.
- QuickGO (checked 2026-10-21): Q0WW53 has 0 GO annotations, matching the empty GOA file. The TAIR rows
  for the locus are on F4JTN4: `GO:0003674` ND, `GO:0008150` ND, and `GO:0005634` nucleus by ISM
  (GO_REF:0000122). No repo review exists for F4JTN4.

### Evolutionary placement

- PANTHER PTHR47821 (PHOSPHOGLYCERATE MUTASE FAMILY PROTEIN) has a single subfamily, SF2. The PANTHER 19
  reference tree (treeinfo service) has 47 leaves: land plants, Klebsormidium, Chlamydomonas,
  Thalassiosira and Monosiga. The root node is PTN005357400 (Eukaryota).
- InterPro member counts: 951 proteins. Viridiplantae 587, Fungi 67, Bacteria 182, Metazoa 15. There
  are no Swiss-Prot members and no members in human, mouse, yeast, fission yeast, E. coli, fly, worm or
  zebrafish. No family member has been characterised experimentally. Q0WW53 has no IBA rows, so PAINT
  has not propagated any function to this family.
- Ortholog names in RefSeq ("metal-independent phosphoserine phosphatase", "Mb2253c-like") are
  automatic name transfers. They are not evidence and are not used.
- The characterised branch-1 enzymes are in other PANTHER families: human and E. coli dPGM are in
  PTHR11931, and TIGAR is in PTHR46517 (verified from UniProt). I used them only as fold-level
  comparators to test whether the catalytic residues are retained. No substrate-specific function is
  transferred from them.

### Catalytic residues (new script `catalytic_residues_rereview.py`)

- Q0WW53 has RHG at 16-18, LRERYFG at 107-113 and SHGD at 172-175.
- In local alignments (31-36% identity), His17 aligns with the curated phosphohistidine nucleophile of
  PGAM1, GpmA and TIGAR. Glu109 aligns with their proton donor/acceptor, and His173 aligns with the
  transition-state stabiliser of PGAM1 and GpmA.
- Conclusion: the protein is probably catalytically active, but its substrate and reaction class are
  unresolved.

### Literature

PubMed and Europe PMC searches for At4g38370, Q0WW53 and F4JTN4 found no functional study. Europe PMC
returned two hits that only mention the locus in large-scale data (a phylogenetic marker set and an
embryo single-nucleus expression study). PMID:22223895 is the large-scale proteomics study behind PE
level 1. The falcon report agrees that no gene-specific literature exists.

### Changes to the review

- Rewrote the description in terms of family placement and the retained catalytic triad.
- Added one core function (predicted phosphotransfer catalysis) with no GO molecular function asserted,
  plus a BIOLOGY knowledge gap and suggested experiments.
- Lowered the relevance of the TIGAR paper to LOW because it is a different PANTHER family. Kept all
  earlier references, and marked the prediction-derived files as unused.
- No GOA rows to act on.

### Relative

No experimentally characterised ortholog or paralog exists within PTHR47821. The next item is the
canonical reference-proteome entry for the same gene, F4JTN4, which holds the TAIR GO rows and has no
review. It would go in `genes/ARATH/AT4G38370__F4JTN4`.

The PANTHER family review `interpro/panther/PTHR47821/PTHR47821-review.yaml` agrees on the SF2
placement. Its coherence is UNKNOWN and it leans on TIGAR, which is in a different family. The review
does not disagree on subfamily placement. No module in `modules/` mentions this gene.
