# ABHD14A — review notes

PAINT no-IBA project review, using the `affinage` deep-research provider plus UniProt Q9BUJ0,
the GOA TSV and the primary literature.

## Outcome: stays dark, with citations for why

Three GO annotations, all localisation. No molecular function, no biological process, and none
proposed. The peer-reviewed literature says so directly
[PMID:37974539, "While ABHD14A still lacks any functional annotation to date, we"] recently
showed that ABHD14B functions as a lysine deacetylase.

## The chief hazard: ABHD14B

[PMID:37974539, "Given \ntheir high sequence similarity, automated databases often wrongly assign
ABHD14A \nand ABHD14B as the same enzyme, and therefore, annotating functions to them in \nvarious
organisms has been problematic."]

ABHD14B **is** characterised — a lysine deacetylase. ABHD14A is not. Sequence determinants
separating them had to be defined explicitly because databases kept merging them. This is the
AASDH failure mode (PR #2226) caught before it happens.

## Topology — the feature that argues against the paralog

Applied to this gene's *own* annotations, not just to hypothetical future ones. UniProt annotates:

| Feature | Value | Evidence |
|---|---|---|
| Subcellular location | Cytoplasm | `ECO:0000250` (by similarity) |
| Topology | **Single-pass type II membrane protein** | `ECO:0000305` |
| `FT TRANSMEM` | 35–55, *"Signal-anchor for type II membrane protein"* | `ECO:0000255` |
| `FT CARBOHYD` | Asn-67, Asn-201 | `ECO:0000255` |

Type II topology with glycosylated residues C-terminal to the anchor puts the **hydrolase domain
on the lumenal/extracellular side**. ABHD14B is soluble. So the two proteins differ in where they
sit, not only in sequence — and "the family behaves this way" is not a reason to accept a
cytoplasmic call for this one.

That matters for the two cytoplasm annotations, which are still `ACCEPT`ed but on narrower
grounds: the IBA is evidence independent of the by-similarity UniProt call, and a type II protein
does present a short cytosolic N-terminal tail. What neither annotation establishes is **which
side the catalytic domain faces**, which is the question that matters here — and which would
reconcile with the Golgi localisation reported in the excluded preprint.

The `GO:0016020` row is marked over-annotated for lack of specificity, not for lack of membrane
association: the protein does carry an annotated signal-anchor, and the bare term conveys none
of it.

## ⚠️ Affinage citation caveat (campaign-wide)

The provider's two most substantive claims — short-chain ester hydrolysis with CoA enhancement,
and Golgi localisation — both cite:

```
PMID:bio_10.1101_2025.11.28.691245
```

**That is a bioRxiv DOI in a PMID-shaped field, not a PubMed identifier.** A reader skimming for
PMIDs would take preprint claims for peer-reviewed ones. Both claims are excluded here. If the
preprint is published they would justify a hydrolase molecular function and a Golgi location.

**Check the affinage `## Citations` list for `PMID:bio_*` before relying on any finding.**

## What is deliberately not annotated

The granule-neuron link comes from *Dorz1*, a rodent transcript expressed in differentiating
cerebellar granule neurons and regulated by Zic1. That is expression biology — being downstream
of a transcription factor is not participation in a process, the same conflation identified for
A1BG (#2217) and AARD (#2225).
