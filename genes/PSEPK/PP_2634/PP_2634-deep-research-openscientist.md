---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T15:53:30.960083'
end_time: '2026-07-11T16:04:42.588422'
duration_seconds: 671.63
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_2634
  gene_symbol: PP_2634
  uniprot_accession: Q88JL5
  protein_description: 'SubName: Full=Cellulose synthase {ECO:0000313|EMBL:AAN68242.1};'
  gene_info: OrderedLocusNames=PP_2634 {ECO:0000313|EMBL:AAN68242.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Cellulose_synthase_operon_BcsQ. (IPR017746); P-loop_NTPase. (IPR027417);
    CBP_BcsQ (PF06564)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_2634-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_2634-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88JL5
- **Protein Description:** SubName: Full=Cellulose synthase {ECO:0000313|EMBL:AAN68242.1};
- **Gene Information:** OrderedLocusNames=PP_2634 {ECO:0000313|EMBL:AAN68242.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Cellulose_synthase_operon_BcsQ. (IPR017746); P-loop_NTPase. (IPR027417); CBP_BcsQ (PF06564)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_2634" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_2634' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_2634** (gene ID: PP_2634, UniProt: Q88JL5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PP_2634 (Q88JL5) in *Pseudomonas putida* KT2440: Functional Annotation Report

## ⚠️ Identity Correction (Read First)

The UniProt entry Q88JL5 carries the automatically generated SubName **"Cellulose synthase"** (evidence code ECO:0000313, derived from EMBL AAN68242.1). **This is a mis-annotation.** PP_2634 is **not** the catalytic cellulose synthase. Based on its domain architecture, its position in the *bcs* operon, and a well-characterized orthology relationship to enterobacterial proteins, PP_2634 is **BcsQ**, an accessory **MinD/ParA-family P-loop ATPase** that organizes and spatially positions the bacterial cellulose-secretion machine. Cellulose polymerization itself is carried out by the neighboring genes PP_2635/PP_2636 (BcsA/BcsB). This report describes PP_2634 in its correct role.

The organism (*Pseudomonas putida* strain KT2440, PSEPK) and the domains listed in the brief — **Cellulose_synthase_operon_BcsQ (IPR017746)**, **P-loop_NTPase (IPR027417)**, and **CBP_BcsQ (PF06564)** — are fully consistent with the BcsQ assignment. Literature for BcsQ (in *E. coli* and in *P. putida* itself) is directly applicable. This is **not** a case of an ambiguous symbol pointing to an unrelated gene; it is a case of a database display-name lagging behind the functional literature.

---

## Summary

**PP_2634 (Q88JL5) is BcsQ, a MinD/ParA-family ATPase that acts as the spatial organizer and assembly regulator of the bacterial cellulose synthesis (Bcs) secretion system — it is not the polysaccharide-polymerizing enzyme.** The 235-residue protein has a P-loop NTPase fold with an N-terminal deviant Walker A motif characteristic of the MinD/ParA subfamily of partition ATPases. It is encoded at the head of the *bcs* operon in *P. putida* KT2440, immediately upstream of the genes for the true catalytic core (BcsA/BcsB, the GT-2 glycosyltransferase synthase and its membrane partner) and the outer-membrane translocon (BcsC).

Functionally, BcsQ is **essential for cellulose biosynthesis** and works by **restricting the active secretion machinery to a defined subcellular location**. In the enterobacterial paradigm (*E. coli*), deletion of *bcsQ* (formerly *yhjQ*) abolishes cellulose production, and BcsQ localizes to the bacterial cell pole where cellulose is deposited, seeding cell-to-cell adhesion. Cryo-EM structures of the assembled system place BcsQ, together with BcsR, as a **cytosolic regulatory subcomplex on the inner-membrane face** of the larger BcsRQABEFG–BcsC macrocomplex, where it participates in ATP-dependent and c-di-GMP-responsive regulation.

In *P. putida* specifically, the *bcs* operon that contains PP_2634 is a **functional, physiologically active cellulose system**. Its transcription is embedded in the c-di-GMP-controlled motility-to-biofilm switch: the operon is repressed by the master regulator FleQ (with its antagonist FleN) and derepressed by the second messenger c-di-GMP. The cellulose the system produces contributes to biofilm matrix cohesion and rhizosphere colonization, and its expression is strongly induced under water/osmotic stress. Thus PP_2634/BcsQ is best understood as a **cytoplasmic, inner-membrane-associated positioning/assembly ATPase** operating within the biofilm-promoting exopolysaccharide program of *P. putida*.

---

## Gene / Protein Identity

| Attribute | Value |
|---|---|
| Locus | PP_2634 (OrderedLocusName) |
| UniProt | Q88JL5 (235 aa; reference proteome) |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125), PSEPK |
| Domains | IPR017746 Cellulose_synthase_operon_BcsQ; IPR027417 P-loop NTPase; Pfam PF06564 CBP_BcsQ |
| Family | ParA/MinD subfamily of deviant-Walker-A P-loop ATPases |
| Correct name | **BcsQ** (bacterial cellulose synthesis subunit Q) |
| KEGG | ppu:PP_2634 |

---

## Key Findings

### Finding 1 — PP_2634 is BcsQ, a MinD/ParA ATPase, not the catalytic cellulose synthase

The primary conclusion of this investigation is an identity correction. UniProt Q88JL5 is a short (235 aa) protein whose InterPro/Pfam signatures are diagnostic: **IPR017746 (Cellulose_synthase_operon_BcsQ)**, **IPR027417 (P-loop NTPase)**, and **Pfam PF06564 (CBP_BcsQ)**. Critically, the protein carries **no GT-2 glycosyltransferase domain** — the domain that actually builds the β-1,4-glucan chain. Instead, its N-terminal **deviant Walker A P-loop motif** (~residues 10–15) is the hallmark of the **MinD/ParA subfamily** of partition/positioning ATPases, which use a "deviant" variant of the canonical GxxxxGKT nucleotide-binding loop.

The gene-neighborhood context independently confirms this. In *P. putida* KT2440, PP_2634 sits immediately upstream of PP_2635/PP_2636, annotated as the "cellulose synthase and translocator subunits" (**BcsA/BcsB**), and PP_2638 (**BcsC**, the outer-membrane porin). This arrangement mirrors the enterobacterial `yhjQ(bcsQ) → bcsAB` operon organization. The catalytic reaction — polymerization of UDP-glucose into β-1,4-glucan (cellulose) — is performed by BcsA/BcsB, which are *"necessary and sufficient for the formation of the polysaccharide chain in vitro"* ([PMID: 26077867](https://pubmed.ncbi.nlm.nih.gov/26077867/)). BcsQ is therefore an **accessory subunit**, and the UniProt "Cellulose synthase" SubName — flagged with the automated ECO:0000313 evidence code — is an EMBL-derived electronic mis-annotation.

The MinD-family identity of BcsQ is established experimentally: *"we demonstrate that BcsQ, a MinD homologue, displays a polar localization"* ([PMID: 19400787](https://pubmed.ncbi.nlm.nih.gov/19400787/)).

### Finding 2 — BcsQ is essential for cellulose biosynthesis and spatially restricts synthesis to the cell pole

BcsQ is not a passive structural filler; it is genetically required for cellulose production. In *E. coli*, targeted deletion analysis showed that *"yhjQ, but not yhjR, is essential for cellulose biosynthesis; it has therefore been renamed bcsQ"* ([PMID: 19400787](https://pubmed.ncbi.nlm.nih.gov/19400787/)). The neighboring gene *yhjR* was dispensable, isolating the essential function to *bcsQ* specifically.

The mechanism of that essential role is **spatial**. A GFP–BcsQ fusion localizes to the bacterial **cell pole**, and immunogold labelling detected cellulose being produced at the same BcsQ-marked pole, initiating cell-to-cell adhesion. This is precisely the behavior expected of a MinD/ParA-family ATPase, whose defining biochemical activity is establishing and reading out subcellular position gradients. The authors concluded that *"these results therefore suggest that BcsQ could participate in spatial restriction of cellulose biosynthesis activity in Enterobacteriaceae"* ([PMID: 19400787](https://pubmed.ncbi.nlm.nih.gov/19400787/)). BcsQ thus behaves as a **positioning device** that concentrates the secretion apparatus at a defined site so cellulose fibers are extruded in a coordinated, adhesion-competent manner rather than dispersed randomly around the cell surface.

### Finding 3 — BcsQ is an inner-membrane-associated cytosolic subunit of the Bcs macrocomplex with ATP-dependent regulatory function

High-resolution structural biology places BcsQ precisely within the assembled machine. Cryo-EM of the *E. coli* Bcs secretion system revealed a macrocomplex with stoichiometry **BcsRQABEFG** plus the outer-membrane porin **BcsC**. Within this assembly, **BcsR and BcsQ form a regulatory subcomplex on the cytosolic face of the inner membrane**. The structural work reported *"unexpected subunit stoichiometry, multisite c-di-GMP recognition, and ATP-dependent regulation"* ([PMID: 33563593](https://pubmed.ncbi.nlm.nih.gov/33563593/)), and a later study confirmed that *"the biogenesis of phosphoethanolamine (pEtN)-modified cellulose relies on the BcsRQABEFG macrocomplex, encompassing inner-membrane and cytosolic subunits, and an outer membrane porin, BcsC"* ([PMID: 39394223](https://pubmed.ncbi.nlm.nih.gov/39394223/)).

These data are consistent with BcsQ being an **ATP-binding ParA/MinD-family subunit** that modulates the assembly and activation state of the system from the cytoplasmic side. Its ATPase cycle (nucleotide binding at the deviant Walker A P-loop) is the presumptive engine that couples positional information to machine assembly, while c-di-GMP sensing by adjacent subunits gates catalytic activity. BcsQ therefore sits at the interface of **spatial control** (via its ParA/MinD activity) and **signaling control** (via the c-di-GMP-responsive macrocomplex).

### Finding 4 — The *P. putida bcs* operon (containing PP_2634/bcsQ) is controlled by FleQ/FleN and c-di-GMP

Bringing the analysis back to the target organism: in *P. putida* KT2440, transcription of the *bcs* operon (driven from the *PbcsD* promoter) is embedded in the central c-di-GMP regulatory circuit. It is *"negatively regulated by FleQ and FleN, and repression was antagonized by c-di-GMP"* ([PMID: 30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/)). FleQ is the master transcriptional regulator of flagellar and biofilm genes; FleN is its ATPase antagonist. High intracellular c-di-GMP — the signal that drives the motile-to-sessile lifestyle transition — relieves FleQ/FleN repression and turns on the cellulose machinery.

This places PP_2634/BcsQ firmly within the **motility-to-biofilm switch**: expression of the cellulose apparatus, including its BcsQ organizer, is switched on precisely when the cell commits to a surface-attached, matrix-producing lifestyle. This is direct *P. putida* evidence (not merely extrapolation from *E. coli*) that the operon containing PP_2634 is a bona fide, regulated component of biofilm physiology.

### Finding 5 — The *P. putida bcs* cluster produces cellulose that contributes to biofilm stability and rhizosphere colonization

Finally, the *bcs* cluster in *P. putida* is a **functional cellulose-producing system**, not just a bioinformatic prediction. Functional characterization in *P. putida* mt-2 showed that *"Bcs plays a minor role in biofilm formation and stability, although it does contribute to rhizosphere colonization based on a competition assay"* ([PMID: 21507177](https://pubmed.ncbi.nlm.nih.gov/21507177/)). The same study found that the system is stress-responsive: *"both forms of water stress highly induced bcs expression"* ([PMID: 21507177](https://pubmed.ncbi.nlm.nih.gov/21507177/)).

The physiological picture is therefore that the cellulose produced by the BcsQ-organized machine supports **biofilm matrix cohesion** and provides a **competitive fitness advantage in the rhizosphere**, particularly under water-limiting/osmotic stress. BcsQ contributes to this outcome by ensuring the secretion machinery is correctly positioned and assembled so cellulose can be exported efficiently.

---

## Mechanistic Model / Interpretation

The *bcs* operon in *P. putida* KT2440 encodes a multi-subunit **cellulose secretion system** that spans both membranes. PP_2634/BcsQ is the cytoplasmic **positioning-and-assembly ATPase** at its head.

### Operon and machine architecture (KEGG neighborhood)

```
   P. putida KT2440 bcs locus (schematic)

   PP_2634        PP_2635 / PP_2636         PP_2637   PP_2638
   ┌──────┐      ┌──────────────────┐      ┌──────┐  ┌────────┐
   │ bcsQ │─────▶│  bcsA  │  bcsB   │─────▶│ bcsZ │─▶│  bcsC  │
   │(ParA/│      │(GT-2   │(peri-   │      │(gluc │  │(OM     │
   │ MinD)│      │ synth.)│ plasmic)│      │ anase│  │ porin) │
   └──────┘      └──────────────────┘      └──────┘  └────────┘
   POSITIONING     CATALYSIS + IM                     EXPORT across
   / ASSEMBLY      TRANSLOCATION                       outer membrane
```

### Assembled macrocomplex (enterobacterial paradigm, PMID 33563593 / 39394223)

```
  OUTER MEMBRANE   ═══════════ BcsC porin ═══════════
                                   │  (glucan chain export)
  PERIPLASM                      BcsB / BcsEFG
                                   │
  INNER MEMBRANE   ───── BcsA (GT-2 synthase) ─────
                          │  ▲ c-di-GMP gating
  CYTOPLASM          ┌────┴─────┐
                     │ BcsR–BcsQ│  ← PP_2634 = BcsQ
                     │regulatory│    ATP-dependent
                     │subcomplex│    positioning/assembly
                     └──────────┘
     Stoichiometry: BcsR Q A B E F G  +  BcsC
```

### Signaling context (P. putida, PMID 30889223 / 21507177)

```
  Motile lifestyle  ──(low c-di-GMP)──▶ FleQ/FleN REPRESS PbcsD ──▶ bcs OFF
                                                 │
        rising c-di-GMP (surface sensing, stress)│ antagonizes repression
                                                 ▼
  Sessile / biofilm ─(high c-di-GMP)──▶ PbcsD DEREPRESSED ──▶ bcs ON
                                                 │
                                                 ▼
                       BcsQ-organized machine extrudes cellulose
                                                 │
                                                 ▼
             Biofilm matrix cohesion + rhizosphere colonization
                      (esp. under water/osmotic stress)
```

**Integrated narrative.** When *P. putida* senses conditions favoring a sessile lifestyle (surface contact, osmotic/water stress), intracellular c-di-GMP rises and derepresses the *bcs* operon by antagonizing FleQ/FleN. The operon's first product, **BcsQ (PP_2634)**, uses its ParA/MinD ATPase activity to establish a subcellular position and nucleate assembly of the secretion machine on the cytoplasmic face of the inner membrane, together with BcsR. This positioned scaffold enables the catalytic **BcsA/BcsB** core to polymerize UDP-glucose into β-1,4-glucan and translocate it across the inner membrane, with the chain finally exported through the **BcsC** porin. The resulting extracellular cellulose reinforces the biofilm matrix and enhances competitive colonization of the plant rhizosphere. BcsQ's role is thus **organizational and regulatory** — it does not make the polymer, it ensures the polymer-making machine is in the right place, correctly assembled, and responsive to the cell's ATP and c-di-GMP status.

### Function-at-a-glance table

| Attribute | Assignment for PP_2634 / BcsQ |
|---|---|
| **True identity** | BcsQ — MinD/ParA-family P-loop ATPase (accessory subunit) |
| **NOT** | The catalytic cellulose synthase (that is BcsA/BcsB = PP_2635/PP_2636) |
| **Primary molecular function** | ATP-dependent spatial positioning + assembly of the Bcs secretion machine |
| **Reaction "catalyzed"** | ATP hydrolysis (ParA/MinD-type); no glycosyltransferase activity |
| **Localization** | Cytoplasmic face of the inner membrane; polar in enterobacteria |
| **Complex** | Cytosolic BcsR–BcsQ regulatory subcomplex within BcsRQABEFG–BcsC |
| **Pathway** | Bacterial cellulose (bcs) biosynthesis / biofilm exopolysaccharide program |
| **Upstream regulation (P. putida)** | c-di-GMP derepresses PbcsD by antagonizing FleQ/FleN |
| **Physiological output** | Cellulose → biofilm cohesion, rhizosphere colonization, water-stress fitness |
| **Domains** | IPR017746 (BcsQ), IPR027417 (P-loop NTPase), PF06564 (CBP_BcsQ) |

### Supported and refuted hypotheses

| Hypothesis | Verdict | Basis |
|---|---|---|
| PP_2634 catalyzes cellulose synthesis (UDP-glucose → glucan) | **Refuted** | No GT-2 domain; catalysis is by BcsA/BcsB (PP_2635/6). |
| PP_2634 = BcsQ, a ParA/MinD ATPase of the *bcs* operon | **Supported** | IPR017746 + PF06564 + deviant Walker A + operon position upstream of *bcsAB*. |
| BcsQ is required for cellulose production and spatially organizes the machinery | **Supported** | Le Quéré & Ghigo 2009 (Δ*bcsQ* abolishes cellulose; polar GFP–BcsQ). |
| BcsQ is a cytosolic inner-membrane subunit of an ATP/c-di-GMP-regulated macrocomplex | **Supported** | Abidi 2021; Anso 2024 (BcsRQABEFG cryo-EM). |
| *P. putida bcs* operon is c-di-GMP/FleQ-regulated | **Supported** | Navarrete 2019. |

---

## Evidence Base

| PMID | Title | How it supports the annotation |
|---|---|---|
| [19400787](https://pubmed.ncbi.nlm.nih.gov/19400787/) | *BcsQ is an essential component of the E. coli cellulose biosynthesis apparatus that localizes at the bacterial cell pole.* | **Core primary reference.** Establishes BcsQ as a MinD homologue, shows *bcsQ* (not *yhjR*) is essential for cellulose, demonstrates polar localization and spatial restriction of synthesis. |
| [26077867](https://pubmed.ncbi.nlm.nih.gov/26077867/) | *Bacterial cellulose biosynthesis: diversity of operons, subunits, products, and functions.* | Authoritative review; confirms BcsA/BcsB are necessary and sufficient for the catalytic step in vitro — so BcsQ is accessory, not the synthase. |
| [33563593](https://pubmed.ncbi.nlm.nih.gov/33563593/) | *Architecture and regulation of an enterobacterial cellulose secretion system.* | Cryo-EM; defines BcsRQABEFG stoichiometry, places BcsR–BcsQ as a cytosolic regulatory subcomplex, reports ATP-dependent and multisite c-di-GMP regulation. |
| [39394223](https://pubmed.ncbi.nlm.nih.gov/39394223/) | *Structural basis for synthase activation and cellulose modification in the E. coli Type II Bcs secretion system.* | Confirms macrocomplex composition (BcsRQABEFG + BcsC) with inner-membrane and cytosolic subunits including BcsQ. |
| [30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/) | *Transcriptional organization, regulation and functional analysis of flhF and fleN in Pseudomonas putida.* | **P. putida-specific.** Shows PbcsD (the bcs operon promoter) is repressed by FleQ/FleN and derepressed by c-di-GMP. |
| [21507177](https://pubmed.ncbi.nlm.nih.gov/21507177/) | *Cell-cell and cell-surface interactions mediated by cellulose ... contribute to P. putida biofilm formation and fitness under water-limiting conditions.* | **P. putida-specific.** Functionally validates the bcs cellulose system: biofilm role, rhizosphere colonization, strong induction under water stress. |

**Consistency of the evidence.** All six references converge on the same model. The two *E. coli* structural/genetic papers (19400787, 33563593, 39394223) define BcsQ's molecular role; the review (26077867) confirms the division of labor (BcsA/BcsB catalyze, BcsQ organizes); and the two *P. putida* papers (30889223, 21507177) confirm that the operon containing PP_2634 is a real, regulated, physiologically relevant cellulose system in the exact target organism. No reference contradicts the BcsQ assignment or supports the "cellulose synthase" display name.

---

## Localization

- **Subcellular site:** cytoplasmic face of the **inner (cytoplasmic) membrane**, associated with the Bcs synthase complex; BcsQ is a cytosolic/peripheral subunit (the BcsR–BcsQ subcomplex).
- **Spatial pattern:** polar localization in enterobacteria, marking the site of active cellulose secretion.
- **Product destination:** the machine it helps organize exports β-1,4-glucan (cellulose) across the envelope (via BcsB translocation and the BcsC porin) to the **cell surface / extracellular biofilm matrix**.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of *P. putida* BcsQ itself.** The essentiality, polar localization, and ATPase inferences come primarily from *E. coli* orthologs. While *P. putida bcs* function is validated at the operon level (21507177) and its transcriptional regulation is *P. putida*-specific (30889223), a *P. putida* PP_2634 deletion/localization/ATPase study has not been reviewed here. The functional transfer relies on strong orthology and conserved operon synteny — robust, but not a direct in-vivo study of this specific protein.

2. **ATPase activity is inferred, not directly measured.** The deviant Walker A motif and MinD/ParA family membership strongly imply ATP hydrolysis, and cryo-EM reports "ATP-dependent regulation," but a purified-protein kinetic characterization of BcsQ's ATPase cycle (kcat, nucleotide affinity, effect of ATP vs ADP on assembly) has not been documented in the reviewed literature.

3. **Polar-localization generality is uncertain.** Polar deposition of cellulose was shown in Enterobacteriaceae. Whether *P. putida* BcsQ localizes to the pole, mid-cell, or another site, and whether cellulose is deposited polar in *P. putida*, remains to be demonstrated.

4. **Precise mechanistic coupling to c-di-GMP.** In the macrocomplex, c-di-GMP is recognized at multiple sites (notably BcsA's PilZ domain and BcsE). How BcsQ's nucleotide state integrates with c-di-GMP sensing to gate machine assembly is not fully resolved.

5. **The UniProt name will mislead automated pipelines.** Any downstream analysis that trusts the "Cellulose synthase" SubName will assign the wrong molecular function (glycosyltransferase/catalysis) to PP_2634. This is a persistent annotation-propagation risk.

---

## Proposed Follow-up Experiments / Actions

1. **Deletion/complementation in *P. putida* KT2440.** Construct a clean ΔPP_2634 mutant and assess cellulose production (Calcofluor/Congo red binding, cellulase-sensitive matrix), biofilm formation, and rhizosphere competition, with plasmid complementation to confirm specificity. This directly tests essentiality in the target organism.

2. **Subcellular localization.** Express a functional fluorescent BcsQ fusion (e.g., mNeonGreen–BcsQ) in *P. putida* and image localization relative to cell poles and to a labeled BcsA, testing whether the *E. coli* polar-positioning paradigm holds.

3. **Biochemical ATPase assay.** Purify recombinant PP_2634/BcsQ and measure ATP hydrolysis kinetics; test Walker-A mutants (e.g., P-loop K→A) for loss of ATPase activity and for downstream loss of cellulose secretion, establishing a structure–function link.

4. **Interaction mapping.** Test the predicted BcsR–BcsQ subcomplex in *P. putida* (bacterial two-hybrid or co-purification) and probe BcsQ's contacts with BcsA to define how positioning couples to the catalytic core.

5. **Regulatory dissection.** Manipulate intracellular c-di-GMP (overexpress a diguanylate cyclase or a phosphodiesterase) and quantify *PbcsD* activity and BcsQ-dependent cellulose output, tying the FleQ/FleN/c-di-GMP circuit (30889223) to machine assembly.

6. **Database correction.** Submit a UniProt annotation update/comment proposing the BcsQ functional name and flagging the "Cellulose synthase" SubName as an automated mis-annotation, citing PMIDs 19400787, 33563593, and 39394223.

---

## Conclusion

PP_2634 (Q88JL5) in *P. putida* KT2440 is **BcsQ**, a **MinD/ParA-family P-loop ATPase** that serves as the **spatial organizer and assembly regulator** of the bacterial cellulose secretion (Bcs) system. It is **not** the catalytic cellulose synthase — that function belongs to the adjacent BcsA/BcsB (PP_2635/PP_2636). BcsQ is essential for cellulose biosynthesis, acts from the cytoplasmic face of the inner membrane as part of the BcsR–BcsQ regulatory subcomplex within the BcsRQABEFG–BcsC macrocomplex, and restricts active synthesis to a defined subcellular site. It operates within the c-di-GMP-driven biofilm program (in *P. putida*, the *bcs* operon is derepressed by c-di-GMP acting against FleQ/FleN), where the resulting extracellular cellulose supports biofilm cohesion and rhizosphere colonization, especially under water/osmotic stress.

---

### Key References

1. Le Quéré B, Ghigo J-M. *BcsQ is an essential component of the Escherichia coli cellulose biosynthesis apparatus that localizes at the bacterial cell pole.* Mol Microbiol. 2009. **[PMID: 19400787](https://pubmed.ncbi.nlm.nih.gov/19400787/).**
2. Römling U, Galperin MY. *Bacterial cellulose biosynthesis: diversity of operons, subunits, products, and functions.* Trends Microbiol. 2015. **[PMID: 26077867](https://pubmed.ncbi.nlm.nih.gov/26077867/).**
3. Abidi W, Zouhir S, Caleechurn M, Roche S, Krasteva PV. *Architecture and regulation of an enterobacterial cellulose secretion system.* Sci Adv. 2021. **[PMID: 33563593](https://pubmed.ncbi.nlm.nih.gov/33563593/).**
4. Anso I, Zouhir S, Sana TG, Krasteva PV. *Structural basis for synthase activation and cellulose modification in the E. coli Type II Bcs secretion system.* 2024. **[PMID: 39394223](https://pubmed.ncbi.nlm.nih.gov/39394223/).**
5. Navarrete B, et al. *Transcriptional organization, regulation and functional analysis of flhF and fleN in Pseudomonas putida.* 2019. **[PMID: 30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/).**
6. Nielsen L, Li X, Halverson LJ. *Cell-cell and cell-surface interactions mediated by cellulose and a novel exopolysaccharide contribute to Pseudomonas putida biofilm formation and fitness under water-limiting conditions.* Environ Microbiol. 2011. **[PMID: 21507177](https://pubmed.ncbi.nlm.nih.gov/21507177/).**


## Artifacts

- [OpenScientist final report](PP_2634-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_2634-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:26077867
2. PMID:19400787
3. PMID:33563593
4. PMID:39394223
5. PMID:30889223
6. PMID:21507177