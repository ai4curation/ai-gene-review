# SepJ (FraG) in *Anabaena variabilis* ATCC 29413 — research notes

UniProt: **Q3MGV3** (Q3MGV3_TRIV2, unreviewed), 751 aa, ordered locus **Ava_0157**,
*Trichormus variabilis* / *Anabaena variabilis* (strain ATCC 29413 / PCC 7937),
NCBITaxon:240292. UniProt names it an "EamA domain-containing protein" (RecName from Pfam
PF00892). This is the **SepJ/FraG ortholog** of the well-studied septal protein SepJ (FraG,
alr2338) of *Nostoc*/*Anabaena* sp. PCC 7120.

This review is an **orthology-based (ISS) review**: there are no gene-specific functional
publications for the *A. variabilis* protein itself, so the functional annotations are
transferred from the experimentally characterized PCC 7120 ortholog (see
`genes/NOSS1/SepJ/SepJ-ai-review.yaml` and `genes/NOSS1/SepJ/SepJ-notes.md`), applying the
same evidential caution used there.

## Orthology evidence

The ortholog assignment comes from the septal-junction module genome scan
(`modules/septal_junction/RESULTS.md`), which used phmmer / reciprocal best hits (RBH) of the
PCC 7120 exemplar against reference proteomes:

- **Q3MGV3 is a reciprocal best hit (RBH) with the PCC 7120 SepJ exemplar A0ACD7RSI0
  (alr2338): forward E = 0, 97% amino-acid identity** — an essentially one-to-one ortholog
  (much closer than the *N. punctiforme* ortholog B2J1N1 at 53% identity), consistent with the
  close phylogenetic relationship between *A. variabilis* ATCC 29413 and *Anabaena* sp. PCC 7120.
- The reciprocal control is clean: in the positive (heterocyst-forming) genomes the SepJ
  exemplar recovers a strong hit (*A. variabilis* Q3MGV3 at ~97% id; *N. punctiforme* B2J1N1),
  whereas in unicellular negative genomes the best hit is a weak paralog (e.g. *Synechocystis*
  P72732 at 34% id, E = 1e-47) rather than a genuine SepJ ortholog.

**Caveat on the domain grounding.** The C-terminal domain of SepJ belongs to the **broad EamA
/ DMT (drug-metabolite transporter) superfamily (InterPro IPR000620; Pfam PF00892), which has
many paralogs in every cyanobacterial genome**, so InterPro family membership alone does not
discriminate SepJ from other DMT permeases. The orthology call therefore rests on the strong
exemplar homology (RBH, E = 0, 97% identity) plus the shared multidomain architecture, not on
the broad domain family.

## Protein family / domain architecture

Like the PCC 7120 ortholog, Q3MGV3 is a **large (751-residue) multidomain protein** with an
N-terminal coiled-coil region and a C-terminal integral-membrane EamA/DMT permease domain.
From the UniProt record (`SepJ-uniprot.txt`):

- **N-terminal coiled-coil** predicted at residues 41–82 (SAM:Coils), embedded in a long
  extramembrane N-terminal section rich in disordered, Pro/Ser/Thr-type low-complexity linker
  (disordered region ~198–408; low-complexity/polar-residue biases throughout).
- **C-terminal integral-membrane permease domain** with ~10 predicted transmembrane helices
  (Phobius; first TM at 413–433) and an annotated **EamA domain at ~597–733** (Pfam PF00892).
- UniProt records "Belongs to the EamA transporter family" and predicts Coiled-coil,
  Membrane, Transmembrane / Transmembrane-helix keywords.

This mirrors the three-region architecture of PCC 7120 SepJ: an N-terminal coiled-coil, a
central Pro/Ser/Thr-rich linker, and a C-terminal DMT/EamA permease domain
[PMID:21299655 "SepJ is a protein conspicuously located at the cell poles in the intercellular
septa of the filaments"].

## Function transferred from the PCC 7120 ortholog

In PCC 7120, SepJ (FraG) is a central component of the septal machinery that joins adjacent
cells in the filament. It is:

- an integral **cytoplasmic (inner/plasma) membrane** protein localized as a focused spot at
  the intercellular **septa (cell poles)** [PMID:17369306 "the protein is localized at the
  intercellular septa, and when cell division starts, it is localized in a ring whose position
  is similar to that of a Z ring."] [PMID:28979840 "SepJ (also known as FraG 13), FraC, and
  FraD are cytoplasmic membrane proteins that are located at the cell poles in the
  intercellular septa of the filament"];
- a **structural, multimer-forming** component of the septal junctions that binds
  peptidoglycan through its coiled-coil domain [PMID:28979840 "SepJ (predicted MW, 81.3 kDa)
  solubilized from Anabaena membranes was found in complexes of about 296-334 kDa, suggesting
  that SepJ forms multimeric complexes."] [PMID:28979840 "Our results indicate that SepJ forms
  multimers, that it interacts with PG, and that the coiled-coil domain is involved in this
  interaction."];
- required for **filament integrity and gated intercellular molecular exchange (cell-cell
  communication)** underpinning diazotrophy [PMID:21299655 "the coiled-coil domain is required
  for polar localization of SepJ, filament integrity, normal intercellular transfer of small
  fluorescent tracers and diazotrophy."] [PMID:20487302 "The fraC and fraD mutants showed an
  impaired localization of SepJ at the intercellular septa and were hampered in the
  intercellular transfer of the fluorescent probe calcein."].

## Transporter-substrate open question

The C-terminal domain's similarity to DMT/EamA transporters, together with SepJ's septal
position, prompted the hypothesis that it moves small molecules between cells
[PMID:17369306 "raises the possibility that it is involved in the movement of metabolites or
regulatory compounds between neighboring cells."]. However, **no specific transport substrate
for the SepJ permease domain has ever been experimentally established**. Following the PCC 7120
review, the core molecular function is therefore annotated as a **structural (non-catalytic)
role (GO:0005198 structural molecule activity)** rather than as a transporter activity, and the
broad-domain-derived membrane IEA is not promoted to an asserted transport MF.

## Annotation plan (mirrors PCC 7120 SepJ)

Existing GOA for Q3MGV3 (`SepJ-goa.tsv`) = a single IEA cellular-component annotation:

- **GO:0016020 membrane** (IEA, GO_REF:0000120, from InterPro IPR000620 EamA / PANTHER) —
  **MODIFY** → GO:0005886 plasma membrane. Correct in essence (SepJ is an integral membrane
  protein) but overly general; the specific location — the bacterial cytoplasmic/inner
  membrane at the intercellular septa — is known from the PCC 7120 ortholog.

NEW orthology-based (ISS) core annotations transferred from PCC 7120 SepJ:

- **GO:0005198 structural molecule activity** (MF) — structural, multimer-forming, PG-binding
  component of the septal junction.
- **GO:0007267 cell-cell signaling** (BP) — gated intercellular molecular transfer / cell-cell
  communication along the filament.
- **GO:0030428 cell septum** (CC) — focused septal/cell-pole localization.

Core function: structural molecule activity, involved_in cell-cell signaling, located_in
plasma membrane + cell septum. No transporter MF asserted (substrate unestablished).

## Key references (all cached; PCC 7120 ortholog studies)

- PMID:17369306 — Flores et al. 2007, J Bacteriol. Original *sepJ*; septal localization,
  Z-ring, filament integrity + diazotrophy; multidomain permease-like C-terminus. Full text.
- PMID:21299655 — Mariscal et al. 2011, Mol Microbiol. Three-domain functional dissection;
  coiled-coil = anchoring, permease = intercellular exchange. Abstract cached.
- PMID:20487302 — Merino-Puerto et al. 2010, Mol Microbiol. FraC/FraD required for SepJ
  localization and intercellular calcein transfer. Abstract cached.
- PMID:28979840 — Ramos-León et al. 2017, FEBS Open Bio. SepJ multimers + peptidoglycan
  interaction; two-junction-types statement. Full text. PRIMARY for the structural role.
