# Foxj3 (mouse, Q8BUR3) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: mouse Foxj3 is reviewed as the experimentally characterised relative of the
HORSE FOXJ3 (F6SCJ5) benchmark gene. ProtNLM2 output was not opened or used.

### Deep research

`just deep-research-falcon mouse Foxj3 --fallback perplexity-lite` failed: the Edison
(falcon) API returned "Failed to authenticate" (403) and the perplexity-lite fallback
also failed (JWT token required). No deep-research file exists. The review is built
from the cached primary literature listed below, found by a PubMed search for "Foxj3"
(about 50 hits, mostly cancer/miRNA-target papers that were not used).

### Evolutionary grounding

- UniProt Q8BUR3 maps to PANTHER PTHR46078:SF3 (FORKHEAD BOX PROTEIN J3); human FOXJ3
  Q9UPW0 and horse F6SCJ5 map to the same subfamily. FOXJ2 (human Q9P0K8, mouse Q9ES18)
  is in the sister subfamily PTHR46078:SF1 (checked against UniProt REST, 2026-10-21).
- The IBA rows come from PAINT node PTN002918318 (FOXJ2/FOXJ3 clade), with human FOXJ2
  (Q9P0K8) and human FOXJ3 (Q9UPW0) as donors. The node carries only generic forkhead
  TF terms: Pol II-specific DNA-binding TF activity, Pol II cis-regulatory region
  sequence-specific DNA binding, nucleus, regulation of transcription by Pol II. PAINT
  did not propagate spermatogenesis, meiosis or muscle terms, so those stay as
  mouse-specific experimental findings.
- InterPro: forkhead domain IPR001766 (Pfam PF00250; DNA_BIND 78-173), FOXJ2/3-like
  IPR045912.

### Experimental evidence in mouse (this species)

- [PMID:19914232 "Foxj3 transcriptionally activates Mef2c and regulates adult skeletal
  muscle fiber type identity."] Gene-trap Foxj3 m/m mice have fewer type I fibres and
  impaired regeneration. Gal4-Foxj3 activates a UAS reporter 12-fold. ChIP in C2C12
  myoblasts shows Foxj3 at the conserved forkhead binding site (FBS) of the Mef2c
  skeletal-muscle enhancer. Foxj3 activates the 1.2 kb Mef2c-luc reporter, and
  mutating the FBS abolishes this. This is direct evidence for GO:0001228 and GO:0000978
  in mouse, although it is not in GOA as an experimental row.
- [PMID:27739607 "Multiple roles of FOXJ3 in spermatogenesis..."] (abstract only).
  Mvh-Cre cKO: Sertoli-cell-only testes and early loss of spermatogonia with DSB
  accumulation. Stra8-Cre cKO: meiotic arrest with reduced Rad51, Dmc1, Brca1/2, Hop2,
  Hormad1 and Rnf212 mRNA. This is the source of the IMP spermatogenesis and male
  meiosis I rows. The likely mechanism is transcriptional control of meiotic genes;
  Foxj3 is not itself a component of the meiotic machinery.
- [PMID:41803108] Mouse cortex: nuclear FOXJ3 in VZ/CP and primary neurons (IF).
  Knockdown by in utero electroporation impairs migration and lamination. ChIP-seq in
  Neuro2A identifies Pten as a target, and Pten rescues the defects.
- [PMID:37939221] (abstract only) Adipose-specific Foxj3 KO impairs brown-fat
  thermogenesis; Foxj3 induces PGC-1alpha (Ppargc1a) and Ucp1.
- [PMID:15366017] (abstract only) Embryonic expression in neuroectoderm, neural crest
  and myotome; the closest paralog is FoxJ2.
- [PMID:23047984] (abstract only) miR-494 targets Foxj3 in myocytes.

### Evidence in other species (used only for ISO context)

- Human FOXJ3: HT-SELEX/methyl-SELEX DNA-binding specificities (PMID:23332764,
  PMID:28473536; the cached text does not name FOXJ3, so the FOXJ3 results are presumably in supplementary data). siRNA in
  U2OS cells disrupts the oscillation of a FOX-binding-site reporter and slows
  proliferation (PMID:22740631); this is indirect, and no FOXJ3 ChIP was done (no
  antibody). FOXJ3 ChIP-seq in U2OS cells, overlapping FOXK2/FOXO3 sites (PMID:26578569).
- Xenopus Foxj3 represses Activin/Nodal/BMP-responsive transcription via RNF152/
  beta-catenin (PMID:40522413; morpholino plus overexpression). This was not transferred.

### Decisions

- Accept the PAINT-level TF terms and the activator terms (ISO/IEA are reinforced by
  the direct mouse Mef2c evidence).
- MODIFY the generic InterPro2GO terms (GO:0003700, GO:0006355) and the generic DNA-binding
  terms (GO:0043565, GO:1990837) to their specific descendants (GO:0000981/GO:0001228,
  GO:0006357, GO:0000978).
- Spermatogenesis and male meiosis I (IMP, ARBA IEA): KEEP_AS_NON_CORE. These are
  real cKO phenotypes, and the curators chose to annotate them. Foxj3's role is upstream
  transcriptional control, so they are not core.
- No NEW process terms. Muscle fibre type, regeneration, thermogenesis and cortical
  lamination are downstream phenotypes of a transcription factor and fail the
  participation test. They are recorded in core_functions as context and in
  suggested questions.
