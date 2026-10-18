# GCNT1 (C2GnT1) — curation notes

## 2026-09-17 — de novo review

No `-deep-research-PROVIDER.md`: deep-research tooling was unavailable (OpenAI
key rejected). Per repository policy nothing self-authored was named as provider
output. Review grounded in the cached publications, which existed for every PMID
GOA cites.

### Core activity is unusually cleanly established

[PMID:1329093 "enabled us to demonstrate unequivocally that the cDNA encodes the
core 2 beta-1,6-N-acetylglucosaminyltransferase, the enzyme responsible for the
formation of Gal beta 1-3(GlcNAc beta 1-6)GalNAc structures"] — and, importantly
for a large family where paralog mis-assignment is the standing risk,
[PMID:1329093 "No activity with this enzyme was detected toward the acceptors for
other beta 1-6GlcNAc transferases"]. The negative specificity control is what
makes the specific MF term safe here.

### Nuclear speckles: an antibody artefact, and how it was established

`GO:0016607 nuclear speck` came from GO_REF:0000052 (immunofluorescence
curation). Removed. The topological argument is a priori — the catalytic domain
occupies residues 33–428 on the lumenal face, leaving a nine-residue cytoplasmic
tail, so a membraneless nuclear body is not reachable — but the decisive evidence
is empirical, from querying the Human Protein Atlas API directly:

| Gene | HPA main | HPA all |
|---|---|---|
| **GCNT1** | Nuclear speckles | Nuclear speckles (no Golgi) |
| GCNT2 | Golgi apparatus | Golgi apparatus |
| GCNT3 | Golgi apparatus | Golgi apparatus, Vesicles |
| GCNT4 | Golgi apparatus | Nucleoplasm, Golgi apparatus |
| C1GALT1 | Nuclear bodies, Cytosol | Nuclear bodies, Cytosol (no Golgi) |
| ST6GALNAC1 | Golgi apparatus | Nucleoplasm, Golgi apparatus |
| B4GALT1 | Golgi apparatus | Golgi apparatus |
| FUT8 | Golgi apparatus | Nucleoplasm, Golgi apparatus, Cytosol |

(B3GNT6, ST3GAL1, GALNT1, MGAT1 have no informative HPA IF record.)

The distinction that matters is **replace vs supplement**. GCNT4, ST6GALNAC1 and
FUT8 each carry a nucleoplasm background call *alongside a retained Golgi call* —
ordinary nuclear background. GCNT1's nuclear call **replaces** the Golgi
entirely, i.e. the antibody misses the compartment where this enzyme's
biochemistry demonstrably occurs. That is the signature of off-target binding.

**Correction to note:** an OpenScientist run claimed GCNT1 *uniquely* lacks a
Golgi call and listed C1GALT1 and GCNT2 as having no HPA data. Both have records,
and C1GALT1 also lacks a Golgi call. Two related core-1/core-2 enzymes showing
the same pattern strengthens the artefact reading — it looks like an
antibody-class problem — but only GCNT1's version was imported into GO. Worth a
broader audit; raised in `suggested_questions`.

### Guilt-by-substrate, concentrated

GCNT1 carries leukocyte tethering or rolling, its positive regulation, and cell
adhesion molecule production, all because it builds the core 2 branch of a
selectin ligand. Two things from reading the full text of PMID:23027862:

- The tethering/rolling/ICAM-1 assays were run on **GOLPH3-depleted** cells, not
  GCNT1-depleted cells — a two-step inference through enzyme mislocalisation.
- Direct GCNT1 knockdown *was* done, for the biosynthetic readout only:
  [PMID:23027862 "following the treatment with C2GnT1 siRNA, there was a 74.6%
  decrease in PSGL-1-associated C2-O-sLe x"], with PSGL-1 protein level unchanged.

So the biosynthetic process annotation is directly supported; the cell-behaviour
terms are downstream and non-core. `GO:0060352 cell adhesion molecule production`
is the weakest: the paper's own control shows the adhesion molecule is still
produced, only differently glycosylated.

### Gated lead — possible shedding

[PMID:35279766 "we found unique peptides mapping to CHST14, GCNT1, B4GALNT1,
MAN1C1 and XYLT2"] — GCNT1 peptides appear among Golgi enzymes whose abundance
tracks SPPL3 expression. GCNT1 has no extracellular annotation in GOA. Recorded
as a `suggested_questions` lead only, **not** asserted: a single peptide
observation in a study focused on SPPL3 is not sufficient, and the same standard
was applied in marking GALNT1's extracellular annotation over-annotated.

### Localization nuance

`GO:0005802 trans-Golgi network` marked over-annotated: the paper reports
[PMID:23027862 "Our data also indicate partial co-localization of C2GnT1 with a
trans- Golgi marker TGN46"] and [PMID:23027862 "We found a higher degree of
colocalization of a cis- Golgi protein GM130"], i.e. distribution across the
stack with a cis-lean, which `GO:0031985 Golgi cisterna` describes better.
