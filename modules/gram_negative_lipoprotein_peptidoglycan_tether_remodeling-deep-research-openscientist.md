---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T01:00:19.937712'
end_time: '2026-09-01T01:30:59.639818'
duration_seconds: 1839.7
template_file: templates/module_research.md.j2
template_variables:
  module_title: Gram-negative lipoprotein-peptidoglycan tether remodeling
  module_summary: A reusable Gram-negative bacterial module for reversible covalent
    attachment of an outer-membrane lipoprotein to peptidoglycan. An ErfK-family L,D-transpeptidase
    transfers a tetrapeptide-stem donor onto the C terminus of a Braun-lipoprotein-like
    substrate, and a YafK/LdtF-family cysteine hydrolase can release the lipoprotein
    by cleaving the resulting amide bond. These reactions remodel the connection between
    the outer membrane and sacculus; they do not represent peptidoglycan glycan polymerization
    or canonical 4-3 peptide crosslinking by penicillin-binding proteins.
  module_outline: "- Gram-negative lipoprotein-peptidoglycan tether remodeling\n \
    \ - 1. outer-membrane lipoprotein anchoring to peptidoglycan\n  - Lipoprotein-peptidoglycan\
    \ tether formation\n    - ErfK-family lipoprotein-anchoring L,D-transpeptidase\
    \ (molecular player: ErfK-family lipoprotein-anchoring L,D-transpeptidases; activity\
    \ or role: peptidoglycan L,D-transpeptidase activity)\n  - 2. lipoprotein-peptidoglycan\
    \ tether release\n  - Lipoprotein-peptidoglycan tether hydrolysis\n    - YafK/LdtF-family\
    \ lipoprotein-tether hydrolase (molecular player: YafK/LdtF-family lipoprotein-tether\
    \ hydrolases; activity or role: peptidoglycan-protein cross-link hydrolase activity)"
  module_connections: '- Lipoprotein-peptidoglycan tether formation feeds into Lipoprotein-peptidoglycan
    tether hydrolysis: The covalent tether formed by the ErfK-family enzyme is the
    substrate for YafK/LdtF-family hydrolysis.'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 18
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: gram_negative_lipoprotein_peptidoglycan_tether_remodeling-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: gram_negative_lipoprotein_peptidoglycan_tether_remodeling-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Gram-negative lipoprotein-peptidoglycan tether remodeling

## Working Scope

A reusable Gram-negative bacterial module for reversible covalent attachment of an outer-membrane lipoprotein to peptidoglycan. An ErfK-family L,D-transpeptidase transfers a tetrapeptide-stem donor onto the C terminus of a Braun-lipoprotein-like substrate, and a YafK/LdtF-family cysteine hydrolase can release the lipoprotein by cleaving the resulting amide bond. These reactions remodel the connection between the outer membrane and sacculus; they do not represent peptidoglycan glycan polymerization or canonical 4-3 peptide crosslinking by penicillin-binding proteins.

## Provisional Biological Outline

- Gram-negative lipoprotein-peptidoglycan tether remodeling
  - 1. outer-membrane lipoprotein anchoring to peptidoglycan
  - Lipoprotein-peptidoglycan tether formation
    - ErfK-family lipoprotein-anchoring L,D-transpeptidase (molecular player: ErfK-family lipoprotein-anchoring L,D-transpeptidases; activity or role: peptidoglycan L,D-transpeptidase activity)
  - 2. lipoprotein-peptidoglycan tether release
  - Lipoprotein-peptidoglycan tether hydrolysis
    - YafK/LdtF-family lipoprotein-tether hydrolase (molecular player: YafK/LdtF-family lipoprotein-tether hydrolases; activity or role: peptidoglycan-protein cross-link hydrolase activity)

## Known Relationships Among Steps

- Lipoprotein-peptidoglycan tether formation feeds into Lipoprotein-peptidoglycan tether hydrolysis: The covalent tether formed by the ErfK-family enzyme is the substrate for YafK/LdtF-family hydrolysis.

## Assignment

Write a rigorous, review-style synthesis suitable for a molecular biology
audience. Treat the topic as a biological system whose boundaries, core
mechanisms, variants, and unresolved points should be made clear to readers who
know the field but are not specialists in this specific process.

The review should be explanatory rather than encyclopedic. Anchor broad claims
in primary literature or authoritative reviews, but keep the focus on how the
system works and how its parts fit together.

## Questions To Address

1. **Scope and boundaries**
   - What exactly is included in this biological system?
   - Which neighboring pathways, organelle processes, complexes, or regulatory
     events are often confused with it but should be treated separately?
   - Are there competing definitions in the literature?

2. **Core mechanism**
   - What is the best current model for the sequence of events?
   - Which steps are obligatory, which are conditional, and which are accessory?
   - What molecular assemblies, enzymes, receptors, adaptors, transporters, or
     structural units carry out each major step?

3. **Variation**
   - How does the system vary across major evolutionary lineages?
   - Are there well-supported differences between cell types, tissues,
     developmental stages, physiological states, or compartments?
   - Where are there alternative routes that achieve a similar outcome by
     different molecular means?

4. **Conservation and origin**
   - What is the deepest plausible evolutionary origin of the system?
   - Which parts appear ancient and conserved, and which appear to be later
     elaborations, replacements, or lineage-specific losses?
   - When a protein family has expanded, which family members are the best
     representatives for understanding the ancestral role?

5. **Physical and biological constraints**
   - What steps must occur in a particular order?
   - Which events are mutually exclusive, compartment-specific, cell-type
     specific, substrate-specific, or stage-specific?
   - What evidence rules out otherwise plausible paths through the system?

6. **Evidence and controversy**
   - Which mechanistic claims are strongly supported by experiments?
   - Where does the literature disagree, rely on indirect evidence, or mix data
     from organisms that may not be comparable?
   - What are the most important open questions?

## Output Format

Use the style and structure of a concise review article:

1. Executive summary
2. Definition and biological boundaries
3. Mechanistic overview
4. Major molecular players and active assemblies
5. Evolutionary and cell-biological variation
6. Constraints, dependencies, and failure modes
7. Controversies and open questions
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty and avoid overgeneralizing from one organism, cell type, or assay
system to all biology.

## Output

# Gram-Negative Lipoprotein–Peptidoglycan Tether Remodeling: A Reversible Covalent Write/Erase Module

*A commissioned review-style synthesis*

---

## 1. Executive Summary

Gram-negative bacteria face a topological problem unique among cells: they must hold a lipid outer membrane (OM) tightly against a rigid, mesh-like peptidoglycan (PG) sacculus while still allowing that sacculus to grow, divide, and be enzymatically remodeled. In the Enterobacteriaceae and their close relatives, the most abundant and best-characterized solution to this problem is a **covalent tether**: Braun's lipoprotein (Lpp, the murein lipoprotein) is chemically bonded to the PG stem peptide. This review treats that tether, and the enzymes that make and break it, as a self-contained biological module — a **reversible, covalent write/erase system** connecting the OM to the sacculus.

The module has three defining features. First, its chemistry is a single **isopeptide amide bond** between the ε-amino group of Lpp's C-terminal lysine and the L-center carboxyl of **meso-diaminopimelic acid (meso-DAP)** at position 3 of a PG stem peptide (Braun & Bosch, [PMID: 4260278](https://pubmed.ncbi.nlm.nih.gov/4260278/)). Second, the "write" reaction is catalyzed by **ErfK-family L,D-transpeptidases** (ErfK/YbiS/YcfS, i.e., LdtA/B/C in *E. coli*), active-site-cysteine enzymes of the YkuD/Ldt superfamily that use a **tetrapeptide** PG donor and transfer its residue-3 acyl group onto the lipoprotein lysine. Third, the "erase" reaction is catalyzed by a **YafK/LdtF-family cysteine hydrolase** — the same enzyme independently discovered and named **LdtF** ([PMID: 33941679](https://pubmed.ncbi.nlm.nih.gov/33941679/)) and **DpaA** ([PMID: 33947763](https://pubmed.ncbi.nlm.nih.gov/33947763/)) in 2021 — which resolves the tether by hydrolysis, detaching Lpp from PG.

The central conceptual insight synthesized here is that **all reactions in this module are variations on one active-site-cysteine acyl-transfer chemistry**. An L,D-transpeptidase forms a thioester acyl-enzyme on the DAP3 carbonyl of a tetrapeptide donor; the acyl-enzyme is then resolved onto one of several acceptor amines — another stem's meso-DAP (yielding a 3→3 crosslink), the C-terminal lysine of Lpp (yielding the tether), or water (yielding hydrolysis/release). The tether module is therefore mechanistically continuous with 3→3 PG crosslinking but must be firmly distinguished from glycan-strand polymerization and from the D,D-transpeptidation of penicillin-binding proteins (PBPs). It is also just one of several parallel OM–sacculus attachment systems: many Gram-negative lineages lack Lpp entirely and instead tether the OM non-covalently through abundant β-barrel proteins or the universally distributed Pal–Tol system. The tether is thus best understood as an **enterobacterial specialization** built on a deeply conserved enzyme family and a conserved anchor point (meso-DAP), whose regulation and division-coupled timing remain the principal open questions.

---

## 2. Definition and Biological Boundaries

### 2.1 What is included

The system as scoped here comprises exactly four elements:

1. **The substrate lipoprotein** — Braun's lipoprotein (Lpp / murein lipoprotein), an OM-anchored lipoprotein delivered to the OM by the Lol pathway, bearing a free C-terminal lysine in the mature form (~57–58 aa mature).
2. **The covalent tether** — the isopeptide amide bond linking Lpp-Lys to meso-DAP(3) of a PG stem peptide.
3. **The "write" enzymes** — ErfK-family L,D-transpeptidases (ErfK/YbiS/YcfS = LdtA/B/C in *E. coli*) that form the tether.
4. **The "erase" enzyme** — a YafK/LdtF-family cysteine hydrolase (LdtF/DpaA) that cleaves the tether.

The core relationship is directional: **tether formation feeds tether hydrolysis.** The covalent bond created by the ErfK-family transpeptidase is the sole substrate for the YafK/LdtF-family hydrolase (Finding F007). This makes the module a genuine "cycle" — a write step and an erase step acting on the same chemical bond — rather than two unrelated activities.

| Step | Reaction | Enzyme family | Representative players (*E. coli*) |
|------|----------|---------------|-----------------------------------|
| Formation ("write") | Lpp-Lys ε-NH₂ + PG-tetrapeptide(→DAP³) → Lpp–meso-DAP amide + D-Ala | ErfK-family L,D-transpeptidase | ErfK/YbiS/YcfS (LdtA/B/C) |
| Release ("erase") | Lpp–meso-DAP amide + H₂O → free Lpp + PG | YafK/LdtF-family cysteine hydrolase | LdtF / DpaA (YafK) |

### 2.2 What is adjacent but should be treated separately

Several neighboring processes share molecular vocabulary with this module and are routinely conflated with it. The review deliberately excludes them:

- **Glycan-strand polymerization** (transglycosylation by PBP glycosyltransferase domains and by SEDS proteins) builds the sugar backbone of PG. It is upstream of, and mechanistically unrelated to, the tether.
- **Canonical 4→3 peptide crosslinking by PBP D,D-transpeptidases** is an active-site-**serine** chemistry that uses a **pentapeptide** donor and the energy of the D-Ala4–D-Ala5 bond. This is chemically and pharmacologically distinct from the active-site-**cysteine**, **tetrapeptide**-donor L,D chemistry of the tether module (Finding F004; [PMID: 16943188](https://pubmed.ncbi.nlm.nih.gov/16943188/)).
- **3→3 (DAP–DAP) crosslinking** by other Ldt-family paralogs (LdtD/YcbB, LdtE/YnhG in *E. coli*; the dominant chemistry in mycobacteria) is mechanistically the *closest neighbor* — it uses the same acyl-enzyme chemistry — but its acceptor is another PG stem, not a lipoprotein. It is a sibling reaction and the most common source of conflation, not part of the tether module per se.
- **Non-covalent OM–PG tethers** — Pal (peptidoglycan-associated lipoprotein) with the Tol system, OmpA, and OM β-barrel proteins — achieve the same *outcome* (OM–sacculus attachment) by different molecular means (Findings F003, F006). Only Lpp is covalent.
- **Amidase regulation during division** (AmiA/B/C activated by EnvC, NlpD, ActS) and the **Tol-Pal-driven OM invagination** at the septum are cell-division processes that intersect the envelope but are not part of the covalent tether cycle.

### 2.3 Competing definitions

Two terminological tensions recur and should be stated plainly:

1. **"L,D-transpeptidase" as a family vs. an activity.** ErfK/YbiS/YcfS are true transpeptidases (they form a new amide). LdtF/YafK/DpaA is classified in the same *sequence/structural* family but performs **hydrolysis**, not transpeptidation. Calling it an "L,D-transpeptidase paralog" is accurate phylogenetically but misleading mechanistically; "peptidoglycan–protein cross-link **hydrolase**" is the functionally correct descriptor.
2. **LdtF vs. DpaA.** The same *E. coli* gene (*yafK*) and enzyme was reported and named independently in 2021 by the Reddy group (**LdtF**; [PMID: 33941679](https://pubmed.ncbi.nlm.nih.gov/33941679/)) and the Vollmer group (**DpaA**; [PMID: 33947763](https://pubmed.ncbi.nlm.nih.gov/33947763/)). Readers should treat these as synonyms.

---

## 3. Mechanistic Overview

### 3.1 The bond and the anchor point

The foundational chemistry was established by Braun and Bosch in 1972 (Finding F001; [PMID: 4260278](https://pubmed.ncbi.nlm.nih.gov/4260278/)). Sequencing of murein-lipoprotein localized the PG linkage to Lpp's C-terminal **Lys-Tyr-Arg-Lys** motif, and the bond itself is an amide between the **ε-amino group of the C-terminal lysine** of Lpp and the **carboxyl group of the L-center of meso-diaminopimelic acid** (position 3 of the PG stem peptide). In the verbatim words of the primary paper: *"The linkage to the murein is formed between the epsilon-amino group of the C-terminal lysine and the carboxyl group of the optical L-center of meso-diaminopimelic acid."* Roughly one-third of Lpp molecules are in the bound (tethered) form at steady state, with the remainder free in the OM.

### 3.2 The unifying cysteine chemistry (write and erase converge here)

The mechanistic heart of the module is a single acyl-transfer chemistry shared across the whole Ldt/YkuD family (Finding F004). L,D-transpeptidases are **active-site-cysteine** enzymes that use **tetrapeptide** (not pentapeptide) donor stems. Cremniter, Arthur and colleagues showed that Ldt_fm *"uses the energy of the L-Lys(3)-D-Ala(4) peptide bond for cross-link formation in contrast to PBPs, which use the energy of the D-Ala(4)-D-Ala(5) bond"* ([PMID: 16943188](https://pubmed.ncbi.nlm.nih.gov/16943188/)). The catalytic cycle proceeds through a **thioester acyl-enzyme** and a rate-limiting **tetrahedral oxyanion intermediate** (Triboulet et al., [PMID: 23861815](https://pubmed.ncbi.nlm.nih.gov/23861815/)). Structural work on *M. tuberculosis* LdtMt2 demonstrated that carbapenem antibiotics acylate the catalytic cysteine (Cys-354), and that *"this adduct formation mimics the acylation of L,D-TP with the donor PG-stem"* ([PMID: 29524047](https://pubmed.ncbi.nlm.nih.gov/29524047/)) — i.e., the antibiotic hijacks the same first half-reaction the enzyme uses on its natural donor.

The elegance of the module is that the **first half-reaction is identical** across all family members, and only the **acceptor** differs:

```
                          ┌─────────────────────────────────────────┐
                          │   Common first half-reaction (all Ldts)  │
   Tetrapeptide donor ───▶│  Cys–S attacks DAP3 carbonyl; D-Ala4     │
   (…-meso-DAP3-D-Ala4)   │  leaves → THIOESTER ACYL-ENZYME          │
                          └──────────────────┬──────────────────────┘
                                             │ resolved by acceptor amine:
                    ┌────────────────────────┼─────────────────────────┐
                    ▼                        ▼                         ▼
        acceptor = meso-DAP        acceptor = Lpp C-term Lys   acceptor = water
          of another stem            (ε-NH2)                    (hydrolysis)
                    │                        │                         │
                    ▼                        ▼                         ▼
        3→3 DAP–DAP CROSSLINK     Lpp–PG TETHER (WRITE)       TETHER RELEASE (ERASE)
        (LdtD/YcbB, LdtE/YnhG)    (ErfK/YbiS/YcfS = LdtA/B/C) (LdtF/YafK = DpaA)
```

This single scheme explains why the "write" and "erase" enzymes are paralogs: they run the same first half-reaction and differ only in the second.

### 3.3 The system-level cycle

```
   Lol delivers mature Lpp to OM (free C-terminal Lys)
                 │
   ErfK / YbiS / YcfS  ── transpeptidation ──►  Lpp–mDAP covalent tether  (~1/3 of Lpp bound)
                 │                                        │
        (OM firmly anchored to sacculus)                  │
                 │                                        ▼
                 └────────────  LdtF / DpaA  ── hydrolysis ──►  free Lpp + intact PG
                                (release / editing)
```

### 3.4 Obligatory, conditional, and accessory steps

| Step | Status | Rationale |
|------|--------|-----------|
| Lol delivery of mature Lpp to OM with free C-terminal Lys | Obligatory prerequisite | The tether cannot form without a membrane-inserted substrate presenting the acceptor lysine |
| Availability of a tetrapeptide PG donor stem | Obligatory | Ldt enzymes cannot use pentapeptide donors ([PMID: 16943188](https://pubmed.ncbi.nlm.nih.gov/16943188/)) |
| ErfK-family transpeptidation (write) | Obligatory for tether existence | Sole route to the covalent bond |
| YafK/LdtF hydrolysis (erase) | Conditional/accessory | Needed for regulated release; not required to *form* the tether. Loss is tolerated but has phenotypes under OM stress |
| 3→3 crosslinking by LdtD/LdtE | Accessory sibling reaction | Same chemistry, different acceptor; not part of the tether per se |

---

## 4. Key Findings

### 4.1 The tether is a covalent isopeptide bond between Lpp's C-terminal lysine and meso-DAP (F001)

Braun & Bosch (1972; [PMID: 4260278](https://pubmed.ncbi.nlm.nih.gov/4260278/)) sequenced murein-lipoprotein and localized the murein linkage to the C-terminal Lys-Tyr-Arg-Lys motif. The bond is an amide between the ε-amino group of the C-terminal lysine and the L-center carboxyl of meso-diaminopimelic acid (position 3 of the PG stem peptide). Approximately one-third of Lpp molecules are in the bound form; Lpp is a small (~57–58 aa mature), trimeric α-helical OM lipoprotein whose N-terminal cysteine is triacylated and embedded in the OM inner leaflet. This finding directly defines the chemical nature and the exact atoms of the covalent tether, and it anchors the entire module: everything downstream is about writing and erasing this one amide bond.

### 4.2 Tether hydrolysis is carried out by a YafK/LdtF-family cysteine enzyme, discovered twice in 2021 (F002)

Bahadur, Chodisetti & Reddy (2021; [PMID: 33941679](https://pubmed.ncbi.nlm.nih.gov/33941679/)) reported that **LdtF**, a paralog of L,D-transpeptidases (*E. coli yafK*), cleaves Braun's lipoprotein Lpp from peptidoglycan. Independently, Winkle et al. (2021; [PMID: 33947763](https://pubmed.ncbi.nlm.nih.gov/33947763/)) named the same activity **DpaA** and showed it detaches Braun's lipoprotein from PG, framing the physiological stakes: *"The tight connection between the outer membrane and peptidoglycan is needed to maintain the outer membrane as an impermeable barrier for many toxic molecules and antibiotics."* Both papers identify the enzyme as the dedicated release ("editing") arm of the tether cycle — a YkuD-fold cysteine enzyme that has abandoned transpeptidation for hydrolysis.

### 4.3 Lpp anchoring is one of several parallel OM–sacculus tethers (F003)

Sandoz et al. (2021; [PMID: 33139883](https://pubmed.ncbi.nlm.nih.gov/33139883/)) showed that β-barrel proteins tether the OM in many Gram-negative bacteria that lack Lpp. Pal binds PG non-covalently via meso-DAP and, with the Tol system, coordinates OM invagination at the division septum: in *Waddlia*/Chlamydiales, *"peptidoglycan provides anchor points that connect the outer membrane to the peptidoglycan during constriction using the Pal-Tol complex"* ([PMID: 26364930](https://pubmed.ncbi.nlm.nih.gov/26364930/)); in *E. coli*, NlpD/Tol-Pal couples PG remodeling to OM invagination ([PMID: 28708841](https://pubmed.ncbi.nlm.nih.gov/28708841/)). Only Lpp is covalently attached; Pal, OmpA, and β-barrels tether non-covalently. This defines the boundary of the module and identifies the systems most often confused with it.

### 4.4 All reactions share one acyl-enzyme chemistry resolved onto different acceptors (F004)

L,D-transpeptidases exploit the energy of the residue3–D-Ala4 amide bond rather than the D-Ala4–D-Ala5 bond used by PBPs ([PMID: 16943188](https://pubmed.ncbi.nlm.nih.gov/16943188/)). Catalysis proceeds via a thioester acyl-enzyme and a tetrahedral oxyanion intermediate ([PMID: 23861815](https://pubmed.ncbi.nlm.nih.gov/23861815/)); structurally, carbapenem acylation of the catalytic Cys mimics acylation by the donor PG stem (LdtMt2 Cys-354; [PMID: 29524047](https://pubmed.ncbi.nlm.nih.gov/29524047/)). The acyl-enzyme is then resolved onto an acceptor amine — another stem's meso-DAP (3→3 crosslink), the ε-amine of Lpp's C-terminal Lys (tether formation), or water (LdtF/DpaA tether hydrolysis). This is the unifying mechanistic principle of the review.

### 4.5 The Ldt/YkuD family has expanded into non-redundant specialists (F005)

*E. coli* encodes ~6 YkuD-family paralogs (LdtA–F): three (ErfK/YbiS/YcfS = LdtA/B/C) anchor Lpp to PG, two (LdtD/YcbB, LdtE/YnhG) form 3→3 DAP–DAP crosslinks, and LdtF (YafK) hydrolyzes the Lpp tether. In *M. tuberculosis*, five LdtMt paralogs are non-redundant: Brammer Basta et al. (2015; [PMID: 26304120](https://pubmed.ncbi.nlm.nih.gov/26304120/)) concluded that *"LdtMt5 is not a functionally redundant ld-transpeptidase, but rather it serves a unique and important role in maintaining the integrity of the M. tuberculosis cell wall,"* and that *"the LdtMt5 active site has marked differences."* The transfer-competent anchoring/crosslinking transpeptidases are the best proxies for the ancestral acyl-transfer role; the hydrolase is a derived specialization.

### 4.6 The covalent module is an enterobacterial specialization with convergent alternatives (F006)

The covalently attached Braun lipoprotein and its ErfK-family anchoring transpeptidases characterize Enterobacteriaceae and close relatives; many Gram-negatives lack Lpp entirely. In such lineages (e.g., *Coxiella burnetii*), OM–PG tethering is achieved instead by abundant OM β-barrel proteins that bind PG non-covalently — *"Gram-negative bacteria have a cell envelope that comprises an outer membrane (OM), a peptidoglycan (PG) layer and an inner membrane (IM)"* ([PMID: 33139883](https://pubmed.ncbi.nlm.nih.gov/33139883/)) — and universally by the Pal–Tol system. Critically, *"diaminopimelic acid is an important determinant recruiting Pal to the division plane"* ([PMID: 26364930](https://pubmed.ncbi.nlm.nih.gov/26364930/)): meso-DAP is the shared conserved anchor point exploited by both covalent (Lpp) and non-covalent (Pal) routes.

### 4.7 Strict ordering and physical constraints (F007)

The reaction topology is directional: the ErfK-family transpeptidase must first create the Lpp(Lys)–meso-DAP amide, which is the sole substrate for YafK/LdtF-family hydrolysis. Both reactions occur in the periplasm on mature, membrane-inserted, Lol-delivered Lpp bearing a free C-terminal Lys, and require a tetrapeptide (D-Ala4-terminated) PG stem as the acyl donor — *"UDP-MurNAc-pentapeptide was extensively converted to UDP-MurNAc-tetrapeptide following hydrolysis of D-Ala(5)"* ([PMID: 16943188](https://pubmed.ncbi.nlm.nih.gov/16943188/)) confirms the tetrapeptide requirement. Because the acyl-enzyme forms at the DAP3 carbonyl, the same donor cannot simultaneously feed a 4→3 PBP crosslink at D-Ala4; and once Lpp is bound, only hydrolysis (LdtF/DpaA) or bulk PG turnover can release it.

---

## 5. Major Molecular Players and Active Assemblies

### 5.1 The *E. coli* YkuD-family paralog set

| Paralog | Alt. name | Function | Acceptor | Role in module |
|---------|-----------|----------|----------|----------------|
| LdtA | ErfK | Lpp anchoring L,D-transpeptidase | Lpp-Lys ε-NH2 | **Write** |
| LdtB | YbiS | Lpp anchoring L,D-transpeptidase | Lpp-Lys ε-NH2 | **Write** (often dominant anchor) |
| LdtC | YcfS | Lpp anchoring L,D-transpeptidase | Lpp-Lys ε-NH2 | **Write** |
| LdtD | YcbB | 3→3 DAP–DAP crosslinker | meso-DAP of another stem | Sibling reaction |
| LdtE | YnhG | 3→3 DAP–DAP crosslinker | meso-DAP of another stem | Sibling reaction |
| LdtF | YafK | Lpp–PG tether hydrolase (= DpaA) | water | **Erase** |

This layout illustrates a general principle: an ancient acyl-transfer enzyme family has expanded and specialized, so that superficially redundant paralogs in fact serve non-redundant roles. The three anchoring transpeptidases collectively "write" the tether (with functional redundancy providing robustness); the two 3→3 crosslinkers act on PG stems; and one paralog has been repurposed as a dedicated hydrolase.

### 5.2 The catalytic module (structural view)

Structures from the *M. tuberculosis* Ldt paralogs provide the best structural windows on the catalytic core, even though *M. tuberculosis* uses 3→3 crosslinking rather than lipoprotein anchoring. LdtMt1 was solved free and in complex with imipenem ([PMID: 23999293](https://pubmed.ncbi.nlm.nih.gov/23999293/)); LdtMt2 structures revealed the catalytic Cys-354 acyl chemistry and calcium-promoted dimerization ([PMID: 29524047](https://pubmed.ncbi.nlm.nih.gov/29524047/)); and molecular-dynamics studies described flap dynamics gating substrate access ([PMID: 28480928](https://pubmed.ncbi.nlm.nih.gov/28480928/)). QM/MM modeling has probed the catalytic role of active-site water in acylation ([PMID: 30514506](https://pubmed.ncbi.nlm.nih.gov/30514506/)) — directly relevant to understanding how the *same* chemistry can be resolved onto water (hydrolysis) versus an amine (transpeptidation). These are the best available structural proxies for the ErfK/LdtF domain, but they are *proxies* — direct structures of the enterobacterial anchoring enzymes and DpaA with physiological substrates are not yet in hand.

### 5.3 The parallel (non-covalent) tethering assemblies

The covalent module operates alongside, and in functional overlap with, several non-covalent OM–PG tethers: **Pal–Tol** (OM invagination at the division septum; meso-DAP-dependent; [PMID: 26364930](https://pubmed.ncbi.nlm.nih.gov/26364930/), [PMID: 28708841](https://pubmed.ncbi.nlm.nih.gov/28708841/)), **OM β-barrel proteins** ([PMID: 33139883](https://pubmed.ncbi.nlm.nih.gov/33139883/)), and **OmpA**. Notably, **meso-DAP is the shared anchor point** exploited by both covalent (Lpp) and non-covalent (Pal) routes — a convergence on the same PG determinant by different molecular means. The amidase/activator network (EnvC, NlpD, ActS; [PMID: 33660879](https://pubmed.ncbi.nlm.nih.gov/33660879/), [PMID: 28708841](https://pubmed.ncbi.nlm.nih.gov/28708841/)) is functionally coupled to envelope remodeling but is not part of the tether module.

---

## 6. Evolutionary and Cell-Biological Variation

### 6.1 Across lineages

The covalent Lpp tether is **not universal** among Gram-negatives; it is an **enterobacterial specialization** (Finding F006). Braun's lipoprotein and its ErfK-family anchoring transpeptidases characterize Enterobacteriaceae and close γ-proteobacterial relatives. Many Gram-negative lineages — including *Coxiella burnetii* and others — lack Lpp entirely and rely on OM β-barrel proteins that bind PG non-covalently ([PMID: 33139883](https://pubmed.ncbi.nlm.nih.gov/33139883/)), plus the near-universal Pal–Tol system ([PMID: 26364930](https://pubmed.ncbi.nlm.nih.gov/26364930/), [PMID: 28708841](https://pubmed.ncbi.nlm.nih.gov/28708841/)). The covalent write/erase module is therefore one evolutionary solution among several convergent routes to the same outcome, distinguished by being the only **covalent** one. The conserved element across all routes is the PG **meso-DAP** acceptor.

### 6.2 Paralog expansion and the "best representative" of the ancestral role

Where the Ldt/YkuD family has expanded, the paralogs are functionally specialized rather than redundant (Finding F005; [PMID: 26304120](https://pubmed.ncbi.nlm.nih.gov/26304120/)). For understanding the **ancestral acyl-transfer role**, the **transfer-competent (anchoring/crosslinking) transpeptidases are the best proxies**: they perform the complete two-half-reaction transfer, whereas the hydrolase paralog (LdtF/DpaA) represents a derived specialization in which the second half-reaction has been redirected to water. In this view, 3→3 crosslinking is plausibly the deep ancestral activity, lipoprotein anchoring a redeployment of the same chemistry onto a protein acceptor, and tether hydrolysis a late specialization.

### 6.3 Physiological states

The 3→3 L,D-transpeptidation pathway — the sibling of the tether chemistry — is famously **conditional and inducible** in some organisms. In *Enterococcus faecium*, bypass of PBPs by Ldt_fm confers β-lactam and glycopeptide cross-resistance, but only after regulatory reprogramming: production of the tetrapeptide substrate via the DdcRS two-component system and the D,D-carboxypeptidase DdcY ([PMID: 20025663](https://pubmed.ncbi.nlm.nih.gov/20025663/)), plus release of Ser/Thr phosphatase (StpA) control ([PMID: 25006233](https://pubmed.ncbi.nlm.nih.gov/25006233/)). Whole-genome analysis showed this cross-resistance requires many mutations remodeling regulatory circuits rather than the enzyme's substrate recognition ([PMID: 26077262](https://pubmed.ncbi.nlm.nih.gov/26077262/)). While these studies concern crosslinking rather than lipoprotein anchoring, they demonstrate that the availability of the **tetrapeptide donor** — the shared substrate constraint of the entire family — is a key regulated node generated by D,D-carboxypeptidase trimming. Bound Lpp appears at late stages of PG synthesis/maturation ([PMID: 7000765](https://pubmed.ncbi.nlm.nih.gov/7000765/)), and the *ldtF* mutant's phenotypes under impaired LPS transport (suppressed by loss of ActS; [PMID: 33660879](https://pubmed.ncbi.nlm.nih.gov/33660879/)) tie the erase enzyme's physiology to OM-biogenesis stress.

---

## 7. Constraints, Dependencies, and Failure Modes

Several hard constraints govern the module (Finding F007):

1. **Obligate ordering — write before erase.** Tether hydrolysis is strictly downstream of tether formation; the hydrolase has no substrate until a tether exists.
2. **Compartment specificity.** Both reactions occur in the **periplasm**, on mature, membrane-inserted, **Lol-delivered** Lpp bearing a free C-terminal lysine. Neither reaction can occur before Lpp translocation and OM insertion, nor on nascent lipid-II.
3. **Substrate specificity — tetrapeptide donor only.** Ldt-family enzymes require a **tetrapeptide (D-Ala4-terminated)** PG stem; pentapeptide stems are excluded ([PMID: 16943188](https://pubmed.ncbi.nlm.nih.gov/16943188/)). This couples tether formation to prior D,D-carboxypeptidase trimming.
4. **Positional mutual exclusivity.** Because the acyl-enzyme forms at the **DAP3 carbonyl**, a stem committed to Lpp anchoring (or a 3→3 crosslink) cannot simultaneously feed a **4→3 PBP crosslink** at D-Ala4. The two chemistries compete for related stems and are chemically incompatible on a single donor.
5. **Release routes.** Once Lpp is bound, only **hydrolysis by LdtF/DpaA** or bulk **PG turnover** can free it. There is no spontaneous reversal.

**What is ruled out:** hydrolysis preceding formation; anchoring on pentapeptide donors; and remodeling of the non-covalent tethers (Pal, OmpA, β-barrels) by ErfK/LdtF enzymes — those lie outside the enzymes' chemistry.

**Failure modes:**
- **Loss of write enzymes (ErfK/YbiS/YcfS):** reduced/abolished covalent Lpp attachment; the OM becomes loosely coupled to PG, degrading the OM permeability barrier and promoting OM instability/vesiculation (the maintained barrier depends on a tight OM–PG connection; [PMID: 33947763](https://pubmed.ncbi.nlm.nih.gov/33947763/)).
- **Loss of the erase enzyme (LdtF/DpaA):** inability to release the tether; phenotypes emerge specifically under OM-biogenesis stress (e.g., impaired LPS export), with suppression by loss of ActS linking this to amidase-regulated PG remodeling ([PMID: 33660879](https://pubmed.ncbi.nlm.nih.gov/33660879/)).
- **Donor shortage (no tetrapeptide):** if D,D-carboxypeptidase activity is insufficient, the tether cannot be written even with functional transpeptidases.

---

## 8. Controversies and Open Questions

**Strongly supported claims.** The bond chemistry ([PMID: 4260278](https://pubmed.ncbi.nlm.nih.gov/4260278/)); the identity of the write enzymes as ErfK-family L,D-transpeptidases; the identity of the erase enzyme as a YafK/LdtF-family cysteine hydrolase (independently confirmed by two groups in 2021; [PMID: 33941679](https://pubmed.ncbi.nlm.nih.gov/33941679/), [PMID: 33947763](https://pubmed.ncbi.nlm.nih.gov/33947763/)); the tetrapeptide-donor/active-site-cysteine/acyl-enzyme mechanism ([PMID: 16943188](https://pubmed.ncbi.nlm.nih.gov/16943188/), [PMID: 23861815](https://pubmed.ncbi.nlm.nih.gov/23861815/), [PMID: 29524047](https://pubmed.ncbi.nlm.nih.gov/29524047/)); and the existence of parallel non-covalent tethers ([PMID: 33139883](https://pubmed.ncbi.nlm.nih.gov/33139883/)) are all well established.

**Areas of uncertainty and mixed evidence:**

1. **Nomenclature and enzyme class.** LdtF = DpaA (same *yafK* product), and it is a **hydrolase**, not a transpeptidase, despite being an "Ldt paralog." The field should converge on a functionally accurate name.
2. **Regulation and timing of release.** The single largest gap is *when* and *why* LdtF/DpaA hydrolyzes the tether in vivo. Is release constitutive, division-coupled (septal OM invagination with Tol–Pal), stress-induced, or spatially localized? Current evidence is largely genetic and indirect.
3. **Division-coupled localization.** Whether the covalent tether is actively "erased" ahead of the constricting septum to permit OM invagination — and whether DpaA is recruited there — is unresolved.
4. **Division of labor among ErfK/YbiS/YcfS.** Their quantitative contributions, substrate preferences (other Lpp-like proteins?), and conditional expression across growth states are incompletely mapped.
5. **Cross-organism extrapolation.** Much mechanistic/structural detail derives from *M. tuberculosis* and *E. faecium* Ldts that predominantly do **3→3 crosslinking**, not lipoprotein anchoring. Generalizing catalytic parameters to the enterobacterial anchoring transpeptidases and to DpaA should be done cautiously; the acceptor chemistry differs.
6. **Structural basis of acceptor discrimination.** What determines whether an Ldt paralog resolves its acyl-enzyme onto a PG stem's meso-DAP, onto Lpp-Lys, or onto water? Active-site and flap differences among paralogs ([PMID: 26304120](https://pubmed.ncbi.nlm.nih.gov/26304120/), [PMID: 28480928](https://pubmed.ncbi.nlm.nih.gov/28480928/)) are suggestive but not decisive.
7. **Substrate scope of the hydrolase.** Whether YafK/LdtF-type hydrolases act only on Lpp or on a broader set of PG-anchored proteins is open.

---

## 9. Evidence Base

| PMID | Short title | Role in this review |
|------|-------------|---------------------|
| [4260278](https://pubmed.ncbi.nlm.nih.gov/4260278/) | Repetitive sequences in murein-lipoprotein of *E. coli* | Defines the Lpp-Lys ↔ meso-DAP isopeptide bond (F001) |
| [33941679](https://pubmed.ncbi.nlm.nih.gov/33941679/) | Cleavage of Lpp from PG by LdtF | Identifies the erase enzyme (F002) |
| [33947763](https://pubmed.ncbi.nlm.nih.gov/33947763/) | DpaA detaches Braun's lipoprotein from PG | Independent identification of the erase enzyme; OM-barrier rationale (F002) |
| [33139883](https://pubmed.ncbi.nlm.nih.gov/33139883/) | β-Barrel proteins tether the OM in many Gram-negatives | Establishes non-covalent alternative tethers (F003, F006) |
| [26364930](https://pubmed.ncbi.nlm.nih.gov/26364930/) | Disassembly of a medial transenvelope structure | Pal–Tol as distinct non-covalent tether; meso-DAP anchor (F003, F006) |
| [28708841](https://pubmed.ncbi.nlm.nih.gov/28708841/) | NlpD links cell-wall remodeling and OM invagination | Division-coupled non-covalent tethering (F003, F006) |
| [16943188](https://pubmed.ncbi.nlm.nih.gov/16943188/) | Novel resistance mechanism in *E. faecium* (Ldt_fm) | Tetrapeptide-donor/cysteine chemistry; donor constraint (F004, F007) |
| [23861815](https://pubmed.ncbi.nlm.nih.gov/23861815/) | Kinetics of L,D-transpeptidase inactivation | Thioester acyl-enzyme and oxyanion intermediate (F004) |
| [29524047](https://pubmed.ncbi.nlm.nih.gov/29524047/) | Structure of LdtMt2 | Catalytic Cys acyl-enzyme mimics donor PG-stem acylation (F004) |
| [26304120](https://pubmed.ncbi.nlm.nih.gov/26304120/) | LdtMt5 functionally/structurally distinct | Paralog specialization after family expansion (F005) |
| [23999293](https://pubmed.ncbi.nlm.nih.gov/23999293/) | Structures of LdtMt1 | Structural view of catalytic core; carbapenem inhibition |
| [28480928](https://pubmed.ncbi.nlm.nih.gov/28480928/) | Flap dynamics in LdtMt2 | Substrate-access gating |
| [30514506](https://pubmed.ncbi.nlm.nih.gov/30514506/) | QM/MM of LdtMt2 acylation | Catalytic role of active-site water in deacylation |
| [33660879](https://pubmed.ncbi.nlm.nih.gov/33660879/) | ActS activates amidases during OM stress | Links *ldtF* physiology to envelope stress |
| [20025663](https://pubmed.ncbi.nlm.nih.gov/20025663/) | Activation of L,D-transpeptidation by DdcY | Regulated tetrapeptide-donor production |
| [25006233](https://pubmed.ncbi.nlm.nih.gov/25006233/) | Ser/Thr phosphatase control of Ldt pathway | Regulatory reprogramming of the pathway |
| [26077262](https://pubmed.ncbi.nlm.nih.gov/26077262/) | Mutation landscape of cross-resistance | Circuit-level regulation of Ldt activation |
| [7000765](https://pubmed.ncbi.nlm.nih.gov/7000765/) | Soluble nascent PG in growing *E. coli* | Lpp attachment as a late PG-synthesis event |
| [29575515](https://pubmed.ncbi.nlm.nih.gov/29575515/) | RTX-adhesin OM anchoring | Contrasting OM-anchoring strategy |

---

## 10. Limitations and Knowledge Gaps

This synthesis is a literature-based review drawing on 19 papers; it did not include new experimental or sequence-analytic data generation. Several structural and mechanistic claims about the anchoring and hydrolase reactions are inferred by analogy from 3→3-crosslinking Ldts in *M. tuberculosis* and *E. faecium*, because those are the systems where high-resolution structures and detailed kinetics exist — a genuine caveat, since those enzymes predominantly perform a different second half-reaction. The phylogenetic distribution of Lpp and its anchoring enzymes is described at the level of "enterobacterial specialization" with specific counterexamples (e.g., *Coxiella*), but a systematic comparative-genomic census across Gram-negative phyla was not performed. The regulation of tether release is described qualitatively because the primary literature itself provides mostly genetic and phenotypic — rather than direct temporal/spatial — data. Quantitative bound-Lpp figures follow the classical *E. coli* accounting and may vary with strain and physiological state.

---

## 11. Proposed Follow-up Experiments and Actions

1. **Temporal/spatial imaging of release.** Fluorescently tag DpaA/LdtF and Lpp; use time-lapse and super-resolution microscopy to test whether tether erasure localizes to and precedes the constricting septum, directly testing the division-coupling hypothesis.
2. **Structural capture of acceptor selection.** Solve structures (or predict with AlphaFold-Multimer, then validate) of an enterobacterial anchoring transpeptidase (e.g., YbiS/LdtB) with a lipoprotein-mimicking acceptor peptide, and of DpaA with a tether-substrate analog, to define the determinants of amine-vs-water resolution.
3. **Comparative-genomic census.** Systematically map co-occurrence of Lpp, ErfK-family anchoring transpeptidases, LdtF/DpaA, β-barrel tethers, and Pal–Tol across Gram-negative phyla to sharpen the "enterobacterial specialization vs. convergent alternatives" claim.
4. **Quantitative flux of the bound/free Lpp pool.** Use pulse-chase and quantitative mass spectrometry across growth phases, division, and OM/LPS stress to measure how the ~1/3 bound fraction changes, and which enzymes (write vs. erase) drive the change.
5. **Genetic epistasis under stress.** Extend the *ldtF*/ActS interaction ([PMID: 33660879](https://pubmed.ncbi.nlm.nih.gov/33660879/)) with systematic double mutants across write enzymes, the erase enzyme, amidase activators, and Tol-Pal components to place tether remodeling in the envelope-stress regulatory network.
6. **Donor-availability perturbation.** Manipulate D,D-carboxypeptidase (e.g., PBP5) activity to modulate the tetrapeptide donor pool and quantify the effect on tether formation, testing the substrate-supply constraint in vivo.

---

*Prepared as a commissioned review synthesis. Claims are anchored to the cited primary literature; uncertainty is flagged explicitly where mechanistic detail is extrapolated across organisms (notably from 3→3-crosslinking Ldts of* M. tuberculosis *and* E. faecium *to the enterobacterial lipoprotein-anchoring transpeptidases and the DpaA/LdtF hydrolase).*


## Artifacts

- [OpenScientist final report](gram_negative_lipoprotein_peptidoglycan_tether_remodeling-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](gram_negative_lipoprotein_peptidoglycan_tether_remodeling-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:4260278
2. PMID:33941679
3. PMID:33947763
4. PMID:16943188
5. PMID:23861815
6. PMID:29524047
7. PMID:33139883
8. PMID:26364930
9. PMID:28708841
10. PMID:26304120
11. PMID:23999293
12. PMID:28480928
13. PMID:30514506
14. PMID:33660879
15. PMID:20025663
16. PMID:25006233
17. PMID:26077262
18. PMID:7000765