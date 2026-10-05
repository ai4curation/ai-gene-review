---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T13:26:12.249777'
end_time: '2026-09-01T14:12:07.773713'
duration_seconds: 2755.52
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Gram-negative bacterial post-translational Sec protein export
  module_summary: A reusable bacterial protein-export module in which SecB carries
    an unfolded precursor to the SecA ATPase, SecA drives the precursor into the SecYEG
    protein-conducting channel, optional SecDF associated with YajC uses proton motive
    force to improve late-stage translocation, and signal peptidase I removes the
    N-terminal signal peptide. The module models the canonical post-translational
    route used by Gram-negative bacteria. Cotranslational SRP targeting, YidC-dependent
    membrane insertion, Tat export of folded proteins, lipoprotein maturation, and
    outer-membrane secretion are neighboring modules.
  module_outline: "- Gram-negative bacterial post-translational Sec protein export\n\
    \  - 1. ATP-independent precursor carriage and SecA delivery\n  - SecB carriage\
    \ of an unfolded export precursor\n    - SecB unfolded-preprotein carrier (molecular\
    \ player: bacterial SecB family; activity or role: unfolded protein holdase activity)\n\
    \  - 2. ATP-driven precursor engagement and translocation motor\n  - SecA ATP-driven\
    \ protein-export motor\n    - SecA protein-exporting ATPase (molecular player:\
    \ bacterial SecA family; activity or role: protein-exporting ATPase activity)\n\
    \  - 3. inner-membrane protein-conducting channel\n  - SecYEG protein-conducting\
    \ channel\n    - SecY pore-forming channel subunit (molecular player: SecY/Sec61-alpha\
    \ family; activity or role: protein transmembrane transporter activity)\n    -\
    \ SecE channel-clamp subunit (molecular player: bacterial SecE family; activity\
    \ or role: contributes to protein transmembrane transporter activity)\n    - SecG\
    \ channel accessory subunit (molecular player: bacterial SecG family; activity\
    \ or role: contributes to protein transmembrane transporter activity)\n  - 4.\
    \ proton-motive-force-assisted translocation completion\n  - SecDF-YajC accessory\
    \ translocation complex\n    - SecD PMF-coupled accessory subunit (molecular player:\
    \ bacterial SecD subfamily; activity or role: contributes to proton motive force\
    \ dependent protein transmembrane transporter activity)\n    - SecF PMF-coupled\
    \ accessory subunit (molecular player: bacterial SecF subfamily; activity or role:\
    \ contributes to proton motive force dependent protein transmembrane transporter\
    \ activity)\n    - YajC complex-associated subunit (molecular player: bacterial\
    \ YajC family)\n  - 5. type I signal-peptide cleavage\n  - LepB cleavage of the\
    \ type I signal peptide\n    - LepB signal peptidase I (molecular player: bacterial\
    \ signal peptidase I family; activity or role: signal peptidase activity)"
  module_connections: '- SecB carriage of an unfolded export precursor feeds into
    SecA ATP-driven protein-export motor

    - SecA ATP-driven protein-export motor feeds into SecYEG protein-conducting channel

    - SecDF-YajC accessory translocation complex promotes SecYEG protein-conducting
    channel: SecDF uses proton motive force to improve late-stage translocation through
    SecYEG; this accessory route is not obligatory for every substrate.

    - SecYEG protein-conducting channel feeds into LepB cleavage of the type I signal
    peptide'
  pathway_query: ppu03060
  pathway_id: ppu03060
  pathway_name: Protein export
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu03060 with 19 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '19'
  candidate_genes: '- yidC: PP_0006 | P0A140 | Membrane protein insertase YidC (Foldase
    YidC) (Membrane integrase YidC) (Membrane protein YidC) (primary bucket kegg:ppu03060)

    - secE: PP_0441 | Q88QP7 | Protein translocase subunit SecE (primary bucket kegg:ppu03060)

    - secY: PP_0474 | Q88QL5 | Protein translocase subunit SecY (primary bucket kegg:ppu03060)

    - lspA: PP_0604 | Q88Q91 | Lipoprotein signal peptidase (EC 3.4.23.36) (Prolipoprotein
    signal peptidase) (Signal peptidase II) (SPase II) (EC 3.4.23.36; primary bucket
    kegg:ppu03060)

    - yajC: PP_0834 | Q88PL6 | Sec translocon accessory complex subunit YajC (primary
    bucket kegg:ppu03060)

    - secD: PP_0835 | Q88PL5 | Protein translocase subunit SecD (primary bucket kegg:ppu03060)

    - secF: PP_0836 | Q88PL4 | Protein-export membrane protein SecF (primary bucket
    kegg:ppu03060)

    - tatC-I: PP_1039 | Q88P14 | Sec-independent protein translocase protein TatC
    (primary bucket kegg:ppu03060)

    - tatB-I: PP_1040 | Q88P13 | Sec-independent protein translocase TatB (primary
    bucket kegg:ppu03060)

    - tatA-I: PP_1041 | Q88P12 | Sec-independent protein translocase protein TatA
    (primary bucket kegg:ppu03060)

    - secA: PP_1345 | Q88N69 | Protein translocase subunit SecA (EC 7.4.2.8) (EC 7.4.2.8;
    primary bucket kegg:ppu03060)

    - lepB: PP_1432 | Q88MY6 | Signal peptidase I (EC 3.4.21.89) (EC 3.4.21.89; primary
    bucket kegg:ppu03060)

    - ffh: PP_1461 | Q88MV7 | Signal recognition particle protein (EC 3.6.5.4) (Fifty-four
    homolog) (EC 3.6.5.4; primary bucket kegg:ppu03060)

    - tatA-II: PP_5016 | Q88D13 | Sec-independent protein translocase protein TatA
    (primary bucket kegg:ppu03060)

    - tatB: PP_5017 | Q88D12 | Sec-independent protein translocase protein TatB (primary
    bucket kegg:ppu03060)

    - tatC-II: PP_5018 | Q88D11 | Sec-independent protein translocase protein TatC
    (primary bucket kegg:ppu03060)

    - secB: PP_5053 | Q88CX7 | Protein-export protein SecB (primary bucket kegg:ppu03060)

    - ftsY: PP_5111 | Q88CR9 | Signal recognition particle receptor FtsY (SRP receptor)
    (EC 3.6.5.4) (EC 3.6.5.4; primary bucket kegg:ppu03060)

    - secG: PP_5706 | A0A140FWQ9 | Protein-export membrane protein SecG (primary bucket
    kegg:ppu03060)'
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_sec_posttranslational_protein_export__ppu03060-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_sec_posttranslational_protein_export__ppu03060-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Gram-negative bacterial post-translational Sec protein export in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu03060
- Resolved ID: ppu03060
- Resolved name: Protein export
- Source: KEGG

Resolved local bucket kegg:ppu03060 with 19 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 19

- yidC: PP_0006 | P0A140 | Membrane protein insertase YidC (Foldase YidC) (Membrane integrase YidC) (Membrane protein YidC) (primary bucket kegg:ppu03060)
- secE: PP_0441 | Q88QP7 | Protein translocase subunit SecE (primary bucket kegg:ppu03060)
- secY: PP_0474 | Q88QL5 | Protein translocase subunit SecY (primary bucket kegg:ppu03060)
- lspA: PP_0604 | Q88Q91 | Lipoprotein signal peptidase (EC 3.4.23.36) (Prolipoprotein signal peptidase) (Signal peptidase II) (SPase II) (EC 3.4.23.36; primary bucket kegg:ppu03060)
- yajC: PP_0834 | Q88PL6 | Sec translocon accessory complex subunit YajC (primary bucket kegg:ppu03060)
- secD: PP_0835 | Q88PL5 | Protein translocase subunit SecD (primary bucket kegg:ppu03060)
- secF: PP_0836 | Q88PL4 | Protein-export membrane protein SecF (primary bucket kegg:ppu03060)
- tatC-I: PP_1039 | Q88P14 | Sec-independent protein translocase protein TatC (primary bucket kegg:ppu03060)
- tatB-I: PP_1040 | Q88P13 | Sec-independent protein translocase TatB (primary bucket kegg:ppu03060)
- tatA-I: PP_1041 | Q88P12 | Sec-independent protein translocase protein TatA (primary bucket kegg:ppu03060)
- secA: PP_1345 | Q88N69 | Protein translocase subunit SecA (EC 7.4.2.8) (EC 7.4.2.8; primary bucket kegg:ppu03060)
- lepB: PP_1432 | Q88MY6 | Signal peptidase I (EC 3.4.21.89) (EC 3.4.21.89; primary bucket kegg:ppu03060)
- ffh: PP_1461 | Q88MV7 | Signal recognition particle protein (EC 3.6.5.4) (Fifty-four homolog) (EC 3.6.5.4; primary bucket kegg:ppu03060)
- tatA-II: PP_5016 | Q88D13 | Sec-independent protein translocase protein TatA (primary bucket kegg:ppu03060)
- tatB: PP_5017 | Q88D12 | Sec-independent protein translocase protein TatB (primary bucket kegg:ppu03060)
- tatC-II: PP_5018 | Q88D11 | Sec-independent protein translocase protein TatC (primary bucket kegg:ppu03060)
- secB: PP_5053 | Q88CX7 | Protein-export protein SecB (primary bucket kegg:ppu03060)
- ftsY: PP_5111 | Q88CR9 | Signal recognition particle receptor FtsY (SRP receptor) (EC 3.6.5.4) (EC 3.6.5.4; primary bucket kegg:ppu03060)
- secG: PP_5706 | A0A140FWQ9 | Protein-export membrane protein SecG (primary bucket kegg:ppu03060)

## Generic Module Context

### Working Scope

A reusable bacterial protein-export module in which SecB carries an unfolded precursor to the SecA ATPase, SecA drives the precursor into the SecYEG protein-conducting channel, optional SecDF associated with YajC uses proton motive force to improve late-stage translocation, and signal peptidase I removes the N-terminal signal peptide. The module models the canonical post-translational route used by Gram-negative bacteria. Cotranslational SRP targeting, YidC-dependent membrane insertion, Tat export of folded proteins, lipoprotein maturation, and outer-membrane secretion are neighboring modules.

### Provisional Biological Outline

- Gram-negative bacterial post-translational Sec protein export
  - 1. ATP-independent precursor carriage and SecA delivery
  - SecB carriage of an unfolded export precursor
    - SecB unfolded-preprotein carrier (molecular player: bacterial SecB family; activity or role: unfolded protein holdase activity)
  - 2. ATP-driven precursor engagement and translocation motor
  - SecA ATP-driven protein-export motor
    - SecA protein-exporting ATPase (molecular player: bacterial SecA family; activity or role: protein-exporting ATPase activity)
  - 3. inner-membrane protein-conducting channel
  - SecYEG protein-conducting channel
    - SecY pore-forming channel subunit (molecular player: SecY/Sec61-alpha family; activity or role: protein transmembrane transporter activity)
    - SecE channel-clamp subunit (molecular player: bacterial SecE family; activity or role: contributes to protein transmembrane transporter activity)
    - SecG channel accessory subunit (molecular player: bacterial SecG family; activity or role: contributes to protein transmembrane transporter activity)
  - 4. proton-motive-force-assisted translocation completion
  - SecDF-YajC accessory translocation complex
    - SecD PMF-coupled accessory subunit (molecular player: bacterial SecD subfamily; activity or role: contributes to proton motive force dependent protein transmembrane transporter activity)
    - SecF PMF-coupled accessory subunit (molecular player: bacterial SecF subfamily; activity or role: contributes to proton motive force dependent protein transmembrane transporter activity)
    - YajC complex-associated subunit (molecular player: bacterial YajC family)
  - 5. type I signal-peptide cleavage
  - LepB cleavage of the type I signal peptide
    - LepB signal peptidase I (molecular player: bacterial signal peptidase I family; activity or role: signal peptidase activity)

### Known Relationships Among Steps

- SecB carriage of an unfolded export precursor feeds into SecA ATP-driven protein-export motor
- SecA ATP-driven protein-export motor feeds into SecYEG protein-conducting channel
- SecDF-YajC accessory translocation complex promotes SecYEG protein-conducting channel: SecDF uses proton motive force to improve late-stage translocation through SecYEG; this accessory route is not obligatory for every substrate.
- SecYEG protein-conducting channel feeds into LepB cleavage of the type I signal peptide

## Assignment

Write a species-aware review of this module/pathway in the target organism. The
goal is not a generic pathway essay; the goal is to support manual module
satisfiability and gene annotation curation.

Treat the candidate gene list as a starting point, not ground truth. Use the
literature and authoritative resources to decide whether each expected pathway
step is present, absent, ambiguous, replaced by a lineage-specific alternative,
or represented by a likely over-propagated annotation.

Prioritize direct evidence from the target species/strain. When using evidence
from related organisms, state the organism and explain whether transfer to the
target taxon is strong, weak, or uncertain. Distinguish *Pseudomonas putida*
KT2440 evidence from broader *Pseudomonas* or generic bacterial evidence.

## Questions To Address

1. **Pathway boundaries**
   - What exact biochemical or cellular process is included?
   - Which neighboring pathways or broad overview maps should be kept separate?
   - Are there alternate names or database-specific definitions for this pathway?

2. **Satisfiability in the target taxon**
   - Which expected steps are encoded by candidate genes?
   - Which steps are missing from the metadata but likely present under a
     different gene name, paralog, or enzyme family?
   - Which steps are probably not expected in this organism?

3. **Candidate gene assessment**
   - For each high-confidence gene, summarize the likely role, evidence type,
     and any curation-relevant caveats.
   - Identify paralog ambiguity, broad EC/GO mappings, and likely annotation
     over-propagation.
   - Note genes that should be promoted to full `fetch-gene` review.

4. **Module implications**
   - What module steps should be marked covered, candidate_uncertain, gap,
     not_expected_in_target_taxon, or module_needs_revision?
   - Are existing generic module boundaries wrong for this organism?
   - Are new module documents or GO term requests likely needed?

5. **Evidence and open questions**
   - Which conclusions are supported by direct experiments?
   - Which are inferred from homology, pathway databases, or neighboring genes?
   - What experiments or expert questions would resolve the important gaps?

## Output Format

Use concise review sections:

1. Executive summary
2. Target-organism pathway definition
3. Expected step model
4. Candidate genes and evidence
5. Gaps, ambiguities, and likely over-annotations
6. Module and GO-curation recommendations
7. Genes to promote to full review
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty, species transfer, and whether evidence is direct for the target
organism.

## Output

# Module/Pathway/Taxon Review: Post-translational Sec Protein Export in *Pseudomonas putida* KT2440

**Review topic:** Gram-negative bacterial post-translational Sec protein export
**Target taxon:** *Pseudomonas putida* KT2440 (organism code PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG `ppu03060` "Protein export" (19 primary genes; module area `other_kegg_pathway`)

---

## Summary

The Gram-negative post-translational Sec protein-export module is **fully satisfiable** in *Pseudomonas putida* KT2440. Every one of the five expected module steps — (1) ATP-independent precursor carriage by SecB, (2) the SecA ATPase motor, (3) the SecYEG protein-conducting channel, (4) the SecDF–YajC proton-motive-force accessory complex, and (5) type I signal-peptide cleavage by LepB — maps to a distinct, correctly annotated, **single-copy** gene in the KT2440 proteome. There is no paralog ambiguity in the core machinery, no evidence of a second (SecA2-type) translocase, and the SecDF–YajC subunits are encoded as an adjacent `yajC–secD–secF` operon (PP_0834–PP_0836) with separate (non-fused) SecD and SecF proteins. All five core module steps should be marked **covered** with high confidence.

The principal curation problem is **not** a missing step but **boundary over-inclusion** in the KEGG bucket. Of the 19 genes in `ppu03060`, only **9** belong to the generic post-translational Sec module (secB, secA, secY, secE, secG, secD, secF, yajC, lepB). The remaining **10** belong to neighboring modules that KEGG's "Protein export" superset map deliberately co-locates: cotranslational SRP targeting (ffh, ftsY), the YidC membrane insertase (yidC), two paralogous twin-arginine (Tat) translocase clusters (tat-I and tat-II, six genes), and lipoprotein signal peptidase II (lspA). These should be routed to their own module documents rather than counted against the Sec module.

Evidence quality is mixed but adequate for a "covered" verdict. The core Sec calls rest on **strong homology plus curated Swiss-Prot review** in UniProt rather than direct KT2440 genetics — no genome-scale essentiality or knockout dataset for secA/secY/secE/secB/lepB in this strain was located. The strongest *direct* KT2440 experimental evidence concerns the **neighboring** Tat module: both Tat clusters were experimentally shown to translocate the phosphatase substrate UxpB, and tat-1 is phosphate-regulated (PMID 23530902). Recommended genes to promote to full `fetch-gene` review: **tatB-I (PP_1040)** (no UniProt recommended name), **secG (PP_5706)** (TrEMBL-only accession), and **lepB (PP_1432)** (broad EC/GO mapping shared conceptually with the SRP/Tat outputs).

---

## Target-Organism Pathway Definition

### What the module includes

The post-translational Sec module in KT2440 models the **canonical Gram-negative route for exporting unfolded periplasmic and outer-membrane precursor proteins across the inner membrane**:

- A cytoplasmic **holdase (SecB)** binds an unfolded preprotein and prevents premature folding.
- SecB delivers the precursor to the **SecA ATPase motor**, which docks on the translocon.
- SecA uses cycles of ATP binding/hydrolysis to push the polypeptide through the **SecYEG protein-conducting channel** in the inner membrane.
- The **SecDF–YajC accessory complex** uses the **proton motive force (PMF)** to improve late-stage translocation; this route is helpful but **not obligatory** for every substrate.
- **Signal peptidase I (LepB)** cleaves the N-terminal type I signal peptide on the periplasmic face, releasing the mature protein.

The molecular logic is well established biochemically: *"In bacteria, the SecA ATPase peripherally associates with the SecYEG channel to form the translocase that mediates preprotein export"* ([PMID: 41652145](https://pubmed.ncbi.nlm.nih.gov/41652145/)); and *"signal peptide-bearing precursors are recognized by the SecA ATPase and pushed across the membrane through a translocon channel made of the proteins SecY, SecE, and SecG"* ([PMID: 39817767](https://pubmed.ncbi.nlm.nih.gov/39817767/)).

### Neighboring pathways to keep separate

The KEGG map `ppu03060` "Protein export" is deliberately a **superset** that pools several export routes. For module curation these must be kept distinct:

| Neighboring module | KT2440 genes in the bucket | Why separate |
|---|---|---|
| Cotranslational SRP targeting | ffh (PP_1461), ftsY (PP_5111) | Ribosome-coupled targeting; feeds SecYEG but is a distinct targeting decision, not post-translational carriage |
| YidC membrane insertase | yidC (PP_0006) | Inserts inner-membrane proteins, often Sec-independent |
| Tat folded-protein export | tatABC-I (PP_1039/1040/1041); tatA/B/C-II (PP_5016/5017/5018) | Transports **folded** proteins using PMF; mechanistically orthogonal to Sec |
| Lipoprotein maturation | lspA (PP_0604) | Signal peptidase II cleaves lipoprotein signal peptides, not type I |

### Alternate names / database definitions

- **KEGG:** map03060 / ppu03060 "Protein export" (broad; includes Sec, SRP, Tat, YidC, and both signal peptidases).
- **GO / module framing:** the target module is the narrower "post-translational protein targeting to membrane, translocation" / SecB-dependent Sec route.
- **Gene synonyms:** LepB = signal peptidase I = SPase I (EC 3.4.21.89); LspA = signal peptidase II = SPase II = prolipoprotein signal peptidase (EC 3.4.23.36); Ffh = "fifty-four homolog" (SRP54 homolog); FtsY = SRP receptor.

---

## Expected Step Model

```
 Post-translational Sec export in P. putida KT2440
 ─────────────────────────────────────────────────────────────────

  [unfolded preprotein in cytoplasm]
            │
   (1) SecB holdase  ── PP_5053 (Q88CX7, reviewed) ──┐  ATP-independent carriage
            │                                          │
   (2) SecA ATPase   ── PP_1345 (Q88N69, reviewed) ───┘  EC 7.4.2.8 motor
            │
   (3) SecYEG channel:
        SecY  PP_0474 (Q88QL5)     pore-forming subunit
        SecE  PP_0441 (Q88QP7)     channel clamp
        SecG  PP_5706 (A0A140FWQ9) accessory
            │
   (4) SecDF–YajC accessory  (yajC–secD–secF operon, PP_0834–0836):
        YajC  PP_0834 (Q88PL6)
        SecD  PP_0835 (Q88PL5)   ── separate, NOT fused ──
        SecF  PP_0836 (Q88PL4)              (PMF-assisted, optional)
            │
   (5) LepB signal peptidase I ── PP_1432 (Q88MY6) ── EC 3.4.21.89
            │
  [mature periplasmic / OM-destined protein]
```

Every step is filled by exactly one KT2440 candidate gene. The SecDF–YajC step is architecturally notable: KT2440 encodes **separate SecD and SecF** (not a SecDF fusion as seen in some bacteria) in a compact operon with YajC, consistent with the canonical Gram-negative arrangement. The step relationships in the generic module — SecB feeds SecA, SecA feeds SecYEG, SecDF-YajC promotes SecYEG, SecYEG feeds LepB — all hold in KT2440 with each node populated.

---

## Key Findings

### F001 — All five core post-translational Sec export steps are encoded in KT2440

A UniProt proteome search (UP000000556, taxon 160488) returns one-to-one candidate genes for every module step, and each annotation matches the expected family assignment. This is the foundational satisfiability result: the module is not merely propagated by pathway inference — every step has a concrete, correctly-named gene product.

| Step | Gene | Locus | UniProt | Status | Notes |
|---|---|---|---|---|---|
| SecB carrier | secB | PP_5053 | Q88CX7 (reviewed) | Covered | Presence confirms the **post-translational** route is real |
| SecA motor | secA | PP_1345 | Q88N69 (reviewed) | Covered | EC 7.4.2.8; single copy, no SecA2 |
| SecY pore | secY | PP_0474 | Q88QL5 | Covered | Single translocon |
| SecE clamp | secE | PP_0441 | Q88QP7 | Covered | |
| SecG accessory | secG | PP_5706 | A0A140FWQ9 | Covered | TrEMBL-only accession → promote |
| SecD | secD | PP_0835 | Q88PL5 | Covered | Separate (non-fused) SecD |
| SecF | secF | PP_0836 | Q88PL4 | Covered | Adjacent to secD |
| YajC | yajC | PP_0834 | Q88PL6 | Covered | Heads the yajC–secD–secF operon |
| LepB SPase I | lepB | PP_1432 | Q88MY6 | Covered | EC 3.4.21.89 → promote (broad EC/GO) |

The canonical translocase architecture these genes encode is exactly the SecA + SecYEG assembly described biochemically: *"In bacteria, the SecA ATPase peripherally associates with the SecYEG channel to form the translocase that mediates preprotein export"* ([PMID: 41652145](https://pubmed.ncbi.nlm.nih.gov/41652145/)). The genome/proteome from which these PP_ loci derive is the KT2440 reference genome: *"Sequence analysis of the 6.18 Mb genome of strain KT2440 reveals diverse transport and metabolic systems"* ([PMID: 12534463](https://pubmed.ncbi.nlm.nih.gov/12534463/)).

### F004 — Core machinery is single-copy; SecB presence confirms the post-translational route

A proteome-wide UniProt name search (taxon 160488, both recommended and submitted names, case-insensitive) returns exactly one protein for each core component — SecA (Q88N69), SecB (Q88CX7), SecY (Q88QL5), SecE (Q88QP7), SecG (A0A140FWQ9), SecD (Q88PL5), SecF (Q88PL4), plus YidC (P0A140), SPase I/LepB (Q88MY6), and SPase II/LspA (Q88Q91). **No SecA2, no second SecYEG translocon, and no additional signal peptidase I paralog** was detected. This is the ideal curation scenario: there is no over-propagation risk from duplicated core subunits, and no ambiguity about which gene fills each step. SecA, SecB, YidC, and LspA carry Swiss-Prot reviewed status, raising confidence further. The single-copy channel components match the canonical definition: *"signal peptide-bearing precursors are recognized by the SecA ATPase and pushed across the membrane through a translocon channel made of the proteins SecY, SecE, and SecG"* ([PMID: 39817767](https://pubmed.ncbi.nlm.nih.gov/39817767/)).

The presence of a genuine **SecB** homolog is the key discriminator for this module. Many bacteria lack SecB and export proteins predominantly co-translationally; a module that specifically models the *SecB-dependent post-translational* route is only satisfiable where SecB is present. Its single-copy presence in KT2440 confirms the route being modeled is genuinely available, not assumed by generic propagation.

### F002 — KEGG bucket over-includes neighboring-module genes

Of the 19 candidates, 10 do not belong to the post-translational Sec module. KEGG "Protein export" is intentionally a superset map covering Sec, SRP, Tat, YidC, and both signal peptidases — so this is a definitional property of the map, not a KT2440-specific annotation error.

| Neighboring module | Genes (loci) | Recommended routing |
|---|---|---|
| SRP cotranslational targeting | ffh (PP_1461, Q88MV7), ftsY (PP_5111, Q88CR9) | Separate SRP module |
| YidC insertase | yidC (PP_0006, P0A140, reviewed) | Separate membrane-insertion module |
| Tat cluster I | tatC-I (PP_1039), tatB-I (PP_1040), tatA-I (PP_1041) | Tat module |
| Tat cluster II | tatA-II (PP_5016), tatB (PP_5017), tatC-II (PP_5018) | Tat module |
| Lipoprotein maturation | lspA (PP_0604, Q88Q91, reviewed) | Lipoprotein/SPase II module |

The two Tat clusters are genuine paralogous systems, not annotation artifacts: *"Two different tat gene clusters were detected in the P. putida genome, of which one, named tat-1, is located adjacent to the uxpB and xcp genes"* ([PMID: 23530902](https://pubmed.ncbi.nlm.nih.gov/23530902/)).

### F003 — Two functionally redundant, phosphate-regulated Tat clusters (neighboring module, directly evidenced)

This is the strongest piece of *direct* KT2440 experimental evidence in the whole bucket, and it concerns a neighboring module. Putker et al. (2013) showed that the twin-arginine substrate UxpB (a PhoX-family phosphatase) is Tat-dependent and processed by leader peptidase II, that **both** Tat systems can transport UxpB, and that tat-1 expression is strongly induced under low inorganic phosphate: *"Both Tat systems appeared to be capable of transporting the UxpB protein"* ([PMID: 23530902](https://pubmed.ncbi.nlm.nih.gov/23530902/)). Loci: tat-I = PP_1039/1040/1041; tat-II = PP_5016/5017/5018. For the Sec module this matters only as a boundary clarification, but the Tat module itself is well supported experimentally in KT2440 and should be curated as its own well-evidenced document.

### F006 — No KT2440-specific essentiality dataset for core Sec genes

Targeted PubMed searches for a genome-scale essential-gene / Tn-seq study in KT2440 returned **no dataset** reporting essentiality or knockout phenotypes for secA/secY/secE/secB/lepB in this strain. An optimized CRISPRi system for KT2440 exists ([PMID: 39163848](https://pubmed.ncbi.nlm.nih.gov/39163848/)) but has not been applied to Sec genes in the retrieved literature. Consequently the satisfiability calls rest on **homology + curated UniProt annotation**, not direct loss-of-function genetics. Indirect functional support that the export machinery is active in KT2440: a documented periplasmic glutaminase/asparaginase (PGA) — *"The uptake of Gln and Asn is facilitated by a periplasmic glutaminase/asparaginase (PGA)"* ([PMID: 14624355](https://pubmed.ncbi.nlm.nih.gov/14624355/)) — and the Tat substrate UxpB phosphatase (PMID 23530902). These exported enzymes require a functioning general export apparatus, giving circumstantial confirmation.

### F005 — Curation verdict

Synthesis across findings: all five module steps map to single-copy, correctly annotated genes (SecB PP_5053, SecA PP_1345, SecY/E/G PP_0474/PP_0441/PP_5706, SecD/F/YajC PP_0835/PP_0836/PP_0834 in one operon, LepB PP_1432). 9/19 bucket genes are in-scope; 10/19 belong to neighboring modules. The KT2440 secretion-system context supports a *housekeeping* interpretation: *"key virulence factors including exotoxin A and type III secretion systems are absent"* ([PMID: 12534463](https://pubmed.ncbi.nlm.nih.gov/12534463/)) — i.e., the machinery curated here is the general Sec/Tat export apparatus, not specialized virulence secretion.

---

## Mechanistic Model / Interpretation

The KT2440 post-translational Sec module is a textbook, minimally redundant instance of the Gram-negative route. Read top to bottom: SecB (single copy) holds the unfolded precursor and hands it to the single SecA ATPase, which threads it through the single SecYEG channel; the adjacent yajC–secD–secF operon supplies an optional PMF-coupled boost to late-stage translocation; and a single LepB signal peptidase I clips the type I signal peptide to release the mature protein. Because every node is single-copy and correctly named, the module graph is unambiguous and there is no over-propagation to reconcile.

```
 Curation map of KEGG ppu03060 (19 genes)
 ────────────────────────────────────────────────────────
   IN-SCOPE  (post-translational Sec, 9)   →  MODULE COVERED
     secB secA secY secE secG secD secF yajC lepB

   OUT-OF-SCOPE (route to neighbor modules, 10)
     SRP:        ffh  ftsY
     YidC:       yidC
     Tat-I:      tatC-I tatB-I tatA-I     ┐ two functional,
     Tat-II:     tatA-II tatB tatC-II     ┘ Pi-regulated clusters
     SPase II:   lspA
 ────────────────────────────────────────────────────────
```

The interpretive tension in the dataset is between **coverage confidence** (very high, from clean single-copy annotation) and **evidence directness** (moderate, since the core Sec calls are homology-based and the only strong KT2440 wet-lab data belong to the Tat neighbor). For module satisfiability this is acceptable: core Sec subunits are among the most deeply conserved proteins in bacteria, so homology transfer from *E. coli* biochemistry is strong for SecA/SecY/SecE; and independent circumstantial evidence (periplasmic PGA, secreted phosphatases) confirms the export apparatus is functionally active in the strain.

---

## Gaps, Ambiguities, and Likely Over-Annotations

- **No coverage gap; a boundary problem.** All five steps are filled. The "issue" is that KEGG `ppu03060` bundles five export routes. Curators should **split** the bucket, not flag missing genes (F002).
- **secG (PP_5706, A0A140FWQ9):** the only core Sec subunit lacking a Swiss-Prot reviewed entry (TrEMBL accession). SecG is short and poorly conserved across bacteria, so automated family assignment is comparatively weak. Promote to full review.
- **lepB (PP_1432, Q88MY6):** carries EC 3.4.21.89 (SPase I). The signal-peptidase EC/GO space overlaps conceptually with the SRP and Tat outputs (all yield periplasmic mature proteins), and "signal peptidase activity" GO terms are broad. Verify LepB is scoped to type I processing and not over-mapped to lipoprotein (SPase II) or Tat. Promote to full review.
- **tatB-I (PP_1040):** no UniProt recommended name (submitted name only). TatB/TatE-type subunits are frequently mis-split or mis-named across annotation pipelines. Out-of-scope for Sec but worth promoting during Tat-module curation.
- **SecDF–YajC (PP_0834–0836):** confirm the operon is transcriptionally intact and that SecD/SecF are genuinely separate proteins (they are, per F001) — some pipelines mis-call a fused SecDF.
- **No direct KT2440 genetics** for the core Sec genes (F006); calls are homology-based. Sec genes are expected to be essential, which itself limits available knockout data.

---

## Module and GO-Curation Recommendations

### Step-by-step module status

| Module step | Gene(s) | Status |
|---|---|---|
| SecB carriage | secB PP_5053 | **covered** |
| SecA motor | secA PP_1345 | **covered** |
| SecYEG channel | secY/E/G PP_0474/0441/5706 | **covered** (secG low-confidence accession) |
| SecDF–YajC accessory | secD/secF/yajC PP_0835/0836/0834 | **covered** |
| LepB SPase I cleavage | lepB PP_1432 | **covered** |

All five core steps = **covered**. No step is a gap, `candidate_uncertain`, or `not_expected_in_target_taxon` within the Sec module scope.

### Bucket / module-boundary actions

1. **Split `kegg:ppu03060`** into (at least) five module documents: post-translational Sec (9 genes, in-scope), SRP targeting (ffh/ftsY), YidC insertase, Tat export (both clusters), and lipoprotein maturation/SPase II (lspA). Mark the 10 non-Sec genes as belonging to neighboring modules — **not** as Sec-module gaps.
2. The generic module boundaries are **correct** for this organism; the misfit is purely at the KEGG-bucket level, which pools routes the module framework separates. No `module_needs_revision` for the Sec module itself.
3. **New module documents likely needed:** a dedicated Tat module for KT2440 is well justified given the direct experimental evidence (two functional clusters, PMF-driven, phosphate-regulated; PMID 23530902).

### GO-term considerations

- Confirm SecG maps to "protein transmembrane transporter activity" / Sec channel accessory rather than a generic term.
- Ensure LepB "signal peptidase activity" (GO) is scoped to type I / SPase I and not over-broadened to lipoprotein (SPase II) processing.
- No new GO term requests appear necessary; existing terms cover all five steps.

---

## Genes to Promote to Full Review

Three genes warrant full `fetch-gene` review before final sign-off:

1. **tatB-I (PP_1040)** — no UniProt recommended name (submitted-name-only); TatB subunits are prone to mis-naming. (Relevant to the Tat module, not Sec, but flagged during this review.)
2. **secG (PP_5706, A0A140FWQ9)** — the only core Sec subunit without a Swiss-Prot reviewed entry; short, poorly conserved, weaker automated assignment.
3. **lepB (PP_1432, Q88MY6)** — broad EC (3.4.21.89) / GO signal-peptidase mapping that overlaps conceptually with neighboring routes; verify scope.

The remaining six core Sec genes (secB, secA, secY, secE, secD, secF, yajC) are high-confidence, single-copy, and — for SecA and SecB — Swiss-Prot reviewed, and do not require promotion.

---

## Evidence Base

| Claim | Evidence type | Strength for KT2440 |
|---|---|---|
| All 5 Sec steps encoded | UniProt homology + curated review | Strong (homology), moderate (no genetics) |
| Core machinery single-copy | Proteome-wide name search | Strong |
| SecB present → post-translational route real | UniProt reviewed entry | Strong |
| Two functional Tat clusters (neighboring) | **Direct KT2440 experiment** (PMID 23530902) | Strong, direct |
| Export machinery functionally active | Periplasmic substrates (PGA, UxpB) | Indirect but supportive |
| No Sec essentiality data | Negative literature search | N/A (gap) |

### Key references

- **[PMID: 12534463](https://pubmed.ncbi.nlm.nih.gov/12534463/)** — *Complete genome sequence and comparative analysis of the metabolically versatile Pseudomonas putida KT2440.* Source of the PP_ loci and the secretion-system inventory (T3SS/exotoxin A absent). Supports F001 and F005.
- **[PMID: 23530902](https://pubmed.ncbi.nlm.nih.gov/23530902/)** — *The type II secretion system (Xcp) of Pseudomonas putida is active and involved in the secretion of phosphatases.* Direct evidence of two functional, phosphate-regulated Tat clusters transporting UxpB. Supports F002 and F003.
- **[PMID: 41652145](https://pubmed.ncbi.nlm.nih.gov/41652145/)** — *A small molecule allosterically activates SecA dependent secretion.* Defines the SecA–SecYEG translocase architecture. Supports F001.
- **[PMID: 39817767](https://pubmed.ncbi.nlm.nih.gov/39817767/)** — *Screening a library of temperature-sensitive mutants to identify secretion factors.* Defines the SecA + SecY/SecE/SecG translocon. Supports F004.
- **[PMID: 39435495](https://pubmed.ncbi.nlm.nih.gov/39435495/)** — *Physical mechanisms of the Sec machinery operation.* MD-based mechanism of the SecA–SecYEG machine and the PMF contribution relevant to the SecDF-YajC accessory step.
- **[PMID: 14624355](https://pubmed.ncbi.nlm.nih.gov/14624355/)** — *A functional gltB gene is essential for utilization of acidic amino acids and expression of periplasmic glutaminase/asparaginase (PGA).* Periplasmic (exported) enzyme in KT2440; indirect evidence of active export. Supports F006.
- **[PMID: 39163848](https://pubmed.ncbi.nlm.nih.gov/39163848/)** — *Optimized CRISPR Interference System for Investigating Pseudomonas.* The available tool for the recommended confirmatory essentiality experiment. Supports F006.

---

## Limitations and Knowledge Gaps

- **No direct loss-of-function evidence** for any core Sec gene in KT2440; all core calls are homology/annotation-based. Sec genes are expected to be essential (as in *E. coli*), which itself limits knockout availability.
- The strongest experimental data pertain to the **neighboring Tat module**, not the target Sec module.
- SecG rests on a **TrEMBL-only accession**; secG family assignment in Gram-negatives is intrinsically weaker at the sequence level.
- Evidence transfer from generic bacterial/*E. coli* Sec biochemistry to KT2440 is **strong for conserved core subunits** (SecA, SecY, SecE) but should be stated as inference, not direct proof for this strain.
- No proteome-wide inventory of KT2440 Sec substrates (signal-peptide prediction / periplasmic proteomics) was performed here, so the operational load on the pathway is not quantified.

---

## Proposed Follow-up Experiments / Actions

1. **CRISPRi knockdown** of secA, secY, secE, secB, and lepB in KT2440 using the existing optimized CRISPRi system ([PMID: 39163848](https://pubmed.ncbi.nlm.nih.gov/39163848/)) to confirm essentiality and export phenotypes — the single most decisive confirmatory experiment for the homology-based calls.
2. **Promote tatB-I (PP_1040), secG (PP_5706), and lepB (PP_1432)** to full `fetch-gene` review.
3. **Split the KEGG `ppu03060` bucket** into five module documents and reassign the 10 non-Sec genes; create a dedicated, well-evidenced Tat module.
4. **Periplasmic proteomics / signal-peptide prediction** across the KT2440 proteome to enumerate Sec substrates and empirically distinguish LepB-cleaved (Sec) precursors from Tat (twin-arginine) substrates.
5. **Expert question:** confirm whether the SecDF–YajC operon (PP_0834–0836) is co-transcribed and whether SecDF is dispensable for a defined substrate set, as the module treats it as a non-obligatory accessory step.

---

*Report generated from a 5-iteration autonomous review. Core Sec conclusions are homology- and curation-based (strong); the dual Tat cluster conclusion is directly experimental in KT2440. The module is fully satisfiable; the primary curation action is bucket splitting, not gap-filling.*


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_sec_posttranslational_protein_export__ppu03060-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_sec_posttranslational_protein_export__ppu03060-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:41652145
2. PMID:39817767
3. PMID:12534463
4. PMID:23530902
5. PMID:39163848
6. PMID:14624355
7. PMID:39435495