# Manual research synthesis for human SLC3A1

## Scope and evidence base

This synthesis was prepared manually after the configured Falcon and
Perplexity-lite research providers failed. It integrates the reviewed UniProt
record for Q07837, all 34 current GOA rows (33 grouped seed annotations), the
cached primary literature, the Reactome records cited by GOA, and GO term
definitions checked through QuickGO on 2026-07-18.

## Molecular identity and topology

SLC3A1 encodes rBAT (related to b0,+ amino-acid transporter), a 685-residue,
single-pass type II membrane glycoprotein. Its short N-terminal region is
cytoplasmic and its large C-terminal ectodomain is extracellular and
glycosylated. The ectodomain resembles glycoside hydrolases structurally, but
the purified human b0,+AT-rBAT complex has no detected alpha-glucosidase
activity [PMID:32494597 "The results showed that the complex has no α-glucosidase activity"].
There is therefore no experimental basis for assigning carbohydrate metabolic
process from the fold alone.

## Heavy-chain role versus catalytic transport

rBAT forms a disulfide-linked heterodimer with SLC7A9/b0,+AT. The native
heterodimer occurs in human kidney brush-border membranes
[PMID:12167606 "rBAT and b(0,+)AT were solely expressed as heterodimers of identical size"].
Older expression-cloning and disease studies described amino-acid transport
"induced by rBAT" because expressing rBAT recruits an endogenous or coexpressed
light chain. The M467T disease variant nearly abolishes this induced activity
[PMID:8054986 "M467T nearly abolished the amino acid transport activity induced by rBAT in Xenopus oocytes"],
which establishes biological necessity but not a pore-forming catalytic role.

Later work establishes the mechanistic boundary. SLC7A9 is the permease-like
catalytic subunit [PMID:10588648 "b(0,+)AT as the catalytic subunit that associates by a disulfide bond with rBAT"].
The structural literature states that the light chain is the transport subunit,
whereas the heavy chain promotes plasma-membrane trafficking and complex
maturation [PMID:32817565 "The light chain constitutes the transport subunit whereas the heavy chain mediates trafficking to the plasma membrane"].
SLC3A1 is therefore a transporter-activating heavy chain and an essential complex component, not the amino-acid permeation pathway itself.

This distinction supports four linked curation choices:

1. Biological-process annotations for amino-acid, cystine, and dibasic-amino-acid transport remain valid because SLC3A1 is required for the complex.
2. Direct `enables` annotations to amino-acid transporter activities are modified to `GO:0141109 transporter activator activity`.
3. The core-function model records `GO:0015171 amino acid transmembrane transporter activity` under `contributes_to_molecular_function`.
4. Generic protein-binding annotations are replaced by the experimentally resolved `GO:0046982 protein heterodimerization activity`.

## Oligomerization and transport complex

The rBAT-SLC7A9 heterodimer is the minimal functional transport unit. rBAT also
supplies the interface that joins two heterodimers into a heterotetramer. Native
and engineered complex analysis found that the heavy chain dictates
oligomerization [PMID:16825196 "The heavy subunit rBAT dictates oligomerization of the heteromeric amino acid transporters"],
while structural work independently reports that "rBAT mediates the dimerization
of HATs" [PMID:32494597]. The specific complex classification is
`GO:1990184 amino acid transport complex`, which is more informative than the
seeded generic transmembrane-transporter-complex term.

## Physiological process and tissue context

At the apical brush border, the SLC7A9-SLC3A1 complex exchanges extracellular
cystine and cationic amino acids for intracellular neutral amino acids. Human
kidney biochemistry links its proximal-tubule expression gradient to virtually
all apical cystine reabsorption [PMID:12167606 "responsible for virtually all apical cystine reabsorption"].
This directly supports the new, more physiological annotation `GO:1990297 renal
amino acid absorption`, while existing cystine and basic-amino-acid transport
process terms remain valid.

UniProt also describes an SLC3A1-SLC7A13 complex in later proximal-tubule
segments, but its human assignment is based primarily on orthology. Evidence for a human SLC3A1-SLC7A13 complex is much less direct than the SLC7A9 evidence.
Partner-specific human localization and substrate flux therefore remain open
questions rather than additional assertions in the core model.

## Secondary localizations and isoforms

Seven SLC3A1 isoforms are listed, but the reviewed record does not establish
distinct protein functions for the noncanonical isoforms. Isoform presence in
the source record is preserved without claiming isoform-specific activity.

The urinary-exosome HDA is left undecided because renal apical membrane proteins
can enter urinary vesicles, but the cached abstract does not expose the
gene-specific identification. The vacuolar-membrane IEA traces to rat forebrain
immunogold localization [PMID:9987991 "immunogold labeling for NBAT was distributed along plasmalemmal and vacuolar membranes"].
That source-side experiment is not contradicted, but it is outside the
well-established human epithelial core.

## Curation conclusion

The strongest coherent model is a noncatalytic but indispensable transporter
heavy chain. SLC3A1 heterodimerizes with a catalytic SLC7 light chain, activates
its functional surface expression, organizes the amino-acid transport complex,
and thereby participates in renal cystine and dibasic-amino-acid absorption.
Carbohydrate metabolism is an erroneous domain-transfer inference; direct
transporter molecular-function annotations are too strong for SLC3A1 itself;
the associated transport biological processes are valid at the complex-subunit
level.
