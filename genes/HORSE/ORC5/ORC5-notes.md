# ORC5 (horse, Equus caballus) — A0A3Q2KSP7

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: ProtNLM2 benchmark cohort DONKEY40 + DONKEY40_HORSE_PARTNER. No prior review existed for this
accession; the folder was created with `just fetch-gene HORSE A0A3Q2KSP7 --alias ORC5` and the stub id
was confirmed as A0A3Q2KSP7. ProtNLM2 outputs were not consulted.

### Deep research

`just deep-research-falcon HORSE ORC5 --fallback perplexity-lite` failed: falcon returned
"Failed to authenticate" and the perplexity-lite fallback returned HTTP 401 (insufficient quota). No
deep-research file was produced. The review uses the cached publications below and a local sequence
comparison.

### Identity

- A0A3Q2KSP7 is an unreviewed TrEMBL entry (PE 3), 437 aa, Ensembl ENSECAP00000026851.3, VGNC:21054
  (ORC5), horse chromosome 4.
- It is a full-length ORC5: it aligns to human ORC5 O43913 (435 aa) at 90.5% identity over 432 paired
  positions, covering 99.3% of the human protein (`ORC5-bioinformatics/RESULTS.md`). It is not a fragment
  or a truncated gene model. Domain architecture matches human ORC5: AAA+ (Orc1-like AAA ATPase, Pfam
  PF13191, 8-155), ORC5 lid (PF21639, 204-271) and ORC5 C-terminal winged-helix region (PF14630).
- All human ORC5 ATP-site residues described in the human ORC structure (Walker A GHTASGKT 37-44,
  non-canonical Walker B DKAE 125-128, R104 tether, P139, R143 arginine finger, Y182, R226) are conserved.

### Evolutionary placement

- PANTHER PTHR12705 (ORIGIN RECOGNITION COMPLEX SUBUNIT 5), subfamily SF0. The family has only one
  subfamily, which contains human, mouse, fly, budding and fission yeast ORC5, so there is no subfamily
  split to worry about.
- Horse is a PAINT reference proteome here: the three IBA rows come from node PTN000295037. The PAINT
  curator propagated nuclear ORC (GO:0005664) and DNA replication initiation (GO:0006270) with five
  donors (fly, fission yeast, budding yeast, human) and DNA replication origin binding (GO:0003688) from
  budding yeast Orc5 alone. I treat that as a sound node placement; the horse protein is unambiguously in
  the clade.
- No PANTHER family review for PTHR12705 exists beyond the fetched metadata/entries under
  `interpro/panther/PTHR12705/`; no subfamily disagreement.

### Literature (human ORC5, the closest characterised ortholog in the same subfamily)

- ORC is a six-subunit complex (ORC1-6); ORCs 2-5 form a stable core present throughout the cell cycle
  that associates with ORC1 in G1 [PMID:12909626 "ORCs 2-5 form a complex that is present throughout the
  cell cycle and that associates with ORC1 when it accumulates in G1 nuclei"].
- Human ORC assembly in vitro needs ATP binding by ORC4 and ORC5, not by ORC1 [PMID:17716973
  "Mutations in the ATP-binding sites of Orc4 or Orc5 impair complex assembly, whereas Orc1 ATP binding is
  not required"]. Abstract only in cache.
- Structure of human ORC: ORC1/4/5 form the AAA+ motor module; ATP binds at the ORC1-ORC4 and ORC4-ORC5
  interfaces, and a third nucleotide binds the ORC5 Walker A/B site, whose Walker B is DKAE
  [PMID:28112645 "The third nucleotide binds to Walker-A and -B motifs on ORC5 (Figure 3c), although the
  Walker-B motif is somewhat different (DKAE, rather than DELD (ORC1) or DEFD (ORC4))."]. In budding yeast
  the only active ATPase is Orc1 with an Orc4 arginine finger; ORC5's nucleotide site is structural.
- OBI1 multi-mono-ubiquitylates chromatin-bound ORC3 and ORC5 in S phase; non-ubiquitylable mutants
  impair origin firing [PMID:31160578]. Human ORC5 localises to nucleus and chromatin (UniProt O43913,
  ECO:0000269 PubMed:31160578).
- Isoform 2 of human ORC5 (ORC5T) does not interact with ORC2 (UniProt O43913, ECO:0000305); no evidence
  either way for horse splice forms.

### Decisions

- GO:0005664 nuclear ORC (IBA): ACCEPT (core).
- GO:0000808 ORC (IEA, InterPro): MODIFY to GO:0005664, which the gene already carries.
- GO:0006270 DNA replication initiation (IBA): ACCEPT (core).
- GO:0006260 DNA replication (IEA): MODIFY to GO:0006270.
- GO:0003688 DNA replication origin binding (IBA): ACCEPT; this is an activity of the ORC complex to
  which ORC5 contributes (in the human structure the ORC subunits, with CDC6, form the DNA-binding channel; which ORC5
  residues contact DNA was not tested in the papers cached here).
- GO:0005634 nucleus (IEA): ACCEPT.
- NEW GO:0005524 ATP binding: supported by human ORC5 Walker A mutant/assembly data and the ATP-bound
  crystal structure; all binding residues conserved in horse. No ATPase activity term is proposed, as
  ORC5 is not the catalytic ATPase.

### Relative

Human ORC5 (O43913), ortholog in the same PANTHER subfamily (PTHR12705:SF0) and a donor of the
PTN000295037 IBAs. No review exists in the repo (`genes/human/ORC5` absent), so it needs review. The
donkey ORC5 (A0A9L0JAR4, `genes/EQUAS/ORC5`) is the campaign partner and is reviewed separately.

### Modules

`modules/dmel_replication_origin_licensing_activation.yaml` contains fly Orc5 as a part; there is no
mammalian ORC/pre-RC module.
