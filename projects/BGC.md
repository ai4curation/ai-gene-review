---
title: "Biosynthetic Gene Cluster (BGC) Enzyme Complexes Project"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
---

# Biosynthetic Gene Cluster (BGC) Enzyme Complexes Project

**Project type:** Gene curation (exemplar enzymes from microbial natural-product gene clusters)
**Status:** Seeding — exemplar genes selected, curation queued

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
- Related internal projects (findings cross-registered): `projects/ALPHAFOLD.md`,
  `projects/PROTEIN_COMPLEX_FUNCTIONS.md` (catalytic-member attribution),
  `projects/PSEUDOENZYMES.md` (EryCII, PqsB, CLF), `projects/OVER_ANNOTATION_PATTERNS.md`
  (patterns 7-8), `projects/CONTESTED_FUNCTION.md` (EryCII + finding-level disputes),
  `projects/ENZYME_SPECIFICITY.md` (EryCIII TDP-vs-UDP donor),
  `projects/STRUCTURE_FUNCTION.md` (catalytic-residue presence/absence calls),
  `projects/TOP_NOTS.md` (NOT candidates: heme-less P450, active-site-less condensing folds).
