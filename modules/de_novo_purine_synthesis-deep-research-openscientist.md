---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T14:43:55.450852'
end_time: '2026-07-25T15:15:56.403642'
duration_seconds: 1920.95
template_file: templates/module_research.md.j2
template_variables:
  module_title: De novo inosine monophosphate biosynthesis
  module_summary: A reusable pathway that assembles the purine ring on 5-phosphoribosyl
    diphosphate (PRPP) to form inosine monophosphate (IMP). The module represents
    ten ordered reaction positions and separates reaction roles from lineage-specific
    protein fusions. It includes alternative folate-dependent PurN and ATP/formate-dependent
    PurT routes for GAR formylation, and alternative two-enzyme and direct routes
    for AIR carboxylation. IMP-to-AMP and IMP-to-GMP branches are outside the module,
    although PurB also has a second physiological role in AMP synthesis.
  module_outline: "- De novo inosine monophosphate biosynthesis\n  - 1. committed\
    \ phosphoribosylamine formation\n  - Amidophosphoribosyltransferase\n    - Glutamine\
    \ PRPP amidotransferase (molecular player: PurF amidophosphoribosyltransferases;\
    \ activity or role: amidophosphoribosyltransferase activity)\n  - 2. glycinamide\
    \ ribonucleotide formation\n  - Phosphoribosylamine--glycine ligase\n    - GAR\
    \ synthetase (molecular player: PurD phosphoribosylamine--glycine ligases; activity\
    \ or role: phosphoribosylamine-glycine ligase activity)\n  - 3. GAR formylation\n\
    \  - Alternative GAR transformylation routes\n    - Alternative versions by one-carbon\
    \ donor and energy coupling: GAR one-carbon donor route\n      - Folate-dependent\
    \ PurN route\n        - Folate-dependent GAR transformylase (molecular player:\
    \ PurN GAR transformylases; activity or role: phosphoribosylglycinamide formyltransferase\
    \ activity)\n      - ATP/formate-dependent PurT route\n        - Formate-dependent\
    \ GAR transformylase (molecular player: PurT formate-dependent GAR transformylases;\
    \ activity or role: phosphoribosylglycinamide formyltransferase 2 activity)\n\
    \  - 4. formylglycinamidine ribonucleotide formation\n  - Phosphoribosylformylglycinamidine\
    \ synthase\n    - FGAM synthase (molecular player: large-type PurL FGAM synthases;\
    \ activity or role: phosphoribosylformylglycinamidine synthase activity)\n  -\
    \ 5. aminoimidazole ribonucleotide formation\n  - Phosphoribosylformylglycinamidine\
    \ cyclo-ligase\n    - AIR synthetase (molecular player: PurM AIR synthetases;\
    \ activity or role: phosphoribosylformylglycinamidine cyclo-ligase activity)\n\
    \  - 6. aminoimidazole ribonucleotide carboxylation\n  - Alternative AIR carboxylation\
    \ routes\n    - Alternative versions by direct versus N5-CAIR intermediate: AIR-to-CAIR\
    \ implementation\n      - Two-enzyme PurK/PurE route\n        - 1. N5-CAIR formation\n\
    \        - N5-CAIR synthetase\n          - ATP-dependent N5-CAIR synthetase (molecular\
    \ player: PurK N5-CAIR synthetases; activity or role: 5-(carboxyamino)imidazole\
    \ ribonucleotide synthase activity)\n        - 2. CAIR rearrangement\n       \
    \ - N5-CAIR mutase\n          - N5-CAIR mutase (molecular player: PurE N5-CAIR\
    \ mutases; activity or role: 5-(carboxyamino)imidazole ribonucleotide mutase activity)\n\
    \      - Direct AIR carboxylase route\n        - Direct AIR carboxylase (molecular\
    \ player: direct AIR carboxylases and PAICS-type fusion proteins; activity or\
    \ role: phosphoribosylaminoimidazole carboxylase activity)\n  - 7. succinylaminoimidazole\
    \ carboxamide ribonucleotide formation\n  - SAICAR synthetase\n    - SAICAR synthetase\
    \ (molecular player: PurC and PAICS SAICAR synthetases; activity or role: phosphoribosylaminoimidazolesuccinocarboxamide\
    \ synthase activity)\n  - 8. aminoimidazole carboxamide ribonucleotide formation\n\
    \  - SAICAR lyase\n    - SAICAR lyase (molecular player: PurB adenylosuccinate\
    \ lyases; activity or role: SAICAR lyase activity)\n  - 9. formylaminoimidazole\
    \ carboxamide ribonucleotide formation\n  - AICAR transformylase\n    - AICAR\
    \ transformylase (molecular player: PurH and ATIC AICAR transformylases; activity\
    \ or role: phosphoribosylaminoimidazolecarboxamide formyltransferase activity)\n\
    \  - 10. inosine monophosphate formation\n  - IMP cyclohydrolase\n    - IMP cyclohydrolase\
    \ (molecular player: PurH and ATIC IMP cyclohydrolases; activity or role: IMP\
    \ cyclohydrolase activity)"
  module_connections: '- Amidophosphoribosyltransferase feeds into Phosphoribosylamine--glycine
    ligase: PurF supplies phosphoribosylamine to PurD.

    - Phosphoribosylamine--glycine ligase feeds into Alternative GAR transformylation
    routes: PurD supplies GAR to either transformylase route.

    - Alternative GAR transformylation routes feeds into Phosphoribosylformylglycinamidine
    synthase: GAR formylation supplies FGAR to PurL.

    - Phosphoribosylformylglycinamidine synthase feeds into Phosphoribosylformylglycinamidine
    cyclo-ligase: PurL supplies FGAM to PurM.

    - Phosphoribosylformylglycinamidine cyclo-ligase feeds into Alternative AIR carboxylation
    routes: PurM supplies AIR to the selected carboxylation route.

    - Alternative AIR carboxylation routes feeds into SAICAR synthetase: AIR carboxylation
    supplies CAIR to SAICAR synthetase.

    - SAICAR synthetase feeds into SAICAR lyase: PurC supplies SAICAR to PurB.

    - SAICAR lyase feeds into AICAR transformylase: PurB supplies AICAR to the penultimate
    reaction.

    - AICAR transformylase feeds into IMP cyclohydrolase: AICAR transformylation supplies
    FAICAR for ring closure.

    - N5-CAIR synthetase feeds into N5-CAIR mutase: PurK supplies N5-CAIR to PurE.'
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
citation_count: 25
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: de_novo_purine_synthesis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: de_novo_purine_synthesis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

De novo inosine monophosphate biosynthesis

## Working Scope

A reusable pathway that assembles the purine ring on 5-phosphoribosyl diphosphate (PRPP) to form inosine monophosphate (IMP). The module represents ten ordered reaction positions and separates reaction roles from lineage-specific protein fusions. It includes alternative folate-dependent PurN and ATP/formate-dependent PurT routes for GAR formylation, and alternative two-enzyme and direct routes for AIR carboxylation. IMP-to-AMP and IMP-to-GMP branches are outside the module, although PurB also has a second physiological role in AMP synthesis.

## Provisional Biological Outline

- De novo inosine monophosphate biosynthesis
  - 1. committed phosphoribosylamine formation
  - Amidophosphoribosyltransferase
    - Glutamine PRPP amidotransferase (molecular player: PurF amidophosphoribosyltransferases; activity or role: amidophosphoribosyltransferase activity)
  - 2. glycinamide ribonucleotide formation
  - Phosphoribosylamine--glycine ligase
    - GAR synthetase (molecular player: PurD phosphoribosylamine--glycine ligases; activity or role: phosphoribosylamine-glycine ligase activity)
  - 3. GAR formylation
  - Alternative GAR transformylation routes
    - Alternative versions by one-carbon donor and energy coupling: GAR one-carbon donor route
      - Folate-dependent PurN route
        - Folate-dependent GAR transformylase (molecular player: PurN GAR transformylases; activity or role: phosphoribosylglycinamide formyltransferase activity)
      - ATP/formate-dependent PurT route
        - Formate-dependent GAR transformylase (molecular player: PurT formate-dependent GAR transformylases; activity or role: phosphoribosylglycinamide formyltransferase 2 activity)
  - 4. formylglycinamidine ribonucleotide formation
  - Phosphoribosylformylglycinamidine synthase
    - FGAM synthase (molecular player: large-type PurL FGAM synthases; activity or role: phosphoribosylformylglycinamidine synthase activity)
  - 5. aminoimidazole ribonucleotide formation
  - Phosphoribosylformylglycinamidine cyclo-ligase
    - AIR synthetase (molecular player: PurM AIR synthetases; activity or role: phosphoribosylformylglycinamidine cyclo-ligase activity)
  - 6. aminoimidazole ribonucleotide carboxylation
  - Alternative AIR carboxylation routes
    - Alternative versions by direct versus N5-CAIR intermediate: AIR-to-CAIR implementation
      - Two-enzyme PurK/PurE route
        - 1. N5-CAIR formation
        - N5-CAIR synthetase
          - ATP-dependent N5-CAIR synthetase (molecular player: PurK N5-CAIR synthetases; activity or role: 5-(carboxyamino)imidazole ribonucleotide synthase activity)
        - 2. CAIR rearrangement
        - N5-CAIR mutase
          - N5-CAIR mutase (molecular player: PurE N5-CAIR mutases; activity or role: 5-(carboxyamino)imidazole ribonucleotide mutase activity)
      - Direct AIR carboxylase route
        - Direct AIR carboxylase (molecular player: direct AIR carboxylases and PAICS-type fusion proteins; activity or role: phosphoribosylaminoimidazole carboxylase activity)
  - 7. succinylaminoimidazole carboxamide ribonucleotide formation
  - SAICAR synthetase
    - SAICAR synthetase (molecular player: PurC and PAICS SAICAR synthetases; activity or role: phosphoribosylaminoimidazolesuccinocarboxamide synthase activity)
  - 8. aminoimidazole carboxamide ribonucleotide formation
  - SAICAR lyase
    - SAICAR lyase (molecular player: PurB adenylosuccinate lyases; activity or role: SAICAR lyase activity)
  - 9. formylaminoimidazole carboxamide ribonucleotide formation
  - AICAR transformylase
    - AICAR transformylase (molecular player: PurH and ATIC AICAR transformylases; activity or role: phosphoribosylaminoimidazolecarboxamide formyltransferase activity)
  - 10. inosine monophosphate formation
  - IMP cyclohydrolase
    - IMP cyclohydrolase (molecular player: PurH and ATIC IMP cyclohydrolases; activity or role: IMP cyclohydrolase activity)

## Known Relationships Among Steps

- Amidophosphoribosyltransferase feeds into Phosphoribosylamine--glycine ligase: PurF supplies phosphoribosylamine to PurD.
- Phosphoribosylamine--glycine ligase feeds into Alternative GAR transformylation routes: PurD supplies GAR to either transformylase route.
- Alternative GAR transformylation routes feeds into Phosphoribosylformylglycinamidine synthase: GAR formylation supplies FGAR to PurL.
- Phosphoribosylformylglycinamidine synthase feeds into Phosphoribosylformylglycinamidine cyclo-ligase: PurL supplies FGAM to PurM.
- Phosphoribosylformylglycinamidine cyclo-ligase feeds into Alternative AIR carboxylation routes: PurM supplies AIR to the selected carboxylation route.
- Alternative AIR carboxylation routes feeds into SAICAR synthetase: AIR carboxylation supplies CAIR to SAICAR synthetase.
- SAICAR synthetase feeds into SAICAR lyase: PurC supplies SAICAR to PurB.
- SAICAR lyase feeds into AICAR transformylase: PurB supplies AICAR to the penultimate reaction.
- AICAR transformylase feeds into IMP cyclohydrolase: AICAR transformylation supplies FAICAR for ring closure.
- N5-CAIR synthetase feeds into N5-CAIR mutase: PurK supplies N5-CAIR to PurE.

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

# De novo Inosine Monophosphate Biosynthesis: A Conserved Ten-Reaction Module with Lineage-Specific Implementations

*Review-style synthesis. Search date: 2026-07-25. Citations are given as PubMed IDs (PMID).*

---

## 1. Executive summary

De novo inosine monophosphate (IMP) biosynthesis is the pathway that builds the purine ring atom-by-atom on 5-phosphoribosyl-1-diphosphate (PRPP), converting a sugar-phosphate and small metabolites (glutamine, glycine, one-carbon units, aspartate, CO₂/bicarbonate, ATP) into IMP, the first complete purine nucleotide and the common precursor of AMP and GMP. The system is best understood not as ten proteins but as **ten ordered reaction roles** that are conserved across all three domains of life, implemented by a variable set of proteins whose fusion state, cofactor choice and quaternary organization differ by lineage (PMID: 25230797; PMID: 33179964).

Three features organize this review. First, the **reaction skeleton is deeply conserved and ancient**, plausibly present in the last common ancestor, whereas the **protein implementation is plastic**: bacteria typically use single-function Pur enzymes, while humans compress the ten reactions into six polypeptides via gene fusions (trifunctional GART; bifunctional PAICS and ATIC) (PMID: 2050105; PMID: 35331738; PMID: 11323713). Second, two reaction positions have **genuine alternative routes**: step 3 (GAR formylation) can use a folate-dependent transformylase (PurN) or an ATP/formate-dependent transformylase (PurT) acting through a formyl-phosphate intermediate (PMID: 8501063; PMID: 9184151); step 6 (AIR carboxylation) can proceed by a two-enzyme bacterial route (PurK makes N⁵-CAIR, PurE mutase rearranges it to CAIR) or by a direct eukaryotic PurE-class carboxylase that fixes CO₂ onto AIR without an N⁵-CAIR intermediate (PMID: 10574791). Third, in eukaryotes the enzymes reversibly assemble into a **channeling metabolon, the purinosome**, coupling the reaction positions into high-flux, spatially organized synthesis (PMID: 18388293; PMID: 32299949) — a claim that has been both strongly supported and contested (PMID: 24413256).

The module's boundaries exclude the salvage pathway, PRPP synthesis, folate one-carbon metabolism, and the IMP→AMP and IMP→GMP branches — although one enzyme, PurB/adenylosuccinate lyase, is physiologically shared between the IMP module (step 8) and the IMP→AMP branch, a dual role with direct clinical consequences (PMID: 41053929; PMID: 35133277).

---

## 2. Definition and biological boundaries

### 2.1 What is included

The system comprises the reactions that assemble the purine ring on PRPP up to and including formation of IMP. In the canonical numbering used here:

1. **Committed step — phosphoribosylamine (PRA) formation.** Glutamine PRPP amidotransferase (PurF / PPAT / GPATase) transfers the glutamine amide nitrogen to PRPP, displacing pyrophosphate to give 5-phospho-β-D-ribosylamine (PMID: 9514258).
2. **GAR formation.** GAR synthetase (PurD) ligates glycine to PRA to form glycinamide ribonucleotide (GAR).
3. **GAR formylation.** A GAR transformylase adds a one-carbon (formyl) group to give formyl-GAR (FGAR) — **alternative routes PurN vs PurT** (PMID: 8501063).
4. **FGAM formation.** FGAM synthase (PurL) uses glutamine + ATP to convert FGAR to formylglycinamidine ribonucleotide (FGAM), with ammonia channeling (PMID: 18597481).
5. **AIR formation.** AIR synthetase (PurM), an ATP-dependent cyclo-ligase, closes the five-membered imidazole ring to give 5-aminoimidazole ribonucleotide (AIR) (PMID: 3015935).
6. **AIR carboxylation.** Carboxylation to 4-carboxy-AIR (CAIR) — **alternative routes: PurK+PurE (via N⁵-CAIR) vs direct PurE-class carboxylase** (PMID: 10574791).
7. **SAICAR formation.** SAICAR synthetase (PurC / PAICS) condenses aspartate onto CAIR to give SAICAR.
8. **AICAR formation.** SAICAR lyase (PurB / adenylosuccinate lyase) eliminates fumarate to give AICAR.
9. **FAICAR formation.** AICAR transformylase (PurH / ATIC) adds a second one-carbon unit to give formyl-AICAR (FAICAR).
10. **IMP formation.** IMP cyclohydrolase (PurH / ATIC) closes the second (pyrimidine) ring to yield IMP (PMID: 11323713).

### 2.2 What should be treated separately (neighbouring processes commonly conflated)

- **PRPP synthesis (PRPP synthetase, PRS).** PRPP is the substrate, not part of the ring-assembly module, and is shared with pyrimidine, histidine, tryptophan and NAD biosynthesis and with purine salvage. It is an upstream supply node, frequently co-regulated but mechanistically distinct.
- **Purine salvage (HGPRT, APRT, adenosine kinase).** Salvage regenerates nucleotides from preformed bases/nucleosides and is the dominant source in many differentiated tissues; it is a parallel, independent route to the same end nucleotides and is often confused with de novo synthesis in flux discussions.
- **Folate one-carbon metabolism.** 10-formyl-THF (supplied through the MTHFD1/serine-hydroxymethyltransferase network) is the one-carbon donor for the PurN and PurH transformylase steps. It is a cofactor-supply pathway, not part of the ring assembly, though physically linked to the metabolon via MTHFD1 (PMID: 35331738).
- **IMP→AMP and IMP→GMP branches.** Adenylosuccinate synthetase (PurA) + adenylosuccinate lyase (PurB) make AMP; IMP dehydrogenase (IMPDH) + GMP synthase make GMP. These lie **downstream** of IMP and are outside the module. The one caveat is **PurB/ADSL**, which physiologically catalyses both step 8 of the IMP module and the S-AMP→AMP reaction of the AMP branch (PMID: 41053929).
- **The purinosome as an organelle.** The metabolon is a reversible, membraneless assembly, not a bounded organelle; treating it as a fixed structure over-states current evidence (see §7).

### 2.3 Competing definitions

Literature differs on **enzyme count** ("six enzymes/10 steps" in eukaryotes because of fusions vs "≥10 gene products" in many bacteria) (PMID: 18388293), on whether the purinosome should be counted as part of the "pathway" definition, and on whether the module ends at IMP or is described together with the AMP/GMP branches as "de novo purine biosynthesis." This review treats PRPP→IMP as the module and the branches as adjacent.

---

## 3. Mechanistic overview

### 3.1 Best current model of the sequence of events

The pathway is a **strictly ordered assembly line**: each enzyme's product is the obligatory substrate of the next, and the purine ring is constructed in a defined atom order (N9→C4/C5→N7→C8→N3→C6→N1→C2). Ordering is enforced both by substrate specificity and by the chemical **instability of several intermediates** (notably phosphoribosylamine, which is labile at physiological pH, and N⁵-CAIR), which strongly favors direct hand-off (channeling) over free diffusion (PMID: 34547238). The energetic cost is high: multiple steps consume ATP (PurD, PurL, PurM, PurT, PurK), making the pathway responsive to energy and purine status.

### 3.2 Obligatory, conditional and accessory elements

- **Obligatory reaction positions:** all ten reaction roles are obligatory to reach IMP; none can be skipped because each supplies the next substrate.
- **Conditional (alternative) implementations:** step 3 (PurN vs PurT) and step 6 (PurK/PurE two-enzyme vs direct carboxylase) are the two positions where different molecular means achieve the same transformation. Which is used depends on the organism (and, for step 3, on folate status and formate availability).
- **Accessory / supply elements:** PRPP synthetase, the folate one-carbon network (MTHFD1), and — in eukaryotes — the purinosome scaffold and its regulators are accessory to, but not part of, the core chemistry.

### 3.3 Molecular assemblies per step

Distinct fold families carry out mechanistically related chemistry. Glutamine amidotransferase chemistry (PurF, PurL) uses a glutaminase domain feeding ammonia through an intramolecular channel to a synthetase domain (PMID: 9514258; PMID: 18597481). ATP-grasp enzymes (PurT, PurK, and mechanistically PurD) activate carboxylate/formate substrates via acyl-phosphate intermediates (PMID: 9184151). PurM defines its own AIR-synthetase fold (PMID: 26515187). The two terminal activities are fused in PurH/ATIC but use two separate active sites ~50 Å apart, with **no intramolecular tunnel** between them (PMID: 11323713).

---

## 4. Major molecular players and active assemblies

| Step | Reaction role | Bacterial protein(s) | Human protein (fusion) | Notable mechanism / assembly |
|---|---|---|---|---|
| 1 | Committed PRA formation | PurF | PPAT (monofunctional) | Glutamine amidotransferase; AMP feedback at PRPP site; metal-free vs Fe–S subfamilies (PMID: 9514258) |
| 2 | GAR formation | PurD | GART (trifunctional, domain 1) | ATP-dependent ligase |
| 3 | GAR formylation | **PurN or PurT** | GART (folate/PurN-type domain) | PurN = folate-dependent; PurT = ATP/formate via formyl-phosphate (PMID: 8501063; PMID: 9184151) |
| 4 | FGAM formation | large PurL **or** smPurL+PurQ+PurS | PFAS/FGAMS (large PurL) | Glutamine amidotransferase; ammonia channel; fused vs multiprotein (PMID: 18597481; PMID: 15301532) |
| 5 | AIR formation | PurM | GART (AIRS domain) | ATP-dependent cyclo-ligase; conserved dimer (PMID: 26515187) |
| 6 | AIR carboxylation | **PurK + PurE (class I mutase)** or direct PurE (class II) | PAICS (direct carboxylase) | Two-enzyme N⁵-CAIR route vs direct CO₂ fixation (PMID: 10574791) |
| 7 | SAICAR formation | PurC | PAICS (SAICAR synthetase) | ATP-dependent aspartate condensation |
| 8 | AICAR formation | PurB | ADSL (monofunctional) | β-elimination of fumarate; **also acts in AMP branch** (PMID: 41053929) |
| 9 | FAICAR formation | PurH | ATIC (transformylase domain) | Folate-dependent transformylase (PMID: 11323713) |
| 10 | IMP formation | PurH | ATIC (cyclohydrolase domain) | Ring closure; no tunnel to transformylase site (PMID: 11323713) |

**Active supramolecular assemblies.** In *Bacillus subtilis*/archaea, step 4 is reconstituted from smPurL, the glutaminase PurQ and the scaffolding PurS in a 2:1:1 PurS:Q:L complex whose assembly is glutamine/ADP-dependent (PMID: 18597481; PMID: 15301532). In eukaryotes, the whole pathway reversibly condenses into the **purinosome** at the microtubule/mitochondria interface; the bifunctional PAICS is an interaction hub that contacts nearly all other pathway enzymes and MTHFD1 (PMID: 35331738; PMID: 33179964). Single-cell chemical imaging shows nine enzymes channel intermediates, raising flux and tuning the AMP/GMP ratio (PMID: 32299949).

---

## 5. Evolutionary and cell-biological variation

### 5.1 Across evolutionary lineages

- **Antiquity.** Comparative genomics across 1,606 genomes places nucleotide metabolism, including purine biosynthesis, in the last common ancestor of Bacteria, Archaea and Eukarya (PMID: 25230797). The reaction skeleton is therefore the ancient, conserved unit.
- **Committed step split.** The first enzyme (GPATase) exists as a **metal-free** subfamily (prototype *E. coli*) and a **Fe–S-cluster-containing** subfamily (*B. subtilis*); a common ancestor may have carried an Fe–S cluster (PMID: 9514258).
- **Step 3 donor choice.** Folate-dependent PurN is widespread; formate/ATP-dependent PurT (ATP-grasp, PurK-like) is present in many bacteria and provides redundancy under folate limitation (PMID: 8501063; PMID: 7496533). Eukaryotes generally use only the PurN (folate) chemistry, embedded in GART.
- **Step 4 architecture.** Large single-chain PurL occurs in most Gram-negative bacteria and eukaryotes; small PurL + PurQ + PurS occurs in Gram-positive bacteria and archaea (PMID: 18597481).
- **Step 6 route.** Bacteria/fungi use PurK + PurE (N⁵-CAIR mutase, class I); higher eukaryotes use a direct PurE-class carboxylase (class II) and lack PurK; the mutase-to-carboxylase divergence is a documented lineage-associated transition (PMID: 10574791; PMID: 25230797).
- **Gene fusions.** Humans compress the ten reactions into six polypeptides — trifunctional GART (steps 2,3,5; 21q22.1), bifunctional PAICS (steps 6,7), bifunctional ATIC (steps 9,10), plus monofunctional PPAT, PFAS and ADSL (PMID: 2050105; PMID: 35331738; PMID: 11323713). **Bacterial single-function Pur enzymes are the best representatives of the ancestral, unfused reaction roles.**

### 5.2 Across cell types, states and compartments

De novo synthesis is most active in proliferating cells (embryonic tissue, activated lymphocytes, tumors) where salvage cannot meet demand; many differentiated tissues rely more on salvage. Purinosome assembly is inducible by purine depletion or increased demand and has been observed in multiple human lines (HeLa, HepG2, Saos-2, HEK293, fibroblasts, keratinocytes) (PMID: 22180458), and is dynamically regulated with cell state (PMID: 18388293; PMID: 33179964). The pathway is a validated antimicrobial/antifungal and anticancer target: ATIC is essential for growth and virulence in *Cryptococcus neoformans* (PMID: 36063996), and human ATIC is inhibited by potent antifolates (PMID: 14966129).

---

## 6. Constraints, dependencies, and failure modes

- **Order is fixed** by substrate specificity: each enzyme accepts only the prior product. There is no experimentally supported shortcut through the ten positions.
- **Intermediate instability** (phosphoribosylamine; N⁵-CAIR) makes free-diffusion routing costly and selects for channeling — the mechanistic rationale for the purinosome and for the bacterial PurLQS and PurK/PurE couplings (PMID: 34547238).
- **Mutually exclusive route choices.** At step 6, an organism using the direct class II carboxylase does not use PurK/N⁵-CAIR; at step 3, PurN and PurT are redundant but only the double mutant is auxotrophic, showing either alone suffices (PMID: 8501063).
- **Cofactor dependence.** Steps 3 (PurN) and 9 require 10-formyl-THF; folate/one-carbon insufficiency throttles the pathway, linking it to MTHFD1 and B-vitamin status (PMID: 35331738).
- **Regulation is multi-tier.** Bacterial *pur* genes are transcriptionally co-repressed (PurR regulon; conserved purF/purM operator regions) (PMID: 3015935; PMID: 8501063); the committed enzyme PurF is allosterically feedback-inhibited by end-product mononucleotides at the PRPP site (PMID: 9514258). In eukaryotes an additional tier is metabolon (dis)assembly (PMID: 33179964).
- **Failure modes with clinical readout.** Loss of ADSL (step 8, also AMP branch) causes a neurometabolic disorder (>80 patients) with psychomotor retardation, epilepsy and autistic features; diagnostic accumulation of dephosphorylated SAICAr and S-Ado; patient fibroblasts show 1–4% residual activity and loss of purinosome assembly, with pathology attributed largely to SAICAr toxicity and secondarily to reduced purine supply and impaired ciliogenesis (PMID: 41053929; PMID: 25112391; PMID: 35133277). ATIC/ADSL mutations destabilize purinosome assembly in proportion to clinical severity (PMID: 22180458).

---

## 7. Controversies and open questions

1. **Is the purinosome a functional channeling metabolon or an artifact of over-expression?** The Benkovic group's live-cell imaging, metabolomics and GCIB-SIMS argue for a genuine, reversible, flux-enhancing metabolon that channels intermediates from PRPP to AMP/GMP (PMID: 18388293; PMID: 32299949; PMID: 33179964). A dissenting view held that fluorescently tagged "purinosome bodies" may correspond to protein aggregation/stress bodies rather than physiological channeling complexes (PMID: 24413256). More recent endogenous-level and single-cell data have shifted the balance toward a real metabolon, but the **stoichiometry, condensate nature, and in vivo flux contribution remain incompletely resolved**.
2. **Nature of channeling without tunnels.** PurH/ATIC has two active sites ~50 Å apart with no connecting tunnel (PMID: 11323713); how intermediates are retained here — by electrostatics, proximity within the metabolon, or transient diffusion — is unsettled.
3. **Regulation of assembly.** Candidate kinases and signaling inputs (extensive phosphorylation of pathway enzymes) are proposed to drive purinosome assembly/disassembly, but a definitive signaling circuit is not established (PMID: 33179964).
4. **Organism transferability.** Much mechanistic detail comes from *E. coli*, *B. subtilis*, *Salmonella*, *Thermotoga* and avian/human enzymes; route usage (PurN/PurT, PurK/PurE, large/small PurL) differs by lineage, so conclusions should not be generalized across organisms without checking gene complement.
5. **Moonlighting/branch coupling.** The physiological consequences of PurB/ADSL serving two pathways, and proposed non-canonical roles of pathway intermediates (e.g., SAICAR signaling), warrant further, organism-specific study.

**Most important open questions:** the precise composition and flux stoichiometry of the endogenous purinosome; the signaling logic that assembles it; and whether alternative-route enzymes (PurT, PurK/PurE vs class II) confer condition-specific fitness advantages beyond simple redundancy.

---

## 8. Key references

- Armenta-Medina D, et al. Comparative genomics of nucleotide metabolism: a tour to the past of the three cellular domains of life. *BMC Genomics* 2014. **PMID: 25230797.**
- Pareek V, Pedley AM, Benkovic SJ. Human de novo purine biosynthesis. *Crit Rev Biochem Mol Biol* 2021. **PMID: 33179964.**
- An S, Kumar R, Sheets ED, Benkovic SJ. Reversible compartmentalization of de novo purine biosynthetic complexes in living cells. *Science* 2008. **PMID: 18388293.**
- Pareek V, et al. Metabolomics and mass spectrometry imaging reveal channeled de novo purine synthesis in cells. *Science* 2020. **PMID: 32299949.**
- Pareek V, et al. Metabolic channeling: predictions, deductions, and evidence. *Mol Cell* 2021. **PMID: 34547238.**
- Zhao H, et al. Revisiting and revising the purinosome. *Mol Biosyst* 2014. **PMID: 24413256.**
- He J, et al. Multienzyme interactions of PAICS facilitate purinosome formation and metabolic channeling. *BMC Biol* 2022. **PMID: 35331738.**
- Muchmore CRA, et al. Crystal structure of glutamine PRPP amidotransferase from E. coli. *Protein Sci* 1998. **PMID: 9514258.**
- Nygaard P, Smith JM. Evidence for a novel GAR transformylase (PurT) in E. coli. *J Bacteriol* 1993. **PMID: 8501063.**
- Marolewski AE, et al. Formyl phosphate: intermediate in the PurT GAR transformylase reaction. *Biochemistry* 1997. **PMID: 9184151.**
- Saxild HH, et al. Functional analysis of B. subtilis purT. *J Bacteriol* 1995. **PMID: 7496533.**
- Morar M, et al. FGAR amidotransferase (PurL) from Thermotoga maritima: complex formation. *Biochemistry* 2008. **PMID: 18597481.**
- Anand R, et al. A model for the B. subtilis FGAR amidotransferase multiprotein complex. *Biochemistry* 2004. **PMID: 15301532.**
- Smith JM, Daum HA. Nucleotide sequence of purM (AIR synthetase) of E. coli. *J Biol Chem* 1986. **PMID: 3015935.**
- Kanagawa M, et al. Crystal structures of PurM from Thermus thermophilus and Geobacillus kaustophilus. *Acta Crystallogr F* 2016. **PMID: 26515187.**
- Mathews II, et al. Crystal structure of E. coli PurE, an unusual mutase. *Structure* 1999. **PMID: 10574791.**
- Greasley SE, et al. Crystal structure of the bifunctional transformylase/cyclohydrolase (ATIC). *Nat Struct Biol* 2001. **PMID: 11323713.**
- Cheong CG, et al. Human ATIC in complex with sulfonyl antifolates. *J Biol Chem* 2004. **PMID: 14966129.**
- Le Nours J, et al. Structural analyses of ATIC (PurH) from M. tuberculosis. 2011. **PMID: 21956117.**
- Wizrah MSI, et al. ATIC is essential for de novo purine biosynthesis and infection by Cryptococcus neoformans. *J Biol Chem* 2022. **PMID: 36063996.**
- Gnirke A, et al. Cloning and in vivo expression of the human GART gene. *Genomics* 1991. **PMID: 2050105.**
- Rousselot-Pailley B, et al. Allopurinol treatment in adenylosuccinate lyase deficiency. 2025. **PMID: 41053929.**
- Dutto I, et al. Pathway-specific effects of ADSL deficiency on neurodevelopment. 2022. **PMID: 35133277.**
- Jurecka A, et al. Adenylosuccinate lyase deficiency. *J Inherit Metab Dis* 2015. **PMID: 25112391.**
- Baresova V, et al. Mutations of ATIC and ADSL affect purinosome assembly. *Hum Mol Genet* 2012. **PMID: 22180458.**

---

*Uncertainty statement.* Structural and mechanistic claims are strongest for the individual enzymes (multiple crystal structures across bacteria, archaea and vertebrates). The channeling/purinosome model is well supported in cultured human cells but its endogenous stoichiometry and in vivo flux contribution remain partly inferential, and route usage varies by lineage; readers should not extrapolate a single organism's gene complement or a single cell line's behavior to all biology.


## Artifacts

- [OpenScientist final report](de_novo_purine_synthesis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](de_novo_purine_synthesis-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:25230797
2. PMID:33179964
3. PMID:2050105
4. PMID:35331738
5. PMID:11323713
6. PMID:8501063
7. PMID:9184151
8. PMID:10574791
9. PMID:18388293
10. PMID:32299949
11. PMID:24413256
12. PMID:41053929
13. PMID:35133277
14. PMID:9514258
15. PMID:18597481
16. PMID:3015935
17. PMID:34547238
18. PMID:26515187
19. PMID:15301532
20. PMID:7496533
21. PMID:22180458
22. PMID:36063996
23. PMID:14966129
24. PMID:25112391
25. PMID:21956117