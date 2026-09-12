# MOCOS (human) — gene review notes

UniProt: Q96EN8 (MOCOS_HUMAN). HGNC:18234. Gene on chr 18q12.2. 888 aa; MW ~98 kDa.
EC 2.8.1.9. HAMAP-Rule MF_03050.

## Core biology

MOCOS is **molybdenum cofactor sulfurase** (molybdenum cofactor sulfurtransferase; MoCo
sulfurase, MCS/MOS/hMCS). It is a **class-V PLP-dependent (cysteine-desulfurase-like)
enzyme** that converts the molybdenum cofactor (MoCo) from its dioxo/oxo form to the
terminal-**sulfido** (thio) form. This sulfurated MoCo is required specifically by the
molybdo-flavoenzymes **xanthine dehydrogenase/oxidase (XDH/XO)** and **aldehyde oxidase
(AOX1/AO)** — but NOT by the third human molybdoenzyme, sulfite oxidase, which uses the
non-sulfurated MoCo. [file:human/MOCOS/MOCOS-uniprot.txt "Sulfurates the molybdenum cofactor"];
[Reactome:R-HSA-947499 "The exchange is catalyzed by the MOCOS cysteine desulfurase (Ichida et al, 2001)"].

### Two-domain architecture
- N-terminal **NifS-like** (class-V aminotransferase / cysteine-desulfurase) domain: binds
  PLP (N6-(pyridoxal phosphate)lysine at Lys264; active-site residue at 424 per UniProt FT)
  and performs the **L-cysteine desulfurase** step, abstracting sulfur from L-cysteine and
  producing L-alanine + a protein persulfide.
- C-terminal **MOSC / Moco-binding** domain (residues ~706–867): binds the MoCo substrate
  and receives the mobilized sulfur.

Mechanistic statement (PMID:34356852): "The NifS-like domain catalyzes the mobilization of
sulfur from L-cysteine in a PLP-dependent manner via its so-called L-cysteine desulfurase
activity, with the liberated sulfur serving as a substrate for sulfuration of the
C-terminally bound Moco." [PMID:34356852].

### Catalytic activity (UniProt / Rhea RHEA:42636)
Mo-molybdopterin + L-cysteine + AH2 = thio-Mo-molybdopterin + L-alanine + A + H2O; EC 2.8.1.9.
Cofactor: pyridoxal 5'-phosphate. Pathway: cofactor biosynthesis; molybdopterin
biosynthesis (UniPathway UPA00344).
[file:human/MOCOS/MOCOS-uniprot.txt].

### Localization
Cytosol (Reactome C:GO:0005829; MoCo biosynthesis / MoCo sulfuration is cytosolic in humans).

## Disease
**Xanthinuria type II (XAN2, MIM:603592)** — autosomal recessive; combined XDH + AOX
deficiency (in contrast to type I, isolated XDH deficiency from XDH variants). Patients
excrete large amounts of xanthine, form xanthine urolithiasis, have very low serum/urine
uric acid, and cannot metabolize allopurinol to oxypurinol.
[file:human/MOCOS/MOCOS-uniprot.txt "Xanthinuria 2 (XAN2)"];
[PMID:11302742 "a functional defect of the HMCS gene is responsible for classical xanthinuria type II"].

## Key references (verified against cached publications)

- **PMID:11302742** (Ichida et al. 2001) — cloned HMCS/MOCOS from liver cDNA; identified a
  nonsense variant (Arg419Ter) in two type II xanthinuria patients; established HMCS as the
  gene responsible for type II and that "HMCS protein functions to provide a sulfur atom for
  the molybdenum cofactor of XDH and AO." Basis of IMP annotations to MoCo biosynthesis and
  sulfurtransferase activity. (Abstract-only in cache; full_text_available: false.)

- **PMID:34356852** (Peretz et al. 2021, Biomedicines) — full text available. Largest
  xanthinuria cohort; direct biochemical characterization of recombinant human MOCOS-NifS
  and its variants. The type II Thr349Ile variant "resulted in a reduced yield, reduced
  binding of the PLP cofactor and absence of cysteine desulfurase activity." C-terminal
  variants Pro591Ser and Arg776Cys impair Moco binding. Establishes the PLP-dependent
  L-cysteine desulfurase mechanism and direct catalytic (IDA) evidence for MoCo sulfuration.
  Source of UniProt CATALYTIC ACTIVITY / COFACTOR / PATHWAY / EC 2.8.1.9.

- **Reactome R-HSA-947499** ("Exchange of oxygen with sulfur in MoCo") and **R-HSA-947581**
  ("Molybdenum cofactor biosynthesis") — TAS annotations; cytosol, MoCo biosynthetic process,
  sulfurtransferase activity. Consistent with UniProt.

## Interactions (GOA IPI "protein binding", GO:0005515)

All six IPI annotations derive from high-throughput human-interactome mapping screens and
name only two interactors, both also listed in the UniProt INTERACTION block:
- **PARVA** / parvin-alpha (Q9NVD7) — PMID:21516116, 25416956, 28514442, 33961781.
- **ARL8A** / ADP-ribosylation-factor-like 8A (Q96BM9) — PMID:32296183, 33961781.
[file:human/MOCOS/MOCOS-uniprot.txt "Q96EN8; Q9NVD7: PARVA" / "Q96EN8; Q96BM9: ARL8A"].
These are systematic Y2H/AP-MS interactome data points with no functional characterization
relating them to MoCo sulfuration; not part of the core evolved enzymatic function. Kept as
bare "protein binding" over-annotations (MARK_AS_OVER_ANNOTATED — never REMOVE an IPI).

## Annotation review summary

Core MF: **GO:0008265 molybdenum cofactor sulfurtransferase activity** (IDA PMID:34356852,
IMP PMID:11302742) — ACCEPT as core. **GO:0030170 pyridoxal phosphate binding** — required
PLP cofactor; IEA is correct but under-supported vs the direct PLP evidence in PMID:34356852;
ACCEPT (core, PLP is the catalytic cofactor).
Core BP: **GO:0006777 Mo-molybdopterin cofactor biosynthetic process** (IMP; well supported).
Location: **GO:0005829 cytosol** (TAS Reactome) — ACCEPT.

Over-general / redundant MF IEAs: GO:0003824 catalytic activity (InterPro IEA, generic parent);
GO:0016829 lyase activity (UniRule IEA — MOCOS is a transferase/sulfurtransferase, EC 2.8.1.9,
NOT a lyase; the reaction is a sulfur-transfer, not a lyase reaction) → REMOVE as clearly
wrong IEA. GO:0030151 molybdenum ion binding (IEA) — MOCOS handles the Mo-molybdopterin
cofactor as substrate rather than binding a free Mo ion in the catalytic sense; kept as
non-core (defensible but not the informative core MF).

Redundant BP terms: GO:0043545 molybdopterin cofactor metabolic process (IBA), GO:0032324
molybdopterin cofactor biosynthetic process (IEA + TAS Reactome) — correct-but-general
relatives of the more specific GO:0006777; KEEP_AS_NON_CORE.
</content>
