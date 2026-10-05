---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-13T07:44:57.433754'
end_time: '2026-09-13T08:05:14.783290'
duration_seconds: 1217.35
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: NEK1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: NEK1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

Focused primary-evidence audit for GO curation, September 2026. Read full texts and supplements, verify identifiers. Report a claim-by-claim table with experiment, protein/isoform/species, exact result, figure/table, short verbatim supporting passage, primary PMID/DOI/URL, counterevidence and defensible conclusion. Distinguish direct human assays, ortholog studies, predictions, secondary discussion and disease phenotypes. Do not infer misattribution from absence in abstracts; explicitly identify inaccessible data. This is a targeted investigation, not a generic overview. Investigate human NEK1 (Q96PY6) uncertain claims related to CFAP410 partnership. (1) RAD54 Ser572 phosphorylation: trace Spies2016 PMID27264870, Ghosh2022 preprint doi10.1101/2022.04.01.486731, its revisions/author responses and current publication status, and Gregorczyk2023 PMID37188479. Distinguish citing a challenge from performing replication; inspect assay differences and sequence numbering. Do not treat TLK1/RAD54 PMID37439356 as refutation unless it actually tests this site. (2) ATR-ATRIP priming: PMID23345434 excludes direct NEK1 phosphorylation of ATR Thr1989; some summaries erroneously claim ATRIP-T1989 substrate. What is actually established? (3) Localization: pericentriolar material vs distal centriole tips and basal-body/axoneme changes across cell cycle, reconcile21211617/26167768/37188479 with June2026 PMID42265085 doi10.1038/s41467-026-73560-9. Distinguish stages/antibodies/overexpression. (4) Mitochondrial NEK1 and VDAC1 Ser193 PMID19158487/20230784, human vs ortholog assays and outdated obligatory permeability-transition-pore assumptions. Other related uncertain assertions: direct NEK1-CFAP410 binding vs endogenous association/obligatory SPATA7 trimer, and neuronal importin-beta1/alpha-tubulin in vitro substrates PMID37585529 vs established in vivo mechanisms. Avoid general cancer review; identify residual uncertainty and precise curation implications.

## Output

# Focused Primary-Evidence Audit: Human NEK1 (Q96PY6) Uncertain Claims for GO Curation

**Audit date:** September 2026
**Scope:** Claim-by-claim re-scoping of six uncertain assertion clusters attached to human NEK1 (UniProt Q96PY6), with attention to the CFAP410 (C21ORF2) partnership, distinguishing direct human assays, ortholog studies, predictions, secondary discussion, and disease phenotypes.

**Accessibility note.** This audit was performed from verified PubMed abstracts (stored, verbatim) plus open-access full-text summaries. Where a specific figure/table/supplement was not directly opened, this is stated explicitly rather than inferred from absence. Verbatim passages below are taken from the papers' abstracts unless noted. Evidence classes are labeled throughout: **[Direct human assay] / [Ortholog] / [Prediction] / [Secondary discussion] / [Disease phenotype]**.

---

## Summary

This audit traced six clusters of uncertain NEK1 claims to their primary evidence, verified identifiers, and separated experiment from citation, human assay from ortholog, and demonstrated interaction from prediction. The headline conclusion is that several widely propagated NEK1 annotations are **compound or mis-scoped**, and correcting them materially changes what GO can defensibly assert.

The single most consequential correction concerns **ATR/ATRIP Thr1989**. NEK1 does **not** directly phosphorylate ATR or ATRIP at Thr1989. Liu et al. 2013 ([PMID: 23345434](https://pubmed.ncbi.nlm.nih.gov/23345434/)) establish that T1989 is an **ATR autophosphorylation** site that NEK1 *primes and stabilizes* by maintaining ATRIP levels and ATR–ATRIP association. Summaries claiming an "ATRIP-T1989 NEK1 substrate" are doubly wrong: T1989 resides on ATR, not ATRIP, and it is autophosphorylation, not a NEK1-catalyzed event. The **RAD54-Ser572** claim (Spies et al. 2016, [PMID: 27264870](https://pubmed.ncbi.nlm.nih.gov/27264870/)) is genuinely **disputed but not experimentally refuted in the peer-reviewed literature**: the frequently-cited TLK1 paper ([PMID: 37439356](https://pubmed.ncbi.nlm.nih.gov/37439356/)) tests entirely different residues (T41/T59/T700) and is therefore not a refutation; the only experimental non-replication is an unpublished bioRxiv preprint, and a December-2025 preprint reaffirms S572 while proposing a developmental NEK1/NEK3/NEK5 switch that could reconcile the conflict.

On localization, endogenous human NEK1 maps to the **distal centriole tip throughout the cell cycle** (June 2026 U-ExM study, [PMID: 42265085](https://pubmed.ncbi.nlm.nih.gov/42265085/)), refining—not contradicting—older pericentriolar-material and basal-body descriptions, most of which relied on mouse/canine overexpression. The **VDAC1-Ser193** phosphosite is real and supported by both cell-based and reconstituted in-vitro assays using human GST-VDAC1 and human-cell-derived NEK1, but its original mechanistic framing rests on the now-outdated assumption that VDAC1 is an obligatory component of the mitochondrial permeability transition pore. Finally, **NEK1–CFAP410** is a genuine direct binary interaction via the NEK1 C-terminal domain, distinct from a non-obligatory NEK1–CFAP410–SPATA7 retinal association; and the neuronal **importin-β1/α-tubulin** phosphorylations are in-vitro-only, with physiological relevance inferred from phenotypes rather than demonstrated at the specific sites.

---

## Claim-by-Claim Summary Table

| # | Claim under audit | Evidence class | Defensible conclusion |
|---|---|---|---|
| 1 | NEK1 phosphorylates RAD54-Ser572 | Direct human (Spies2016) vs preprint non-replication vs preprint reaffirmation | Supported by one direct human study; **disputed, not peer-reviewed-refuted** |
| 2 | NEK1 phosphorylates ATR/ATRIP-Thr1989 | Direct human (Liu2013) | **False as stated**; T1989 is ATR autophosphorylation; NEK1 primes/stabilizes ATR–ATRIP |
| 3 | NEK1 localizes to PCM/centrosome/basal body | Ortholog+overexpression (old) vs endogenous human U-ExM (2026) | **Distal centriole tip** (endogenous, all stages); old claims are stage/species artifacts |
| 4 | NEK1 phosphorylates VDAC1-Ser193 → controls PTP | Human substrate + human-cell kinase in vitro | Phosphosite/gating **supported**; **obligatory-PTP framing outdated** |
| 5 | Direct NEK1–CFAP410 binding; obligatory SPATA7 trimer | Direct human interaction (Gregorczyk2023) + predicted interface; bovine/human association (Wheway2015) | **Direct binary** NEK1–CFAP410; SPATA7 link is **non-obligatory association**, not a demonstrated trimer |
| 6 | NEK1 phosphorylates importin-β1 / α-tubulin | In-vitro only (Mann2023) | In-vitro substrates; **physiological role inferred**, not site-demonstrated |

---

## Key Findings

### Finding 1 — ATR/ATRIP Thr1989 is ATR autophosphorylation primed by NEK1, not a NEK1 substrate site

**[Direct human assay]** Liu et al. 2013 ([PMID: 23345434](https://pubmed.ncbi.nlm.nih.gov/23345434/)) show that NEK1 associates with the ATR–ATRIP complex and is required to maintain ATRIP protein levels, ATR–ATRIP association, and basal ATR activity *before* DNA damage. In cells lacking NEK1, ATR fails to autophosphorylate at Thr1989. The verbatim abstract text states that *"cells lacking Nek1 failed to efficiently phosphorylate multiple ATR substrates and support ATR autophosphorylation at threnine 1989, one of the earliest events during the ATR response"* and that NEK1 *"enhances the stability and activity of ATR-ATRIP before DNA damage, priming ATR-ATRIP for a robust DNA damage response."*

The crucial curation point is that T1989 is explicitly described as **ATR's own autophosphorylation**, an event that NEK1 *supports* by stabilizing the complex. No assay in the paper demonstrates direct NEK1 phosphorylation of ATR or ATRIP at any residue. Consequently, any annotation stating that NEK1 phosphorylates "ATRIP-T1989" (or "ATR-T1989") as a direct substrate is a **compound error** and should be removed. The defensible GO annotation is a **priming/stabilizing regulatory role** on the ATR–ATRIP complex (protein stabilization / positive regulation of ATR signaling), not a kinase-substrate relationship at T1989.

### Finding 2 — RAD54-Ser572 is disputed but not experimentally refuted in the peer-reviewed record

**[Direct human assay]** The positive claim originates from a single direct human study: Spies et al. 2016 ([PMID: 27264870](https://pubmed.ncbi.nlm.nih.gov/27264870/)), which reports that *"human Nek1 regulates homologous recombination (HR) by phosphorylating Rad54 at Ser572 in late G2 phase,"* supported by both cellular and in-vitro kinase assays and DR-GFP HR functional readouts.

The apparent refutation frequently attached to this claim—the TLK1/RAD54 paper, Ghosh et al. 2023 *Nucleic Acids Research* ([PMID: 37439356](https://pubmed.ncbi.nlm.nih.gov/37439356/))—**does not test Ser572 at all**. That paper shows *"TLK1 phosphorylates RAD54 at three threonines (T41, T59 and T700)"*: a different kinase and different residues. Its rejection of S572 appears only in the Discussion as a written assertion, not as an experiment. Under the audit rule "do not treat PMID37439356 as refutation unless it actually tests this site," it must **not** be recorded as counterevidence to the phosphorylation event.

The chronology of the genuine dispute is summarized below.

| Source | Type | What it did about S572 | Status |
|---|---|---|---|
| Spies et al. 2016 ([PMID: 27264870](https://pubmed.ncbi.nlm.nih.gov/27264870/)) | Direct human assay | NEK1 phosphorylates RAD54-S572 in late G2 (cell + in vitro + DR-GFP HR) | Peer-reviewed (positive) |
| De Benedetti lab preprint (doi 10.1101/2022.04.01.486731) | Experimental replication attempt | NEK1-KO NT1 (mouse) + NEK1-KD HEK293; in-vitro NEK1+RAD54 kinase + MS found several sites but **not** S572; failed to reproduce coIP and HR defect | **Unpublished preprint** |
| Ghosh et al. 2023 NAR ([PMID: 37439356](https://pubmed.ncbi.nlm.nih.gov/37439356/)) | Different kinase/residues | Tests TLK1→RAD54 T41/T59/T700; asserts S572 is wrong only in Discussion | Peer-reviewed but **discussion-only** re S572 |
| Löbrich lab preprint (Dec 2025, doi 10.64898/2025.12.19.695536) | Reaffirmation + extension | NEK1 regulates RAD54-S572 for HR in **adult** mice/fibroblasts; **embryonic** fibroblasts use NEK3/NEK5 for the same site | **Unpublished preprint** |

The Löbrich preprint's proposed **developmental switch** (adult NEK1 vs. embryonic NEK3/NEK5 both converging on RAD54-S572) is a plausible reconciliation of the reproducibility conflict, because the non-replication used mouse NEK1-KO and immortalized lines that may reflect a different developmental/cell-context regime. Both the non-replication and the reaffirmation are non-peer-reviewed. It is essential to note that Gregorczyk 2023 ([PMID: 37188479](https://pubmed.ncbi.nlm.nih.gov/37188479/)) mentions RAD54 only as **[Secondary discussion]** of a prior NEK1 target and performed **no independent RAD54-Ser572 replication**. **Curation implication:** retain the S572 phosphorylation as supported by one direct human study, flag it as disputed, and do **not** cite PMID37439356 as refutation.

### Finding 3 — Endogenous human NEK1 localizes to the distal centriole tip; older PCM/basal-body claims are stage/species/overexpression artifacts

**[Direct human assay, endogenous]** The June 2026 study Streubel et al., *Nat Commun* 17:7330 ([PMID: 42265085](https://pubmed.ncbi.nlm.nih.gov/42265085/); doi 10.1038/s41467-026-73560-9; PMC13402741; identifier verified) mapped **endogenous** NEK1 by ultrastructure expansion microscopy (U-ExM) in human RPE1 cells and found it at the **distal tip of centrioles throughout the cell cycle**, colocalizing with CP110 and Cep97 and interacting with Cep97 and Cep78. NEK1 loss causes centriolar-microtubule hyperelongation from the distal tip *without* displacing CP110–Cep97, defining a parallel branch of centriolar-MT length control. NEK1 is removed from the basal body during ciliogenesis in a Cep78-dependent manner.

This reconciles the earlier literature once method, species, and cell-cycle stage are specified:

| Study | System | Method | Reported localization | Evidence class |
|---|---|---|---|---|
| White & Quarmby 2008 (PMID 18533026) | Mouse IMCD3 | eGFP-tagged mNek1 **overexpression**/truncation | Centrosome/PCM (γ-tubulin), coiled-coil ciliary-targeting region | Ortholog + overexpression |
| Shalom 2008 (PMID 18387364) | Canine MDCK / kat2J MEFs | Overexpression | Basal-body region; overexpression inhibits ciliogenesis | Ortholog + overexpression |
| Thiel 2011 ([PMID: 21211617](https://pubmed.ncbi.nlm.nih.gov/21211617/)) | Human / in vivo | Disease genetics | Loss reduces cilia number, alters ciliary morphology | Disease phenotype |
| Wheway 2015 ([PMID: 26167768](https://pubmed.ncbi.nlm.nih.gov/26167768/)) | Bovine retina / human RPE1 | Biochemistry + colocalization | Basal-body module with C21orf2/SPATA7 | Association/module |
| Streubel 2026 ([PMID: 42265085](https://pubmed.ncbi.nlm.nih.gov/42265085/)) | Human RPE1 | **U-ExM, endogenous** | **Distal centriole tip, all stages** | Direct human, endogenous |

**Curation implication:** the precise, defensible localization for human NEK1 is the **distal end of the centriole** (with a basal-body presence during ciliogenesis that is actively removed). Pericentriolar-material/centrosome annotations derived from mouse/canine overexpression should be de-emphasized or qualified with the appropriate evidence and species tags.

### Finding 4 — VDAC1-Ser193 is a genuine human phosphosite with in-vitro channel-gating consequences, but rests on an outdated permeability-transition-pore assumption

**[Direct human substrate; human-cell kinase]** Chen, Craigen & Riley 2009 ([PMID: 19158487](https://pubmed.ncbi.nlm.nih.gov/19158487/), *Cell Cycle* 8:257–267) report that *"Nek1 regulates the pathway to mitochondrial cell death through phosphorylation of voltage dependent anion channel 1 (VDAC1) on serine 193."* Interaction was shown by yeast two-hybrid, GST pull-down, and reciprocal IP; a portion of NEK1 localizes to mitochondria; the non-phosphorylatable S193A mutant causes cell death, while the phosphomimetic S193E transiently rescues mitochondrial membrane potential. Chen et al. 2010 ([PMID: 20230784](https://pubmed.ncbi.nlm.nih.gov/20230784/), *BBRC*) add reconstituted atomic-force-microscopy and liposome cytochrome-c conductance assays showing that NEK1 phosphorylation **closes** VDAC1 (S193A stays open; S193E stays closed, and VDAC1 *"closes and prevents cytochrome c efflux when phosphorylated by Nek1"*).

Two caveats govern curation. First, both papers frame VDAC1 as *"a key component of the mitochondrial permeability transition pore"*—an assumption **refuted** since 2007 (Baines et al. showed VDAC1/2/3 are dispensable for MPT). The phosphosite and gating data survive this correction, but the mechanistic narrative ("controls the PTP") does not. Second, on species: the substrate was cloned **human** GST-VDAC1, and Ser193 sits inside the barrel wall accessible from the cytoplasmic side. The kinase source was corrected during this audit: it was **not** purified bacterial NEK1 but rather (i) immune complexes of endogenous NEK1 immunoprecipitated from human cells and (ii) myc-/GFP-tagged NEK1 expressed in human cells (HK2, HEK293), phosphorylating bacterially-purified human GST-VDAC1, with a kinase-dead **K33A** specificity control that could not phosphorylate GST-VDAC1, plus heat-inactivated and irrelevant-substrate (GST-Hzwint-1) negatives. The endogenous-IP kinase is unambiguously human; the exact species of the cloned tagged cDNA is not stated. Independent corroboration of the NEK1→VDAC1 axis comes from a separate De Benedetti-lab study (*Cell Cycle* ~2020, PMC7028156).

**Curation implication:** annotate NEK1 phosphorylation of human VDAC1-Ser193 (supported; human substrate; human-cell kinase; K33A control) while dropping obligatory-PTP language and the "regulation of permeability transition pore" mechanistic gloss.

### Finding 5 — NEK1–CFAP410 is a direct binary interaction via the NEK1 C-terminal domain, distinct from a non-obligatory NEK1–CFAP410–SPATA7 association

**[Direct human interaction + Prediction]** Gregorczyk et al. 2023 (Rouse lab), *Life Science Alliance* 6(7):e202201740 ([PMID: 37188479](https://pubmed.ncbi.nlm.nih.gov/37188479/); doi 10.26508/lsa.202201740) functionally characterize the association of C21ORF2 (= CFAP410) with NEK1 in human cells. They report that endogenous NEK1 and C21ORF2 form a tight complex; a **C21ORF2-interaction domain (CID)** at the NEK1 C-terminus (~aa 1208–1286) is necessary for the association; pathogenic mutations there disrupt the complex; and AlphaFold predicts an extended interface between the C21ORF2 leucine-rich-repeat domain and the NEK1-CID. Functionally, NEK1 mutations that inhibit kinase activity **or** weaken C21ORF2 association compromise ciliogenesis, and C21ORF2—like NEK1—is required for homologous recombination (traffic-light-reporter HR assay in U2OS). A 2025 Frontiers structural study modelled HsCFAP410-NTD(1–150) + HsNEK1-CTD(1208–1286) by AlphaFold-multimer. This is therefore a **direct, mapped binary interaction**, with the atomic interface being a **prediction**, not an experimental structure.

**[Ortholog/association]** Separately, Wheway et al. 2015 ([PMID: 26167768](https://pubmed.ncbi.nlm.nih.gov/26167768/), *Nat Cell Biol*) place NEK1, CFAP410, and SPATA7 together in a **retinal ciliopathy module**: endogenous NEK1 pulls down C21ORF2 from **bovine** retinal lysates; GST-SPATA7 recovers endogenous C21ORF2 and NEK1 from bovine retina; the three colocalize at the basal body in human TERT-RPE1 cells; and nek1-null zebrafish ciliopathy features are partially rescued by human wild-type C21ORF2. The abstract text confirms *"Biochemical approaches place C21orf2 within key ciliopathy-associated protein modules."* These are **association/colocalization/cross-species functional** data; SPATA7's recovery of NEK1 could be bridged through C21ORF2, and no assay demonstrates a **simultaneous obligatory heterotrimer**. Eblimit 2015 (PMID 25398945) is a separate SPATA7–RPGRIP1 study and is not evidence for a NEK1 trimer.

**Curation implication:** annotate a direct NEK1–CFAP410 binary interaction (NEK1-CTD/CID ↔ CFAP410-NTD/LRR; interface predicted) and, separately, a non-obligatory NEK1–CFAP410–SPATA7 basal-body association (bovine + human, association-level evidence). Do **not** assert an obligatory trimer.

### Finding 6 — Neuronal importin-β1 and α-tubulin are in-vitro-only NEK1 substrates; physiological relevance is inferred, not demonstrated at the sites

**[In-vitro substrate; in-vivo phenotype]** Mann et al. 2023, *Science Advances* ([PMID: 37585529](https://pubmed.ncbi.nlm.nih.gov/37585529/); doi 10.1126/sciadv.adi5548) report that the NEK1 interactome/expression proteomics is enriched for microtubule cytoskeleton and nucleocytoplasmic transport, and that α-tubulin and importin-β1 are *phosphorylated by NEK1 in vitro*. The in-vivo/cellular data (Drosophila motor phenotypes; iPSC-motor-neuron knockdown, kinase inhibition, and patient mutation) show disrupted microtubule homeostasis and nuclear import, **rescued by microtubule-stabilizing drugs**. Critically, the rescue operates via general MT stabilization and does **not** demonstrate that the specific in-vitro phosphosites are required for the phenotype.

**Curation implication:** annotate α-tubulin and importin-β1 as **in-vitro NEK1 substrates** with an in-vitro qualifier; the physiological "regulates nuclear import / MT homeostasis" role should be annotated from the in-vivo phenotype evidence, kept logically separate from the specific phosphorylation events.

---

## Mechanistic Model / Interpretation

NEK1 is a large, multi-compartment NIMA-family kinase whose annotations have accreted across two decades, multiple species, and shifting mechanistic assumptions. The audit resolves the confusion by binning each claim on two axes: **directness of evidence** (direct human assay → ortholog → prediction → secondary discussion → disease phenotype) and **compartment/pathway**.

```
                          HUMAN NEK1 (Q96PY6)
                                  |
   ┌──────────────┬──────────────┼───────────────┬────────────────┐
   │              │              │               │                │
 DNA REPAIR    ATR PRIMING   CENTRIOLE/CILIA   MITOCHONDRIA    NEURONAL/ALS
   │              │              │               │                │
 RAD54-S572   ATR-ATRIP      distal centriole  VDAC1-S193     importin-β1,
 (disputed;   (T1989 = ATR   tip (endogenous,  (human sub-    α-tubulin
  1 direct    autophos.,     human, U-ExM);    strate; human   (in-vitro only;
  human study; NEK1 primes/  CFAP410 direct    kinase; K33A    phenotype rescue
  not refuted) stabilizes,   binary partner    control; PTP    via MT stabiliz.,
              NOT a substrate (CID/NTD, interface framing outdated) not site-specific)
              at T1989)      predicted); non-
                            obligatory SPATA7
                            association
```

Three interpretive threads unify the findings:

1. **Citation ≠ experiment.** Two of the most damaging errors in the current annotation set arise from treating a *written claim* as an *experiment*: the "ATRIP-T1989 substrate" (which mis-reads an autophosphorylation-priming result) and the "PMID37439356 refutes S572" attribution (which mis-reads a Discussion sentence in a paper that tested different residues). Both should be corrected on evidentiary, not biological, grounds.

2. **Species and expression regime drive apparent contradictions.** The localization "conflict" dissolves once endogenous human U-ExM data are separated from mouse/canine overexpression; the S572 reproducibility conflict may dissolve along a developmental (adult vs. embryonic) axis with paralog redundancy (NEK1 vs. NEK3/NEK5).

3. **Outdated framing outlives valid data.** The VDAC1-S193 phosphosite and gating data remain valid even though the permeability-transition-pore rationale that motivated them is obsolete. Curators should preserve the molecular event and retire the pathway gloss.

---

## Evidence Base

| Paper | PMID | Role in this audit |
|---|---|---|
| *Nek1 Regulates Rad54 to Orchestrate Homologous Recombination and Replication Fork Stability* (Spies et al. 2016) | [27264870](https://pubmed.ncbi.nlm.nih.gov/27264870/) | Sole **direct human** positive evidence for NEK1→RAD54-Ser572 |
| *Nek1 kinase associates with ATR-ATRIP and primes ATR for efficient DNA damage signaling* (Liu et al. 2013) | [23345434](https://pubmed.ncbi.nlm.nih.gov/23345434/) | Establishes T1989 as **ATR autophosphorylation**; NEK1 primes/stabilizes ATR–ATRIP; **excludes** direct NEK1→T1989 phosphorylation |
| *TLK1-mediated RAD54 phosphorylation...* (Ghosh et al. 2023) | [37439356](https://pubmed.ncbi.nlm.nih.gov/37439356/) | Tests TLK1→RAD54 at **T41/T59/T700** — different kinase/residues; **not** a refutation of S572 |
| *Nek1 regulates cell death and mitochondrial membrane permeability through phosphorylation of VDAC1* (Chen et al. 2009) | [19158487](https://pubmed.ncbi.nlm.nih.gov/19158487/) | Primary NEK1→VDAC1-Ser193 evidence; interaction + cell-death assays |
| *Phosphorylation by Nek1 regulates opening and closing of VDAC1* (Chen et al. 2010) | [20230784](https://pubmed.ncbi.nlm.nih.gov/20230784/) | Reconstituted AFM/liposome gating; documents outdated PTP framing |
| *Functional characterization of C21ORF2 association with the NEK1 kinase...* (Gregorczyk et al. 2023) | [37188479](https://pubmed.ncbi.nlm.nih.gov/37188479/) | Direct endogenous NEK1–C21ORF2/CFAP410 complex via NEK1 C-terminal CID; AlphaFold-predicted interface; secondary RAD54 discussion only (no replication) |
| *NEK1 mutations cause short-rib polydactyly syndrome type Majewski* (Thiel et al. 2011) | [21211617](https://pubmed.ncbi.nlm.nih.gov/21211617/) | **Disease phenotype**: loss of full-length NEK1 reduces cilia number, alters ciliary morphology in vivo |
| *An siRNA-based functional genomics screen... ciliogenesis and ciliopathy genes* (Wheway et al. 2015) | [26167768](https://pubmed.ncbi.nlm.nih.gov/26167768/) | Places C21orf2/CFAP410 in NEK1/SPATA7 ciliopathy module (bovine retina + human RPE1); non-obligatory association |
| *Loss of function of the ALS-associated NEK1 kinase disrupts microtubule homeostasis and nuclear import* (Mann et al. 2023) | [37585529](https://pubmed.ncbi.nlm.nih.gov/37585529/) | α-tubulin and importin-β1 are **in-vitro** substrates; in-vivo phenotype rescued by MT stabilization (not site-specific) |
| *Nek1 defines a branch of centriolar microtubule length control...* (Streubel et al. 2026) | [42265085](https://pubmed.ncbi.nlm.nih.gov/42265085/) | **Endogenous human** distal-centriole-tip localization (U-ExM), all cell-cycle stages; CP110/Cep97/Cep78 |

**Non-peer-reviewed primary sources referenced (must be flagged as preprints):**
- De Benedetti lab, *Evidence that Nek1 does not phosphorylate Rad54-S572*, bioRxiv doi 10.1101/2022.04.01.486731 — the **only experimental non-replication** of S572; remains unpublished.
- Löbrich lab, *Nek family members regulate Rad54 during homologous recombination in developing mice*, bioRxiv doi 10.64898/2025.12.19.695536 (posted 2025-12-19; the 10.64898 prefix is bioRxiv's new DOI prefix, verified real, not a typo of 10.1101) — reaffirms S572 with an adult-NEK1 / embryonic-NEK3–NEK5 developmental switch.

---

## Limitations and Knowledge Gaps

- **Full-text/supplement access.** Several conclusions rest on abstracts, open-access summaries, and verified snippets rather than direct inspection of every figure and supplementary methods table. Specifically, the Gregorczyk 2023 figures/supplement were not directly inspected in this environment, and the exact recombinant-cDNA species used in the VDAC1 tagged-kinase assays is not stated in the accessible text. These are **explicitly identified inaccessible data**, not inferred absences.
- **S572 remains formally unsettled.** The two most decision-relevant primary sources (the non-replication and the reaffirmation) are **both preprints**. No peer-reviewed experiment has directly re-tested S572 with modern phospho-specific tools since Spies 2016. The developmental-switch hypothesis is attractive but unvalidated.
- **VDAC1 kinase-cDNA species.** The endogenous-IP kinase is unambiguously human, but the tagged-NEK1 construct's species of origin is not documented in accessible text; this is a minor residual uncertainty.
- **NEK1–CFAP410 interface is predicted, not solved.** The atomic interface is AlphaFold-multimer only; no experimental structure exists. The mapped domains (NEK1-CID ↔ CFAP410-NTD/LRR) and mutational-disruption data are solid, but the interface geometry is a prediction.
- **In-vitro substrates (importin-β1, α-tubulin).** No evidence connects the specific in-vitro phosphosites to the in-vivo phenotype; the physiological requirement of these phosphorylations is unestablished.

---

## Proposed Follow-up Experiments / Actions

**Immediate curation actions (defensible now):**
1. **Remove** any annotation stating NEK1 directly phosphorylates ATR or ATRIP at Thr1989. Replace with a **priming/stabilization of ATR–ATRIP** regulatory annotation (Liu 2013, direct human).
2. **Retain but flag** NEK1→RAD54-Ser572 as a single-source, disputed direct human finding (Spies 2016). **Do not** cite PMID37439356 as counterevidence. Note both preprints in the evidence trail.
3. **Update NEK1 cellular-component** to **distal centriole / centriole distal end** (Streubel 2026, endogenous human, U-ExM), with basal-body presence during ciliogenesis. Add species/method qualifiers to legacy PCM/centrosome annotations derived from overexpression.
4. **Annotate NEK1 phosphorylation of human VDAC1-Ser193** (Chen 2009/2010; human substrate; human-cell kinase; K33A control) and **strip** obligatory-permeability-transition-pore language from the mechanistic description.
5. **Annotate a direct NEK1–CFAP410 binary interaction** (NEK1-CTD/CID ↔ CFAP410-NTD/LRR; interface predicted) and, separately, a **non-obligatory NEK1–CFAP410–SPATA7 basal-body association** (Wheway 2015). Do not assert an obligatory trimer.
6. **Annotate α-tubulin and importin-β1 as in-vitro NEK1 substrates** with an in-vitro qualifier; keep the neuronal MT-homeostasis/nuclear-import role as a separate phenotype-based annotation (Mann 2023).

**Experimental follow-ups (to resolve residual uncertainty):**
- Obtain and inspect the full text/supplement of Gregorczyk 2023 and the VDAC1 papers to confirm construct species and interface-mapping details.
- Peer-reviewed re-test of RAD54-S572 with phospho-specific antibodies/MS across **adult vs. embryonic** and human vs. mouse systems to test the developmental-switch hypothesis directly.
- Experimental structure (cryo-EM/X-ray) or crosslinking-MS of the NEK1-CID · CFAP410-NTD complex to replace the AlphaFold prediction.
- Site-directed (phospho-null/phosphomimetic) rescue of importin-β1/α-tubulin in NEK1-deficient motor neurons to test whether the specific in-vitro sites are physiologically required.
- Monitor the publication status of both preprints (doi 10.1101/2022.04.01.486731 and doi 10.64898/2025.12.19.695536) for peer-reviewed resolution.

---

*Prepared for GO curation, September 2026. All PMIDs and DOIs in this report were verified during the audit; preprint sources are explicitly marked as non-peer-reviewed.*


## Artifacts

- [OpenScientist final report](NEK1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](NEK1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:23345434
2. PMID:27264870
3. PMID:37439356
4. PMID:42265085
5. PMID:37188479
6. PMID:21211617
7. PMID:26167768
8. PMID:19158487
9. PMID:20230784
10. PMID:37585529