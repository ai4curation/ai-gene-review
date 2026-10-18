---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T14:14:43.358213'
end_time: '2026-09-01T14:31:49.451033'
duration_seconds: 1026.09
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial nitrogen-regulatory phosphotransferase system
  module_summary: A species-neutral bacterial signaling module in which enzyme I(Ntr)
    accepts phosphate from phosphoenolpyruvate, NPr relays it, and EIIA(Ntr) acts
    as the terminal phosphorylation-state-dependent regulator. Unlike carbohydrate
    PTS pathways, this module does not transport or phosphorylate a sugar.
  module_outline: "- Bacterial nitrogen-regulatory phosphotransferase system\n  -\
    \ 1. PEP-dependent phosphorylation entry\n  - PtsP enzyme I(Ntr) phosphate entry\n\
    \    - PtsP enzyme I(Ntr) (molecular player: PtsP enzyme I(Ntr) family; activity\
    \ or role: phosphoenolpyruvate-protein phosphotransferase activity)\n  - 2. NPr\
    \ phosphocarrier relay\n  - NPr phosphocarrier relay\n    - NPr phosphocarrier\
    \ (molecular player: experimentally assigned KT2440 NPr phosphocarrier; activity\
    \ or role: transferase activity, transferring phosphorus-containing groups)\n\
    \  - 3. Terminal EIIA(Ntr) phosphorylation-state regulator\n  - PtsN EIIA(Ntr)\
    \ terminal regulator\n    - PtsN EIIA(Ntr) (molecular player: nitrogen-regulatory\
    \ EIIA family; activity or role: protein kinase regulator activity)"
  module_connections: '- PtsP enzyme I(Ntr) phosphate entry feeds into NPr phosphocarrier
    relay

    - NPr phosphocarrier relay feeds into PtsN EIIA(Ntr) terminal regulator'
  pathway_query: ppu02060
  pathway_id: ppu02060
  pathway_name: Phosphotransferase system (PTS)
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu02060 with 6 primary genes; module
    area: transport_motility_signaling.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '6'
  candidate_genes: '- fruB: PP_0793 | Q88PQ5 | phosphoenolpyruvate--protein phosphotransferase
    (EC 2.7.3.9) (EC 2.7.3.9; primary bucket kegg:ppu02060)

    - fruK: PP_0794 | Q88PQ4 | Phosphofructokinase (primary bucket kegg:ppu02060)

    - fruA: PP_0795 | Q88PQ3 | protein-N(pi)-phosphohistidine--D-fructose phosphotransferase
    (EC 2.7.1.202) (EC 2.7.1.202; primary bucket kegg:ppu02060)

    - ... 3 additional candidate genes omitted from prompt.'
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_nitrogen_regulatory_pts__ppu02060-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_nitrogen_regulatory_pts__ppu02060-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial nitrogen-regulatory phosphotransferase system in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu02060
- Resolved ID: ppu02060
- Resolved name: Phosphotransferase system (PTS)
- Source: KEGG

Resolved local bucket kegg:ppu02060 with 6 primary genes; module area: transport_motility_signaling.

## Candidate Genes From Local Metadata

Candidate gene count: 6

- fruB: PP_0793 | Q88PQ5 | phosphoenolpyruvate--protein phosphotransferase (EC 2.7.3.9) (EC 2.7.3.9; primary bucket kegg:ppu02060)
- fruK: PP_0794 | Q88PQ4 | Phosphofructokinase (primary bucket kegg:ppu02060)
- fruA: PP_0795 | Q88PQ3 | protein-N(pi)-phosphohistidine--D-fructose phosphotransferase (EC 2.7.1.202) (EC 2.7.1.202; primary bucket kegg:ppu02060)
- ... 3 additional candidate genes omitted from prompt.

## Generic Module Context

### Working Scope

A species-neutral bacterial signaling module in which enzyme I(Ntr) accepts phosphate from phosphoenolpyruvate, NPr relays it, and EIIA(Ntr) acts as the terminal phosphorylation-state-dependent regulator. Unlike carbohydrate PTS pathways, this module does not transport or phosphorylate a sugar.

### Provisional Biological Outline

- Bacterial nitrogen-regulatory phosphotransferase system
  - 1. PEP-dependent phosphorylation entry
  - PtsP enzyme I(Ntr) phosphate entry
    - PtsP enzyme I(Ntr) (molecular player: PtsP enzyme I(Ntr) family; activity or role: phosphoenolpyruvate-protein phosphotransferase activity)
  - 2. NPr phosphocarrier relay
  - NPr phosphocarrier relay
    - NPr phosphocarrier (molecular player: experimentally assigned KT2440 NPr phosphocarrier; activity or role: transferase activity, transferring phosphorus-containing groups)
  - 3. Terminal EIIA(Ntr) phosphorylation-state regulator
  - PtsN EIIA(Ntr) terminal regulator
    - PtsN EIIA(Ntr) (molecular player: nitrogen-regulatory EIIA family; activity or role: protein kinase regulator activity)

### Known Relationships Among Steps

- PtsP enzyme I(Ntr) phosphate entry feeds into NPr phosphocarrier relay
- NPr phosphocarrier relay feeds into PtsN EIIA(Ntr) terminal regulator

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

# Module Review: Nitrogen-Regulatory Phosphotransferase System (PTS^Ntr) in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Local bucket:** kegg:ppu02060 — KEGG "Phosphotransferase system (PTS)"
**Module area:** transport_motility_signaling
**Date:** 2026-09-01

---

## 1. Executive summary

The nitrogen-regulatory PTS (PTS^Ntr) module is **fully satisfiable** in *P. putida* KT2440, and every step is supported by **direct experiments in the target strain** (not homology transfer). The three module steps map cleanly to three genes:

| Module step | Protein | Gene (symbol) | Locus | UniProt | KEGG KO / EC |
|---|---|---|---|---|---|
| 1. PEP-dependent entry | Enzyme I^Ntr (EI^Ntr) | *ptsP* | **PP_5145** | Q88CN5 | K08484 / EC 2.7.3.9 |
| 2. Phosphocarrier relay | NPr | *ptsO* (KEGG symbol legacy "*ptsH*") | **PP_0948** | Q88PA2 | K08485 (NPr) |
| 3. Terminal regulator | EIIA^Ntr | *ptsN* | **PP_0950** | Q88PA0 | K02806 |

The primary phosphate flow **PEP → EI^Ntr → NPr → EIIA^Ntr** was demonstrated in KT2440 by in-vivo phosphorylation-state assays (PMID 18296519), and each protein has genetically confirmed function in the strain (PMIDs 17416664, 11489866, 21236318, 26224366, 22434849).

**Three curation actions dominate this review:**
1. The KEGG bucket **ppu02060 conflates two biologically distinct processes** — the fructose/sugar PTS (*fruBKA*) and the regulatory PTS^Ntr. Only the latter belongs to this module; **fruB/fruK/fruA should be excluded** (fruK is a glycolytic 1-phosphofructokinase, not a PTS component at all).
2. **PP_0948 carries a misleading legacy symbol "*ptsH*"/"HPr"** but is the nitrogen-PTS **NPr** (KEGG ortholog K08485), confirmed by rpoN-operon synteny and His15 mutagenesis. Its symbol should be corrected to *ptsO*/*npr*.
3. Phosphate entry is **not strictly *ptsP*-exclusive** (a second EI-type enzyme "*mtp*" and FruB cross-talk provide redundancy), a caveat for the step-1 molecular-player annotation.

---

## 2. Target-organism pathway definition

**What the module IS (in KT2440):** a cytoplasmic, membrane-independent PEP-driven phosphorelay that functions **purely in signaling/regulation** — it does not transport or phosphorylate any sugar. PEP donates a phosphoryl group to EI^Ntr (PtsP), which relays via the small phosphocarrier NPr (His15) to the terminal regulator EIIA^Ntr (PtsN). The **phosphorylation state of EIIA^Ntr** (set by the cell's PEP/pyruvate ratio and C/N status) is read out by direct protein–protein interactions with downstream targets. This is the "N/C-sensing" or "nitrogen-related/metabolic" PTS.

**Alternate names / database definitions:**
- PTS^Ntr, PTS(Ntr), "nitrogen-related PTS", "nitrogen-metabolic PTS", "N/C-sensing PTS", "regulatory PTS", "paralogous/branch PTS".
- KEGG places all of these genes on map **ppu02060 "Phosphotransferase system (PTS)"**, which is an **overview transport map that also contains all sugar PTS proteins** — the map name is broader than this module.

**Neighboring processes to keep SEPARATE from this module:**
- **Fructose PTS / PTS^Fru** (*fruBKA*, PP_0793–0795): carbohydrate uptake + fructose-1-P phosphorylation. Shares map ppu02060 and cross-talks with PTS^Ntr but is a distinct pathway.
- **Glycolysis / fructose metabolism** (fruK = 1-phosphofructokinase).
- **σ⁵⁴ (RpoN) regulon / nitrogen assimilation** (Ntr/GlnK–NtrBC systems): functionally connected but a separate module. Note NPr/PtsN are *genomically* embedded in the *rpoN* operon here, which can invite conflation.
- **KdpD/KdpE two-component system and KdpFABC K⁺ transport**: a *target* of PtsN, not part of the phosphorelay module.

---

## 3. Expected step model

```
        PEP ─(EI^Ntr, PtsP / PP_5145)→ EI^Ntr~P
                     │
                     ▼
        NPr (ptsO / PP_0948, His15) ──→ NPr~P
                     │
                     ▼
        EIIA^Ntr (PtsN / PP_0950) ──→ EIIA^Ntr~P  ⇄  EIIA^Ntr (dephospho)
                     │                                    │
     PtsN~P: represses kdpFABC via KdpD            dephospho-PtsN: inhibits PDH (AceE),
     (K⁺ transport)                                 controls PHA, central C-flux, Pu promoter
```

All three steps and both inter-step relationships in the provisional module outline are **confirmed in KT2440**.

---

## 4. Candidate genes and evidence

### 4.1 Genes that ARE the module (high confidence)

**EI^Ntr — *ptsP* / PP_5145** (Q88CN5; K08484; EC 2.7.3.9; 759 aa)
- Role: PEP-dependent autophosphorylating Enzyme I of the Ntr branch; entry point of the relay.
- Domain architecture: N-terminal **GAF** sensory domain + PEP-utilizer (PEP-utilizers_N/C) catalytic domains — the GAF domain is the presumptive metabolic-signal input (analogous to other EI^Ntr proteins).
- Evidence: direct KT2440 genetics — part of the PEP→EI^Ntr→NPr→EIIA^Ntr flow (PMID 18296519); *ptsP/ptsO/ptsN* act in concert to control PHA (PMID 17416664).
- Caveat: **phosphodonor redundancy** — a second EI-type ORF "*mtp*" was noted, and neither *ptsP* nor *mtp* single mutants abolished Pu carbon regulation (PMID 11489866); FruB cross-talk can also phosphorylate downstream EIIA^Ntr in a *ptsP* background (PMID 18296519). → mark step 1 "covered (PtsP primary) with documented redundancy."

**NPr — PP_0948** (Q88PA2; **KO K08485 = NPr**; 90 aa; PTS-HPr fold; active-site His15)
- Role: phosphocarrier relay between EI^Ntr and EIIA^Ntr.
- Evidence: H15A substitution abolishes ptsO function in carbon regulation of Pu (PMID 11489866) — direct proof of the phospho-His relay; coexpressed with *ptsN*, mapped adjacent to *rpoN* (PMID 11489866); part of the concerted PHA-controlling cascade (PMID 17416664).
- **Curation caveat (important):** the KEGG/GenBank **symbol is "*ptsH*" and name "Phosphocarrier protein HPr"**, but the ortholog assignment (K08485) and all functional/synteny evidence identify it as the **NPr (*ptsO*/*npr*)**. KT2440 has **no separate canonical carbohydrate HPr** — the fructose branch's HPr activity is fused into the FruB multidomain protein (PMID 18296519). → **Recommend symbol correction PP_0948: ptsH → ptsO/npr.**

**EIIA^Ntr — *ptsN* / PP_0950** (Q88PA0; K02806; 154 aa; PTS_EIIA_2)
- Role: terminal phosphorylation-state-dependent regulator acting by direct protein–protein interaction (no sugar phosphorylation).
- Direct KT2440 targets:
  - **PtsN~P represses *kdpFABC*** (K⁺ transport) via direct interaction with the sensor kinase **KdpD**; K⁺-dependent (PMID 26224366; modeled in PMID 26159078).
  - **Dephospho-PtsN inhibits pyruvate dehydrogenase** (AceE, E1 subunit) — co-IP/MS, co-localization, activity assays (PMID 21236318).
  - Controls **central-carbon flux** (elevated pyruvate-shunt flux in *ptsN* mutants; PMID 22434849) and **PHA accumulation** (PMID 17416664).
  - Modulates the **Pu/TOL biodegradation promoter** in response to carbon (PMID 11489866, 30209872).
- Opposite phospho-forms act on different targets — a bona fide phosphorylation-state switch.

### 4.2 Candidate genes that are NOT this module (KEGG map overlap only)

**fruB / PP_0793** (Q88PQ5; multidomain EI–HPr–EIIA^Fru; EC 2.7.3.9) — fructose PTS; relevant only as a documented **cross-talk phosphodonor** to EIIA^Ntr (PMID 18296519, 22708906). Not a PTS^Ntr component.
**fruK / PP_0794** (Q88PQ4; 1-phosphofructokinase) — a **glycolytic enzyme, not a PTS protein at all**; broad "Phosphofructokinase" annotation. Exclude.
**fruA / PP_0795** (Q88PQ3; IIBC^Fru permease; EC 2.7.1.202) — fructose PTS permease. Not a PTS^Ntr component.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **Module-boundary error in the source bucket:** ppu02060 mixes PTS^Ntr with the fructose PTS. The generic module boundary is correct in concept (it explicitly excludes sugar transport), but the *local candidate list* is contaminated with *fruBKA*. → `module_needs_revision` at the gene-membership level.
- **PP_0948 symbol over-propagation:** "*ptsH*/HPr" is a legacy mislabel; the protein is NPr. High-impact for curation because a curator could wrongly assign it to carbohydrate PTS or expect a separate NPr elsewhere (there is none). **Genome-wide KO check confirms this:** KT2440 has **zero** genes assigned to the canonical HPr ortholog **K02784** and **zero** to the carbohydrate Enzyme I ortholog **K08483** — so the "HPr" label has no legitimate genomic referent, and FruB is the sole sugar-PTS Enzyme I.
- **No intra-genome paralog ambiguity:** each PTS^Ntr step is single-copy in KT2440 — *ptsP*=PP_5145 (K08484), NPr=PP_0948 (K08485), *ptsN*=PP_0950 (K02806). This contrasts with *Rhizobium leguminosarum* (two *ptsN* copies; PMID 22340847), so KT2440 module steps map unambiguously to one gene each.
- **"mtp" is not a distinct Enzyme I:** the only other PEP-utilizing enzyme in KT2440 is PEP synthase (*ppsA*, PP_2082, K01007); there is no second EI/EI^Ntr ortholog. Step-1 redundancy therefore most plausibly operates through FruB cross-talk rather than a bona fide second Enzyme I.
- **fruK broad EC/name:** "Phosphofructokinase" — ensure it is annotated as 1-phosphofructokinase (fructose-1-P → fructose-1,6-bisP) and not counted toward any PTS step.
- **EI^Ntr phosphodonor redundancy:** step-1 input is not strictly PtsP-exclusive — FruB cross-talk feeds the relay in a *ptsP* background (PMID 18296519), and the historic "*mtp*" ORF (PMID 11489866) has no distinct modern EI ortholog (see above). Curate step 1 as "PtsP primary, with documented redundancy."
- **PP_0949 (UPF0042 ATP-binding, RapZ/YhbJ homolog):** present in the operon; associated in other taxa with GlmZ sRNA / RNase adaptor regulation — outside this three-step module but a candidate for a separate module/review.
- **NPr's own direct targets:** in *E. coli*, dephospho-NPr regulates LpxD/LPS and envelope stress (PMID 25701731). Whether NPr has PtsN-independent targets in KT2440 is **untested (uncertain species transfer)** — an open question.
- **Broader-organism inferences (flag as transfer, not direct):** *E. coli* cross-talk→Kdp (PMID 26159077); *Rhizobium* PTS^Ntr→ABC transporters (PMID 22340847); *P. aeruginosa* PtsN redundant phosphorylation and virulence links (PMID 37074168). These are **weak-to-moderate** transfer to KT2440 and should not be asserted as KT2440 facts.

---

## 6. Module and GO-curation recommendations

**Step status:**
| Module step | Gene | Status |
|---|---|---|
| 1. EI^Ntr PEP entry | *ptsP* / PP_5145 | **covered** (primary donor; note redundancy) |
| 2. NPr relay | PP_0948 (*ptsO*/*npr*) | **covered** (correct the "*ptsH*" symbol) |
| 3. EIIA^Ntr terminal regulator | *ptsN* / PP_0950 | **covered** |
| Sugar PTS genes in bucket | *fruB/fruK/fruA* | **not_expected_in_module** (belong to PTS^Fru / glycolysis) |

**Module document:** Retain a dedicated PTS^Ntr module distinct from the KEGG ppu02060 overview map; explicitly list membership = {PP_5145, PP_0948, PP_0950} and explicitly exclude {PP_0793, PP_0794, PP_0795}. Record FruB and "mtp" as *cross-talk/redundant inputs*, not members.

**GO-curation suggestions (KT2440-supported):**
- PP_5145 (PtsP): GO:0008965 phosphoenolpyruvate-protein phosphotransferase activity; GO:0009401 PTS; phosphorelay signal transduction.
- PP_0948 (NPr): protein-histidine phosphotransfer / phosphorelay carrier; **request symbol change**; ensure it is NOT annotated as carbohydrate HPr.
- PP_0950 (PtsN): protein-kinase-regulator/enzyme-regulator activity via KdpD interaction → **GO:0043266 regulation of potassium ion transport** (and negative regulation of K⁺ import); **negative regulation of pyruvate dehydrogenase (acetyl-transferring) activity / pyruvate metabolic process**; regulation of PHA/carbon storage. These are direct-experiment-supported and appropriate as `IMP/IPI` (KT2440).
- Consider a **new/checked GO term** for "regulation of potassium ion transmembrane transport by protein-protein interaction with a sensor histidine kinase" if existing terms are too generic.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_0948** (top priority) — resolve the *ptsH*→*ptsO*/*npr* symbol/name discrepancy; confirm NPr status and His15 annotation. *(direct evidence: PMID 11489866; ortholog K08485)*
2. **PP_5145 (*ptsP*)** — annotate GAF sensory domain, EC 2.7.3.9, and the redundancy caveat.
3. **PP_0950 (*ptsN*)** — attach the KdpD / PDH / PHA / central-C regulatory GO annotations.
4. **PP_0949** (UPF0042 / RapZ-YhbJ homolog) — clarify whether it belongs to a separate regulatory module.
5. **"mtp"** — flagged in PMID 11489866 as a second EI-type ORF, but a genome-wide KO check finds no distinct Enzyme I/EI^Ntr ortholog (only *ppsA*/PP_2082 PEP synthase); low priority — likely superseded by the FruB cross-talk explanation. Track only if resolving historical nomenclature.

---

## 8. Key references

- Pflüger & de Lorenzo, 2008. In-vivo cross-talk between nitrogen- and fructose-related PTS branches of *P. putida*. *J Bacteriol.* **PMID 18296519.** (Direct: PEP→EI^Ntr→NPr→EIIA^Ntr flow; only 5 PTS proteins; FruB cross-talk.)
- Cases, Velázquez & de Lorenzo, 2001. Role of *ptsO* in carbon inhibition of the Pu promoter. *J Bacteriol.* **PMID 11489866.** (Direct: NPr His15 required; ptsO–ptsN–rpoN synteny; ptsP/mtp redundancy.)
- Velázquez et al., 2007. PtsP/PtsO/PtsN control PHA accumulation in *P. putida*. **PMID 17416664.** (Direct: three-protein cascade intact.)
- Pflüger-Grau, Chavarría & de Lorenzo, 2011. EIIA^Ntr interplay with pyruvate dehydrogenase. *Mol Microbiol.* **PMID 21236318.** (Direct: dephospho-PtsN inhibits PDH/AceE.)
- Chavarría et al., 2012. Regulatory tasks of the PTS in central carbon metabolism of *P. putida*. **PMID 22434849.** (Direct: PtsN controls pyruvate-shunt flux.)
- Deuschle et al., 2015. PtsN–KdpD interplay controlling K⁺ transport. **PMID 26224366.** (Direct: PtsN~P represses kdpFABC via KdpD.)
- Chavarría et al., 2013. Cra regulates cross-talk between the two PTS branches. **PMID 22708906.** (Direct: FruB→EIIA^Ntr phosphotransfer.)
- Pérez-Pantoja et al., 2018. EIIA interplay with Pu promoter regulation. **PMID 30209872.**
- Wolf, Pflüger-Grau & Kremling, 2015. Modeling PtsN–KdpFABC interplay. **PMID 26159078.**
- *Transfer/context (non-KT2440):* Lüttmann et al., 2015 (*E. coli* cross-talk→Kdp, PMID 26159077); Lee et al., 2015 (*E. coli* NPr→LpxD/envelope stress, PMID 25701731); Prell et al., 2012 (*Rhizobium* PTS^Ntr→ABC transporters, PMID 22340847); Underhill et al., 2023 (*P. aeruginosa* PtsN redundancy/virulence, PMID 37074168).

---

*Prepared for manual module satisfiability and gene-annotation curation. Direct KT2440 evidence is explicitly distinguished from cross-species inference throughout.*


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_nitrogen_regulatory_pts__ppu02060-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_nitrogen_regulatory_pts__ppu02060-deep-research-openscientist_artifacts/final_report.pdf)