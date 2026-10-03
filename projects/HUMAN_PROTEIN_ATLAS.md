---
title: "Human Protein Atlas: Primary Cilium Life Cycle Module"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [human]
genes:
  - "human/CEP83"
  - "human/SCLT1"
  - "human/CEP89"
  - "human/FBF1"
  - "human/CEP164"
  - "human/TTBK2"
  - "human/CCP110"
  - "human/CEP97"
  - "human/KIF24"
  - "human/MYO5A"
  - "human/EHD1"
  - "human/EHD3"
  - "human/RAB3IP"
  - "human/RAB8A"
  - "human/CEP290"
  - "human/MKS1"
  - "human/TMEM67"
  - "human/CC2D2A"
  - "human/B9D1"
  - "human/B9D2"
  - "human/TCTN1"
  - "human/TCTN2"
  - "human/TMEM216"
  - "human/TMEM231"
  - "human/NPHP1"
  - "human/NPHP4"
  - "human/RPGRIP1L"
  - "human/IFT88"
  - "human/IFT52"
  - "human/IFT81"
  - "human/IFT74"
  - "human/IFT172"
  - "human/IFT140"
  - "human/IFT122"
  - "human/WDR35"
  - "human/TTC21B"
  - "human/KIF3A"
  - "human/KIF3B"
  - "human/KIFAP3"
  - "human/DYNC2H1"
  - "human/DYNC2LI1"
  - "human/DYNC2I1"
  - "human/DYNC2I2"
  - "human/ARL13B"
  - "human/ARL3"
  - "human/PDE6D"
  - "human/UNC119B"
  - "human/RP2"
  - "human/INPP5E"
  - "human/TULP3"
  - "human/CILK1"
  - "human/MAK"
  - "human/KIF7"
  - "human/AURKA"
  - "human/NEDD9"
  - "human/CIMAP3"
  - "human/HDAC6"
  - "human/PLK1"
  - "human/KIF2A"
  - "human/DYNLT1"
---

# Human Protein Atlas: Primary Cilium Life Cycle Module

**Bottom line:** The project now builds a module for the life cycle of the
primary cilium, from licensing of the mother centriole to resorption before
mitosis, and uses the Human Protein Atlas (HPA) cilium atlas as localization
evidence for its members. A first draft,
[modules/primary_cilium_life_cycle.yaml](../modules/primary_cilium_life_cycle.yaml),
has 7 stages, 28 role annotons and 60 human proteins. It passes schema and module
validation. Only 6 of the 60 members have gene reviews, so reviewing them is
the main work ahead.

The project started as a general re-evaluation of HPA subcellular evidence in
GO. That analysis is kept on a sub-page:
[HPA subcellular evidence re-evaluation](HUMAN_PROTEIN_ATLAS/hpa-evidence-reevaluation.md).

## Why combine HPA with a cilium module

The HPA primary-cilium atlas
([Hansen et al. 2025, *Cell*, PMID:41005307](https://doi.org/10.1016/j.cell.2025.08.039))
mapped 715 proteins to four sub-ciliary classes (cilium, ciliary tip,
transition zone, basal body) in three cell lines. About 85% of its calls are
graded Approved or Uncertain, so they never reach GOA (see the sub-page).
On their own, those calls cannot tell a real ciliary protein from antibody
noise. A module supplies the missing context: if a protein has a defined role
at a defined life-cycle stage, its atlas call can be judged against that
role. Going the other way, the atlas tests whether each module member is
seen where the module puts it.

## Module structure

| # | Stage | GO process | Members (human) |
|---|---|---|---|
| 1 | Mother centriole licensing | non-motile cilium assembly | distal appendages CEP83, SCLT1, CEP89, FBF1, CEP164; TTBK2; CP110 cap CCP110, CEP97, KIF24 |
| 2 | Ciliary vesicle formation | ciliary vesicle assembly | MYO5A; EHD1, EHD3; RAB3IP (Rabin8); RAB8A |
| 3 | Transition zone assembly | ciliary transition zone assembly | MKS module MKS1, TMEM67, CC2D2A, B9D1, B9D2, TCTN1, TCTN2, TMEM216, TMEM231; NPHP module NPHP1, NPHP4, RPGRIP1L; CEP290 |
| 4 | Axoneme extension by IFT | intraciliary transport | IFT-B IFT88, IFT52, IFT81, IFT74, IFT172; IFT-A IFT140, IFT122, WDR35, TTC21B; kinesin-2 KIF3A, KIF3B, KIFAP3; dynein-2 DYNC2H1, DYNC2LI1, DYNC2I1, DYNC2I2 |
| 5 | Ciliary membrane composition | protein localization to cilium | ARL13B, ARL3, RP2; PDE6D, UNC119B; INPP5E; TULP3 (BBSome export is in [modules/bbsome.yaml](../modules/bbsome.yaml)) |
| 6 | Length control | regulation of cilium assembly | CILK1, MAK; KIF7 |
| 7 | Disassembly | cilium disassembly | AURKA, NEDD9, CIMAP3 (Pitchfork), HDAC6; PLK1, KIF2A; DYNLT1 (Tctex-1) |

Each stage cites primary literature checked against PubMed (distal
appendages PMID:23348840, TTBK2 PMID:23141541, EHD1/EHD3 PMID:25686250,
transition zone PMID:21725307, dynein-2 PMID:31451806, Aurora A–HDAC6
PMID:17604723, KIF2A PMID:25660017, and others in the YAML).

**Boundary.** The module covers primary (non-motile) cilia. Motile cilia,
centriole duplication, ciliary signaling pathways (Hedgehog is
[modules/hedgehog_signaling.yaml](../modules/hedgehog_signaling.yaml)) and the
ciliary pocket are outside it.

**Ontology gaps found while building it** (recorded as `knowledge_gaps`):

- GO has no term for regulation of cilium length and no cytoplasmic dynein-2
  complex term.
- Distal appendage scaffolds, transition zone barrier proteins, IFT adaptors
  and microtubule depolymerases have no molecular-function term. These
  annotons carry a free-text function only.
- `primary cilium` (GO:0072372) is obsolete. The module uses
  `non-motile cilium` (GO:0097730) as context.

## HPA evidence for module members

From [cilium_life_cycle/member_evidence.md](HUMAN_PROTEIN_ATLAS/cilium_life_cycle/member_evidence.md),
counting cilium, tip, transition zone and basal body calls for the 68 candidate
members:

| Best HPA cilium call | Members |
|---|---|
| Supported or Enhanced | 24 (e.g. SCLT1, FBF1, EHD1, MKS1, IFT88, IFT140, ARL13B, TULP3, KIF7) |
| Approved or Uncertain only | 22 (e.g. CEP83, CEP164, TTBK2, CEP290, RAB8A, IFT52, IFT81, KIF3A, KIF3B) |
| No cilium call | 22 (e.g. TMEM67, CC2D2A, NPHP1, IFT172, DYNC2H1, INPP5E, PLK1) |

The middle row is the key finding. Canonical ciliogenesis proteins
(CEP83, CEP164, CEP290, IFT52, KIF3A) carry only Approved or Uncertain grades.
For core ciliary proteins, HPA's grade says little about whether the location
is real. Module membership and literature are the better guide. The
"no call" row is mostly transmembrane transition zone proteins and
low-abundance motors, which antibody IF often misses.

## Files

- Module: [modules/primary_cilium_life_cycle.yaml](../modules/primary_cilium_life_cycle.yaml)
  (generated by [scripts/build_cilium_module.py](HUMAN_PROTEIN_ATLAS/scripts/build_cilium_module.py)
  from a curated spec; UniProt names are read from the candidate table)
- Candidates: [cilium_life_cycle/candidate_members.tsv](HUMAN_PROTEIN_ATLAS/cilium_life_cycle/candidate_members.tsv)
  (accessions from the UniProt REST API)
- Member evidence: `scripts/cilium_members.py` produces
  `cilium_life_cycle/member_evidence.tsv` and `.md`
- HPA cilia analysis: `scripts/hpa_cilia.py` and `data/hpa_cilia_*`
- HPA data snapshot (v25): `data/subcellular_location.tsv`

```bash
uv run python projects/HUMAN_PROTEIN_ATLAS/scripts/cilium_members.py
uv run python projects/HUMAN_PROTEIN_ATLAS/scripts/build_cilium_module.py
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/primary_cilium_life_cycle.yaml
uv run python -m ai_gene_review.validation.module_validator modules/primary_cilium_life_cycle.yaml
```

---
# STATUS

Last updated: 2026-10-03

## Module
- [x] Define boundary and stages
- [x] Fetch UniProt accessions for candidates (UniProt REST)
- [x] Draft `modules/primary_cilium_life_cycle.yaml` (schema and module validation pass)
- [ ] Module deep research (`just module-deep-research-falcon modules/primary_cilium_life_cycle.yaml`) and reconcile with the draft
- [ ] Replace GENE_PRODUCT selectors with PANTHER families and PAINT nodes where they can be verified from local data
- [ ] Add HPA atlas localization evidence (PMID:41005307) to annotons where the member's review accepts it
- [ ] Decide whether the 8 candidates left out of the module belong in a stage: OFD1, KIF17, MPHOSPH9, PACSIN1, RAB11A, AHI1, LZTFL1 (BBSome regulator) and BBS1 (covered by modules/bbsome.yaml)
- [ ] Propose GO terms: regulation of cilium length; cytoplasmic dynein-2 complex

## Member gene reviews (priority order: stage, then core role)
Already reviewed: human/TMEM67, human/CC2D2A, human/B9D1, human/ARL13B, human/HDAC6, human/PLK1 (plus candidates human/AHI1, human/BBS1, human/LZTFL1)

Stage 1, licensing:
- [ ] human/CEP164
- [ ] human/TTBK2
- [ ] human/CEP83
- [ ] human/SCLT1
- [ ] human/CEP89
- [ ] human/FBF1
- [ ] human/CCP110
- [ ] human/CEP97
- [ ] human/KIF24

Stage 2, ciliary vesicle:
- [ ] human/MYO5A
- [ ] human/EHD1
- [ ] human/EHD3
- [ ] human/RAB3IP
- [ ] human/RAB8A

Stage 3, transition zone:
- [ ] human/CEP290
- [ ] human/MKS1
- [ ] human/TCTN1
- [ ] human/TCTN2
- [ ] human/B9D2
- [ ] human/TMEM216
- [ ] human/TMEM231
- [ ] human/NPHP1
- [ ] human/NPHP4
- [ ] human/RPGRIP1L

Stage 4, IFT:
- [ ] human/IFT88
- [ ] human/IFT52
- [ ] human/IFT81
- [ ] human/IFT74
- [ ] human/IFT172
- [ ] human/IFT140
- [ ] human/IFT122
- [ ] human/WDR35
- [ ] human/TTC21B
- [ ] human/KIF3A
- [ ] human/KIF3B
- [ ] human/KIFAP3
- [ ] human/DYNC2H1
- [ ] human/DYNC2LI1
- [ ] human/DYNC2I1
- [ ] human/DYNC2I2

Stage 5, membrane composition:
- [ ] human/ARL3
- [ ] human/INPP5E
- [ ] human/TULP3
- [ ] human/RP2
- [ ] human/PDE6D
- [ ] human/UNC119B

Stage 6, length control:
- [ ] human/CILK1
- [ ] human/MAK
- [ ] human/KIF7

Stage 7, disassembly:
- [ ] human/AURKA
- [ ] human/NEDD9
- [ ] human/CIMAP3
- [ ] human/KIF2A
- [ ] human/DYNLT1

For each review, record how the HPA cilium call (grade, sub-ciliary class)
compares with the role the module assigns.

# NOTES

## 2026-10-03 (pivot)

- Pivoted the project from general HPA evidence re-evaluation to a primary
  cilium life-cycle module, with the HPA cilium atlas as evidence. The earlier
  work moved to `HUMAN_PROTEIN_ATLAS/hpa-evidence-reevaluation.md`; its
  worklists are paused, not abandoned.
- Kept the `HUMAN_PROTEIN_ATLAS` slug to avoid renaming churn.
- Built the draft module with a generator script so UniProt names come from
  the API-derived table, not memory. GO ids were checked in OLS, and 21 PMIDs
  were checked in PubMed. Three PMIDs that I first had in mind resolved to
  unrelated papers and were dropped.
- The module validator rejects complex terms (IFT-A, IFT-B, kinesin II, MKS
  complex) as locations. They now sit on the complex descriptors, and the
  locations are anatomical (axoneme, non-motile cilium, basal body).
- Canonical members often carry only Approved or Uncertain HPA grades. That
  is the main argument for judging atlas calls in a module context.
