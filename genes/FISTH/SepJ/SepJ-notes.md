# SepJ (FraG) in *Fischerella thermalis* JSC-11 — research notes

UniProt: **G6FMI5** (G6FMI5_9CYAN, unreviewed), 650 aa, ORF name **FJSC11DRAFT_0082**,
*Fischerella thermalis* JSC-11, NCBITaxon:741277. UniProt names it an "EamA
domain-containing protein" (RecName from Pfam PF00892). *Fischerella* is a true-branching
(Stigonematales-type; UniProt lineage Nostocales / Hapalosiphonaceae), heterocyst-forming
filamentous cyanobacterium. This protein is the **SepJ/FraG ortholog** of the well-studied
septal protein SepJ (FraG, alr2338) of *Nostoc*/*Anabaena* sp. PCC 7120.

This review is an **orthology-based (ISS) review**: there are no gene-specific functional
publications for the *Fischerella thermalis* protein itself, so the functional annotations are
transferred from the experimentally characterized PCC 7120 ortholog (see
`genes/NOSS1/SepJ/SepJ-ai-review.yaml` and `genes/NOSS1/SepJ/SepJ-notes.md`), applying the
same evidential caution used there.

## Orthology evidence

The ortholog assignment comes from the septal-junction module genome scan
(`modules/septal_junction/RESULTS.md`), which used reciprocal-best-hit (RBH) searches of the
PCC 7120 exemplars against reference proteomes:

- **G6FMI5 is the reciprocal best hit in the *F. thermalis* JSC-11 genome to the PCC 7120 SepJ
  exemplar (A0ACD7RSI0): forward E = 1.2e-167, 53.5% amino-acid identity** — a strong match
  consistent with a true one-to-one ortholog.
- The whole septal-junction module reaches *F. thermalis* JSC-11: **all six components
  (FraD G6FUM3, FraC G6FUM4, FraE G6FUM2, SepN G6FVY1, SepJ G6FMI5, AmiC G6FW05) are recovered
  as reciprocal orthologs (48–66% identity)** in this genome, so the deep-branching
  Stigonematales lineage retains an intact septal-junction gene set — corroborating the SepJ
  call by pathway/operon context, not just by a single homology hit.

**Caveat on the domain grounding.** The C-terminal domain of SepJ belongs to the **broad EamA
/ DMT (drug-metabolite transporter) superfamily (InterPro IPR000620; Pfam PF00892), which has
many paralogs in every cyanobacterial genome**, so InterPro family membership alone does not
discriminate SepJ from other DMT permeases. The orthology call therefore rests on the strong
exemplar RBH homology (E = 1.2e-167, 53.5% identity) plus the shared multidomain architecture
and syntenic septal-junction module, not on the broad domain family.

## Protein family / domain architecture

Like the PCC 7120 ortholog, G6FMI5 is a **large multidomain protein** with an N-terminal
coiled-coil region and a C-terminal integral-membrane EamA/DMT permease domain. From the
UniProt record (`SepJ-uniprot.txt`):

- **N-terminal coiled-coil** predicted at residues 39–80 and 139–166 (SAM:Coils), within a
  long extramembrane N-terminal section that carries Pro/Ser/Thr-type low-complexity,
  disordered linker regions (~190–240 and ~280–311).
- **C-terminal integral-membrane permease domain** with ~10 predicted transmembrane helices
  (Phobius; first TM at 319) and an annotated **EamA domain at ~500–639** (Pfam PF00892).
- UniProt records "SUBCELLULAR LOCATION: Cell membrane; Multi-pass membrane protein" and
  "Belongs to the EamA transporter family."

This mirrors the three-region architecture of PCC 7120 SepJ: an N-terminal coiled-coil, a
central Pro/Ser/Thr-rich linker, and a C-terminal DMT/EamA permease domain
[PMID:21299655 "SepJ is a protein conspicuously located at the cell poles in the intercellular
septa of the filaments that has three well-defined domains: an N-terminal coiled-coil domain,
a central linker and a C-terminal permease domain."].

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
  that SepJ forms multimeric complexes."] [PMID:28979840 "These observations support the idea
  that SepJ is a component of the septal junctions that join the cells in the Anabaena
  filament."];
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
broad-domain-derived membrane/transport IEA is not promoted to an asserted transport MF.

## Annotation plan (mirrors PCC 7120 SepJ)

Existing GOA for G6FMI5 (`SepJ-goa.tsv`) = two IEA cellular-component annotations:

- **GO:0005886 plasma membrane** (IEA, GO_REF:0000044, UniProtKB-SubCell) — **ACCEPT**. This
  is already the correct, specific bacterial cytoplasmic/inner-membrane location supported by
  the ortholog's experimental data.
- **GO:0016020 membrane** (IEA, GO_REF:0000002, InterPro IPR000620 EamA) — **MODIFY** →
  GO:0005886 plasma membrane. Correct in essence but overly general; the specific location is
  known.

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
</content>
</invoke>
