# mmf2 (SPAC1039.10) — S. pombe — curation notes

## Identity / provenance

- UniProt: **Q9UR06** (MMF2_SCHPO), 126 aa precursor, "Protein mmf2, mitochondrial";
  AltName "Maintenance of mitochondrial function 2". PomBase standard name **mmf2**,
  systematic name **SPAC1039.10** (synonym hpm1; obsolete ORF SPAC922.01).
  [genes/SCHPO/mmf2/mmf2-uniprot.txt]
- PomBase product line: "mitochondrial matrix protein, YjgF family protein Mmf2,
  reactive intermediate imine deaminase A homolog, NNf2, implicated in detoxification
  and branched amino acid biosynthesis"; **characterisation status = "conserved unknown"**
  (queried PomBase JSON API 2026-07-06). So there is *no direct experimental
  characterisation of the pombe protein's biochemical activity*; the annotations are
  homology/phylogeny-based.

## Domain / family (inline domain reasoning)

- Family: **RidA / YjgF / YER057c / UK114** (a.k.a. RutC family). UniProt SIMILARITY:
  "Belongs to the RutC family." InterPro IPR006056 (RidA), IPR006175
  (YjgF/YER057c/UK114), IPR035959 (RutC-like_sf); Pfam PF01042 (Ribonuc_L-PSP);
  CDD cd00448 (YjgF_YER057c_UK114_family); NCBIfam TIGR00004 "Rid family detoxifying
  hydrolase"; PANTHER PTHR11803 "2-IMINOBUTANOATE/2-IMINOPROPANOATE DEAMINASE RIDA",
  subfamily PTHR11803:SF58 "PROTEIN HMF1-RELATED". [mmf2-uniprot.txt]
- These proteins form homotrimers with three active-site clefts at the subunit
  interfaces (canonical RidA fold; Gene3D 3.30.1330.40 RutC-like).
- **Catalytic-residue check (done inline).** RidA imine/enamine deaminase activity
  requires a single conserved active-site **arginine** (Arg105 in *S. enterica* RidA;
  Arg107 in human hp14.5) that makes a bidentate salt bridge to the substrate
  carboxylate. I aligned mmf2 (Q9UR06) to *S. enterica* RidA by pairwise global
  alignment (script run under uv/python 3.12). mmf2 retains:
  - the catalytic Arg in the conserved C-terminal **P-A-R** motif: mmf2 `...DPMPAR...`
    R at **position 101** aligns to RidA `...NATFPAR...` R105.
  - the conserved N-terminal **G-P-Y** substrate-pocket motif (mmf2 pos 15 `GGPY`,
    RidA pos 15 `GPY`).
  - the conserved C-terminal **KIEIE** motif (mmf2 pos 117, RidA pos 118).
  => The catalytic machinery for imine/enamine (2-iminopropanoate / 2-iminobutanoate /
  2-aminoacrylate) deamination is intact. A RidA-type deaminase MF is therefore
  **domain-defensible** for mmf2.

## What is KNOWN (well-supported)

1. **RidA-family enamine/imine deaminase activity (by orthology + conserved catalytic Arg).**
   RidA proteins hydrolyze the reactive enamine 2-aminoacrylate (2AA) and related
   enamines/imines (e.g. 2-iminopropanoate/2-iminobutanoate) to the corresponding
   2-oxo (keto) acids, pre-empting metabolite damage.
   [PMID:29487232 "RidA family proteins are deaminases that hydrolyze the reactive enamine 2-aminoacrylate (2AA), and other enamine/imine substrates, to ketoacids"]
   [PMID:25975565 "The Rid1, Rid2, and Rid3 subfamilies retain the conserved arginine and glutamate residues found in RidA"]
2. **Mitochondrial (matrix) localization** — UniProt has a predicted N-terminal
   mitochondrial transit peptide (Flags: Precursor; KW Transit peptide) and
   SUBCELLULAR LOCATION Mitochondrion + Cytoplasm. PomBase/GOA: mitochondrial matrix
   (ISO from *S. cerevisiae* Mmf1p, SGD:S000001313) and cytosol/mitochondrion (IBA).
   [mmf2-uniprot.txt]
3. **Ortholog function (S. cerevisiae Mmf1p / YIL051C) — the source of the "Mmf" name.**
   Mmf1p is a mitochondrial-matrix RidA protein; deletion causes loss of mtDNA and a
   growth defect (Δmmf1 → rho0 petite). The paralog Hmf1p (cytoplasmic) has no visible
   deletion phenotype but can functionally replace Mmf1p when routed to mitochondria.
   [PMID:11003673 "Mmf1p is a mitochondrial matrix factor" ... "Deltammf1 cells lose mitochondrial DNA (mtDNA) and have a decreased growth rate, while Deltahmf1 cells do not display any visible phenotype"]
   Mechanistically, Mmf1p maintains mtDNA **indirectly** by deaminating 2AA generated
   by mitochondrial PLP-dependent serine/threonine dehydratases (Ilv1p, Cha1p); without
   Mmf1p, 2AA accumulates and damages PLP enzymes (incl. iron-metabolism enzymes),
   destabilizing the mitochondrial genome. Human UK114 can substitute for Mmf1p.
   [PMID:29487232 "The RidA family protein Mmf1p deaminates 2-aminoacrylate, preempting metabolic stress and loss of the mitochondrial genome"]
   [PMID:29487232 "Mmf1p indirectly contributes to mitochondrial DNA maintenance by preventing 2-aminoacrylate stress derived from mitochondrial amino acid metabolism"]

## What is NOT known (gaps specific to pombe mmf2)

- **No direct biochemistry on the pombe protein**: the specific in-vivo enamine/imine
  substrate for mmf2 (2-aminoacrylate vs 2-iminobutanoate vs a broader set) has not
  been demonstrated experimentally. Family assignment (PANTHER SF58 "HMF1-RELATED")
  and the intact catalytic Arg make 2AA/2-iminopropanoate the most likely substrate,
  but this is inference.
- **No characterized mmf2Δ phenotype in pombe tied to mtDNA/2AA.** PomBase records
  only high-throughput screen phenotypes (deletion is **viable, normal morphology**;
  scattered stress sensitivities: diamide, lithium/LiCl, tunicamycin, terbinafine,
  itraconazole, KCl/MgCl2/LiCl+SDS; resistance to EGTA; decreased centromeric outer-repeat
  silencing). None of these was individually followed up, and none directly demonstrates
  a 2AA / mtDNA-maintenance role in pombe. (PomBase single-locus phenotype list,
  queried 2026-07-06.)
- **Mitochondrial-matrix localization is inferred, not directly shown in pombe**
  (ISO from cerevisiae + transit-peptide prediction). The dual mito/cytoplasm
  annotation may reflect a fraction in the cytosol (as for the cerevisiae paralog Hmf1p)
  or simply pre-import protein; not experimentally resolved for pombe.
- The pombe genome may encode more than one RidA paralog; whether mmf2 is the sole
  mitochondrial RidA and which serine/threonine dehydratases generate its substrate
  in pombe are open questions.

## Annotation-by-annotation reasoning (GOA)

| term | ev | ref | decision |
|------|----|-----|----------|
| GO:0019239 deaminase activity (MF, enables) | IBA | GO_REF:0000033 | MODIFY → GO:0016838 carbon-nitrogen lyase, or keep general; family MF is the core. Actually deaminase activity is defensible but non-specific; propose more specific RidA activity via core_functions. Decision: ACCEPT (domain-defensible, catalytic Arg present) but note it is general. |
| GO:0005739 mitochondrion (CC, is_active_in) | IBA | GO_REF:0000033 | ACCEPT (redundant with matrix) |
| GO:0005829 cytosol (CC, is_active_in) | IBA | GO_REF:0000033 | KEEP_AS_NON_CORE — RidA paralogs are partly cytosolic; but for a matrix-targeted protein this is likely IBA tree noise / pre-import pool. Keep, non-core. |
| GO:0005737 cytoplasm (CC, located_in) | IEA | GO_REF:0000044 | KEEP_AS_NON_CORE (SubCell mapping; parent of cytosol) |
| GO:0005739 mitochondrion (CC, located_in) | IEA | GO_REF:0000044 | ACCEPT (SubCell mapping consistent with transit peptide) |
| GO:0008150 biological_process (ND) | ND | GO_REF:0000015 | KEEP_AS_NON_CORE (root ND placeholder; leave) |
| GO:0005759 mitochondrial matrix (CC, is_active_in) | ISO | GO_REF:0000024 | ACCEPT — best-supported localization (ISO from cerevisiae Mmf1p matrix). |

Note: existing-annotation term ids are trusted (from GOA) — do not rewrite.

## Core function summary (for core_functions)

mmf2 is, by family assignment and retention of the catalytic active-site arginine,
a **RidA/Rid-family reactive enamine/imine deaminase** (a "metabolite-damage
pre-emption" / hydrolase-type enzyme) that most plausibly hydrolyzes the reactive
enamine 2-aminoacrylate (and/or 2-iminopropanoate/2-iminobutanoate) to the stable
2-oxo acid, acting in the **mitochondrial matrix**. By analogy to the *S. cerevisiae*
ortholog Mmf1p and human UK114, its likely physiological role is protecting
mitochondrial PLP-dependent enzymes (and thereby indirectly mitochondrial genome
integrity) from enamine/imine damage arising from serine/threonine catabolism. The
specific in-vivo substrate and phenotype in pombe are not experimentally established.
