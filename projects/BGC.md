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
| PqsB (PSEAE) | PQS condensing heterodimer | Queued |
| PqsC (PSEAE) | PQS condensing heterodimer | Queued |
| ActVA region pair (STRCO) | actinorhodin tailoring | Queued |
| Erythromycin DEBS pair (SACEN) | modular PKS | Queued |
| Nosiheptide pair (STRAT) | thiopeptide RiPP | Queued |
| Pyoluteorin pair (PSEF5) | edge-case control | Queued |

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
- Related internal projects: `projects/ALPHAFOLD.md`,
  `projects/PROTEIN_COMPLEX_FUNCTIONS.md`.
