---
title: "Antimicrobial Resistance (AMR) Project"
maturity: MATURE
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
---

# Antimicrobial Resistance (AMR) Project

## Overview

This project tracks the annotation review of **antimicrobial resistance (AMR) determinants** — bacterial genes whose products allow a microorganism to withstand the effects of an antibiotic. These genes are excellent targets for AI-assisted curation because:

1. **Well-characterized biochemistry, sparse GO** — many resistance enzymes are mechanistically and structurally well-studied, yet their UniProt/GOA records carry only an over-general electronic keyword term (e.g. `GO:0016740` transferase activity) or are entirely empty for TrEMBL accessions.
2. **A purpose-built reference ontology already exists** — the [Comprehensive Antibiotic Resistance Database (CARD)](https://card.mcmaster.ca/) and its **Antibiotic Resistance Ontology (ARO)** provide expert-curated drug-class, mechanism, gene-family, substrate, and literature data per determinant. This is a high-value, structured source we can mine to seed and quality-check reviews (see [Using CARD/ARO](#using-cardaro) below).
3. **Clinically important and mobile** — most clinical determinants are plasmid/transposon-borne, so the same gene recurs across many UniProt accessions, organisms, and strains. Consistent, mechanism-grounded annotation has direct surveillance value.

**Scope:** modification/inactivation enzymes (phosphotransferases, esterases, acetyltransferases, β-lactamases), target-protection and target-modification proteins (e.g. rRNA methyltransferases), and efflux systems. The initial featured examples focus on the **macrolide phosphotransferase (MPH) family**.

## Primary Mapping Page

> **Open the curator-facing mapping page:** [ARO → GO mapping table](ANTIMICROBIAL_RESISTANCE/aro2go.html)
>
> This is the central reusable artifact for the AMR project. It shows the curated ARO→GO mappings, mapping gaps, CARD/AmiGO links, propagation scope, and candidate annotation impact in one place. Start here when reviewing or extending the AMR mapping set.

## Key Concepts

### Resistance mechanism categories (ARO)
- **Antibiotic inactivation** — covalent modification (phosphorylation, acetylation, hydrolysis) of the drug. The MPH enzymes below are the canonical example.
- **Antibiotic target alteration** — e.g. *erm* rRNA methyltransferases that dimethylate 23S rRNA A2058.
- **Antibiotic target protection** — e.g. ribosomal protection proteins.
- **Antibiotic efflux** — active export (e.g. AcrAB-TolC, *mef* macrolide efflux pumps).
- **Reduced permeability** — porin loss.

### GO annotation challenges
- The molecular function (e.g. `GO:0050073` macrolide 2'-kinase activity) is often a **leaf MF term** that exactly captures the chemistry, but the only term propagated electronically is its uninformative parent.
- The biological process is almost always **`GO:0046677` response to antibiotic** (the drug is modified, **not** catabolized — `antibiotic catabolic process` would over-state degradation).
- **Substrate scope is finer-grained than any single GO MF term.** GO has one `macrolide 2'-kinase activity` term, but MphA and MphB differ biologically in which macrolides they modify. We record this distinction in `core_functions.substrates` using ChEBI.

## Featured Examples: the Macrolide Phosphotransferase (MPH) family

Macrolide 2'-phosphotransferases inactivate macrolide antibiotics by transferring the γ-phosphate of a purine nucleoside triphosphate (GTP/ITP/ATP, GTP favored) onto the **2'-OH of the desosamine sugar**, yielding an inactive macrolide 2'-O-phosphate that can no longer bind the bacterial ribosome. They adopt the bi-lobed **protein-kinase-like / aminoglycoside-phosphotransferase (APH) fold**, distinguished by a large interdomain linker forming an expanded, hydrophobic macrolide-binding pocket (Fong et al. 2017, PMID:28416110). MphA and MphB are the clinically prevalent, mobile-element-borne paralogs and make an instructive **substrate-specificity contrast**.

### MphA — macrolide 2'-phosphotransferase I (MPH(2')-I)

| | |
|---|---|
| **Organism** | *Escherichia coli* (NCBITaxon:562) |
| **UniProt** | Q47396 |
| **CARD/ARO** | [ARO:3000316](https://card.mcmaster.ca/aro/3000316) |
| **Review** | <gene species="ECOLX" symbol="mphA">mphA</gene> |
| **Status** | COMPLETE (DRAFT) |

**Key findings**
- **Narrow spectrum:** highly active on 14-membered (erythromycin, oleandomycin, clarithromycin, roxithromycin) and 15-membered (azithromycin) macrolides, but only very weakly on 16-membered macrolides — the discriminator from MphB (O'Hara/PMID:2478074; Golkar 2018 PMID:30177927).
- **Inducible:** synthesis is induced by erythromycin via the upstream TetR-family repressor **MphR(A)** (PMID:10960087) — unlike constitutive MphB.
- High-level resistance from the native determinant requires **mphA + mrx** (accessory membrane protein; PMID:8619599).
- The most clinically prevalent plasmid-borne macrolide-resistance determinant in Enterobacterales; carried on an **IS26/IS6100 composite transposon** (mphA-mrx(A)-mphR(A)) predominantly on IncF plasmids (PMID:38318209), conferring transferable high-level azithromycin resistance (PMID:38521802).

**GO calls (all NEW — GOA was empty for this accession)**
- `GO:0050073` macrolide 2'-kinase activity (IDA) — core MF
- `GO:0046677` response to antibiotic (IMP) — core BP
- `GO:0005737` cytoplasm (IDA) — soluble intracellular enzyme

### MphB — macrolide 2'-phosphotransferase II (MPH(2')-II)

| | |
|---|---|
| **Organism** | *Escherichia coli* O83:H1 (strain NRG 857C / AIEC; NCBITaxon:685038) |
| **UniProt** | A0A0H3EUF3 |
| **CARD/ARO** | [ARO:3000318](https://card.mcmaster.ca/aro/3000318) (cross-referenced from the UniProt `DR CARD` line) |
| **Review** | <gene species="ECO8N" symbol="mphB">mphB</gene> |
| **Status** | COMPLETE (DRAFT) |

**Key findings**
- **Broad spectrum:** inactivates 14-, 15- **and 16-membered** macrolides (spiramycin, tylosin, josamycin) plus the ketolide **telithromycin**. Early phenotyping called MphB narrow, but enzymatic/MS work (Pawlowski 2018, PMID:29317655) showed it modifies essentially all macrolides tested. The 16-membered substrates are the discriminator from MphA.
- **Constitutive** intracellular enzyme (Kono 1992, PMID:1330822).
- Mechanism mapped: catalytic aspartates D200/D209/D219/D231 and **His205** are essential; D227 contributes to 16-membered-ring recognition (PMID:10428938, PMID:15033229).
- Identity triple-anchored: UniProt SubName + CARD ARO:3000318 + the original cloning paper (Noguchi 1996, PMID:8900063; 302 aa / 34483 Da matches this entry exactly).

**GO calls (all NEW — GOA was empty for this accession)**
- `GO:0050073` macrolide 2'-kinase activity (IDA) — core MF
- `GO:0046677` response to antibiotic (IMP) — core BP
- `GO:0005737` cytoplasm (IDA) — soluble intracellular enzyme

### The MphA vs MphB contrast (curation lesson)

Both enzymes share the **same GO MF leaf term** (`GO:0050073`), yet are biologically distinct in substrate scope and regulation. GO alone cannot express this difference; we capture it in `core_functions.substrates` (ChEBI) — MphA: 14-/15-membered only; MphB: adds josamycin/tylosin (16-membered) + telithromycin. This is a concrete case where **CARD's curated drug list adds resolution beyond the available GO term**, and a good argument for recording substrate specificity structurally.

## Genes for Review

| Species | Gene | UniProt | ARO | Family / Mechanism | Status |
|---------|------|---------|-----|--------------------|--------|
| ECOLX | <gene species="ECOLX" symbol="mphA">mphA</gene> | Q47396 | ARO:3000316 | MPH / antibiotic inactivation | COMPLETE |
| ECO8N | <gene species="ECO8N" symbol="mphB">mphB</gene> | A0A0H3EUF3 | ARO:3000318 | MPH / antibiotic inactivation | COMPLETE |
| ECOLX | <gene species="ECOLX" symbol="mcr-1">mcr-1</gene> | A0A0R6L508 | ARO:3003689 | pEtN transferase / colistin target modification | COMPLETE |
| ENTCL | <gene species="ENTCL" symbol="aac6-Ib">aac6-Ib</gene> | A0A076UB44 | ARO:3002579 | AAC / antibiotic inactivation | COMPLETE |

### Focused AMR candidate review batch

The following 20 draft reviews were selected from the ARO→GO annotation-gain candidates to cover multiple AMR mechanisms and mapping classes. These are focused AMR reviews anchored on UniProt/CARD identity and the curated ARO→GO mapping artifacts; they are intended as curator leads rather than full gene-specific literature syntheses.

| Species | Gene | UniProt | Primary AMR call | Status |
|---------|------|---------|------------------|--------|
| ECOLX | <gene species="ECOLX" symbol="mcr2">mcr2</gene> | A0A1C3NEV1 | MCR pEtN transferase + antibiotic response | DRAFT |
| SALSP | <gene species="SALSP" symbol="mcr-4">mcr-4</gene> | A0A222YQC1 | MCR pEtN transferase + antibiotic response | DRAFT |
| AERME | <gene species="AERME" symbol="mcr-3">mcr-3</gene> | A0A223HCL9 | MCR pEtN transferase + antibiotic response | DRAFT |
| ECOLX | <gene species="ECOLX" symbol="rmtE">rmtE</gene> | A0A0M5JP06 | 16S rRNA guanine-N7 methyltransferase | DRAFT |
| KLEPN | <gene species="KLEPN" symbol="rmtD">rmtD</gene> | B0F9V0 | 16S rRNA guanine-N7 methyltransferase | DRAFT |
| KLEPN | <gene species="KLEPN" symbol="rmtF">rmtF</gene> | I1YZZ5 | 16S rRNA guanine-N7 methyltransferase | DRAFT |
| AERER | <gene species="AERER" symbol="ermA">ermA</gene> | P09891 | rRNA adenine-N6 methyltransferase + antibiotic response | DRAFT |
| BACFG | <gene species="BACFG" symbol="ermF">ermF</gene> | P10337 | rRNA adenine-N6 methyltransferase + antibiotic response | DRAFT |
| BACAN | <gene species="BACAN" symbol="ermJ">ermJ</gene> | Q04720 | rRNA adenine-N6 methyltransferase + antibiotic response | DRAFT |
| BACSP | <gene species="BACSP" symbol="knt">knt</gene> | P05058 | aminoglycoside nucleotidyltransferase + antibiotic response | DRAFT |
| STAAU | <gene species="STAAU" symbol="ant">ant</gene> | P0A0D2 | aminoglycoside nucleotidyltransferase + antibiotic response | DRAFT |
| BACSU | <gene species="BACSU" symbol="aadK">aadK</gene> | P17585 | aminoglycoside nucleotidyltransferase + antibiotic response | DRAFT |
| ECOLX | <gene species="ECOLX" symbol="hph">hph</gene> | P00557 | aminoglycoside phosphotransferase + antibiotic response | DRAFT |
| PSEAI | <gene species="PSEAI" symbol="strB">strB</gene> | O84956 | aminoglycoside phosphotransferase + antibiotic response | DRAFT |
| STAAU | <gene species="STAAU" symbol="apmA">apmA</gene> | A0A1D0AST6 | aminoglycoside acetyltransferase + antibiotic response | DRAFT |
| ENTCL | <gene species="ENTCL" symbol="fosA5">fosA5</gene> | A0A346FWD3 | glutathione transferase + antibiotic response | DRAFT |
| PRORE | <gene species="PRORE" symbol="fosA3">fosA3</gene> | A0AB35LIB0 | glutathione transferase + antibiotic response | DRAFT |
| ACIBZ | <gene species="ACIBZ" symbol="blaOXA-418">blaOXA-418</gene> | A0A088NUF2 | beta-lactamase + antibiotic response | DRAFT |
| ACIBA | <gene species="ACIBA" symbol="blaOXA-400">blaOXA-400</gene> | A0A097A0C1 | beta-lactamase + antibiotic response | DRAFT |
| ACIBA | <gene species="ACIBA" symbol="blaOXA-480">blaOXA-480</gene> | A0A0S1NF91 | beta-lactamase + antibiotic response | DRAFT |

### Full reviews of high-value GO term gaps

After triaging the unmapped ARO terms, the most valuable misses were not broad
CARD mechanism classes but concrete enzyme chemistries where GO has no suitable
leaf molecular-function term. The following reviews are full curation drafts:
all fetched GOA annotations are adjudicated, zero-GOA cases have explicit `NEW`
candidate annotations, and each proposed term is backed by UniProt plus cached
primary literature where available.

| Species | Gene | UniProt | ARO gap | Review outcome |
|---------|------|---------|---------|----------------|
| SPHSM | <gene species="SPHSM" symbol="tetX">tetX</gene> | Q06DK7 | `ARO:3000036` tetracycline inactivation enzyme | Accept broad `GO:0004497`; propose **tetracycline 11a-monooxygenase activity** |
| STAAT | <gene species="STAAT" symbol="fosB">fosB</gene> | A8Z522 | FosB excluded from FosA/GST mapping | Accept broad `GO:0016765`; propose **fosfomycin bacillithiol-S-transferase activity** |
| MYCSM | <gene species="MYCSM" symbol="arr">arr</gene> | O67972 | `ARO:3000390` rifampin ADP-ribosyltransferase | Add interim broad transferase; propose **rifampin mono-ADP-ribosyltransferase activity** |
| ECOLX | <gene species="ECOLX" symbol="ereB">ereB</gene> | P05789 | `ARO:3000320` macrolide esterase | Add broad hydrolase parent; propose **erythromycin esterase activity** |
| STAHA | <gene species="STAHA" symbol="lnuA">lnuA</gene> | P06107 | `ARO:3000221` lincosamide nucleotidyltransferase | Add broad transferase/antibiotic response; propose **lincosamide O-nucleotidyltransferase activity** |
| STAWA | <gene species="STAWA" symbol="cfr">cfr</gene> | A2AXI2 | `ARO:3000202` Cfr 23S rRNA methyltransferase | Remove tRNA carryover; propose **23S rRNA A2503 C8 methyltransferase activity** |

Two practical lessons from this batch:

- The high-level `GO:0046677` response-to-antibiotic annotation is usually true,
  but it is not the real curation win; the win is the missing enzyme chemistry.
- UniProt flat files and GOA TSVs can diverge for these accessions. Several
  entries had useful `DR GO` lines in UniProt that did not appear in fetched GOA,
  so full review should inspect both rather than trusting only the GOA seed.

### Reviews validating annotation-gain candidates

<gene species="ECOLX" symbol="mcr-1">MCR-1</gene> and <gene species="ENTCL" symbol="aac6-Ib">AAC(6')-Ib8</gene> were reviewed through the full curation process specifically to ground-truth the
[annotation-gain candidates](ANTIMICROBIAL_RESISTANCE/ANNOTATION_GAIN.md), giving two contrasting outcomes:

- **<gene species="ECOLX" symbol="mcr-1">MCR-1</gene> (A0A0R6L508)** — the candidate `GO:0043838` (phosphatidylethanolamine:Kdo2-lipid A pEtN
  transferase) is a **genuine gain**: the GOA carries only the over-general `GO:0016772`/`GO:0016776`,
  which are refined (`MODIFY`) to the specific EC 2.7.8.43 activity, structurally/biochemically
  supported (PMID:27655155, 29079699). The review also flags the mis-propagated
  `GO:0009244` (LPS core biosynthesis → over-annotated) and adds `GO:0046677` and zinc binding.
- **<gene species="ENTCL" symbol="aac6-Ib">AAC(6')-Ib8</gene> (A0A076UB44)** — the candidate `GO:0034069` (aminoglycoside N-acetyltransferase) is
  **correctly rejected**: the entry already has the more specific child `GO:0047663`
  (aminoglycoside 6'-N-acetyltransferase, EC 2.3.1.82), so the family-level term would be a redundant
  over-annotation. This is the subsumption case from the embedded [spot review](#spot-review-of-annotation-gain-candidates).

## Spot Review of Annotation-Gain Candidates

Manual QA of 6 candidate new annotations from the [annotation-gain report](ANTIMICROBIAL_RESISTANCE/ANNOTATION_GAIN.md) (one per family, including the
broad `relatedMatch` ones), checked against the UniProt record (protein name / EC number / existing
GO) and GO subsumption (OAK). Goal: confirm correct gains and surface false positives.

| # | UniProt | ARO (gene) | candidate GO | verdict |
|---|---------|-----------|--------------|---------|
| 1 | A0A0R6L508 <gene species="ECOLX" symbol="mcr-1">MCR-1</gene> | ARO:3003689 MCR-1.1 | GO:0043838 PE:Kdo2-lipidA pEtN transferase | ✅ **correct, high value** |
| 2 | A0A0M5JP06 <gene species="ECOLX" symbol="rmtE">RmtE</gene> | ARO:3004679 rmtE2 | GO:0070043 rRNA guanine-N7-MTase | ✅ **correct refinement** |
| 3 | A0A0K2B0L6 srm1 | ARO:3004605 ermZ | GO:0052910 23S rRNA A-N6-diMTase | ✅ **correct, more precise** |
| 4 | A0A076UB44 <gene species="ENTCL" symbol="aac6-Ib">AAC(6')-Ib8</gene> | ARO:3002579 | GO:0034069 aminoglycoside N-acetyltransferase | ⚠️ **redundant (over-general)** |
| 5 | A0A062U9V1 | ARO:3008508 OXA-1090 | GO:0008800 beta-lactamase | ❓ **questionable (PBP vs OXA)** |
| 6 | A0A024FRF7 FosK | ARO:3003207 | GO:0004364 glutathione transferase | ⚠️ **mapping over-generalizes** |

### Spot Review Details

**1. <gene species="ECOLX" symbol="mcr-1">MCR-1</gene> → GO:0043838 — correct, high value.** UniProt names it "Phosphatidylethanolamine
transferase Mcr-1 (**EC 2.7.8.43**)"; EC 2.7.8.43 *is* GO:0043838. Existing GO has only the broad
`GO:0016776` (phosphotransferase, phosphate acceptor), which is **not** an ancestor of GO:0043838 —
so the specific MF is genuinely missing. Representative of all 79 colistin/MCR gains.

**2. <gene species="ECOLX" symbol="rmtE">RmtE</gene> → GO:0070043 — correct refinement.** UniProt: "16S rRNA (guanine(1405)-N(7))-
methyltransferase (**EC 2.1.1.179**)". Entry currently has `GO:0008649` (general rRNA
methyltransferase); candidate GO:0070043 is a *descendant* of it → a valid, more-specific term. (The
ideal m7G1405 term is the recorded GO gap.)

**3. ermZ/srm1 → GO:0052910 — correct, more precise.** *Streptomyces ambofaciens* spiramycin-
producer resistance methylase. Existing `GO:0000179` is the generic N6,N6-dimethyltransferase (covers
KsgA too); candidate GO:0052910 is the Erm 23S-A2058-specific term and is **not** subsumed by
GO:0000179 → a genuine precision gain.

**4. <gene species="ENTCL" symbol="aac6-Ib">AAC(6')-Ib8</gene> → GO:0034069 — redundant.** UniProt: "Aminoglycoside N(6')-acetyltransferase
(**EC 2.3.1.82**)". Entry already has `GO:0047663` "aminoglycoside 6'-N-acetyltransferase activity",
which **is a child of** the candidate GO:0034069. So the candidate is *true but over-general* — the
entry already carries a more specific term. **Quantified across the snapshot, this affects the
aminoglycoside families specifically:**

| candidate GO | candidates | already have a more-specific child (redundant) |
|---|---:|---:|
| GO:0034069 aminoglycoside N-acetyltransferase (AAC) | 76 | **51** |
| GO:0034068 aminoglycoside nucleotidyltransferase (ANT) | 35 | **22** |
| GO:0034071 aminoglycoside phosphotransferase (APH) | 31 | **19** |
| GO:0008800 beta-lactamase | 448 | 0 |
| GO:0043838 colistin/MCR pEtN transferase | 79 | 0 |
| GO:0052910 Erm 23S diMTase | 29 | 0 |

Approximately **92 of 746** candidates are subsumption-redundant — all in the aminoglycoside
families (GO has a well-developed sub-hierarchy there). The β-lactamase/MCR/Erm/FosA/16S gains have
**no** such child term, so the family-level MF is a genuine addition. **Action: the gain filter should
suppress a candidate when the entry already has a more specific (is_a descendant) GO term.**

**5. OXA-1090 → GO:0008800 — questionable.** UniProt names A0A062U9V1 generically as "Penicillin-
binding protein transpeptidase domain-containing protein" in an environmental alphaproteobacterium
(*Hyphomonas beringensis*), with only `GO:0008658` (penicillin binding). Class D (OXA) β-lactamases
and PBPs share the serine-transpeptidase fold; CARD's protein-homolog model can match a genuine **PBP**
that is **not** a β-lactamase. GO:0008800 should not be asserted here without review — illustrates
that the 5,317-descendant β-lactamase family node can over-reach to distant homologs.

**6. FosK → GO:0004364 — mapping over-generalizes.** UniProt: "Integron-mediated fosfomycin-modifying
enzyme (FosK)", *Acinetobacter* (Gram-negative → likely FosA-type/glutathione, so plausibly fine
*here*). But the mapped node `ARO:3000133` "fosfomycin **thiol** transferase" also covers **FosB**,
which uses **bacillithiol/L-cysteine, not glutathione** — so propagating GO:0004364 (glutathione
transferase) family-wide would mis-annotate FosB members. (Existing `GO:0004462` lactoylglutathione
lyase on this entry is itself a VOC/glyoxalase-superfamily over-annotation.) **Action: restrict the
fosfomycin mapping to a FosA-specific ARO node, or keep `relatedMatch` with an explicit FosA-only
caveat.**

### Spot Review Takeaways / Actions

1. **Add a subsumption-aware filter to the gain report**: drop a candidate GO term when the entry
   already has a more specific descendant of it (fixes #4). *(DONE — implemented in
   `annotation_gain_report.py`; suppressed 104 redundant candidates, 734 → 630, almost all in the
   aminoglycoside AAC/ANT/APH families.)*
2. **Tighten the fosfomycin mapping** (#6): map FosA, not the FosA+FosB "thiol transferase" parent.
   *(DONE — re-anchored ARO:3000133 → glutathione-specific FosA/FosA2/FosA3/fosA5, excluding FosB/FosX.
   Also from PR review: Erm now maps to the family-safe `GO:0008988` (not the di-methyltransferase
   `GO:0052910`) so mono-methylating variants are not over-annotated; <gene species="ENTCL" symbol="aac6-Ib">AAC(6')-Ib</gene> review gained primary
   references PMID:18710261 and PMID:16369542 plus a cytoplasm location.)*
3. **Flag homology over-reach** (#5): family-node candidates for distant/environmental homologs (e.g.
   proteins UniProt names as generic PBP/transpeptidase) warrant curator review before assertion.
4. Net: 2/6 high-confidence correct, 2/6 correct precision gains, 1/6 redundant, 1/6 questionable —
   consistent with treating these as **curator leads, not automatic assertions**.

### Candidate next genes
- **mph(C), mph(E), mph(G)** — other macrolide phosphotransferase family members (ARO macrolide phosphotransferase family).
- **erm(B) / erm(C)** — 23S rRNA (adenine-N6)-methyltransferases (target alteration; MF `GO:0008988` rRNA (adenine-N6-)-methyltransferase activity).
- **mef(A) / mef(E)** — macrolide efflux (MFS transporter; target efflux).
- **ere(A) / ere(B)** — macrolide esterases (antibiotic inactivation by hydrolysis).
- **Aminoglycoside APH/AAC/ANT** enzymes — same kinase superfamily as MPH; natural extension.
- **β-lactamases** (e.g. *bla*CTX-M, KPC) — large, clinically dominant inactivation family.

## Using CARD/ARO

This section is the **methodology research deliverable**: how the CARD/ARO resource can be incorporated into the gene-review workflow.

### What CARD/ARO is
- **CARD** (Comprehensive Antibiotic Resistance Database, McMaster) is an expert-curated, peer-reviewed collection of AMR determinants, organized by the **Antibiotic Resistance Ontology (ARO)**. Each determinant is an ARO term (e.g. `ARO:3000316` mphA, `ARO:3000318` mphB) classified along three axes: **Drug Class**, **Resistance Mechanism**, and **AMR Gene Family**, with `confers_resistance_to_drug(_class)` relations, curated reference sequences, and citation PMIDs.
- The **ARO is an OBO Foundry ontology**, CC-BY 4.0. It is distributed as `aro.owl` (also OBO / TSV / JSON), with a PURL at `http://purl.obolibrary.org/obo/aro.owl` and source at [github.com/arpcard/aro](https://github.com/arpcard/aro). CARD bulk data (`card.json`, FASTA, TSV) is downloadable from <https://card.mcmaster.ca/download> (and `https://card.mcmaster.ca/latest/ontology` / `.../latest/data` for automation). Updated every 1–3 months.

### Integration points for this repo

1. **UniProt → ARO is already wired.** UniProt records carry a `DR CARD;` cross-reference line. For MphB the `*-uniprot.txt` already contains:
   ```
   DR   CARD; ARO:3000318; mphB; ARO:0001004; antibiotic inactivation.
   ```
   This means: when fetching a bacterial gene, the `DR CARD` line gives us the **ARO id, gene symbol, and mechanism for free**. (MphA's UniProt entry lacks the DR line, but the ARO term `ARO:3000316` is easily resolved by gene symbol — a small parser could backfill this.) A lightweight enhancement to `fetch-gene` could surface any `DR CARD` accession into the notes stub.

2. **Seed the `description` and substrate scope.** The ARO term page lists the **curated drug list** (= substrate scope) and mechanism. We used `ARO:3000318`'s curated list (erythromycin, roxithromycin, clarithromycin, dirithromycin, oleandomycin, azithromycin, spiramycin, tylosin, telithromycin) to expand the MphB description and to populate `core_functions.substrates` with ChEBI ids — at **finer granularity than the single GO MF term**.

3. **Harvest reference PMIDs.** ARO terms cite the primary literature establishing the determinant. Two CARD-cited PMIDs (8900063, 17302923) were added to the MphB review directly from `ARO:3000318`. These can be auto-fetched into `publications/`.

4. **Mechanism → GO mapping (QC).** The ARO resistance-mechanism class is a strong prior for the GO BP/MF, per the table below.

| ARO mechanism | GO BP | typical GO MF pattern |
|---|---|---|
| antibiotic inactivation | `GO:0046677` response to antibiotic | drug-modifying enzyme MF (kinase/acetyltransferase/hydrolase) |
| antibiotic target alteration | `GO:0046677` | methyltransferase / modifying-enzyme MF |
| antibiotic efflux | `GO:0046677` (+ transport BP) | transmembrane transporter activity |

A small **ARO-mechanism → GO** lookup table like this lets us (a) seed candidate GO terms and (b) flag reviews whose GO calls disagree with the curated mechanism. **Note: no ARO→GO mapping exists today.** Inspection of `aro.owl` (8,602 classes) shows `hasDbXref` namespaces of only ARO, PMID, PubChem, ChEBI, ChEMBL, CAS, PDB, ISBN, RO, DOID — and zero `GO:` references; GO is not imported into ARO. So any ARO↔GO bridge has to be **built and maintained by us** (e.g. the small table above, or a richer mapping keyed on AMR-gene-family + mechanism), not pulled from CARD. This bridge is provided as a SSSOM mapping set at `projects/ANTIMICROBIAL_RESISTANCE/aro2go.sssom.yaml` (23 mappings: MPH, beta-lactamase, CAT, APH/AAC/ANT, Erm, dfr, sul, FosA/FosA2/FosA3/fosA5, colistin/MCR phosphoethanolamine transferase, and aminoglycoside 16S rRNA methyltransferase families → GO MF, plus the six ARO mechanism classes → GO BP). `just validate-mappings` runs both `linkml-validate` (structure) and **`linkml-term-validator`** (every ARO/GO CURIE resolves and its label matches the ontology — the curie+label-tuple guarantee), via the sidecar schema `src/ai_gene_review/schema/aro_go_mapping.yaml`. ChEBI xrefs on ARO drug terms *are* present, which is directly useful for the `substrates` field even though the GO side is not.

5. **Identity anchoring.** The ARO reference sequence + family HMM (here NCBIfam `NF000242` macrolide_MphB) gives an independent check that a TrEMBL accession is the determinant we think it is — valuable when GOA is empty and we are minting `NEW` annotations.

6. **Tooling.** `argNorm` (Bioinformatics 2025) normalizes ARG-annotation output (from RGI, AMRFinderPlus, etc.) to ARO accessions, and **RGI** assigns ARO ids to protein/contig sequences. Either could be wrapped in a `*-bioinformatics/` analysis to confirm a sequence's ARO identity reproducibly before annotation.

### Pipeline: UniProt → ARO → GO

A working pipeline applies the ARO→GO mapping to UniProt records: `projects/ANTIMICROBIAL_RESISTANCE/uniprot2aro2go.py` (run with `just aro2go-pipeline`). It gets **UniProt→ARO** from `DR CARD` lines where present (deterministic, but sparse — 1/2334 cached records here), falls back to parsing **RGI** output for entries without one (e.g. MphA), then chains **ARO→GO** via `aro2go.sssom.yaml`. As a check it reproduces the hand-curated GO calls — MphB (`DR CARD`) → `GO:0050073` + `GO:0046677`; MphA (RGI) → `GO:0050073`.

**Propagation is exact-or-narrower**: a GO term mapped at an ARO term applies to any gene whose ARO assignment is that term *or a narrower (is_a descendant)* ARO term. This makes family nodes the high-value targets — the single `beta-lactamase` (`ARO:3000001`) → `GO:0008800` mapping reaches all **5,317** descendant ARO gene terms (CTX-M, KPC, NDM, …). The pipeline walks each gene's ARO is_a ancestors (via OAK) and records `aro_relation` = `exact`/`narrower` in the output. Candidates carry full provenance (gene ARO, mapped ARO, relation, predicate, GO, route) for curator review. See `projects/ANTIMICROBIAL_RESISTANCE/README.md`.

**Curator view & impact.** `just render-mappings` builds a browsable HTML page of all mappings + gaps with CARD/AmiGO links. `just annotation-gain` applies the mappings to the **4,182** UniProtKB entries carrying a CARD cross-reference and reports the GO terms they would gain but don't yet have: **630** candidate new annotations (subsumption-aware — a further 104 over-general parents are suppressed where the entry already has a more specific child term) — e.g. all 79 colistin/MCR entries lack `GO:0043838`; 448 beta-lactamases lack `GO:0008800`.

**Project artifacts** (rendered to `pages/projects/ANTIMICROBIAL_RESISTANCE/` by `just render-ar-pages`):

- **Primary:** [ARO → GO mapping table (HTML)](ANTIMICROBIAL_RESISTANCE/aro2go.html) — the curator view of all 23 mappings + 9 gaps.
- [Annotation-gain report](ANTIMICROBIAL_RESISTANCE/ANNOTATION_GAIN.html) — candidate new UniProt annotations.
- [Spot review](#spot-review-of-annotation-gain-candidates) — manual QA of sample candidates, embedded above.
- [Mappings & pipeline README](ANTIMICROBIAL_RESISTANCE/README.html) — methods, validation, propagation logic.

### Recommended convention
- Record the ARO id in the gene notes (`- CARD/ARO: ARO:NNNNNNN (gene); mechanism = ...`) with provenance, as already done for both MPH genes.
- Treat CARD as a **HIGH-relevance curated source** but still **verify, don't trust**: confirm each CARD-cited PMID against PubMed and anchor substrate/mechanism claims to a checkable primary reference before marking a `reference_review` as `VERIFIED`.

## Key References

- McArthur AG et al. (2013) *Antimicrob Agents Chemother* — The Comprehensive Antibiotic Resistance Database. PMID:23650175
- Alcock BP et al. (2023) *Nucleic Acids Res* — CARD 2023: expanded curation, support for machine learning, and resistome prediction. PMID:36263822
- Fong DH et al. (2017) *Structure* — Structural basis for kinase-mediated macrolide antibiotic resistance (MPH(2')-I and -II crystal structures). PMID:28416110
- Pawlowski AC et al. (2018) *Nat Commun* — The evolution of substrate discrimination in macrolide antibiotic resistance enzymes (MphB broad spectrum, 2'-OH MS confirmation). PMID:29317655
- Golkar T et al. (2018) *Front Microbiol* — Look and Outlook on enzyme-mediated macrolide resistance (MphA vs MphB substrate contrast). PMID:30177927
- Kono M et al. (1992) *FEMS Microbiol Lett* — Purification/characterization of MPH(2')II. PMID:1330822
- O'Hara K et al. (1989) *Antimicrob Agents Chemother* — Purification/characterization of MPH(2')I. PMID:2478074
- argNorm: normalization of antibiotic resistance gene annotations to the ARO (2025) *Bioinformatics*

**Source**: AI Gene Review project, [ai4curation/ai-gene-review](https://github.com/ai4curation/ai-gene-review). CARD/ARO are products of the Comprehensive Antibiotic Resistance Database (card.mcmaster.ca), CC-BY 4.0.
</content>
</invoke>
