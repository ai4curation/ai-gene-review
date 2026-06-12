# Antimicrobial Resistance (AMR) Project

## Overview

This project tracks the annotation review of **antimicrobial resistance (AMR) determinants** — bacterial genes whose products allow a microorganism to withstand the effects of an antibiotic. These genes are excellent targets for AI-assisted curation because:

1. **Well-characterized biochemistry, sparse GO** — many resistance enzymes are mechanistically and structurally well-studied, yet their UniProt/GOA records carry only an over-general electronic keyword term (e.g. `GO:0016740` transferase activity) or are entirely empty for TrEMBL accessions.
2. **A purpose-built reference ontology already exists** — the [Comprehensive Antibiotic Resistance Database (CARD)](https://card.mcmaster.ca/) and its **Antibiotic Resistance Ontology (ARO)** provide expert-curated drug-class, mechanism, gene-family, substrate, and literature data per determinant. This is a high-value, structured source we can mine to seed and quality-check reviews (see [Using CARD/ARO](#using-cardaro) below).
3. **Clinically important and mobile** — most clinical determinants are plasmid/transposon-borne, so the same gene recurs across many UniProt accessions, organisms, and strains. Consistent, mechanism-grounded annotation has direct surveillance value.

**Scope:** modification/inactivation enzymes (phosphotransferases, esterases, acetyltransferases, β-lactamases), target-protection and target-modification proteins (e.g. rRNA methyltransferases), and efflux systems. The first batch focuses on the **macrolide phosphotransferase (MPH) family**.

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
| **Review** | `genes/ECOLX/Q47396_ECOLX/Q47396_ECOLX-ai-review.yaml` |
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
| **Review** | `genes/ECO8N/A0A0H3EUF3_ECO8N/A0A0H3EUF3_ECO8N-ai-review.yaml` |
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
| ECOLX | mphA | Q47396 | ARO:3000316 | MPH / antibiotic inactivation | COMPLETE |
| ECO8N | mphB | A0A0H3EUF3 | ARO:3000318 | MPH / antibiotic inactivation | COMPLETE |

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

4. **Mechanism → GO mapping (QC).** The ARO resistance-mechanism class is a strong prior for the GO BP/MF:
   | ARO mechanism | GO BP | typical GO MF pattern |
   |---|---|---|
   | antibiotic inactivation | `GO:0046677` response to antibiotic | drug-modifying enzyme MF (kinase/acetyltransferase/hydrolase) |
   | antibiotic target alteration | `GO:0046677` | methyltransferase / modifying-enzyme MF |
   | antibiotic efflux | `GO:0046677` (+ transport BP) | transmembrane transporter activity |
   A small **ARO-mechanism → GO** lookup table would let us (a) seed candidate GO terms and (b) flag reviews whose GO calls disagree with the curated mechanism. **Note: no ARO→GO mapping exists today.** Inspection of `aro.owl` (8,602 classes) shows `hasDbXref` namespaces of only ARO, PMID, PubChem, ChEBI, ChEMBL, CAS, PDB, ISBN, RO, DOID — and zero `GO:` references; GO is not imported into ARO. So any ARO↔GO bridge has to be **built and maintained by us** (e.g. the small table above, or a richer mapping keyed on AMR-gene-family + mechanism), not pulled from CARD. This bridge is provided as a SSSOM mapping set at `projects/mappings/aro2go.sssom.yaml` (18 mappings: MPH, beta-lactamase, CAT, APH/AAC/ANT, Erm, dfr, sul, FosA families → GO MF, plus the six ARO mechanism classes → GO BP). `just validate-mappings` runs both `linkml-validate` (structure) and **`linkml-term-validator`** (every ARO/GO CURIE resolves and its label matches the ontology — the curie+label-tuple guarantee), via the sidecar schema `src/ai_gene_review/schema/aro_go_mapping.yaml`. ChEBI xrefs on ARO drug terms *are* present, which is directly useful for the `substrates` field even though the GO side is not.

5. **Identity anchoring.** The ARO reference sequence + family HMM (here NCBIfam `NF000242` macrolide_MphB) gives an independent check that a TrEMBL accession is the determinant we think it is — valuable when GOA is empty and we are minting `NEW` annotations.

6. **Tooling.** `argNorm` (Bioinformatics 2025) normalizes ARG-annotation output (from RGI, AMRFinderPlus, etc.) to ARO accessions, and **RGI** assigns ARO ids to protein/contig sequences. Either could be wrapped in a `*-bioinformatics/` analysis to confirm a sequence's ARO identity reproducibly before annotation.

### Pipeline: UniProt → ARO → GO

A working pipeline applies the ARO→GO mapping to UniProt records: `projects/mappings/uniprot2aro2go.py` (run with `just aro2go-pipeline`). It gets **UniProt→ARO** from `DR CARD` lines where present (deterministic, but sparse — 1/2334 cached records here), falls back to parsing **RGI** output for entries without one (e.g. MphA), then chains **ARO→GO** via `aro2go.sssom.yaml`. As a check it reproduces the hand-curated GO calls — MphB (`DR CARD`) → `GO:0050073` + `GO:0046677`; MphA (RGI) → `GO:0050073`.

**Propagation is exact-or-narrower**: a GO term mapped at an ARO term applies to any gene whose ARO assignment is that term *or a narrower (is_a descendant)* ARO term. This makes family nodes the high-value targets — the single `beta-lactamase` (`ARO:3000001`) → `GO:0008800` mapping reaches all **5,317** descendant ARO gene terms (CTX-M, KPC, NDM, …). The pipeline walks each gene's ARO is_a ancestors (via OAK) and records `aro_relation` = `exact`/`narrower` in the output. Candidates carry full provenance (gene ARO, mapped ARO, relation, predicate, GO, route) for curator review. See `projects/mappings/README.md`.

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
