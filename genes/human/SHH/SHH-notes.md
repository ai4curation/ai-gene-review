# SHH review notes

## 2026-07-14 — source acquisition and review scope

- Seeded the human review with `just fetch-gene human SHH`; the current GOA snapshot contains
  194 annotations. Ran `just fetch-gene-pmids human SHH`, which cached all 21 PMIDs cited by
  those annotations. Seven cached records expose full text; the remainder are abstract-only.
- Ran the required `just deep-research-falcon human SHH --fallback perplexity-lite`. Falcon
  failed with HTTP 402 (payment required) and the fallback failed with HTTP 401 (quota
  exceeded). No provider-named deep-research file was created. This manual journal records the
  fallback review based on UniProt, GOA, cached publications, and targeted official-source
  lookup.
- Added PMID:10226030 because it directly addresses the cerebellar granule-cell-precursor
  annotation and was not among the original GOA references.

## Protein architecture, maturation, and defining molecular activities

SHH is synthesized as a 462-aa precursor with a signal peptide, N-terminal signaling domain,
and C-terminal HINT-related autoprocessing domain. The C-terminal domain catalyzes a coupled
cholesterolysis reaction: precursor cleavage generates SHH-N and transfers cholesterol onto its
new C terminus. HHAT subsequently palmitoylates the N terminus. The C-terminal product is not the
secreted morphogen; mature dually lipidated SHH-N is the signaling product. [PMID:24342078,
"human SHH is synthesized as a 462aa protein precursor of approximately 45 kDa designated as
‘preproprotein’"; "a 265aa C-terminal autoprocessing domain endowed with autoproteolysis and
cholesterol transferase activity"] [PMID:30139912, "After signal peptide cleavage, HH undergoes
autocatalytic processing between its N and C-terminal domain (HH-N and HH-C) in the endoplasmic
reticulum"; "During this reaction, cholesterol is covalently linked to the carboxyl terminus of
HH-N"]

HHAT directly attaches palmitate through an amide linkage to the N-terminal cysteine of SHH; the
reaction occurs during secretory-pathway transit and does not require prior autocleavage or
cholesterylation. [PMID:18534984, "We provide direct biochemical evidence that Hhat is a PAT with
specificity for attaching palmitate via amide linkage to the N-terminal cysteine of Shh";
"Neither autocleavage nor cholesterol modification is required for Shh palmitoylation"]

The mature ligand binds PTCH receptors. Direct human structures show native, dually lipidated
SHH-N engaging PTCH1, including a palmitate-dominated interface and a calcium-mediated interface;
engagement of both is needed for efficient signaling. [PMID:29995851, "The palmitoylated N
terminus of SHH-N inserts into a cavity between the extracellular domains of PTCH1 and dominates
the PTCH1-SHH-N interface"] [PMID:30139912, "one SHH-N molecule engages both epitopes to bind two
PTCH1 receptors in an asymmetric manner"; "simultaneous engagement of both interfaces is
required for efficient signaling in cells"]

SHH-N binding removes PTCH-mediated suppression of SMO, producing GLI-dependent transcriptional
responses. This is SHH's defining signaling activity; downstream developmental phenotypes are
contexts in which the same ligand-receptor mechanism is deployed. [PMID:30139912, "Activation
occurs when the lipid-modified HH-N binds to its receptor, Patched-1 (PTCH1) protein"]
[PMID:24342078, "Hh ligand binding to Ptch relieves this inhibition of Smo, allowing Smo to
activate a signaling cascade through the primary cilium"]

Calcium and zinc binding are real structural/cofactor properties but were retained as non-core.
The HHIP-SHH structure shows HHIP directly coordinating the SHH-bound zinc ion, while later PTCH1
structures establish a calcium-dependent receptor interface. [PMID:19561609, "a critical loop
from HHIP binds the pseudo active site groove of SHH and directly coordinates its Zn2+ cation"]
[PMID:30139912, "its Ca2+-mediated interface directly binds the ECDs of PTCH1-B"]

## Localization and signaling range

The precursor and intermediates pass through ER and Golgi compartments. Dually lipidated SHH-N
is initially retained at the producing-cell membrane; DISP/SCUBE-dependent release enables local
and longer-range signaling. Thus extracellular region is a core active location, whereas ER,
Golgi, plasma membrane, membrane raft, and transient cytosolic C-terminal-fragment locations are
valid but non-core lifecycle contexts. [PMID:24342078, "The processed N-terminal fragment would
be retained in the cell by its cholesterol tail, except it is actively secreted by the synergistic
actions of Disp and the secreted protein Scube2"; "Secreted N-Hh forms a signaling gradient from
the producing cells to responsive cells localized near or distant"]

PMID:24342078 also cautions against treating SHH exclusively as a freely diffusible morphogen:
endogenous SHH in the tested LNCaP context supported cell-contact-mediated signaling. This makes
paracrine versus juxtacrine deployment a biological variable, not a distinct intrinsic activity.
[PMID:24342078, "the LnCAP prostate cancer cell, when induced to express endogenous DHH and SHH,
is active only in juxtacrine signaling"]

## Developmental contexts and the cerebellar decomposition

Human SHH loss-of-function provides direct evidence for a crucial forebrain/midline role.
Heterozygous mutations segregate with holoprosencephaly, including incomplete forebrain and
midline development. [PMID:8896572, "we report the identification of human Sonic Hedgehog (SHH)
as HPE3-the first known gene to cause HPE"; "five families that segregate different heterozygous
SHH mutations"]

For cerebellar development, mouse evidence establishes a directional source-to-target module:
developing Purkinje cells express Shh, granule-cell precursors in the external granule layer
express pathway-response genes, Shh neutralization reduces precursor proliferation, and
recombinant Shh stimulates it. This supports retaining GO:0021930 as a non-core developmental
context for human SHH by orthology; it must not replace SHH's general PTCH-binding molecular
function in `core_functions`. [PMID:10226030, "PCs in the developing mouse cerebellum express the
gene encoding the morphogen Sonic hedgehog (Shh)"; "treatment of dissociated granule neuron
cultures with recombinant Shh stimulated BrdU incorporation"; "PC-derived Shh normally promotes
the proliferation of granule neuron precursors in the EGL"]

Other retained non-core contexts include neural-tube and forebrain patterning, limb/digit and
somite development, neural precursor proliferation/differentiation, epithelial-mesenchymal organ
development, and thymocyte development. These annotations generally derive from mouse ortholog
transfer or tissue-specific primary studies and describe deployment of the same SHH morphogen
activity rather than additional core molecular activities.

The thymus annotations are supported by mouse loss-of-function/pathway activation, but they are
context-specific. [PMID:14764698, "Analysis of Shh(-/-) mouse embryos revealed that Shh regulates
fetal thymus cellularity and thymocyte differentiation"] [PMID:17227833, "in the Shh(-/-) thymus
the ratio of CD4/CD8 cells and both positive and negative selection of a transgenic TCR were
increased"]

The human urinary-tract paper is descriptive expression evidence rather than a causal perturbation
study, so its IEP annotations were kept non-core and not elevated to core functions.
[PMID:17850284, "We used immunohistochemistry to demonstrate that SHH protein was localised in
distinct urinary tract epithelia in developing normal humans"]

## Annotation decisions and unresolved evidence

- `GO:0004175 endopeptidase activity` was modified to `GO:0140853
  cholesterol-protein transferase activity`. SHH cholesterolysis is more specific than generic
  peptide-bond hydrolysis.
- `GO:0016539 intein-mediated protein splicing` was removed. It is an InterPro/HINT homology
  artifact: SHH catalyzes precursor cholesterolysis but does not excise and ligate an intein from
  a host protein.
- Generic `GO:0005515 protein binding` records from the human PTCH1 structural papers were
  modified to `GO:0005113 patched binding`. The HHIP record was removed as an uninformative
  generic binding annotation while retaining the verified SHH-HHIP interaction in these notes.
- Very broad terms (`tissue development`, `tube development`, `cell development`, `animal organ
  development`, and `regulation of developmental process`) were marked over-annotated because
  specific developmental terms convey the biology better.
- Narrow claims without an exposed underlying source experiment were left `UNDECIDED`, including
  androgen metabolism, laminin-1 binding, regulation of proteolysis, opposing kidney/ureter
  smooth-muscle differentiation terms, and dopaminergic differentiation polarity.
- `GO:0031012 extracellular matrix` was left `UNDECIDED`: PMID:28344315 is a human bone-marrow
  ECM proteomics study, but the cached abstract does not enumerate SHH and full text is
  unavailable. This is not evidence for removal.
- The PMID:17507406 left-right/Nodal records were left `UNDECIDED` where citation-specific: the
  cached abstract explicitly describes chick Cerberus feedback on Nodal but does not expose the
  basis for the SHH claim, and full text is unavailable.
- PMID:24431302 is a Wnt-focused dopaminergic-neuron review whose cached abstract does not expose
  the SHH-specific evidence. Its dopaminergic annotations remain `UNDECIDED`; the independently
  supported morphogen activity is retained.

## Core-function synthesis

1. Mature SHH-N enables `GO:0005113 patched binding` in the extracellular region and directly
   participates in `GO:0045880 positive regulation of smoothened signaling pathway`.
2. The SHH precursor enables `GO:0140853 cholesterol-protein transferase activity` in the
   endoplasmic reticulum and directly participates in `GO:0016540 protein autoprocessing`.

These two activity units deliberately separate ligand signaling from precursor maturation and
keep cerebellar granule-cell-precursor proliferation as a downstream developmental deployment.
