---
title: "Biosynthetic Gene Cluster (BGC) Enzyme Complexes Project"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [PSEAE, STRCO, SACEN]
genes: [pqsB, pqsC, actI-ORF1, actI-ORF2, eryCII, eryCIII]
sidecars:
  slide_assets:
    - BGC/slides/complex-pairs.svg
    - BGC/slides/eryCII-review-table.jpg
manifest:
  slides:
    - href: BGC/slides/BGC-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/JVCyoqSc6xLv4upJ5x28fH
      title: Project brief
---

# Biosynthetic Gene Cluster (BGC) Enzyme Complexes Project

**Bottom line:** many enzymes in microbial natural-product gene clusters work
only as heteromeric complexes, and GO annotation often gives the complex's
catalytic activity to the wrong subunit. Using a recent AlphaFold3 screen of
2,437 MIBiG clusters (Moriwaki *et al.*) as structural evidence, we chose five
exemplar complexes whose predicted pairing matches a solved PDB structure, and
have reviewed three of them: PqsB/PqsC (quinolone quorum-sensing signal),
actinorhodin KSα/KSβ-CLF (type II PKS) and erythromycin EryCIII/EryCII
(desosaminyl transferase and its activator). The six reviews cover 29
annotation rows: 15 accepted, 7 removed, 3 modified, 3 marked over-annotated
and 1 proposed as `NEW`. Two reusable patterns emerged: non-catalytic partners
(PqsB, the chain-length factor) inherit the catalytic acyltransferase term
from their fold, and a pseudoenzyme (EryCII, a heme-less P450 homologue)
inherits a full P450 cofactor set, all four rows of which were removed.
Catalytic KAS-fold partners also inherit fatty-acid synthesis terms that do
not fit a polyketide or quinolone pathway. The nosiheptide and pyoluteorin pairs are
still queued. The queued "ActVA" and "DEBS" rows in the status table below predate
this work: those two candidates share their MIBiG
and PDB entries (1TQY, 2YJN) with the reviewed KS-CLF and EryCII/EryCIII
pairs.

**Project type:** Gene curation (exemplar enzymes from microbial natural-product gene clusters)
**Status:** In progress — three of five exemplar pairs reviewed; nosiheptide and pyoluteorin pairs queued, plus candidate targets drawn from the 2025–2026 BGC review literature

## Overview

Biosynthetic gene clusters (BGCs) are contiguous genomic regions encoding the
enzymes that assemble microbial secondary metabolites — antibiotics, siderophores,
quorum-sensing signals, pigments, and mycotoxins. They are attractive targets for
AI-assisted GO curation because:

1. **Function follows pathway context.** A protein's molecular function and the
   biological process it contributes to are strongly constrained by the cluster it
   sits in and the compound that cluster makes. This gives an unusually strong
   prior for evaluating (and challenging) existing annotations.
2. **Many cluster members are under- or mis-annotated.** Tailoring enzymes,
   carrier proteins, and "uncharacterized" cluster proteins frequently carry only
   generic IEA terms despite well-resolved biochemistry.
3. **Complexes matter.** Intermediate channeling, enzymatic regulation, and
   structural stability in BGCs are often mediated by **heteromeric enzyme
   complexes that are only functional when assembled** — a fact that is poorly
   reflected in current Cellular Component / "protein-containing complex"
   annotations.

### Motivating resource

Moriwaki *et al.*, *"High-throughput prediction of protein–protein interactions
uncovers hidden molecular networks in biosynthetic gene clusters"* (bioRxiv
[10.1101/2025.10.26.684697](https://doi.org/10.1101/2025.10.26.684697), v2 2026;
data at Zenodo [10.5281/zenodo.17451667](https://doi.org/10.5281/zenodo.17451667)).

The authors replaced AlphaFold3's MSA step with MMseqs2 to run a genome-scale,
all-vs-all complex screen over **2,437 active MIBiG v4.0 BGCs** (487,828 protein
pairs), predicting **15,438 heteromeric interactions** at ipTM ≥ 0.6, of which
**1,390** also showed structural homology (RMSD ≤ 2.0 Å) to known structures.
A curated subset of **381 high-confidence structurally-homologous pairs across 239
BGCs** is released, alongside a **validation set of ~30 experimentally-solved
heterocomplexes** (each tied to a PDB entry) used as positive controls.

This resource is used here as **one line of structural evidence** (predicted
complex membership / interaction) when reviewing BGC enzyme annotations — analogous
to how `projects/ALPHAFOLD.md` and `projects/PROTEIN_COMPLEX_FUNCTIONS.md` use
predicted quaternary structure. **Predictions are hypotheses, not facts** (see
Caveats).

## Exemplar selection criteria

Exemplars are drawn primarily from the paper's **PDB-backed validation set** (so the
predicted complex corresponds to a *real, solved* structure), favouring:

- well-studied natural products with a clear, citable biosynthetic literature;
- organisms with reasonable GO coverage;
- a spread of cluster classes (type II PKS, modular PKS, condensation enzymes, RiPP);
- complexes whose "only-functional-when-assembled" nature is a genuine annotation
  opportunity.

All BGC accessions, GenBank protein IDs, PDB IDs, and ipTM/ipSAE values below are
taken directly from the authors' deposited data (verified, not inferred). UniProt
accessions and final gene symbols are resolved at the `fetch-gene` step.

## Candidate exemplar complexes

| BGC (MIBiG) | Organism (species code) | Product | Class | Protein pair (GenBank) | PDB | ipTM | Notes / annotation angle |
|---|---|---|---|---|---|---|---|
| BGC0000922 | *Pseudomonas aeruginosa* PAO1 (PSEAE) | 2-alkyl-4-quinolones (PQS precursors) | PKS | aag04386.1 / aag04387.1 | 5DWZ | 0.95 | **PqsB / PqsC** condensing heterodimer of the *pqs* quorum-sensing pathway; clinically important; classic obligate heterocomplex. |
| BGC0000194 | *Streptomyces coelicolor* A3(2) (STRCO) | actinorhodin | type II PKS | cac44200.1 / cac44201.1 | 1TQY | 0.96 | Model type II PKS tailoring step (ActVA region monooxygenase/cyclase); textbook system. |
| BGC0000055 | *Saccharopolyspora erythraea* NRRL 2338 (SACEN) | erythromycin A–D | modular PKS | cam00066.1 / cam00067.1 | 2YJN | 0.92 | DEBS-associated pair (Hetero 4-mer); modular PKS docking/tailoring; flagship polyketide. |
| BGC0000610 | *Streptomyces actuosus* (STRAT) | nosiheptide | RiPP (thiopeptide) | acr48346.1 / acr48347.1 | 8K60 | 0.88 | RiPP maturation enzymes; tests CC/MF annotation of post-translational tailoring complex. |
| BGC0000127 | *Pseudomonas protegens* Pf-5 (PSEF5) | pyoluteorin | PKS | aad24885.1 / aad24881.1 | 6O6E | 0.76 | Lower-confidence positive control — useful "edge case" for calibrating how much weight to give an ipTM≈0.76 prediction. |

**Stretch / discovery targets** (high-confidence *novel* predictions, not in the
validation set — candidates for `-predictions-review.yaml` rather than direct
acceptance): BGC0001288 (maklamicin, *Micromonospora* sp. GMKU326, ipTM 0.95),
BGC0001665 (alkyl-resorcinol, *Mycobacterium marinum* M, ipTM 0.95).

## Curation workflow (per exemplar)

For each protein in a selected complex:

1. `just fetch-gene <SPECIES_CODE> <GENE>` — resolve the GenBank accession to its
   UniProt entry and HGNC-style/standard gene symbol, and create the review stub,
   uniprot, and goa files. **Record the GenBank→UniProt mapping in
   `<GENE>-notes.md`** (do not guess identifiers).
2. Deep-research the gene/pathway; capture provenance inline
   (`[PMID:xxxxx "supporting text"]`) in `<GENE>-notes.md`.
3. Review existing GOA annotations per the standard guidelines (ACCEPT /
   KEEP_AS_NON_CORE / MODIFY / MARK_AS_OVER_ANNOTATED / REMOVE / UNDECIDED). Do
   **not** REMOVE experimental annotations on the basis of cached abstracts alone.
4. Use the predicted complex as **supporting structural evidence**, especially for:
   - Cellular Component / `protein-containing complex` membership;
   - Molecular Function where the activity is only realized in the assembled
     heterocomplex (note this explicitly in `core_functions`).
   Cite as `file:<SPECIES>/<GENE>/...` or reference the bioRxiv DOI + PDB ID.
5. For *novel* (non-validation) predictions, record adjudication in
   `<GENE>-predictions-review.yaml` (COR / CNN / LSP / UNC / PLI / NPI / REP).
6. `just validate <SPECIES_CODE> <GENE>`.

## Status

| Gene / protein | Complex | Stage |
|---|---|---|
| PqsB (PSEAE, Q9I4X2) | PqsBC condensing heterodimer (non-catalytic subunit) | **Review complete** |
| PqsC (PSEAE, Q9I4X1) | PqsBC condensing heterodimer (catalytic subunit) | **Review complete** |
| actI-ORF1 / KSα (STRCO, Q02059) | actinorhodin KS-CLF (catalytic ketosynthase) | **Review complete** |
| actI-ORF2 / KSβ-CLF (STRCO, Q02062) | actinorhodin KS-CLF (non-catalytic chain-length factor) | **Review complete** |
| eryCII (SACEN, A4F7P2) | EryCII-EryCIII (P450-homologue GT activator; pseudoenzyme) | **Review complete** |
| eryCIII (SACEN, A4F7P3) | EryCII-EryCIII (desosaminyl glycosyltransferase) | **Review complete** |
| ActVA region pair (STRCO) | actinorhodin tailoring | Queued |
| Erythromycin DEBS pair (SACEN) | modular PKS | Queued |
| Nosiheptide pair (STRAT) | thiopeptide RiPP | Queued |
| Pyoluteorin pair (PSEF5) | edge-case control | Queued |

### Candidate targets from the recent BGC reviews

Not started; see "What the recent BGC reviews imply for this project" below for
the reasoning. Accessions are from UniProt REST queries made 2026-10-06 and must
be re-confirmed at the `fetch-gene` step.

- [ ] **Terrein TerA / TerB (ASPTN; Q0D1N9 / Q0D1P0)** — a *fungal* pair of
  two **catalytic** enzymes that act sequentially and are proposed to interact
  (substrate channeling): TerA is the non-reducing PKS, and TerB is a KS-less
  PKS-like protein (DH, MeT and KR regions per UniProt) that reduces TerA's
  2,3-dehydro-6-hydroxymellein to 6-hydroxymellein (PMID:41614020). This is
  *not* the non-catalytic-partner pattern of PqsB / KSβ-CLF / EryCII; it tests
  whether fatty-acid mis-propagation on a fungal PKS and a PKS-like reductase
  follows the same signature seen on bacterial condensing enzymes. GOA currently gives both IEA
  `fatty acid synthase activity` (GO:0004312) and `fatty acid biosynthetic
  process` (GO:0006633), and TerA additionally IEA `3-oxoacyl-[acyl-carrier-protein]
  synthase activity` (GO:0004315) — the same fatty-acid mis-propagation seen on
  KSα and PqsC. On TerB, a `fatty acid synthase activity` IEA would reflect a
  KR/DH-domain mapping on a real reductase, not fold inheritance by a
  non-catalytic subunit, so the right replacement is a reductase-class term
  rather than `contributes_to`. Check first whether this pair appears in MIBiG / the Moriwaki
  screen, which covers bacterial clusters only.
- [ ] **TerR (ASPTN; Q0D1P5)** — cluster-situated Zn2Cys6 activator, IEA-only.
  Reference case for how far a cluster-specific regulator's BP scope should
  extend.
- [ ] **γ-butyrolactone system, *S. coelicolor*: ScbA (Q7AKF0 / SCO6266),
  ScbR (Q7AKF1 / SCO6265),
  pseudo-receptor ScbR2** (accession unresolved — `SCO6286`/Q93S03 is a
  candidate but was not confirmed; resolve at `fetch-gene`). ScbA has only IEA
  `transferase activity` despite a reviewed EC 2.3.1.277 assignment; ScbR has no
  ligand-binding MF. Both the receptor MF and the AfsA reaction look like
  `proposed_new_terms`.
- [ ] **A-factor system, *S. griseus*: AfsA (B1VN93), ArpA (Q9ZN78)** — ArpA
  carries NAS `involved_in streptomycin biosynthetic process` (GO:0019872,
  PMID:2111804) and NAS `negative regulation of sporulation...` (GO:0042174).
  A signal receptor/repressor annotated to the biosynthetic process it controls
  is exactly the regulator-to-process conflation to adjudicate; read PMID:2111804
  first — as an author statement the likely action is MODIFY to a regulation
  term, not REMOVE. An OLS search (2026-10-10) found no streptomycin- or
  antibiotic-specific regulation term; the candidate replacement is
  `negative regulation of secondary metabolite biosynthetic process`
  (GO:1900377), child of GO:1900376.
- [ ] **MbtH-like proteins (STRCO; Q9Z388 / SCO3218, Q9RK17 / SCO0489)** —
  non-catalytic activators of NRPS adenylation domains, i.e. the project's
  "only functional when assembled" premise in NRPS form. Both are
  TrEMBL-only with IBA annotations. Check whether the Moriwaki data predict
  MLP–A-domain pairs before promoting these to exemplars.

### First worked example: PqsBC (BGC0000922)

The PqsB/PqsC pair validates the project premise. Reviewing both subunits
(PqsB, PqsC) surfaced exactly the annotation issues the
"only-functional-when-assembled" framing predicts:

- **Over-annotation of the catalytic MF to a non-catalytic subunit.** PqsB carries
  the condensing-enzyme fold but lacks the active-site Cys-129/His-269 (which are in
  PqsC; PDB 5DWZ, PMID:26811339), yet it was IEA-annotated `enables acyltransferase
  activity` → flagged MARK_AS_OVER_ANNOTATED (better: `contributes_to` / annotate to
  the PqsBC complex).
- **Fold-based process mis-propagation.** PqsC inherited `fatty acid biosynthetic
  process` and `3-oxoacyl-ACP synthase activity` from the FabH/KAS III signature,
  but PqsBC makes a quinolone QS signal (octanoate is a substrate, not the product;
  PMID:24239007) → REMOVE / MODIFY respectively.
- **Missing specific MF.** EC 2.3.1.230 ("2-heptyl-4(1H)-quinolone synthase") has no
  GO term → `proposed_new_terms`.

The predicted complex (ipTM 0.95, matching PDB 5DWZ) agreed with the experimentally
established obligate heterodimer — a positive-control case where the structural
prediction corroborated, rather than drove, the curation.

### Second worked example: actinorhodin KS-CLF (BGC0000194)

The *S. coelicolor* actinorhodin minimal-PKS KSα/KSβ pair (actI-ORF1,
actI-ORF2; predicted at ipTM 0.96, matching PDB 1TQY) is the **same
catalytic + non-catalytic heterodimer pattern** as PqsBC, and reproduces the same
annotation failure mode from a different protein family:

- **Catalytic KSα (actI-ORF1)** inherited fatty-acid-synthase terms from the KAS
  domain signature — `3-oxoacyl-ACP synthase activity`, `fatty acid biosynthetic
  process`, `fatty acid elongation`. These were MODIFY'd / REMOVE'd to the accurate
  **polyketide** terms (GO:0016218 polyketide synthase activity, GO:1901112
  actinorhodin biosynthetic process) — here GO already has the right terms, so no new
  term was needed (unlike PqsBC's EC 2.3.1.230).
- **Non-catalytic KSβ/CLF (actI-ORF2)** "does not have an active site" (PMID:15286722)
  yet was IEA-annotated `enables acyltransferase activity` → MARK_AS_OVER_ANNOTATED,
  with GO:0034082 (type II PKS complex) and GO:1901112 added as the accurate roles,
  plus a proposed "polyketide chain length factor activity" MF term.

**Emerging pattern for the project:** type II PKS / FabH-like condensing systems are
systematically over-annotated with fatty-acid MF/BP terms and mis-assign the complex's
catalytic activity to the non-catalytic subunit. This is a reusable curation signature
for the remaining BGC exemplars.

### Third worked example: erythromycin EryCII-EryCIII (BGC0000055)

The *S. erythraea* desosaminylation pair (eryCII, eryCIII;
predicted ipTM 0.92, matching PDB 2YJN) generalises the pattern beyond
catalytic/non-catalytic *condensing* enzymes to a **catalytic enzyme + pseudoenzyme
activator** pair:

- **EryCIII (catalytic GT)** is the desosaminyl transferase (EC 2.4.1.278); cleanly
  annotated (IDA, PMID:15303858). Minor fixes: MODIFY `UDP-glycosyltransferase
  activity` → hexosyltransferase (donor is **TDP**-D-desosamine, not UDP), and add the
  specific erythromycin-biosynthesis BP; propose an EC 2.4.1.278 MF term.
- **EryCII is a P450 PSEUDOENZYME.** UniProt states it "lacks the heme-binding sites";
  it functions as an allosteric activator/stabiliser of EryCIII (PMID:22056329). All
  four of its IEA P450 terms (monooxygenase, heme binding, iron ion binding,
  oxidoreductase) were **REMOVE'd** as domain-propagation over-annotations, and
  replaced with the accurate **GO:0008047 enzyme activator activity** + complex + BP.
  Cross-links to `projects/PSEUDOENZYMES.md`.

The full erythromycin cluster (23 MIBiG genes) is captured as a representative-species
pathway concept in **`terms/erythromycin_biosynthesis/erythromycin_biosynthesis-notes.md`**
(S. erythraea; aligned to MIBiG BGC0000055, all genes mapped to UniProt). Only the
desosaminylation node (eryCIII + eryCII) is fully reviewed so far; the concept doc also records
two MIBiG/UniProt annotation discrepancies flagged for upstream correction (eryCII
"3,4-isomerase" → activator pseudoenzyme; eryCI "sensory transduction protein" → transaminase).

This adds a second over-annotation signature to the project: **sequence-similarity to a
catalytic family (here cytochrome P450) propagates a full catalytic/cofactor annotation
set onto a pseudoenzyme that has demonstrably lost the active site** — flagged whenever
UniProt carries a "lacks the ... binding sites" CAUTION.

## What the recent BGC reviews imply for this project

A 2026 *Essays in Biochemistry* special issue revisited the BGC concept
(editorial PMID:42619353), and is read here alongside a review of BGC
regulation (PMID:42469370, 2026) and one of the fungal terrein cluster
(PMID:41614020, 2025). All are secondary sources: the primary papers they cite must be
fetched before any point below is used as annotation evidence.

**1. Complexes constrain the backbone; tailoring enzymes vary it.** In modular
systems, "highly evolved protein-protein interactions [36,44–50] within modular
enzymes typically constrain PKSs and NRPSs to the production of only one or a
handful of core backbones", while "different products mostly result from
variable or incomplete tailoring reactions acting on the same backbone"
(PMID:42124485). The project's choice of core condensing/assembly complexes as
annotation units is thus the stable end of the spectrum. The corollary is a
caution: compound-specific MF or BP terms are riskiest on **tailoring enzymes**,
which is where our remaining queued pairs (ActVA region, nosiheptide maturation)
sit.

**2. Substrate specificity can drift between related copies, but unevenly.**
The diversification evidence in PMID:42124485 is mostly about the core
assembly-line enzymes, and it cuts both ways. For NRPS adenylation domains,
"point mutations can also alter the substrate specificity of NRPSs, often
resulting in promiscuous variants", and intra-BGC gene conversion
"‘copy-pastes’ sequences from one gene to another within the same BGC, often
changing the encoded enzymatic functions" (PMID:42124485). But the same
paragraph adds: "In contrast, phylogenetic analyses of AT domains from modular
PKSs suggest that point mutations do not normally change the building block
these domains select" (PMID:42124485) — so specificity is not uniformly labile
even within core enzymes, which reinforces point 1 for PKS AT domains. For
tailoring enzymes the cited claim is a different one, cross-cluster
promiscuity rather than allelic divergence: a *Streptomyces* essay proposes
that "tailoring enzymes such as the monooxygenase (example B) and the
glucosyltransferase (example A) are not limited to their own BGC but can
interact with the PKSs encoded elsewhere in the genome" (PMID:42388094) — a
hypothesis in that paper, not an established result. Practical consequence for
us: treat an IBA or ISS that transfers a *specific* substrate/product term
between allelic or HGT-acquired copies with caution wherever the evidence
shows specificity can drift (NRPS A domains; enzymes that may act on
substrates from other clusters), and do not assume the same caution applies
to PKS AT domains, whose building-block selection appears conserved. Prefer the
donor-independent activity term (e.g. the oxidoreductase or glycosyltransferase
class) unless the specific product was assayed for *that* protein. The same
logic applies to heterologous-expression literature, where "host enzymes acting
on pathway intermediates (e.g. promiscuous tailoring enzymes, host-encoded
cytochrome P450s, or glycosyltransferases) may generate modified metabolites
that are not detected in the native host" (PMID:41847751) — a novel congener
seen in a heterologous host does not license a product-specific term on the
cluster's own enzyme. HGT itself is "now well acknowledged but also properly
dimensioned in the context of vertical evolution" (PMID:42619353), which is the
right frame for reading an IBA node placement over a mobilisable cluster.

**3. Cluster-situated regulators: annotate the regulation, and do not assume the
ortholog regulates the same cluster.** Pathway-specific transcription factors
"act as dedicated switches to coordinate expression of all biosynthetic genes"
(PMID:42469370), but their target can be rewired between relatives: a XanC
homologue "no longer controls xanthocillin but instead activates the entirely
different citrinin BGC", so "the function of a PSTF is context-dependent and can
diverge even between related species" (PMID:42469370). For curation this means
(a) orthology alone does not transfer a *cluster-specific* regulation term, and
(b) a regulator belongs on a regulation-of-expression term plus, where the
evidence supports it, regulation of the biosynthetic process — not on the
biosynthetic process itself, which the enzymes perform (the CLAUDE.md
participation test: a product is `involved_in` a process only if it does some
of the work of that process). In the terrein cluster the
TerR-binding motifs are informative about scope rather than activity: they
"were not detected in the promoter regions of terG, terH, and terI, which are
dispensable for terrein production" (PMID:41614020).

**4. γ-butyrolactone receptors are a distinct, under-annotated MF class.** The
*Streptomyces* lactone-signalling systems comprise a signal synthase (AfsA
family, Pfam03756), a TetR-family receptor and often a "pseudo-receptor":
"some of them (termed as ‘pseudo-receptors’) act as negative regulators for
antibiotic production" (PMID:42494319). Two statements in that review are
directly about annotation transfer. First, ligand identity does not follow from
sequence: "their specific ligands are unable to predict in terms of their amino
acid sequence homology" (PMID:42494319) — so a specific signalling-molecule
binding MF should not be propagated by similarity between receptor homologues.
Second, genomic context is usually a good guide — the system "is generally
predictable due to their vicinal genetic location" (PMID:42494319) — but not
always: the A-factor system belongs to the stand-alone type, which "is rare
distribution in Streptomyces" (PMID:42494319), and there "it is difficult to
predict the functional receptor genes on the basis of genetic locus of signaling-molecule/receptor system" (PMID:42494319).
The mechanism is well defined where it has been tested: "Its cognate receptor,
ScbR, is a TetR-family repressor that binds directly to the promoter of kasO
(also known as cpkO), the PSTF for a cryptic polyketide BGC" (PMID:42469370).
A QuickGO/OLS check (2026-10-06) found **no GO molecular-function term for
γ-butyrolactone / A-factor binding**, and no term for EC 2.3.1.277 (the AfsA
reaction), while GOA gives ScbA (Q7AKF0) and AfsA (B1VN93) only IEA
`transferase activity`. Both are `proposed_new_terms` candidates.

**5. Non-catalytic activating partners extend beyond our current exemplars.**
MbtH-like proteins are the NRPS version of the project's pattern — "PacL showed
no adenylation activity unless combined with the MLP PacJ" (PMID:42210863) — as
are type II thioesterases, which "function as proofreading enzymes to remove
aberrant acyl groups from stalled carrier proteins" (PMID:42210863) and so act
on the assembly line without being part of the chain-extension chemistry.

**6. Interacting sequential enzymes are a separate case.** The fungal terrein
cluster offers a contrasting pair in which *both* partners are catalytic:
"TerA and TerB act collaboratively, and a close interaction between the two was
proposed" (PMID:41614020), yet "TerB reduces 2,3-dehydro-6-hydroxymellein to
6-hydroxymellein (Figure 1)" (PMID:41614020). Here each protein carries its own
activity term and the interaction is best read as substrate channeling, not
activation of a non-catalytic subunit. Separately, TerA's "low extension cycle specificity enables adding two
to four extender units, leading to different chain length products"
(PMID:41614020) — a documented case where one PKS yields several products, so a
single product-specific MF term would be wrong.

## Caveats when using the predictions as evidence

- **ipTM/ipSAE are confidence scores, not truth.** The authors' own validation set
  includes genuine, PDB-confirmed complexes that scored poorly (e.g. PDB 6M01 at
  ipTM 0.35, 7YN3 at 0.17) — i.e. **false negatives are real**, so absence of a
  high-ipTM prediction is *not* evidence against a complex.
- **Paralog look-alikes.** When a BGC encodes several functionally homologous
  proteins, structural-homology hits can mis-pair them. The paper's **ipSAE** metric
  is meant to discriminate the correct pair; prefer pairs with both high ipTM and
  ipSAE, and cross-check against the literature before asserting a specific pairing.
- **Prediction ≠ in vivo function.** A predicted interface does not establish that
  the complex forms or is catalytically relevant in the native organism; treat as a
  hypothesis to be corroborated by experimental literature.

## References

- Moriwaki Y, Shiraishi T, Katsuyama Y, Matsuda K, Ose T, Minami A, Oikawa H,
  Kuzuyama T, Ishitani R, Terada T. High-throughput prediction of protein–protein
  interactions uncovers hidden molecular networks in biosynthetic gene clusters.
  bioRxiv 2025.10.26.684697 (v2, 2026). doi:10.1101/2025.10.26.684697.
- Data deposit: Zenodo doi:10.5281/zenodo.17451667.
- MIBiG: Minimum Information about a Biosynthetic Gene cluster database, v4.0.
- Barona-Gómez F. Bacterial biosynthetic gene clusters. *Essays Biochem* 2026.
  PMID:42619353 (editorial for the special issue).
- Nivina A, Thiel Pizarro P. Evolutionary strategies of late-stage diversification
  in bacterial biosynthetic gene clusters. *Essays Biochem* 2026. PMID:42124485.
- Zotchev SB. Inter-species horizontal transfer of biosynthetic gene clusters.
  *Essays Biochem* 2026. PMID:41847751.
- Nayeb G Hosseini G, Barona-Gómez F. Intra- and inter-biosynthetic gene cluster
  allelic variation as drivers of chemical diversification in *Streptomyces*.
  *Essays Biochem* 2026. PMID:42388094.
- Göbner L *et al.* Heterologous expression of NRPS and PKS pathways in
  *Escherichia coli*. *Essays Biochem* 2026. PMID:42210863.
- Teshima A *et al.* Distribution of lactone-signaling system for expression of
  secondary metabolite BGCs in *Streptomyces* species. *Essays Biochem* 2026.
  PMID:42494319.
- Matine I *et al.* Regulatory and metabolic control of microbial biosynthetic
  gene clusters. *Commun Biol* 2026. PMID:42469370.
- Németh MZ *et al.* The terrein biosynthetic gene cluster of *Aspergillus
  terreus*: structure, function, regulation, and similar gene clusters.
  *Front Fungal Biol* 2025. PMID:41614020.
- Related internal projects (findings cross-registered): `projects/ALPHAFOLD.md`,
  `projects/PROTEIN_COMPLEX_FUNCTIONS.md` (catalytic-member attribution),
  `projects/PSEUDOENZYMES.md` (EryCII, PqsB, CLF), `projects/OVER_ANNOTATION_PATTERNS.md`
  (patterns 7-8), `projects/CONTESTED_FUNCTION.md` (EryCII + finding-level disputes),
  `projects/ENZYME_SPECIFICITY.md` (EryCIII TDP-vs-UDP donor),
  `projects/STRUCTURE_FUNCTION.md` (catalytic-residue presence/absence calls),
  `projects/TOP_NOTS.md` (NOT candidates: heme-less P450, active-site-less condensing folds).
