---
title: "VAMPIROME: Vampire Bat Salivary Modulators"
marp: true
theme: default
paginate: true
backgroundColor: #fff
style: |
  section { font-size: 24px; }
  h1 { color: #2c3e50; }
  h2 { color: #34495e; }
  table { font-size: 18px; }
  section.lead h1 { font-size: 48px; }
---

<!-- _class: lead -->

# VAMPIROME

### Vampire bat salivary proteins that modulate host hemostasis and immunity

Chris Mungall | AI-Assisted Gene Review

2026-06-22

---

## Why this is interesting

- *Desmodus rotundus* (vampire bat; UniProt code **DESRO**) feeds exclusively on blood.
- To keep host blood flowing, its salivary glands secrete a cocktail of proteins that **block coagulation, dissolve clots, dilate vessels, and dampen innate immunity**.
- These host-manipulating proteins are a rich source of **anticoagulant and antithrombotic drug leads** (e.g. the bat-derived plasminogen activator concept).
- Yet most of the underlying gene products are **poorly annotated** in public databases.

---

## Key biology: a blood-feeding pharmacopeia

The salivary secretome targets the host across several axes:

- **Hemostasis / coagulation** — plasminogen activators, Kunitz/TFPI-like inhibitors, serpins, apyrase, phosphatase (platelet function).
- **Vascular tone / angiogenesis** — natriuretic/CNP peptide, PACAP, ADAMTS metalloproteases.
- **Innate immune modulation** — DNases (neutrophil function), chemokine/lymphotoxin-like cytokines, TSG-6-related TNF-inducible protein.
- **Antimicrobial defense** — beta-defensin, lysozyme (accessory-gland enriched).

Source: Vampirome transcriptome/proteome of *D. rotundus* salivary glands (PMC3685427).

---

## The approach: AI-assisted gene review

- Curate DESRO salivary candidates within the **AI gene review framework**: synthesize literature, existing GO annotations, and bioinformatics into structured `*-ai-review.yaml` records.
- Map Vampirome **transcript IDs** (`BatTrinityAbyss-*`, `DrSigp-SigP-*`) to **TSA accessions** (GABZ01*) and **UniProt** entries via NCBI E-utilities + UniProt REST.
- Prioritize the most hemostasis/immune-relevant candidates for deep review.
- Cross-links with the broader **PARASITE_IMMUNE_MODULATORS** project on host immune manipulation.

---

## From transcript to UniProt: the mapping

Example mappings (transcript → TSA → UniProt → protein):

| Transcript | TSA | UniProt | Protein |
|---|---|---|---|
| BatTrinityAbyss-499018 | GABZ01006477 | K9IJK6 | t-plasminogen activator |
| BatTrinityAbyss-541822 | GABZ01007556 | K9IZA2 | Kunitz-type protease inhibitor 2 |
| BatTrinityAbyss-532109 | GABZ01002174 | K9J287 | Deoxyribonuclease-1-like 1 |
| BatTrinityAbyss-506850 | GABZ01008475 | K9IFY6 | C-C motif chemokine |
| BatTrinityAbyss-86412 | GABZ01007969 | K9IWR0 | Lymphotoxin-alpha |

---

## Priority shortlist (13 candidates)

Focused on hemostasis and immune modulation:

- **Hemostasis:** t-plasminogen activator (K9IJK6), Kunitz-type protease inhibitor 2 (K9IZA2), plasma protease C1 inhibitor (K9IYM3), ADAMTS-1 (K9IUF6)
- **Innate immune / neutrophil:** Deoxyribonuclease-1-like 1 (K9J287), C-C motif chemokine (K9IFY6), Lymphotoxin-alpha (K9IWR0), TNF-inducible gene 6 / TSG-6 (K9IIP0)
- **Antimicrobial:** Beta-defensin 1 (K9IFT7), lysozyme / LYZ (K9IWH5)
- **Vascular / other:** Natriuretic peptides B (K9IWC0), SCP/CRISP (K9IWX5), Dipeptidyl peptidase 4 (K9J2R0)

---

## Protein families represented

The secretome recruits recurring, repurposed protein families:

- **Protease inhibitors:** Kunitz/TFPI-like, serpins (neuroserpin, alpha-1-antichymotrypsin, Serpin B6), cystatin, Kazal, TIL, alpha-macroglobulin, TIMP-like.
- **Proteases:** plasminogen activator, ADAMTS metalloproteases, dipeptidyl peptidase 4.
- **Lipocalins:** multiple putative salivary lipocalins (lipid/ligand binding).
- **CAP / antigen-5 (CRISP)**, **chemokine/cytokine-like**, **DNases**, **antimicrobials** (defensin, lysozyme).

A small number of families, repeatedly expanded, do the host-manipulation work.

---

## Highlight: Draculin (seed gene)

- **Draculin** — the canonical vampire bat anticoagulant, curated as **Lactotransferrin (LTF), UniProt K9IMD0**.
- First seed gene with a completed annotation review in this project.
- Anchors the project's hemostasis theme and serves as the template for reviewing the remaining secreted modulators.

---

## Highlight: fibrinolytics & vasodilators

- **t-plasminogen activator (K9IJK6)** — fibrinolytic; the family behind bat-derived plasminogen-activator therapeutics; keeps the wound site clot-free.
- **Natriuretic peptides B / CNP (K9IWC0)** and **PACAP (K9IGD6)** — vasodilatory peptides that promote local blood flow.
- **vCGRP** — a calcitonin gene-related peptide-like vasodilatory peptide reported in the literature (Toxins 2019, Kakumanu et al.); DESRO transcript/UniProt mapping still **pending**.

---

## Challenges of curating these proteins

- **No Swiss-Prot entries** for DESRO in this candidate set — every mapped entry is **UniProtKB unreviewed (TrEMBL)**.
- Names are frequently **"Putative ..."** and based on homology, not direct functional evidence.
- Some Vampirome transcripts have **no TSA/UniProt hit yet** (e.g. several BatTrinityAbyss-* and DrSigp-SigP-* IDs; vCGRP unmapped).
- Original condensed Table 4 / supplemental spreadsheets are on a **moved NIAID portal** and not yet re-accessible.
- Function must be inferred carefully: salivary repurposing means the host-facing role can differ from the family's canonical role.

---

## Status & future directions

**Done:**
- Project structure, Table 4 extract, UniProt mapping, candidate list (Swiss-Prot prioritized — none found).
- 13-candidate priority shortlist; UniProt/GOA fetched; falcon deep-research for all 13.
- Annotation reviews + notes for Draculin and the full shortlist; core_functions for Draculin, K9IZA2, K9IYM3, K9J287.

**Next:**
- Synthesize core functions across remaining candidates.
- Map unmapped transcripts (incl. vCGRP/CALCA) and recover full supplemental tables.
- Expand cross-links with PARASITE_IMMUNE_MODULATORS.

---

<!-- _class: lead -->

# Thank you

A poorly-annotated, drug-relevant secretome — made curatable, one salivary protein at a time.

Project: `projects/VAMPIROME.md` | Code: DESRO (*Desmodus rotundus*)
