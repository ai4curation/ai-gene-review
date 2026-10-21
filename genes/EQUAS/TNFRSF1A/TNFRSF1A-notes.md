# TNFRSF1A (donkey, A0A9L0JKX4) notes

## Sequence and record

- Unreviewed TrEMBL entry, 410 aa, "TNF receptor superfamily member 1A" (PE 4, predicted);
  PANTHER PTHR46861:SF1; signal peptide 1..29, two annotated TNFR-Cys repeats (43..82, 83..126),
  transmembrane segment 172..194, death domain 311..396
  [file:EQUAS/TNFRSF1A/TNFRSF1A-uniprot.txt "Lacks conserved residue(s) required for the propagation of"].
- 7 GOA rows, all IEA (5 TreeGrafter, 1 InterPro2GO, 1 GO_REF:0000108 inferred from the
  TreeGrafter receptor-activity row).
- Donkey vs human P19438 (455 aa): 74.32% identity over 405 paired residues, 89% coverage of
  human. The alignment leaves human residues 64-106 unpaired (in-frame 43-residue gap) and a
  short cytoplasmic gap 261-265
  [file:EQUAS/TNFRSF1A/TNFRSF1A-bioinformatics/RESULTS.md "- human residues 64-106."].
  Human 64-106 spans the C-terminal half of TNFR-Cys 1 (43-82) and most of TNFR-Cys 2 (83-125),
  removing human disulfides 62-81 and 84-99. The membrane-proximal TNFR-Cys 3/4 region,
  transmembrane segment and the death domain are retained (the death-domain region aligns
  without gaps in `alignment.txt`).
- A second donkey TNFRSF1A entry (A0A8C4MD74, 453 aa) exists (UniProt REST query 2026-10-14),
  and horse also has a 410-aa model (A0A5F5PQM0) besides longer entries, so A0A9L0JKX4 looks like
  an alternative transcript/gene model lacking part of the ligand-binding ectodomain.

## Ortholog biology

- Human TNFR1 is the receptor for TNF and lymphotoxin-alpha; the death domain recruits TRADD
  and downstream adaptors for NF-kB and apoptotic signalling
  [file:EQUAS/TNFRSF1A/TNFRSF1A-bioinformatics/human_P19438-uniprot.txt "Receptor for TNFSF2/TNF and homotrimeric TNFSF1/lymphotoxin-alpha."].
- Ligand binding is by the elongated four-domain ectodomain in the groove between TNF subunits
  [PMID:8387891 "The receptor fragment, a very elongated end to end assembly of four similar folding domains, binds in the groove between two adjacent TNF beta subunits."].
  The abstract does not map contacts to individual CRDs; that the 43-residue deletion
  compromises ligand binding is an inference, not an observation.
- Existing human review: genes/human/TNFRSF1A/TNFRSF1A-ai-review.yaml (ACCEPTs TNF receptor
  activity, TNF binding, receptor complex, membrane raft, inflammatory response).

## Decisions

- Ligand-dependent terms (TNF binding, TNF receptor activity, TNF-mediated signaling, receptor
  complex, inflammatory response): UNDECIDED for this sequence model - correct for the gene,
  but this protein lacks part of CRD1 and most of CRD2.
- Membrane raft: KEEP_AS_NON_CORE (membrane anchor retained).
- Signal transduction (death domain InterPro2GO): ACCEPT (broad, but the most specific process
  assertable for this model).
- NEW: plasma membrane (ISS from human, PMID:22801493 via UniProt).

## ProtNLM2 (donkey40 snapshot)

- GO:0016020 membrane -> LSP: correct; donkey GOA has the more specific membrane raft
  (a descendant of membrane in GO).
- GO:0007165 signal transduction -> CNN (exact term in GOA via InterPro death domain; the
  intracellular signalling module is intact).
- Non-GO: subcellular_location "Cell membrane", "Membrane", "Golgi apparatus membrane" (not
  scored).

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Deep research: `just deep-research-falcon EQUAS TNFRSF1A --fallback perplexity-lite` failed
(falcon and the perplexity-lite fallback both exited with an error; no deep-research file was
written). The re-review uses the cached publications, the human P19438 record and new sequence and
exon-structure analysis.

### Identity of the benchmark accession (alternative gene model)

- New analysis `TNFRSF1A-bioinformatics/compare_isoforms_rereview.py` -> `RESULTS-rereview.md`,
  `results-isoforms-rereview.json`. Both donkey entries map to Ensembl gene ENSEASG00005016176.
  A0A9L0JKX4 (410 aa, ENSEAST00005054546, non-canonical transcript) equals the canonical
  A0A8C4MD74 (453 aa, ENSEAST00005025834, Ensembl canonical) minus one contiguous 43-residue block
  (A0A8C4MD74 65-107)
  [file:EQUAS/TNFRSF1A/TNFRSF1A-bioinformatics/RESULTS-rereview.md "The 410-aa transcript lacks exactly one exon of the canonical transcript: exon 3 (ENSEASE00005153555, 129 nt = 43 codons, in frame)."].
- So the benchmark accession is an exon-3-skipping splice-variant model of TNFRSF1A, 43 aa shorter
  than the canonical product. Missing: second half of CRD1 and most of CRD2 (human 64-106 equivalent,
  disulfides 62-81 and 84-99). Retained: signal peptide, first half of CRD1, CRD3/CRD4 region,
  transmembrane helix, death domain (aligns gap-free to human). No catalytic residues are relevant
  (receptor, not enzyme). The exon-3-skipped form is not among the five human P19438 isoforms;
  expression of the donkey transcript is unverified.
- Neither donkey entry is Swiss-Prot reviewed; A0A8C4MD74 is the canonical product. No review for it
  exists in the repo.

### Evolutionary grounding

- Both donkey entries are PANTHER PTHR46861:SF1 (TNFRSF1A). PAINT places TNF receptor activity,
  TNF binding, signaling receptor complex, membrane raft and inflammatory response by IBD at the
  Euteleostomi node PTN002930098 (seeds human P19438 and/or mouse MGI:1314884;
  `interpro/panther/PTHR46861/PTHR46861-paint.tsv`). The donkey TreeGrafter rows are these terms.
  PAINT did not place TNF-mediated signaling, apoptosis or NF-kB terms at this node; the
  TNF-mediated signaling row here is a GO_REF:0000108 inference from the receptor-activity row, not a
  PAINT decision. No disagreement on subfamily placement: the family review
  (`interpro/panther/PTHR46861/PTHR46861-review.md`) describes PTHR46861 as a narrow TNFR1 ortholog
  family, consistent with both donkey entries.

### Decisions (unchanged in substance from the earlier review)

- Ligand-dependent rows (TNF receptor activity, TNF binding, TNF-mediated signaling, signaling
  receptor complex, inflammatory response): UNDECIDED. Correct for the gene and its canonical
  product; not confirmable for a product lacking most of CRD2. Reasons now name the exon-3 skip,
  the PAINT node and the canonical accession.
- Signal transduction (InterPro death domain): ACCEPT; death domain intact.
- Membrane raft: KEEP_AS_NON_CORE. Plasma membrane NEW (ISS from human) kept.
- Quote fixes: replaced the bare "Death" feature quote with the TNFRSF1A_death InterPro xref, and the
  "Transmembrane helix" keyword quote with the Phobius TRANSMEM feature line.
- Description rewritten to state the alternative-transcript identity.

### Relative to review next

- Same-gene canonical product A0A8C4MD74 (donkey TNFRSF1A, 453 aa); no review exists. Folder would
  be genes/EQUAS/TNFRSF1A__A0A8C4MD74 because genes/EQUAS/TNFRSF1A is keyed to A0A9L0JKX4.
- Characterised orthologs already reviewed: genes/human/TNFRSF1A (P19438), genes/mouse/Tnfrsf1a (P25118).
- Modules mentioning TNFRSF1A: modules/tnf_signaling.yaml, modules/nfkb_canonical_signaling.yaml,
  modules/death_receptor_apoptotic_signaling.yaml.

## 2026-10-21 — NEW rows withdrawn: already annotated on another product of the same gene

The re-review proposed NEW rows (GO:0005886 plasma membrane) on this accession. GOA already carries the same terms on
another product of the same gene, reviewed in `genes/EQUAS/TNFRSF1A__A0A8C4MD74/`. GOA propagates gene-level
annotations to one representative product per gene, so adding them to a second product fills a
convention rather than a curation gap. The rows were withdrawn under the rule applied across the
ProtNLM2 re-review cohorts, first raised in the review of PR #5303. The gene-level function is unchanged.
