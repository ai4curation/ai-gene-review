# ABCB6 (human, Q9NP58) curation notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: ABCB6 is the closest experimentally characterised relative of
*Drosophila* Hmt-1 (Q9VF20). Both are in PANTHER subfamily PTHR24221:SF654
(ABCB6) [file:human/ABCB6/ABCB6-uniprot.txt "DR   PANTHER; PTHR24221:SF654; ATP-BINDING CASSETTE SUB-FAMILY B MEMBER 6; 1."].
This review was done without opening any ProtNLM2 prediction file.

### Provenance / process

- `just fetch-gene human ABCB6` created the uniprot, goa and stub review files
  (101 GOA rows). `just fetch-gene-pmids` cached all 20 GOA PMIDs.
- Deep research FAILED: `just deep-research-falcon human ABCB6 --fallback perplexity-lite`
  failed on Edison authentication ("Failed to authenticate"), and the
  perplexity fallback returned HTTP 401 (insufficient quota). No
  deep-research file exists; the review is based on the cached publications,
  the UniProt record, the PAINT data in `interpro/panther/PTHR24221/` and
  Reactome cache entries.

### PAINT / phylogenetic placement (interpro/panther/PTHR24221/PTHR24221-paint.tsv)

- PTN001199916 (taxon:6072, Eumetazoa): IBD GO:0015439 ABC-type heme transporter
  activity, GO:0020037 heme binding, GO:0015886 heme transport. Sole seed
  UniProtKB:Q9NP58 (human ABCB6).
- PTN008609345 (taxon:33154, Opisthokonta): IBD GO:0005774 vacuolar membrane.
  Seeds FB:FBgn0038376 (Hmt-1), RGD:71077 (rat Abcb6), Q9NP58, WB:WBGene00001815 (C. elegans hmt-1).
- PTN000657189 (deep ABCB node): GO:0042626 / GO:0055085 transmembrane transport.
- No PAINT node in this family carries a cadmium term (GO:0098849 cellular
  detoxification of cadmium ion, GO:0015434 ABC-type cadmium transporter activity),
  although human ABCB6 has an IDA for GO:0098849 (PMID:31053883, 2019) and the
  PAINT heme nodes were annotated 2019-2021. Treated as a deliberate curator
  decision not to propagate cadmium detoxification; consistent with the fact that
  *Drosophila* HMT-1 confers Cd tolerance but does not transport Cd-phytochelatin
  [PMID:19001374 "heterologously expressed DmHMT-1 suppresses the Cd2+ hypersensitivity of S. pombe hmt-1 mutants and localizes to the vacuolar membrane but does not transport Cd.PC complexes"],
  i.e. the transported species is not established across the clade.

### Experimentally established in human (direct evidence on ABCB6 itself)

- ATP-dependent porphyrin transport, including hemin and coproporphyrin III:
  - mitochondrial porphyrin uptake [PMID:17006453 "Here we demonstrate that ABCB6 is uniquely located in the outer mitochondrial membrane and is required for mitochondrial porphyrin uptake"];
  - purified, liposome-reconstituted protein; Walker A K629A dead
    [PMID:23792964 "Mutagenesis of the conserved lysine to alanine (K629A) in the Walker A motif abolished ATP hydrolysis and substrate transport"];
  - plasma-membrane export [PMID:27507172 "Plasma membrane ABCB6 exports a variety of disease-related porphyrins"];
  - porphyrin/GSH-stimulated ATPase and cryo-EM with CPIII and hemin
    [PMID:33007128 "the ATPase activity of ABCB6 stimulated with a variety of porphyrin substrates showed different profiles in the presence of glutathione (GSH)"]
    [PMID:35950458 "Here we report the cryo-electron microscopy (cryo-EM) structures of human ABCB6 with its substrates, coproporphyrin III (CPIII) and hemin"].
- Heme/porphyrin binding (hemin-agarose; structures) and ATP binding (ATP-agarose,
  K629G negative control) [PMID:27507172 "as expected the positive control K629G did not bind ATP"].
- Localization: plasma membrane (erythrocyte Lan antigen) [PMID:22246506], endolysosomal
  limiting membrane, MVBs, lysosomes [PMID:25627919 "we confirm the endo-lysosomal localization of ABCB6 and show that the protein is internalized from the plasma membrane through endocytosis, to be distributed to multivesicular bodies and lysosomes"],
  melanosomes [PMID:29940187], exosomes [PMID:22655043]. Transits ER/Golgi (glycoprotein)
  [PMID:21199866, PMID:18279659].
- Cadmium tolerance: rescues S. pombe and C. elegans hmt-1 mutants; restores vacuolar Cd
  sequestration; catalytic mutants fail; knockdown in glioblastoma cells alters Cd sensitivity
  [PMID:31053883 "Inactivating mutations of ABCB6 abolished vacuolar sequestration of cadmium, effectively suppressing the cadmium tolerance phenotype"].
- Melanosome PMEL amyloid formation requires catalytically active ABCB6 (siRNA + rescue)
  [PMID:29940187 "PMEL fibril formation and normal maturation of pigmented melanosomes could be restored by the overexpression of wild-type ABCB6 but not by variants containing an inactivating catalytic mutation (K629M) or the G579E DUH mutation"].

### Contested

- Mitochondrial (outer membrane) localization: supported by PMID:10837493, 17006453,
  17661442, 23792964, MitoCoP HTP (PMID:34800366; the cached text does not name ABCB6,
  so not verifiable here); contradicted with endogenous-protein imaging by PMID:18279659,
  22655043, 25627919, 31053883 ("absence in mitochondria (labeled by AIF)").
  Both positive and NOT mitochondrion rows left UNDECIDED.
- Role in de novo heme biosynthesis: claimed by PMID:17006453; contradicted by
  knockdown in K562 [PMID:22655043 "Knock-down studies demonstrate that ABCB6 function is not required for de novo heme biosynthesis in differentiating K562 cells"]
  and by healthy Lan(-) ABCB6-null humans [PMID:22246506 "Lan(-) (ABCB6(-/-)) individuals do not suffer any clinical consequences"].
  UNDECIDED on both sides.

### Source defect

- GO:0007420 brain development and GO:0043588 skin development (IMP, PMID:22100072,
  assigned by UniProt 2012-03-30): PMID:22100072 is the ELOVL4 ichthyosis/intellectual
  disability paper. The cached full text mentions ELOVL4 16 times and ABCB6 zero times;
  its conclusion is "Our findings highlight the critical role of ELOVL4 and VLCFAs in early brain development and in the integrity of the epidermal water barrier."
  These rows appear to be ELOVL4 annotations attached to ABCB6 (or mis-keyed). REMOVE
  with a source_defects entry (PROBABLE).

### Transfer guidance (for Hmt-1)

- Safe at the PAINT level: vacuolar/lysosomal membrane (opisthokont node, seeded by
  Hmt-1 itself plus ABCB6, rat Abcb6, worm hmt-1); heme transporter activity / heme
  binding / heme transport (eumetazoan node seeded only by human ABCB6 — a sound node
  placement but the only experimental support is human).
- Not propagated by PAINT: cadmium detoxification (treat as deliberate), plasma membrane,
  melanosome, mitochondrial localization, porphyria/heme-biosynthesis roles.
