# Pseudoenzymes Project

**Project Start Date:** 2026-04-09
**Focus:** Identification, annotation, and curation of catalytically inactive enzyme homologs

## Project Overview

Pseudoenzymes are proteins that retain the structural fold and (often) the
metal-binding or substrate-binding capacity of an enzyme family but have lost
the ability to catalyze the canonical reaction. They are a surprisingly common
evolutionary outcome - estimated at **~10% of eukaryotic enzyme families
contain at least one pseudoenzyme member**, and in some families (protein
kinases, proteases) the proportion is higher.

**Pseudoenzymes are NOT pseudogenes.** They are expressed, stably folded
proteins that typically have:
- A new molecular function (neofunctionalization: allosteric regulator,
  scaffold, signaling hub, substrate carrier, pseudo-substrate)
- Residual or weakened catalytic activity (sub-catalytic; may still cleave
  slow substrates or bind intermediates)
- A regulatory role for the parental enzyme family (activator, inhibitor,
  decoy substrate, competitor)
- An unresolved function (possibly in neutral decay toward pseudogene status)

This project tracks pseudoenzymes encountered during gene curation, documents
the bioinformatic tools and patterns used to identify them, and catalogs the
specific annotation errors that arise from family-based propagation of enzyme
activity annotations. It complements `OVER_ANNOTATION_PATTERNS.md` (broad
annotation quality catalog) by focusing specifically on the pseudoenzyme
problem.

## Why this matters for GO annotation

Standard automated annotation pipelines (InterPro2GO, EC2GO, UniRule, ARBA,
Pfam-based) propagate enzyme activity annotations from family membership
without checking catalytic residue conservation. This produces a systematic
class of annotation errors for pseudoenzymes:

- **Molecular function terms** like GO:0004672 (protein kinase activity),
  GO:0004784 (superoxide dismutase activity), GO:0032452 (histone demethylase
  activity) propagated from family membership
- **Downstream biological process terms** like GO:0006468 (protein
  phosphorylation), GO:0019430 (removal of superoxide radicals),
  GO:0070076 (histone lysine demethylation)
- **Cofactor/binding terms** that depend on the activity (e.g., GO:0005507
  copper ion binding, GO:0051213 dioxygenase activity → metal ion binding,
  GO:0031624 ubiquitin conjugating enzyme binding)
- **Pathway annotations** that assume the protein performs the family
  reaction

Manual curation can catch these errors when:
1. Crystal structures or biochemical data exist showing catalytic incompetence
2. Critical catalytic residues are missing from the sequence
3. Conserved motifs around the active site (PROSITE patterns, PRINTS, etc.) fail
4. The protein is functionally annotated as something else (e.g., copper chaperone)
5. Functional studies demonstrate a non-enzymatic role (scaffold, regulator)

## Classification of pseudoenzymes by function

Pseudoenzymes fall into several functional categories (Murphy et al., 2017,
*Trends in Biochem Sci*; Ribeiro et al., 2019):

### Type 1: Allosteric activators of homologous active enzymes
The pseudoenzyme binds and activates its active paralog, often by promoting
the catalytically competent conformation. Classic examples:
- **HER3/ErbB3**: pseudokinase that heterodimerizes with and activates EGFR
- **STRAD**: pseudokinase that forms a heterotrimeric complex with LKB1 and
  MO25, essential for LKB1 activation
- **KSR1**: pseudokinase scaffold that activates RAF in MAPK signaling

### Type 2: Scaffolding / signaling hubs
The pseudoenzyme brings multiple proteins together through protein-protein
interactions, often via residual substrate-binding grooves:
- **TRIB1/2/3** (tribbles): pseudokinases that act as scaffolds in MAPK
  signaling and ubiquitin ligase recruitment
- **ILK** (integrin-linked kinase): pseudokinase scaffold in focal adhesions
- **RNase L pseudokinase domain**: scaffold within an RNase

### Type 3: Regulators of active family members (decoys, competitors)
The pseudoenzyme competes with active family members for substrates, cofactors,
or regulatory binding partners:
- **iRhom1/iRhom2**: pseudo-rhomboid proteases that regulate trafficking and
  stability of active rhomboid proteases
- **CCS (Copper Chaperone for SOD)**: delivers copper to SOD1 but does not
  itself catalyze dismutation (the SOD1 paralog in yeast is a similar pseudo-SOD)

### Type 4: Substrate binding / sequestration
The pseudoenzyme binds substrate without processing it, providing a buffering
or sequestration function:
- **Prostate-specific membrane antigen (PSMA)**: pseudo-glutamate carboxypeptidase
  that binds glutamate-containing substrates
- **Pseudo-phosphatases** that bind phospho-substrates without dephosphorylating them

### Type 5: Retaining reader/recognition function
The pseudoenzyme retains substrate recognition (e.g., modification state)
without modifying the substrate:
- **Epe1**: JmjC "pseudo-demethylase" that reads H3K9me marks without removing
  them, acting as an anti-silencing factor
- **MLL3/KMT2C SET domain**: reduced methyltransferase activity; may primarily
  read H3K4me

### Type 6: Unknown / novel function
The pseudoenzyme exists and is conserved under selection, but its function is
not yet clear:
- **RvSOD15** and 3 related *R. varieornatus* paralogs: still under investigation
- Many pseudokinases and pseudo-phosphatases in mammalian genomes

### Type 7: Degraded / decay
Some "pseudoenzymes" are actually proteins in the process of neutral decay
toward pseudogene status, with accumulated mutations but no selection for
function. Hard to distinguish from Type 6 without knockout experiments.

## Detection methodology

### 1. Direct catalytic residue conservation

Align target protein to a well-characterized canonical family member (e.g.,
human SOD1 for Cu/Zn SODs, a catalytically active JmjC demethylase for JmjC
domains) and check whether catalytic residues identified in mechanism
databases (M-CSA, Catalytic Site Atlas) are preserved.

**Advantages:** Simple, interpretable, no external database dependency.
**Limitation:** Detects only loss-of-residue mutations. Misses subtle
structural defects where residues are present but the surrounding context
is altered.

**Example implementations:**
- `genes/RAMVA/RvY_13070/RvY_13070-bioinformatics/analyze_sods.py` - Cu/Zn
  SOD catalytic residue check against human SOD1
- `genes/SCHPO/Epe1/Epe1-bioinformatics/analyze_jmjc_protein.py` - JmjC
  Fe(II) coordination motif check

### 2. PROSITE motif matching

PROSITE patterns require both the catalytic residues AND specific flanking
residues that maintain the structural geometry of the active site loop. A
protein matching the parental Pfam family but failing the PROSITE pattern
is a strong pseudoenzyme candidate.

**Why PROSITE > simple residue check:**
- PROSITE captures structural context, not just individual residues
- Flanking residues maintain the loop geometry that supports proper metal
  coordination
- Even when catalytic residues are present, altered flanking context can
  destabilize the active site (e.g., V87H rescue failure in RvSOD15)

**Example: Cu/Zn SOD family**
- PS00087 = N-terminal Cu coordination signature (H-x-H motif region):
  `[GA]-[IMFAT]-H-[LIVF]-H-{S}-x-[GP]-[SDG]-x-[STAGDE]`
- PS00332 = C-terminal disulfide signature (Cys146 region):
  `G-[GNHD]-[SGA]-[GR]-x-R-x-[SGAWRV]-C-x(2)-[IV]`

**Tools:**
- InterPro REST API (best for batch queries):
  `https://www.ebi.ac.uk/interpro/api/entry/prosite/protein/UniProt/{acc}/`
- ScanProsite local CLI from PROSITE distribution
- Direct pattern matching with Python `re` module for simple patterns
- Example: `genes/RAMVA/RvY_13070/RvY_13070-bioinformatics/check_prosite.py`

### 3. M-CSA-based conservation scoring

The Mechanism and Catalytic Site Atlas (M-CSA) at EBI curates catalytic
residues for enzyme families with 3D structures, including specific residue
roles (nucleophile, acid, base, metal ligand, transition state stabilizer).
Programmatic comparison of catalytic residue conservation against M-CSA
entries can flag pseudoenzymes across any enzyme family.

**Published tools:**
- **PseudoHunter** (Byrne et al. 2020, *Bioinformatics*) - detects pseudoenzymes
  by scoring conservation of M-CSA catalytic residues against a query sequence
- **Ribeiro et al. 2019** - M-CSA-based conservation scoring for detecting
  pseudoenzymes across PDB structures

**Access:**
- M-CSA REST API: `https://www.ebi.ac.uk/thornton-srv/m-csa/api/`
- Full download: M-CSA provides a JSON dump of all catalytic sites

### 4. HMM-based conservation scoring

For families where PROSITE patterns don't exist but Pfam HMMs do, you can
extract catalytic column positions from the HMM and check conservation at
those specific positions:
- `hmmalign` maps a query sequence to HMM columns
- Check catalytic column identities against the HMM consensus
- Lower conservation at catalytic columns than at non-catalytic columns
  suggests pseudoenzyme

**Example use case:** Epe1 JmjC domain - the Epe1 analysis uses conservation
scoring across the JmjC domain with focus on Fe(II)-binding positions.

### 5. Structural analysis (when crystal structure available)

- Check metal coordination distances and geometry
- Check active site accessibility and water coordination
- Compare to canonical family structure
- Mutagenesis rescue experiments (e.g., RvSOD15 V87H) can confirm whether
  restoring the putative missing residue restores activity

### 6. Family-specific resources

- **Pseudokinase Database** and **KLIFS** for kinases
- **MEROPS** flags "non-peptidase homologs" across protease families
- **CAZy** annotates non-catalytic members of glycoside hydrolase families
- **PROSITE PROFILE** patterns (more sensitive than PATTERN entries for
  divergent homologs)
- **InterPro signature integration** - inconsistent signature matches can
  flag divergent proteins

## Documented pseudoenzymes from gene reviews

### Cu/Zn Superoxide Dismutase family (Ramazzottius varieornatus)

The expanded SOD gene family (~10 paralogs) in *R. varieornatus* shows
substantial pseudoenzyme content. See
`genes/RAMVA/RvY_13070/RvY_13070-bioinformatics/RESULTS.md` for full analysis.

| Gene | UniProt | Status | Evidence | Reference |
|------|---------|--------|----------|-----------|
| **RvSOD15 (RvY_13070)** | A0A1D1VU85 | **Confirmed pseudoenzyme** | Crystal structure shows V87 replaces catalytic His; V87H rescue mutant did NOT restore activity (loop dynamics) | Sim & Inoue 2023 (PMID:37358501) |
| RvY_00650 | A0A1D1UDY8 | Probable pseudoenzyme | All Cu His preserved but PROSITE PS00087 fails (loop context divergent) | TARDIGRADE_STRESS_RESPONSE project |
| RvY_03757 | A0A1D1UP59 | Probable pseudoenzyme | All Cu His preserved but PROSITE PS00087 fails | TARDIGRADE_STRESS_RESPONSE project |
| RvY_17310 | A0A1D1W3Y1 | Probable pseudoenzyme | 475 aa (3x normal); all Cu His preserved but PROSITE PS00087 fails | TARDIGRADE_STRESS_RESPONSE project |
| RvY_15948 | A0A1D1VWP9 | **Not a SOD** - copper chaperone (CCS-like) | H46→A, H48→C; Pfam SODC but no PROSITE match; UniProt already classifies as chaperone | UniProt automatic |

**Key insight:** Roughly half of the expanded Cu/Zn-SOD repertoire in this
extremotolerant tardigrade is non-catalytic or serves chaperone roles. The
narrative of "more SOD gene copies = more antioxidant capacity" is only
partially correct.

**Annotation impact:** GO:0004784 (SOD activity), GO:0019430 (removal of
superoxide radicals), GO:0006801 (superoxide metabolic process) should be
MARK_AS_OVER_ANNOTATED for RvSOD15, RvY_00650, RvY_03757, RvY_17310; and
REMOVED for RvY_15948 (which is a chaperone, not a SOD).

### JmjC histone demethylase pseudoenzyme (Schizosaccharomyces pombe)

**Epe1** (*S. pombe*, UniProt O94603) - **confirmed pseudoenzyme** with
well-documented alternative function.

| Feature | Details |
|---------|---------|
| **Family** | JmjC domain (IPR003347); cupin superfamily (Fe(II)/α-KG dioxygenase) |
| **Defect** | Degenerate Fe(II)-binding motif (HVD at position 279-282 instead of canonical HxD); missing key catalytic residues |
| **Biochemical evidence** | Purified Epe1 shows NO detectable removal of H3K9me marks in mass spec assays; H297A "catalytic" mutant retains anti-silencing function |
| **Actual function** | Anti-silencing factor; recruits SAGA histone acetyltransferase and Bdf2 bromodomain protein to heterochromatin boundaries; promotes nucleosome turnover; functions as H3K9me **reader**, not eraser |
| **Type** | Type 5 (reader/recognition without modification) |
| **Annotations removed** | GO:0032452 (histone demethylase activity), GO:0051213 (dioxygenase activity), GO:0005506 (iron ion binding), GO:0070076 (histone lysine demethylation) |
| **Annotations added** | GO:0042393 (histone binding), GO:0140030 (modification-dependent protein binding) |
| **References** | Raiymbek 2020; Bao 2019; Epe1 gene review at `genes/SCHPO/Epe1/` |

**Key insight:** Epe1 is a paradigm for the Type 5 (reader) pseudoenzyme.
Its JmjC domain retains substrate recognition capability (binds H3K9me) but
cannot catalyze demethylation. This creates a common annotation error where
JmjC domain presence alone leads to multiple incorrect MF/BP annotations.

### Other enzymes that exist but aren't pseudoenzymes (clarification)

Some genes in the review set are described as "catalytically inactive" but
are not pseudoenzymes in the strict sense:

- **AlgG** (*P. putida*, alginate C5-epimerase): The protein has been shown
  to support polymer formation even when catalytically inactive, implying a
  structural role, but the protein is normally a functional epimerase. This
  is a dual-function protein, not a pseudoenzyme.
- **CipA** (*A. thermocellum*): A non-catalytic scaffolding protein that
  organizes cellulase enzymes. This is a *bona fide* non-enzymatic
  scaffoldin (contains cohesin domains), not a pseudoenzyme derived from
  a catalytic ancestor. Correctly annotated as structural.

### References to pseudoenzymes in other reviews

These reviews mention pseudoenzymes but the target gene is not itself the
pseudoenzyme:
- **DROME/Lkb1**: STRAD pseudokinase mentioned as obligate binding partner
  of active LKB1; classic Type 1 allosteric activator pseudokinase

## Patterns and lessons

### Pattern 1: Family expansion includes pseudoenzymes
When a single organism has many paralogs of an enzyme family (e.g., 10+
Cu/Zn-SODs in tardigrades, the vertebrate pseudokinome, the mammalian JmjC
family), expect ~30-50% of the paralogs to have lost canonical activity.
This appears to be a general feature of gene family expansion: some copies
retain function, others drift or neofunctionalize.

### Pattern 2: Pfam membership ≠ catalytic activity
The most common annotation error is propagating enzyme activity from Pfam
family assignment alone. PROSITE patterns are more rigorous because they
require canonical flanking residues, not just the catalytic residues.
Always check PROSITE, PRINTS, or other motif databases in addition to Pfam.

### Pattern 3: Subtle context defects matter
A protein with all catalytic residues intact can still be a pseudoenzyme if
the surrounding loop context is altered. The RvSOD15 V87H rescue failure is
the cleanest demonstration: restoring the missing histidine alone did not
restore activity because a nearby flexible loop destabilized the coordination.
Sequence-only checks miss these. Structural methods (crystal structures,
AlphaFold confidence at catalytic positions, molecular dynamics) or
motif-based methods (PROSITE PATTERN/PROFILE with contextual residues) are
needed to catch them.

### Pattern 4: Pseudoenzymes can have new functions
Many pseudoenzymes are not just degraded - they have evolved new roles.
When marking catalytic annotations as over-annotated, also consider whether
a NEW annotation for the actual function is appropriate:
- Pseudokinases → scaffolds, allosteric activators (GO:0030234 enzyme regulator activity)
- Pseudoproteases → protease regulators, trafficking factors
- Pseudo-demethylases → histone/DNA binding readers (GO:0042393)
- Pseudo-SODs → possibly Cu/Zn metal storage or chaperone functions

### Pattern 5: Automated pipelines over-propagate downstream annotations
When a pseudoenzyme is incorrectly annotated with a catalytic activity, the
downstream biological process and pathway annotations are also incorrectly
propagated. For example, Epe1's incorrect histone demethylase activity leads
to incorrect histone demethylation (BP), which leads to incorrect
"negative regulation of gene expression, epigenetic." All these downstream
annotations must be removed together.

### Pattern 6: The "catalytic residue plus flanking context" rule
For reliable pseudoenzyme detection, check THREE things:
1. Are the canonical catalytic residues present? (sequence conservation)
2. Are the flanking residues canonical? (PROSITE pattern match)
3. Is there experimental biochemical data? (literature)

If any one of these fails, the protein may be a pseudoenzyme. If all three
pass, it's likely functional. If all three fail, it's definitely a pseudoenzyme
(or not in the family at all, e.g., RvY_01767 which turned out to be a Mn-SOD,
not a Cu/Zn-SOD).

### Pattern 7: Beware cross-family comparisons
A "broken" Cu/Zn SOD might actually be a perfectly normal Mn/Fe SOD from a
different family entirely. Always verify that the protein is really in the
family you think it's in (check Pfam, InterPro, domain architecture) before
concluding it's a pseudoenzyme of that family. RvY_01767 was initially
flagged as a degraded Cu/Zn SOD but turned out to be a canonical Mn-SOD
(IPR001189 Mn/Fe_SOD family).

## Curation workflow / decision tree

When reviewing a gene in an enzyme family:

```
1. Identify the protein family (Pfam, InterPro domain composition)
   │
   ├─ Is the protein in the expected family?
   │  ├─ NO → Reconsider the family; it may be a different family's protein
   │  └─ YES → continue
   │
2. Check catalytic residues (M-CSA or literature-derived list)
   │
   ├─ Are all catalytic residues preserved?
   │  ├─ NO → Likely pseudoenzyme; MARK_AS_OVER_ANNOTATED SOD activity terms
   │  └─ YES → continue
   │
3. Check PROSITE/PRINTS/other motif patterns
   │
   ├─ Does the protein match the family-specific motifs?
   │  ├─ NO → Probably a context pseudoenzyme; MARK_AS_OVER_ANNOTATED with caveat
   │  └─ YES → continue
   │
4. Check literature for biochemical data
   │
   ├─ Is there published enzymatic assay data?
   │  ├─ Activity confirmed → ACCEPT catalytic annotations
   │  ├─ Activity refuted → REMOVE catalytic annotations; add NEW actual function
   │  └─ No data → ACCEPT with caveat about sequence-only evidence
   │
5. Consider whether a NEW annotation for non-catalytic function is warranted
   │
   └─ For known pseudoenzymes, propose scaffold/regulator/reader annotations
```

## Reusable analysis scripts

Two gene reviews contain reusable bioinformatic pipelines that can be adapted
to other enzyme families:

### Cu/Zn SOD template (`genes/RAMVA/RvY_13070/RvY_13070-bioinformatics/`)
- `analyze_sods.py` - direct catalytic residue conservation against human SOD1
- `check_prosite.py` - PROSITE pattern matching via InterPro REST API
- `RESULTS.md` - structured reporting template

**To adapt to a new enzyme family:**
1. Replace human SOD1 reference with a canonical family member
2. Update catalytic residue list for the new family (use M-CSA as authoritative source)
3. Update PROSITE pattern IDs and Pfam family accession
4. Run on all paralogs of interest

### JmjC domain template (`genes/SCHPO/Epe1/Epe1-bioinformatics/`)
More elaborate pipeline with:
- `01_fetch_sequences.py` - fetch paralogs and orthologs
- `02_jmjc_domain_analysis.py` - domain boundary + Fe(II)-binding motif search
- `03_conservation_analysis.py` - multiple sequence alignment conservation scoring
- `04_functional_regions_analysis.py` - non-catalytic region analysis (coiled coil, NLS, etc.)
- `05_structural_features.py` - structural feature prediction
- `justfile` - reproducible pipeline

Good template for families where the pseudoenzyme has neofunctionalized
(i.e., has active domains besides the catalytic domain, which is common).

## Open questions and research frontiers

1. **How many eukaryotic pseudoenzymes are there?** Estimates range from
   5-15% per enzyme family, but systematic surveys for most families are lacking.

2. **Can pseudoenzymes be experimentally resurrected?** Sim & Inoue's V87H
   rescue failure suggests it's not a single mutation fix. But for some
   pseudokinases, single mutations have partially restored activity.

3. **What's the difference between decay-in-progress and stable
   pseudoenzymes?** Requires population genetics (dN/dS), expression data,
   and functional characterization to distinguish.

4. **Do pseudoenzymes retain substrate binding?** Yes in many cases (HER3
   binds ATP; Epe1 binds H3K9me; iRhoms bind protease substrates). This is
   the common "retained substrate binding + lost catalysis" pattern.

5. **Are there pseudoenzymes in non-enzyme families?** Pseudo-receptors,
   pseudo-transcription factors, etc. exist. Similar principles apply.

## Key references

- **Sim & Inoue 2023** (PMID:37358501) - RvSOD15 crystal structure showing
  catalytic His replaced by Val; exemplar for context-dependent pseudoenzyme
  detection
- **Murphy et al. 2017** - "Bio-Zombie: the rise of pseudoenzymes in biology"
  *Trends in Biochem Sci*; foundational review of the pseudoenzyme concept
- **Ribeiro et al. 2019** - M-CSA-based conservation scoring *Nucleic Acids
  Res*; methodology paper
- **Byrne et al. 2020** - PseudoHunter detection pipeline *Bioinformatics*;
  tool paper
- **Raiymbek et al. 2020** - Epe1 biochemistry and anti-silencing function
- **Bao et al. 2019** - Epe1 H297A mutant retains anti-silencing; confirms
  non-enzymatic mechanism
- **Manning et al. 2002** - Original identification of ~10% of human kinome
  as pseudokinases *Cell*

## Cross-references

- `OVER_ANNOTATION_PATTERNS.md` - broader catalog of annotation quality issues
  (includes pseudoenzymes as one category among many)
- `TARDIGRADE_STRESS_RESPONSE.md` - the SOD pseudoenzyme analysis was first
  developed here; serves as an extended case study
- Individual reviews:
  - `genes/RAMVA/RvY_13070/` - RvSOD15 (confirmed pseudoenzyme)
  - `genes/RAMVA/RvY_00650/`, `genes/RAMVA/RvY_03757/`, `genes/RAMVA/RvY_17310/`
    (PROSITE-identified impaired paralogs)
  - `genes/RAMVA/RvY_15948/` - CCS chaperone (different pseudoenzyme type)
  - `genes/SCHPO/Epe1/` - JmjC pseudo-demethylase (paradigmatic Type 5 example)

## TODO / future work

- [ ] Search existing gene reviews systematically for additional pseudoenzyme
      candidates that may have been reviewed without being identified as such
- [ ] Add examples from human/mouse reviews (mammalian pseudokinases are
      the best-studied pseudoenzyme class)
- [ ] Create a generic "pseudoenzyme-screen.py" script that takes a protein
      family Pfam ID and canonical member, and screens all paralogs in a
      given organism
- [ ] Link to M-CSA programmatically for catalytic residue extraction
- [ ] Consider a curated CSV/TSV database of all identified pseudoenzymes
      across the project (gene, family, evidence type, category, references)
- [ ] Compare pseudoenzyme detection results to what PANTHER/IBA annotates,
      to quantify over-annotation rate for pseudoenzymes specifically
