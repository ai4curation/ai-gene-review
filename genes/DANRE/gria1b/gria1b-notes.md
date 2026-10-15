# gria1b notes (Danio rerio, glutamate receptor, ionotropic, AMPA 1b; UniProt E7F1V8)

## 2026-09-28 — session log (DANRE_DUPLICATION batch 4, random TGD_tree sample)

**Deep research:** not available (Edison/Falcon 402 Payment Required; OpenAI key invalid). Not
attempted, per instructions. Literature searched by hand (queries listed in `../gria1a/gria1a-notes.md`).
Pair analysis in `../gria1a/gria1a-bioinformatics/RESULTS.md`.

Accession E7F1V8 (TrEMBL, RefSeq XP_005161396 "isoform X1", 917 aa), ZFIN:ZDB-GENE-020125-2,
Ensembl ENSDARG00000032714, chr21. 15 GOA rows (IBA and IEA only), identical to gria1a.

### Literature
- No study of gria1b alone. It appears in the survey of all eight AMPA receptor genes:
  [PMID:18224707 "As a general rule, each pair of duplicated gria genes is differentially expressed, indicating subfunctionalization of AMPA receptor subunit expression in the teleost lineage."]
  ZFIN curation of that paper gives gria1b 17 anatomy terms, all shared with gria1a except otic
  vesicle (long-pec and protruding-mouth stages).
- Maternal transcript: [PMID:16887104 "Transcripts of all AMPAR genes are detected at the time of fertilization, suggesting maternal transcriptions of zebrafish AMPAR genes."]
- The Thyme et al. 2019 screen mutated both copies of duplicated genes
  [PMID:30929901 "If the human gene of interest was duplicated in zebrafish, homozygous mutations were generated for both orthologs."];
  which copy (or the double) gave the gria1 pallium phenotype is not stated in the text.

### Protein (RESULTS.md)
- 82.5% identical to gria1a, 81.7% to gar GRIA1 (gria1a 88.3%). gria1b has significantly more
  changes than gria1a relative to gar (86 vs 34, chi2 = 22.5).
- Ligand-binding residues, pore loop, M2-M3 segment and palmitoylation cysteines unchanged.
- The C-terminal tail is the most diverged part: I at the position of human S849 (mature S831,
  CaMKII/PKC site) and no aligned serine at S863 (mature S845, PKA site); C-terminus TTGM.
  [PMID:20716669 "Native GluA1 subunits undergo regulated phosphorylation at two sites (Ser831 and Ser845) in their C-terminal tails"]
  All Ensembl gria1b translations carry the same changes (not an isoform artefact). The medaka
  gria1b ortholog has L at S849 (so this change is shared by the teleost b lineage) but keeps S at
  S863, and is itself strongly diverged from gar (71.6% vs 87.4% for medaka gria1a).

### Expression (RESULTS.md)
- E-ERAD-475 whole embryo: 5-6 TPM in larvae vs 12-14 for gria1a.
- Bgee: brain, retina, testis (both copies; testis score higher for gria1b) plus mature ovarian follicle, spleen, gill (gria1b only).

### Annotation decisions
- Same as gria1a (see gria1a notes): MF, complex, membrane locations and glutamatergic transmission
  terms accepted; dendritic spine and modulation of chemical synaptic transmission kept as non-core.
- The C-terminal changes do not touch any existing GO term, so no copy-specific change is made;
  they are recorded as a question.
