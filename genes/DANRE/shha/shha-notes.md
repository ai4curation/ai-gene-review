# shha (Q92008) review notes

## 2026-09-28 — provenance and scope

- Review run from outside the repository via the `gene-review` front-door skill.
  `just fetch-gene DANRE shha` seeded 117 GOA annotations; `just fetch-gene-pmids`
  cached all 54 cited PMIDs (15 with PMC full text, 39 abstract-only).
- **Deep research was not run.** No provider API key (Edison/Asta/Perplexity) is
  available in this environment, so no `shha-deep-research-<provider>.md` exists.
  This file is the manual literature synthesis that replaces it, built from the
  cached publications, the UniProt record and the human SHH review in
  `genes/human/SHH/` (added to the sparse checkout as the ortholog reference).
- Three extra references were cached with `ai-gene-review fetch-pmid` to support the
  precursor-processing core function and the classical morphogen framing:
  PMID:8824192 (Porter, Young & Beachy 1996), PMID:7583153 (Ekker et al. 1995) and
  PMID:8269518 (Riddle et al. 1993). PMID:8269518 turned out to be the chick ZPA
  paper rather than the zebrafish cloning paper; it is kept as background only.

## Gene identity

shha (formerly shh, vhh1) is the zebrafish co-ortholog of mammalian SHH and the gene
disrupted in the ENU mutant *sonic you* (syu). [PMID:9655820, "We show that the
zebrafish sonic-you (syu) gene, a member of a group of five genes required for somite
patterning, is encoding Shh."] The second co-ortholog is shhb (tiggy-winkle
hedgehog, twhh); the two are redundant in several tissues, which colours many of the
loss-of-function phenotypes below. [PMID:12588855, "both Sonic hedgehog and
Tiggy-winkle hedgehog are involved in anteroposterior patterning of the zebrafish
otic vesicle"] [PMID:16452095, "shh and twhh display both unique and redundant
functions during diencephalic patterning"]

## Precursor processing and molecular activities

UniProt (by similarity to mouse/human) records a signal peptide (1-23), an
N-terminal signalling chain (24-197), a C-terminal Hint domain, cholesterol at
Gly197 and palmitate at Cys24, and Ca2+/Zn2+ sites within the N-domain. The
defining chemistry is the Hint-domain cholesterolysis: [PMID:8824192, "cholesterol
is the lipophilic moiety covalently attached to the amino-terminal signaling domain
during autoprocessing and that the carboxyl-terminal domain acts as an
intramolecular cholesterol transferase"]. Zebrafish Shh and Twhh do this in vivo,
and the N-fragment carries all signalling activity: [PMID:7583153, "Both twhh and
shh proteins undergo autoproteolytic processing in vivo; a fragment corresponding to
the amino-terminal cleavage product was sufficient to carry out all signaling
activities associated with twhh in eye and brain development."]

Decisions that follow:

- `GO:0140853 cholesterol-protein transferase activity` (ISS) — ACCEPT, core.
- `GO:0016540 protein autoprocessing` (IEA, ISS) — ACCEPT, core.
- `GO:0004175 endopeptidase activity` (ISS) — MODIFY to GO:0140853. The cleavage is
  resolved by cholesterol, not water (RHEA:59504), mirroring the human review.
- `GO:0016539 intein-mediated protein splicing` (IEA, InterPro Intein_N) — REMOVE.
  Hint domains share the first half-reaction with inteins but never re-ligate
  exteins; no splicing occurs.
- `GO:0005113 patched binding` (IBA) — ACCEPT, core ligand activity.
- `GO:0005509 calcium ion binding` (IBA) — KEEP_AS_NON_CORE (structural).
- Locations: extracellular region (IBA) and endoplasmic reticulum (ISS) are core
  (site of action; site of autoprocessing). ER membrane, Golgi membrane, Golgi
  apparatus and plasma membrane are kept as non-core lifecycle locations.
- `GO:0016015 morphogen activity` was considered as a NEW term and **not proposed**.
  QuickGO shows it on human SHH only by ARBA/TAS/NAS and on mouse by ISO; the
  zebrafish literature in hand emphasises short-range action [PMID:15253932, "Shh
  directs these events as a short-range signal within the neural retina"] with
  graded action stated at the pathway level [PMID:15539490, "Graded Hedgehog (Hh)
  signaling patterns the spinal cord dorsoventral axis"]. Raised as a question.

## Pathway-level process terms (core)

`GO:0007224 smoothened signaling pathway` (IBA; IGI with scube2 and scube1/2/3) and
`GO:0045880 positive regulation of smoothened signaling pathway` (ISS) are the
processes the ligand directly performs. [PMID:16626681, "Epistatic and molecular
analyses position Scube2 function upstream of Smoothened (Smoh), the signalling
component of the HH receptor complex"] [PMID:22609552, "Knocking down the function
of all three scube genes simultaneously phenocopies a complete loss of HH signal
transduction in the embryo"]. Direct reception by target cells is shown by
ptc1/nk2.2 induction: [PMID:12606279, "the Hh responsive genes ptc1 and nk2.2 are
expressed in preplacodal cells at the anterior margin of the neural tube at this
time, indicating that these cells are directly receiving Hh signals"].
`GO:0010468 regulation of gene expression` (IBA, IDA) is accepted as the downstream
consequence PAINT chose to record at the family node; `GO:0007267 cell-cell
signaling` (InterPro IEA) is accepted as a correct generalisation.

## Developmental deployments (KEEP_AS_NON_CORE)

Ninety-odd ZFIN experimental annotations record tissues in which the single ligand
activity is used. All are retained as non-core; notable nuances:

- **Floor plate / motor neurons.** Unlike mouse, shha is dispensable for the medial
  floor plate and required for the lateral floor plate. [PMID:9655820, "syu mutant
  embryos do form medial floor plate cells and motorneurons"] [PMID:10694427, "shh,
  expressed in the notochord and/or the MFP cells, induces the formation of LFP
  cells"]. Motor neuron loss needs the Nodal pathway removed too: [PMID:10694427,
  "The number of primary motor neurons is strongly reduced in cyc;syu double
  mutants, while almost normal in single mutants"]. The `GO:0021520` citation
  (PMID:9242415) predates the cloning of syu and is correlative; PMID:10694427 is
  added as support.
- **Ventral spinal cord precursors, glia, oligodendrocytes.** [PMID:15539490, "Hh
  acting over time to set, maintain, subdivide and enlarge the olig2+ precursor
  domain and subsequently specify oligodendrocyte development"]. PMID:23345245
  shows Shh stimulates precursor proliferation and maintains olig2 but cannot
  replace Ihhb in OPC specification; the shha evidence there is overexpression.
- **Somites.** syu mutants form somites but mis-pattern them (U-shaped, no
  horizontal myoseptum, slow muscle reduced). `GO:0001756 somitogenesis` (3 rows)
  is therefore MODIFIED to `GO:0061053 somite development`, a term mouse Shh already
  carries by IMP. Slow-muscle terms are kept: [PMID:11428131, "in syu mutant embryos,
  a small number of slow muscle cells could still form"].
- **Pectoral and caudal fins.** ZPA-like role, partially Shh-independent early A/P
  polarity. [PMID:10518498, "Shh is required for normal development of the apical
  ectodermal fold, for growth of the fin bud, and for formation of the fin
  endoskeleton"] [PMID:17597528, "Shh signaling is required for normal patterning
  of the ACFP"].
- **Forebrain / diencephalon / habenula / pituitary.** ZLI-derived shha patterns
  thalamus and prethalamus and drives habenular neurogenesis [PMID:27387288, "Shha
  is the main Hedgehog ligand involved in habenular neurogenesis"]; ventral
  diencephalic Shh induces the adenohypophysis [PMID:12606280].
- **Retina.** Short-range Shh from ganglion/amacrine cells drives cell-cycle exit
  via p57Kip2 and differentiation/lamination [PMID:15891769, "Shh activity is
  required for cell-cycle exit of progenitor cells in the zebrafish retina"];
  adult syu heterozygotes show age-related cone loss [PMID:18502998].
- **Heart.** shha mRNA increases cardiomyocyte number [PMID:18842815]; epicardial
  conditional knockout gives a thin myocardium and fewer cardiomyocytes and reduces
  subepicardial proliferation after injury [PMID:28513431]. Left/right and heart
  looping annotations (PMID:9334285) rest on ubiquitous shh overexpression only.
- **Endoderm derivatives.** Endocrine pancreas [PMID:11900460], oesophagus
  [PMID:12618131], cloaca [PMID:19123126], swimbladder [PMID:19422819], teeth
  [PMID:21118524, "morphological and gene expression evidence of tooth initiation
  is eliminated in shha mutant embryos"], craniofacial cartilage [PMID:16049113,
  PMID:22185793].
- **Vasculature.** Shh acts upstream of vegf and Notch in arterial specification
  [PMID:12110173]; hence `GO:0030947` is kept and `GO:0008015 blood circulation`
  (PMID:9007249, screen abstract not mentioning syu) is flagged over-annotated.

## Flagged as over-annotation

- `GO:0007411 axon guidance` (PMID:19846707): the paper attributes the Rohon-Beard
  axon phenotype of syu to absent muscle contraction, and reproduces it by
  restraining wild-type embryos in agarose. shha is upstream via muscle
  specification, not a guidance cue here.
- `GO:0030917 midbrain-hindbrain boundary development` (PMID:28493069): morpholino
  only, MHB markers unchanged in shha morphants.
- `GO:0008015 blood circulation` (see above).
- ARBA IEAs `tissue development`, `tube development`, `animal organ development`,
  `regulation of developmental process`: true but uninformative.

## Core-function synthesis

1. ShhN enables `GO:0005113 patched binding` in `GO:0005576 extracellular region`
   and is directly involved in `GO:0007224 smoothened signaling pathway` /
   `GO:0045880 positive regulation of smoothened signaling pathway`.
2. The precursor enables `GO:0140853 cholesterol-protein transferase activity` in
   `GO:0005783 endoplasmic reticulum`, directly involved in `GO:0016540 protein
   autoprocessing`.

Action tally over 117 rows: 13 ACCEPT, 92 KEEP_AS_NON_CORE, 7 MARK_AS_OVER_ANNOTATED,
4 MODIFY, 1 REMOVE, 0 NEW.
