---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T19:41:58.694432'
end_time: '2026-07-20T20:03:46.388214'
duration_seconds: 1307.69
template_file: templates/module_research.md.j2
template_variables:
  module_title: Folate one-carbon carrier-state interconversion
  module_summary: 'A taxon-neutral module for interconversion of the substituted tetrahydrofolate
    carrier states 5,10-methylene-THF, 5,10-methenyl-THF, 10-formyl-THF, 5-methyl-THF,
    and the salvaged 5-formyl-THF pool. The module separates four chemically distinct
    transformations: pyridine-nucleotide-linked oxidation of 5,10-methylene-THF to
    5,10-methenyl-THF, hydrolysis of 5,10-methenyl-THF to 10-formyl-THF, reduction
    of 5,10-methylene-THF to 5-methyl-THF, and ATP-dependent salvage of 5-formyl-THF
    to 5,10-methenyl-THF. Fused FolD/MTHFD architectures and NAD(H)- versus NADP(H)-linked
    variants are represented as alternative implementations of the same carrier-state
    conversions. The dehydrogenase and cyclohydrolase operations form the required
    coupled core; MTHFR reduction and 5-formyl-THF salvage are independent optional
    branches. Upstream one-carbon loading by serine hydroxymethyltransferase, glycine
    cleavage, or formate-tetrahydrofolate ligase and downstream use by purine, thymidylate,
    or methionine synthesis are outside this module.'
  module_outline: "- Folate one-carbon carrier-state interconversion\n  - Required\
    \ core 5,10-methylene-THF and 5,10-methenyl-THF redox interconversion\n  - 5,10-methylene-THF\
    \ to 5,10-methenyl-THF redox\n    - Alternative versions by redox cofactor and\
    \ enzyme architecture: Pyridine-nucleotide-linked dehydrogenase variants\n   \
    \   - NADP-linked bifunctional FolD reaction\n        - Bacterial FolD NADP-linked\
    \ dehydrogenase (molecular player: bifunctional FolD enzymes; activity or role:\
    \ methylenetetrahydrofolate dehydrogenase (NADP+) activity)\n      - NADP-linked\
    \ monofunctional MtdA reaction\n        - Monofunctional MtdA NADP-linked dehydrogenase\
    \ (molecular player: MtdA (Methylorubrum extorquens AM1); activity or role: methylenetetrahydrofolate\
    \ dehydrogenase (NADP+) activity)\n      - NADP-linked cytosolic MTHFD1 reaction\n\
    \        - Cytosolic MTHFD1 NADP-linked dehydrogenase (molecular player: eukaryotic\
    \ cytosolic MTHFD1 enzymes; activity or role: methylenetetrahydrofolate dehydrogenase\
    \ (NADP+) activity)\n      - NAD-linked MTHFD2 reaction\n        - NAD-linked\
    \ methylenetetrahydrofolate dehydrogenase (molecular player: mitochondrial MTHFD2\
    \ enzymes; activity or role: methylenetetrahydrofolate dehydrogenase (NAD+) activity)\n\
    \  - Required core 5,10-methenyl-THF and 10-formyl-THF hydrolytic interconversion\n\
    \  - 5,10-methenyl-THF to 10-formyl-THF hydrolysis\n    - Alternative versions\
    \ by fused versus monofunctional enzyme architecture: Methenyltetrahydrofolate\
    \ cyclohydrolase architecture variants\n      - Fused FolD/MTHFD cyclohydrolase\
    \ reaction\n        - Fused FolD/MTHFD methenyltetrahydrofolate cyclohydrolase\
    \ (molecular player: FolD/MTHFD methenyltetrahydrofolate cyclohydrolases; activity\
    \ or role: methenyltetrahydrofolate cyclohydrolase activity)\n      - Monofunctional\
    \ FchA cyclohydrolase reaction\n        - Monofunctional FchA methenyltetrahydrofolate\
    \ cyclohydrolase (molecular player: monofunctional FchA cyclohydrolases; activity\
    \ or role: methenyltetrahydrofolate cyclohydrolase activity)\n  - Optional 5,10-methylene-THF\
    \ reduction to 5-methyl-THF branch\n  - 5,10-methylene-THF to 5-methyl-THF reduction\n\
    \    - Alternative versions by pyridine-nucleotide specificity and enzyme architecture:\
    \ Methylenetetrahydrofolate reductase cofactor variants\n      - NADH-linked compact\
    \ MetF reaction\n        - NADH-linked methylenetetrahydrofolate reductase (molecular\
    \ player: compact bacterial MetF enzymes; activity or role: methylenetetrahydrofolate\
    \ reductase (NADH) activity)\n      - NADH-linked regulatory MTHFR reaction\n\
    \        - Regulatory-architecture NADH methylenetetrahydrofolate reductase (molecular\
    \ player: MTHFR2 (Arabidopsis thaliana); activity or role: methylenetetrahydrofolate\
    \ reductase (NADH) activity)\n      - NADPH-linked regulatory MTHFR reaction\n\
    \        - NADPH-linked methylenetetrahydrofolate reductase (molecular player:\
    \ MTHFR (human); activity or role: methylenetetrahydrofolate reductase (NADPH)\
    \ activity)\n  - Optional 5-formyl-THF salvage to 5,10-methenyl-THF branch\n \
    \ - 5-formyl-THF salvage\n    - 5-Formyltetrahydrofolate cyclo-ligase (molecular\
    \ player: Fau/MTHFS 5-formyltetrahydrofolate cyclo-ligases; activity or role:\
    \ 5-formyltetrahydrofolate cyclo-ligase activity)"
  module_connections: '- 5,10-methylene-THF to 5,10-methenyl-THF redox feeds into
    5,10-methenyl-THF to 10-formyl-THF hydrolysis: 5,10-methenyl-THF produced by the
    dehydrogenase reaction is the cyclohydrolase substrate; the two activities are
    often fused but are chemically distinct.

    - 5-formyl-THF salvage feeds into 5,10-methenyl-THF to 10-formyl-THF hydrolysis:
    Salvaged 5,10-methenyl-THF rejoins the methenyl/formyl carrier-state interconversion.'
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: folate_one_carbon_interconversion-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: folate_one_carbon_interconversion-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Folate one-carbon carrier-state interconversion

## Working Scope

A taxon-neutral module for interconversion of the substituted tetrahydrofolate carrier states 5,10-methylene-THF, 5,10-methenyl-THF, 10-formyl-THF, 5-methyl-THF, and the salvaged 5-formyl-THF pool. The module separates four chemically distinct transformations: pyridine-nucleotide-linked oxidation of 5,10-methylene-THF to 5,10-methenyl-THF, hydrolysis of 5,10-methenyl-THF to 10-formyl-THF, reduction of 5,10-methylene-THF to 5-methyl-THF, and ATP-dependent salvage of 5-formyl-THF to 5,10-methenyl-THF. Fused FolD/MTHFD architectures and NAD(H)- versus NADP(H)-linked variants are represented as alternative implementations of the same carrier-state conversions. The dehydrogenase and cyclohydrolase operations form the required coupled core; MTHFR reduction and 5-formyl-THF salvage are independent optional branches. Upstream one-carbon loading by serine hydroxymethyltransferase, glycine cleavage, or formate-tetrahydrofolate ligase and downstream use by purine, thymidylate, or methionine synthesis are outside this module.

## Provisional Biological Outline

- Folate one-carbon carrier-state interconversion
  - Required core 5,10-methylene-THF and 5,10-methenyl-THF redox interconversion
  - 5,10-methylene-THF to 5,10-methenyl-THF redox
    - Alternative versions by redox cofactor and enzyme architecture: Pyridine-nucleotide-linked dehydrogenase variants
      - NADP-linked bifunctional FolD reaction
        - Bacterial FolD NADP-linked dehydrogenase (molecular player: bifunctional FolD enzymes; activity or role: methylenetetrahydrofolate dehydrogenase (NADP+) activity)
      - NADP-linked monofunctional MtdA reaction
        - Monofunctional MtdA NADP-linked dehydrogenase (molecular player: MtdA (Methylorubrum extorquens AM1); activity or role: methylenetetrahydrofolate dehydrogenase (NADP+) activity)
      - NADP-linked cytosolic MTHFD1 reaction
        - Cytosolic MTHFD1 NADP-linked dehydrogenase (molecular player: eukaryotic cytosolic MTHFD1 enzymes; activity or role: methylenetetrahydrofolate dehydrogenase (NADP+) activity)
      - NAD-linked MTHFD2 reaction
        - NAD-linked methylenetetrahydrofolate dehydrogenase (molecular player: mitochondrial MTHFD2 enzymes; activity or role: methylenetetrahydrofolate dehydrogenase (NAD+) activity)
  - Required core 5,10-methenyl-THF and 10-formyl-THF hydrolytic interconversion
  - 5,10-methenyl-THF to 10-formyl-THF hydrolysis
    - Alternative versions by fused versus monofunctional enzyme architecture: Methenyltetrahydrofolate cyclohydrolase architecture variants
      - Fused FolD/MTHFD cyclohydrolase reaction
        - Fused FolD/MTHFD methenyltetrahydrofolate cyclohydrolase (molecular player: FolD/MTHFD methenyltetrahydrofolate cyclohydrolases; activity or role: methenyltetrahydrofolate cyclohydrolase activity)
      - Monofunctional FchA cyclohydrolase reaction
        - Monofunctional FchA methenyltetrahydrofolate cyclohydrolase (molecular player: monofunctional FchA cyclohydrolases; activity or role: methenyltetrahydrofolate cyclohydrolase activity)
  - Optional 5,10-methylene-THF reduction to 5-methyl-THF branch
  - 5,10-methylene-THF to 5-methyl-THF reduction
    - Alternative versions by pyridine-nucleotide specificity and enzyme architecture: Methylenetetrahydrofolate reductase cofactor variants
      - NADH-linked compact MetF reaction
        - NADH-linked methylenetetrahydrofolate reductase (molecular player: compact bacterial MetF enzymes; activity or role: methylenetetrahydrofolate reductase (NADH) activity)
      - NADH-linked regulatory MTHFR reaction
        - Regulatory-architecture NADH methylenetetrahydrofolate reductase (molecular player: MTHFR2 (Arabidopsis thaliana); activity or role: methylenetetrahydrofolate reductase (NADH) activity)
      - NADPH-linked regulatory MTHFR reaction
        - NADPH-linked methylenetetrahydrofolate reductase (molecular player: MTHFR (human); activity or role: methylenetetrahydrofolate reductase (NADPH) activity)
  - Optional 5-formyl-THF salvage to 5,10-methenyl-THF branch
  - 5-formyl-THF salvage
    - 5-Formyltetrahydrofolate cyclo-ligase (molecular player: Fau/MTHFS 5-formyltetrahydrofolate cyclo-ligases; activity or role: 5-formyltetrahydrofolate cyclo-ligase activity)

## Known Relationships Among Steps

- 5,10-methylene-THF to 5,10-methenyl-THF redox feeds into 5,10-methenyl-THF to 10-formyl-THF hydrolysis: 5,10-methenyl-THF produced by the dehydrogenase reaction is the cyclohydrolase substrate; the two activities are often fused but are chemically distinct.
- 5-formyl-THF salvage feeds into 5,10-methenyl-THF to 10-formyl-THF hydrolysis: Salvaged 5,10-methenyl-THF rejoins the methenyl/formyl carrier-state interconversion.

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

# Folate One-Carbon Carrier-State Interconversion

*A review-style synthesis of the taxon-neutral module that interconverts substituted tetrahydrofolate carrier states*

---

## 1. Executive summary

Tetrahydrofolate (THF) is a molecular "shuttle" that carries a single carbon atom at three oxidation levels—methyl, methylene, and the formyl/methenyl group—between the enzymes that generate one-carbon (C1) units and the enzymes that consume them. This review defines a self-contained biochemical **module** whose only job is to move a bound C1 unit *between* these oxidation states, without loading it onto or removing it from the folate. The module comprises four chemically distinct transformations:

1. **Pyridine-nucleotide-linked oxidation** of 5,10-methylene-THF to 5,10-methenyl-THF (methylene-THF dehydrogenase; NAD+ or NADP+).
2. **Hydrolytic ring opening** of 5,10-methenyl-THF to 10-formyl-THF (methenyl-THF cyclohydrolase).
3. **Reduction** of 5,10-methylene-THF to 5-methyl-THF (methylene-THF reductase, MTHFR)—an optional, physiologically irreversible exit branch.
4. **ATP-dependent salvage** of 5-formyl-THF to 5,10-methenyl-THF (5-formyl-THF cyclo-ligase, MTHFS)—an optional recycling branch that re-injects a stable side-pool into the core.

Steps 1 and 2 form the **obligatory coupled core**: the methenyl intermediate produced by the dehydrogenase is the substrate of the cyclohydrolase, and in most organisms the two activities are fused into one polypeptide (bacterial FolD; eukaryotic MTHFD1/MTHFD2/MTHFD2L). Yet the two chemistries are mechanistically separable—single point mutations can knock out one activity while sparing the other (PMID 25988590). Variation across life is played out along three axes: **redox cofactor** (NAD+ vs NADP+), **enzyme architecture** (fused bifunctional/trifunctional vs monofunctional), and **subcellular compartment** (cytosol vs mitochondrion in eukaryotes). The module's boundaries are important: C1 *loading* (serine hydroxymethyltransferase, glycine cleavage, formate–THF ligase) and C1 *use* (purine, thymidylate, methionine synthesis) are neighboring systems, not part of the module. Below I make the model, its parts, its variants, and its unresolved questions explicit, and flag where claims rest on one organism or assay.

---

## 2. Definition and biological boundaries

### 2.1 What is inside the module

The module is the set of reactions that interconvert **five substituted-THF carrier states**—5,10-methylene-THF, 5,10-methenyl-THF, 10-formyl-THF, 5-methyl-THF, and the salvaged 5-formyl-THF pool—**at the level of the C1 substituent's oxidation state and ring topology**, with the pterin, the p-aminobenzoate, and the (poly)glutamate tail unchanged. Formally:

| Reaction | Substrate → Product | Chemistry | Status |
|---|---|---|---|
| Dehydrogenase (D) | 5,10-CH2-THF ⇌ 5,10-CH+=THF | 2-electron oxidation, hydride to NAD(P)+ | Core, reversible |
| Cyclohydrolase (C) | 5,10-CH+=THF ⇌ 10-CHO-THF | hydrolytic ring opening (add/remove H2O) | Core, reversible |
| Reductase (MTHFR) | 5,10-CH2-THF → 5-CH3-THF | 2-electron reduction via FAD, from NAD(P)H | Optional branch, irreversible in vivo |
| Cyclo-ligase (MTHFS) | 5-CHO-THF → 5,10-CH+=THF | ATP-dependent intramolecular cyclization | Optional branch, irreversible |

The D and C reactions are freely reversible and near-equilibrium; direction is set by the demand pulling on 10-formyl-THF (purine/formyl-Met synthesis) or on 5,10-methylene-THF (thymidylate synthesis). The **methenyl cation (5,10-CH+=THF)** is the shared hub linking all four reactions.

### 2.2 What is adjacent and often conflated—but excluded

- **C1 loading (upstream).** Serine hydroxymethyltransferase (SHMT1/2), the glycine cleavage system (GCS), and formate–THF ligase (FTHFS/Fhs, part of MTHFD1's synthetase domain) *create* 5,10-methylene-THF or 10-formyl-THF from serine, glycine, or formate. These are C1-input reactions and sit outside the module even though FTHFS is physically fused to the D/C core in eukaryotic MTHFD1.
- **C1 use (downstream).** Thymidylate synthase (consumes 5,10-methylene-THF, generating DHF), GAR/AICAR transformylases (consume 10-formyl-THF), and methionine synthase (consumes 5-methyl-THF) draw from the carrier pool but are not interconversion reactions.
- **Redox re-reduction of the folate ring.** Dihydrofolate reductase (DHFR) regenerates THF from DHF after thymidylate synthesis. This restores the *carrier*, not the C1 oxidation state, and is a separate salvage system.
- **The methanopterin analog.** In methanogenic archaea and some methylotrophs the C1 carrier is **tetrahydromethanopterin (H4MPT)**, and the homologous dehydrogenase/cyclohydrolase chemistry operates on H4MPT rather than THF (PMID 32061937). This is a parallel, evolutionarily related module on a different cofactor scaffold and should be distinguished, though it clarifies the deep origin of the chemistry.
- **The tetrahydromethanopterin-independent formaldehyde-oxidation and Wood–Ljungdahl pathways** use the same intermediates but for CO2 fixation/formaldehyde detox; the reactions belong to the module, but the physiological framing differs.

### 2.3 Competing definitions in the literature

Two framing tensions recur. First, whether the "folate cycle" includes MTHFR: metabolically MTHFR is a committed exit toward methylation, so many authors (correctly, in our framing) treat it as a branch rather than part of the reversible core (PMID 27641100). Second, whether the module is defined by *enzyme* (FolD/MTHFD gene products) or by *reaction* (carrier-state chemistry). Because the same chemistry is carried by fused vs monofunctional proteins and by NAD+- vs NADP+-linked variants, the **reaction-centric, taxon-neutral definition adopted here** is the more robust one.

---

## 3. Mechanistic overview

### 3.1 The coupled core: dehydrogenase → cyclohydrolase

The best current model treats D and C as a **tightly coupled but chemically distinct pair**, usually co-localized on one protein that channels the reactive methenyl cation between two active sites:

1. **Dehydrogenase step.** 5,10-methylene-THF (a five-membered imidazolidine ring bridging N5 and N10) is oxidized by transfer of a hydride to NAD(P)+, yielding the aromatic, positively charged 5,10-methenyl-THF cation. This is a near-equilibrium redox step; direction follows the NAD(P)H/NAD(P)+ ratio and downstream pull.
2. **Cyclohydrolase step.** Water adds to the methenyl cation and the N5–C–N10 ring opens to give 10-formyl-THF (a formyl group on N10). No redox change occurs; only hydration/ring topology changes.

**Evidence that the two are separable.** In *E. coli* FolD, structure-guided mutagenesis produces a clean double dissociation: K54S abolishes cyclohydrolase activity while retaining high dehydrogenase activity, whereas R191E retains cyclohydrolase but loses almost all dehydrogenase activity (PMID 25988590). This proves two independent catalytic centers on one chain, justifying counting D and C as two core steps rather than one.

**Directionality in vivo.** The D/C pair runs "backward" (10-formyl-THF → methenyl → methylene) in cytosol when 10-formyl-THF is abundant and thymidylate synthesis demands 5,10-methylene-THF; it runs "forward" (methylene → methenyl → formyl) in mitochondria to generate 10-formyl-THF and, via formyl-THF ligase reversal, **formate for export**. Elegantly, depletion of a single metabolite—10-formyl-THF—is sufficient to reverse net cytosolic flux, showing how thin the thermodynamic margin is (PMID 27211901).

### 3.2 The MTHFR branch (optional, irreversible)

MTHFR is a **flavoprotein** that reduces 5,10-methylene-THF to 5-methyl-THF using electrons from NAD(P)H via a tightly bound FAD. Mechanistically the reductive half-reaction (NAD(P)H → FADH2) and the oxidative half-reaction (FADH2 → 5-methyl-THF) are separable; an active-site aspartate (Asp120 in *E. coli*) tunes flavin reactivity and stabilizes a proposed 5-iminium cation intermediate during folate reduction (PMID 11371182). The reaction is effectively **irreversible in vivo** and commits the C1 unit to methionine/SAM synthesis. It is therefore the module's regulated "off-ramp," not part of the reversible core.

### 3.3 The 5-formyl-THF salvage branch (optional)

5-Formyl-THF (folinic acid, leucovorin) is not produced by the core; it arises as a side-product (e.g., from SHMT abortive turnover) and is a **stable storage/inhibitory form**. MTHFS (5,10-methenyltetrahydrofolate synthetase; Fau in bacteria) uses **ATP** to cyclize 5-formyl-THF back to the 5,10-methenyl cation, re-injecting it into the core hub. This is the only reaction that produces or consumes 5-formyl-THF productively, so failure of MTHFS causes 5-formyl-THF to accumulate to toxic levels (~30-fold in patient fibroblasts), with severe neurological disease (PMID 30031689). The branch is thus best understood as a **detoxifying recycle valve** feeding the methenyl/formyl node.

### 3.4 Obligatory vs conditional vs accessory

- **Obligatory core:** D and C. Every organism using folate C1 metabolism needs interconversion between the methylene/methenyl/formyl states.
- **Conditional:** the *direction* of core flux (compartment- and demand-dependent); dual vs single cofactor use.
- **Accessory/optional:** MTHFR (present only where methyl-THF/SAM output is needed) and MTHFS salvage (present where 5-formyl-THF must be recycled).

---

## 4. Major molecular players and active assemblies

### 4.1 The bifunctional/trifunctional D+C fusions

- **Bacterial FolD** — the canonical NADP+-linked bifunctional methylenetetrahydrofolate dehydrogenase/methenyltetrahydrofolate cyclohydrolase. Essential in many bacteria; its two active sites are separable (PMID 25988590). It interconverts 5,10-methylene-THF and 10-formyl-THF in a single protein.
- **Eukaryotic cytosolic MTHFD1** — a **trifunctional** enzyme (D + C + 10-formyl-THF synthetase). The synthetase domain performs C1 *loading* (formate + THF + ATP → 10-formyl-THF) and is formally outside the module, but the D and C domains are the cytosolic core. Loss-of-function human variants abolish dehydrogenase activity and cause megaloblastic anemia, hyperhomocysteinemia, immunodeficiency, and hemolytic-uremic syndrome (PMID 32414565, PMID 25633902); the common p.Arg653Gln variant is thermolabile and linked to congenital heart and neural-tube risk (PMID 18767138).
- **Mitochondrial MTHFD2** — a **bifunctional D+C** enzyme expressed mainly in embryonic and proliferating (including cancer) cells. It requires inorganic phosphate/Mg2+ and, contrary to older "NAD-only" descriptions, shows **dual NAD+/NADP+ specificity** in purified form (PMID 29225823). Its crystal structure with NAD and a substrate-based inhibitor made it a validated anticancer target (PMID 27899380).
- **Mitochondrial MTHFD2L** — the constitutively expressed adult paralog of MTHFD2, also **dual-specific** (PMID 29225823); its first structure highlighted how similar the three human isozymes' active sites are, complicating selective inhibitor design (PMID 35712863).

### 4.2 Monofunctional variants

- **Monofunctional MtdA** (e.g., *Methylorubrum/Methylobacterium extorquens*) — an NADP-linked methylene dehydrogenase that in methylotrophs acts on both H4-folate and H4-methanopterin substrates, illustrating how the dehydrogenase can exist as a standalone enzyme decoupled from the cyclohydrolase.
- **Monofunctional FchA cyclohydrolase** — a standalone methenyl-THF cyclohydrolase found in some bacteria/archaea, demonstrating that the C activity does not obligatorily co-reside with D. The existence of monofunctional D (MtdA) and monofunctional C (FchA) is the strongest biological proof that fusion is an evolutionary convenience, not a mechanistic requirement.
- **Archaeal/methanogen H4MPT dehydrogenases** — NADP-dependent methylene-H4MPT dehydrogenase performs the same hydride-transfer chemistry on the methanopterin scaffold (PMID 32061937), and a separate H2-dependent methylene-H4MPT dehydrogenase (Hmd) uses no pyridine nucleotide at all—an alternative electron source for the same net transformation.

### 4.3 The reductase and the ligase

- **MTHFR variants.** Compact bacterial **MetF** (NAD(P)H-linked, catalytic domain only); plant **MTHFR** (e.g., Arabidopsis MTHFR2, NADH-linked, with regulatory architecture); and human **MTHFR** (NADPH-linked, with an appended SAM-sensing regulatory domain). Cryo-EM of human MTHFR shows a dual-SAM/single-SAH switch that reorients the catalytic domain and blocks substrate access—an allosteric brake absent from the bacterial enzyme (PMID 38622112).
- **MTHFS/Fau cyclo-ligase.** ATP-dependent; the only enzyme handling 5-formyl-THF. Human deficiency is a Mendelian neurometabolic disease (PMID 30031689).

### 4.4 Physical assemblies

The core enzymes are typically **homodimers** (FolD, MTHFD2). Fusion and dimerization favor **substrate channeling** of the labile methenyl cation, which is chemically unstable in bulk solution. In eukaryotes the enzymes are further organized by compartment (see §5) and, for cytosolic C1 enzymes, can associate into higher-order "purinosome"-type assemblies with downstream users—an association relevant to flux but not part of the interconversion chemistry itself.

---

## 5. Evolutionary and cell-biological variation

### 5.1 Across lineages

- **Bacteria:** usually a single bifunctional NADP+-linked FolD; some also have monofunctional D (MtdA) and/or C (FchA) and a compact NAD(P)H MTHFR (MetF).
- **Archaea/methanogens:** the homologous chemistry runs on H4MPT; dehydrogenases include NADP-linked and H2-linked (Hmd) forms (PMID 32061937). This lineage best preserves the ancestral "carrier-state redox + hydrolysis" logic on a non-folate scaffold.
- **Fungi/plants:** multiple MTHFD isozymes partition between cytosol, mitochondria, and (plants) plastids; plant MTHFRs (MTHFR1/2) are NADH-linked and differently regulated than the human NADPH enzyme.
- **Animals:** three D+C isozymes—cytosolic trifunctional MTHFD1, mitochondrial MTHFD2 (developmental/proliferative) and MTHFD2L (adult)—plus a single SAM-regulated NADPH-MTHFR.

### 5.2 Compartment and cell state (best-supported eukaryotic variation)

The mammalian system is spatially split. The **mitochondrial** D/C flux runs oxidatively to make 10-formyl-THF and export **formate**, simultaneously generating NAD(P)H, glycine, and ATP-equivalents (PMID 31289137); the **cytosolic** flux typically runs reductively (formate → 10-formyl-THF → methenyl → methylene) to feed thymidylate and, via MTHFR, methionine. Crucially, these are **redundant at the pathway level**: CRISPR knockout of the mitochondrial pathway reverses cytosolic flux and sustains growth in nutrient-replete conditions, with loss of *both* being lethal to tumor xenografts (PMID 27211901). Cell-state variation is stark: **MTHFD2 is an embryonic/proliferation-restricted isozyme** essentially silent in healthy adult tissue but strongly re-expressed in cancer—hence its appeal as a selective drug target that spares normal cells (PMID 27899380, PMID 35712863).

### 5.3 Conservation and deepest plausible origin

The **carrier-state redox+hydrolysis chemistry is ancient and near-universal**, but the specific cofactor scaffold and enzyme fusions are lineage-elaborations. Several lines of reasoning (offered here as inference, since direct phylogenetic studies were beyond the literature retrievable for this review) frame the origin:

- **Most conserved element:** the two core reactions (methylene↔methenyl oxidation; methenyl↔formyl hydrolysis) recur on *both* the folate and the methanopterin scaffolds (PMID 32061937), and the analogous C1 chemistry is central to the Wood–Ljungdahl (reductive acetyl-CoA) pathway that is frequently argued to be among the most ancient carbon-fixation routes. This makes the **dehydrogenase/cyclohydrolase carrier-state interconversion the ancient, conserved kernel**, plausibly predating the folate/methanopterin split.
- **Best ancestral representatives:** among the expanded MTHFD family, the **monofunctional dehydrogenase (MtdA-type) and monofunctional cyclohydrolase (FchA-type)** and the compact bacterial **FolD** are better proxies for the ancestral, standalone activities than the eukaryotic **trifunctional MTHFD1** (which acquired a fused formyl-THF synthetase domain) or the developmentally restricted **MTHFD2/MTHFD2L** (later gene duplications with compartmental and cofactor specialization). The pyridine-nucleotide-binding (Rossmann-type) and catalytic folds are shared, consistent with descent from a common dehydrogenase ancestor.
- **Later elaborations / lineage-specific changes:** (i) domain fusion (FolD→trifunctional MTHFD1; and separately the FTHFS synthetase capture); (ii) the eukaryotic **MTHFR regulatory domain** that grafts SAM feedback onto a conserved catalytic core absent in bacterial MetF (PMID 38622112); (iii) gene **duplication and subfunctionalization** producing cytosolic vs mitochondrial isozymes with distinct NAD+/NADP+ preferences (PMID 29225823); and (iv) lineage-specific **losses**—e.g., organisms relying on formyl-THF ligase for 10-formyl-THF can tolerate reduced FolD dependence.
- **Uncertainty:** whether the folate or the methanopterin carrier is ancestral, and the exact order of fusion events, remains genuinely unsettled; the claims above should be read as the most parsimonious interpretation rather than established phylogeny.

### 5.4 Alternative routes to the same outcome

The net conversion 5,10-methylene-THF → 10-formyl-THF can be achieved by: (i) fused FolD/MTHFD; (ii) separate MtdA + FchA; or (iii) bypassed entirely, since 10-formyl-THF can also be made directly by formyl-THF ligase from formate (a *loading* reaction outside the module). Likewise the dehydrogenase electron acceptor can be NAD+, NADP+, both (MTHFD2/2L), or H2 (Hmd)—different molecular means, same carrier-state change.

---

## 6. Constraints, dependencies, and failure modes

### 6.1 Ordering constraints

- **D precedes C in the oxidative direction** and C precedes D in the reductive direction: 10-formyl-THF and 5,10-methylene-THF **cannot interconvert directly**; they must pass through the 5,10-methenyl cation hub. This is an obligatory two-step topology.
- **MTHFS salvage rejoins only at the methenyl node**, not at the methylene or formyl states—5-formyl-THF is chemically re-cyclized to the methenyl cation, then enters the core.
- **MTHFR draws only from 5,10-methylene-THF**, never from methenyl or formyl states; it is the sole exit from the methylene pool toward methyl-THF.

### 6.2 Mutually exclusive / directional constraints

- The MTHFR reduction is **thermodynamically one-way** in vivo; 5-methyl-THF cannot be reoxidized to methylene-THF within the module (it leaves only via methionine synthase, a downstream, B12-dependent reaction). This creates the classic **"methyl-folate trap."** The trap is directly documented in humans: a B12-deficient patient homozygous for MTHFR C677T had 94.5% of red-cell folate stranded as 5-methyl-THF (vs 67.4% after B12 repletion), with reduced total folate, shorter polyglutamate tails, and 22% lower global DNA methylation (PMID 16445837); nitrous-oxide inactivation of methionine synthase in rats reproduces the 5-methyl-THF build-up at the expense of formyl-THF and THF (PMID 3947060). Because MTHFR is not reversible, blocking the sole downstream exit strands the whole carrier pool and starves the interconversion core—an ordering/irreversibility constraint imposed by a reaction *outside* the module.
- Compartmental flux directions are effectively mutually exclusive per organelle at steady state, set by local NAD(P)H/NAD(P)+ ratios and 10-formyl-THF levels (PMID 27211901).

### 6.3 Substrate/chemistry constraints

- The **5,10-methenyl cation is labile**; enzymatic channeling (fusion, dimer interfaces) protects it, which is a plausible selective driver of the FolD/MTHFD fusion.
- **5-Formyl-THF is a stable inhibitor/dead-end** of several folate enzymes; without ATP-dependent MTHFS salvage it accumulates and is toxic (PMID 30031689). This rules out a "do-nothing" tolerance of 5-formyl-THF accumulation.

### 6.4 Failure modes (human disease as natural knockouts)

- **MTHFD1 deficiency:** loss of cytosolic D activity → megaloblastic anemia, hyperhomocysteinemia, immunodeficiency, HUS (PMID 32414565, PMID 25633902); hypomorphic p.Arg653Gln raises congenital-heart/neural-tube risk via thermolability (PMID 18767138).
- **MTHFR deficiency / C677T thermolabile variant:** reduced 5-methyl-THF → hyperhomocysteinemia, neural-tube and vascular risk; the branch's regulation by SAM (PMID 38622112) contextualizes why partial loss perturbs methylation homeostasis.
- **MTHFS deficiency:** 5-formyl-THF toxicity → microcephaly, epilepsy, hypomyelination; paradoxically worsened by folinic acid (which raises 5-formyl-THF) (PMID 30031689).

These natural experiments confirm the module's wiring: each branch's loss produces the metabolite-accumulation phenotype predicted by the topology.

---

## 7. Controversies and open questions

1. **Redox-cofactor identity of MTHFD2 in vivo.** MTHFD2 was long labeled "NAD-dependent," but purified enzyme is **dual NAD+/NADP+-specific** (PMID 29225823). Which cofactor dominates in the intact mitochondrion—and hence whether MTHFD2 is primarily an NADH or NADPH producer—remains debated and likely context-dependent.
2. **Degree and necessity of substrate channeling.** Whether the methenyl cation is truly channeled between the D and C sites (vs released and re-bound) is not fully resolved; the separable-mutant data (PMID 25988590) show independence but not the absence of channeling.
3. **Directionality control.** The finding that a single metabolite (10-formyl-THF) can flip net cytosolic flux (PMID 27211901) raises unanswered questions about how robustly cells sense and set direction across compartments and cell types.
4. **Isozyme-selective pharmacology.** The near-identical active sites of MTHFD1/MTHFD2/MTHFD2L (PMID 35712863) make truly selective MTHFD2 inhibition an open medicinal-chemistry problem despite validated target biology.
5. **Physiological role and origin of 5-formyl-THF.** Its exact cellular source, its signaling/regulatory role (beyond inhibition), and why a dedicated ATP-burning salvage evolved are incompletely understood.
6. **Trap vs "active-formate" theories of B12–folate coupling.** The megaloblastic anemia of B12 deficiency was historically explained either by the methyl-folate trap (5-methyl-THF stranding) or by a competing "active-formate/formyl-THF depletion" theory. Deoxyuridine-suppression experiments showing that THF itself corrects the defect favor the trap interpretation (PMID 8518179), but the two are not fully mutually exclusive and the debate illustrates how indirect much of the classic human evidence is.
7. **Cross-organism extrapolation.** Much mechanism comes from *E. coli* (MTHFR, FolD), human cancer lines (MTHFD2), and methanogens (H4MPT enzymes). Kinetic and regulatory details are **not safely generalized** across these systems—e.g., bacterial MetF lacks the SAM-regulatory domain of human MTHFR (PMID 38622112).

---

## 8. Key references

- Ducker GS, Rabinowitz JD. **One-Carbon Metabolism in Health and Disease.** *Cell Metab* 2017. PMID 27641100. — Authoritative review of compartmentalized folate C1 metabolism.
- Ducker GS, et al. **Reversal of Cytosolic One-Carbon Flux Compensates for Loss of the Mitochondrial Folate Pathway.** *Cell Metab* 2016. PMID 27211901. — Flux directionality and 10-formyl-THF as the switch.
- Sah S, Varshney U. **Impact of Mutating the Key Residues of a Bifunctional 5,10-Methylenetetrahydrofolate Dehydrogenase-Cyclohydrolase from E. coli...** 2015. PMID 25988590. — Separable D and C active sites.
- Shin M, Momb J, Appling DR. **Human mitochondrial MTHFD2 is a dual redox cofactor-specific methylenetetrahydrofolate dehydrogenase/cyclohydrolase.** 2017. PMID 29225823. — NAD+/NADP+ dual specificity of MTHFD2/2L.
- Gustafsson R, et al. **Crystal Structure of the Emerging Cancer Target MTHFD2 in Complex with a Substrate-Based Inhibitor.** *Cancer Res* 2017. PMID 27899380.
- Scaletti ER, et al. **The First Structure of Human MTHFD2L...** 2022. PMID 35712863. — Isoform-selectivity challenge.
- Blomgren J, et al. **Dynamic inter-domain transformations mediate the allosteric regulation of human MTHFR.** 2024. PMID 38622112. — SAM-feedback cryo-EM mechanism.
- Trimmer EE, Ballou DP, Ludwig ML, Matthews RG. **Folate activation and catalysis in MTHFR from E. coli: roles for Asp120 and Glu28.** 2001. PMID 11371182. — Flavin mechanism of the reductase.
- Rodan LH, et al. **5,10-methenyltetrahydrofolate synthetase deficiency...** 2018. PMID 30031689. — MTHFS salvage, 5-formyl-THF toxicity.
- Bidla G, et al. **Biochemical analysis of patients with MTHFD1 deficiency.** 2020. PMID 32414565; Burda P, et al. 2015. PMID 25633902; Christensen KE, et al. **MTHFD1 p.Arg653Gln...** 2009. PMID 18767138. — MTHFD1 human genetics.
- Huang G, et al. **The Hydride Transfer Process in NADP-dependent Methylene-tetrahydromethanopterin Dehydrogenase.** 2020. PMID 32061937. — Archaeal H4MPT homolog.
- Dekhne AS, et al. 2019. PMID 31289137. — Mitochondrial C1 outputs (glycine, NAD(P)H, ATP, C1 units).
- Watkins D, Rosenblatt DS. **Vitamin responsive disorders of folate transport and metabolism.** 2012. PMID 22108709. — Inborn errors overview.
- Smulders YM, et al. **Cellular folate vitamer distribution during and after correction of vitamin B12 deficiency: a case for the methylfolate trap.** 2006. PMID 16445837. — First human demonstration of the trap.
- Hoffbrand AV, Jackson BF. **Correction of the DNA synthesis defect in vitamin B12 deficiency by tetrahydrofolate...** 1993. PMID 8518179. — Evidence favoring the trap over the active-formate theory.
- Wilson SD, Horne DW. **Effect of nitrous oxide inactivation of vitamin B12 on folate coenzymes in rat tissues.** 1986. PMID 3947060. — Animal support for the trap.

---

*Uncertainty note:* Kinetic and regulatory statements are anchored where possible to purified-enzyme or structural studies in a named organism. Extrapolation across bacteria, archaea (H4MPT), plants, and mammals is flagged in §5–§7 and should not be read as universal.


## Artifacts

- [OpenScientist final report](folate_one_carbon_interconversion-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](folate_one_carbon_interconversion-deep-research-openscientist_artifacts/final_report.pdf)