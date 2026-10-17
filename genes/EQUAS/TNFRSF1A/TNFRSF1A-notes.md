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
