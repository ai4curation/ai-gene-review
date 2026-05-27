# SPKW Bacteriophage T4 (BPT4) Subproject

**Parent project:** [SPKW.md](SPKW.md)

## Overview

Bacteriophages present a unique test case for SPKW annotation quality. Many GO terms relating to host-pathogen interactions were designed for eukaryotic pathogens (viruses, bacteria, fungi) infecting eukaryotic hosts. When these terms are applied to bacteriophages (which infect bacteria), semantic mismatches can occur.

**Key question**: Do GO terms for broad "immune suppression" and "defense response" capture bacteriophage biology, or should they be replaced by precise bacterial anti-phage counter-defense and viral release terms?

## Statistics

| Metric | Count |
|--------|-------|
| T4 genes in UniProt | ~300 |
| SPKW annotations originally targeted in this focused case study | ~150 |
| Manually reviewed high-risk genes in this subproject | 3 |

Updated `virus.ddb` counts for Enterobacteria phage T4 (`taxon:10665`) on 2026-05-21:

| Metric | Count |
|--------|------:|
| Raw SPKW annotations (`GO_REF:0000043` / `UniProtKB-KW`) | 461 |
| Proteins with SPKW annotations | 129 |
| Distinct UniProt keywords observed | 77 |
| Naive SPKW-unique annotations | 353 |
| Closure-filtered SPKW-unique annotations | 209 |
| ViralZone-primary KW annotations | 91 |
| Proteins with ViralZone-primary KW annotations | 44 |
| Distinct ViralZone-primary KWs observed | 24 |
| Closure-filtered unique annotations from ViralZone-primary KWs | 50 |
| Closure-filtered unique annotations from other KWs | 159 |

The original three gene reviews deliberately targeted high-risk SPKW rows, so their 3/3 failure rate should not be read as the rate for all T4 SPKW. The ViralZone split shows a more useful pattern: broad non-VZ keywords drive the worst over-annotations, while many VZ-primary keywords are phage-specific and are often better replacement targets.

## ViralZone-Primary Keyword Analysis

For this section, `VZ-primary` means the UniProt keyword is the primary keyword declared in a ViralZone page header. This is a confidence flag, not evidence by itself. It helps distinguish deliberate viral biology terms from generic UniProt keywords such as `hydrolase`, `virion`, `DNA binding`, or broad immune-response labels.

### High-Signal VZ-Primary T4 Rows

| VZ / KW | GO term | T4 rows | Representative T4 rows reviewed | Manual assessment |
|---------|---------|--------:|---------------------------------|-------------------|
| VZ-3958 / KW-1227 Viral tail protein | GO:0098015 virus tail | 20 | `10/P10928`; `11/P10929`; `12/P10930`; `18/P13332`; `19/P13333`; `25/P09425`; `27/P17172`; `35/P03742`; `36/P03743`; `37/P03744`; `5/P16009`; `53/P16011`; `54/P13341` | Mostly ACCEPT. This is a useful phage-specific CC term for actual tail proteins. Prefer it over generic `virion component` when tail localization is the meaningful structure. |
| VZ-3955 / KW-1245 Viral tail assembly | GO:0098003 viral tail assembly | 17 | `10/P10928`; `11/P10929`; `26/P13335`; `27/P17172`; `28/P13336`; `29/P13337`; `38/P03739`; `48/P13339`; `5/P16009`; `51/P17173`; `57/P04532`; `6/P19060`; `7/P19061`; `8/P19062`; `9/P10927` | Mostly ACCEPT for bona fide tail assembly factors and baseplate/tail components. Review whether a structural component is directly involved in assembly or only part of the assembled tail. |
| VZ-3957 / KW-1226 Viral baseplate protein | GO:0098025 virus tail, baseplate | 12 | `10/P10928`; `11/P10929`; `25/P09425`; `27/P17172`; `48/P13339`; `5/P16009`; `53/P16011`; `54/P13341`; `6/P19060`; `7/P19061`; `8/P19062`; `9/P10927` | ACCEPT as a precise CC term. This is exactly the kind of granularity that should replace broad `virion component`. |
| VZ-3950 / KW-1242 Viral contractile tail ejection system | GO:0099000 symbiont genome ejection through host cell envelope, contractile tail mechanism | 3 | `18/P13332`; `19/P13333`; `20/P13334` | ACCEPT. UniProt says gp18 sheath contraction drives gp19 tube penetration and creates the DNA-ejection channel; gp20 is the portal vertex involved in genome ejection. |
| VZ-4416 / KW-1230 and VZ-3943 / KW-1233 Tail fiber / adhesion receptor attachment | GO:0098024 virus tail, fiber; GO:0098671 adhesion receptor-mediated virion attachment to host cell | 5 / 3 | `12/P10930`; `35/P03742`; `36/P03743`; `37/P03744` | ACCEPT/MODIFY to the specific attachment or tail-fiber term. gp12 binds Escherichia coli LPS irreversibly; gp36/gp37 are distal long-tail fiber receptor-recognition proteins. Generic `symbiont entry into host cell` should be non-core when these terms are present. |
| VZ-3942 / KW-1234 Viral attachment to host entry receptor | GO:0098670 entry receptor-mediated virion attachment to host cell | 1 | `12/P10930` | ACCEPT. gp12 short tail fiber binds the LPS receptor/core region during irreversible attachment. |
| VZ-3938 / KW-1235 and VZ-3940 / KW-1236 Host envelope / peptidoglycan disruption during entry | GO:0098994 host envelope disruption; GO:0098932 peptidoglycan disruption | 1 / 1 | `5/P16009` | ACCEPT/MODIFY. gp5 is the baseplate central spike with lysozyme activity that locally digests peptidoglycan so the tail tube can penetrate. This is the correct phage-entry framing; the non-VZ `defense response to bacterium` and `killing of cells` rows on gp5 are over-annotations. |
| VZ-3966 / KW-1258 Restriction-modification system evasion by virus | GO:0099018 symbiont-mediated evasion of host restriction-modification system | 5 | <gene species="BPT4" symbol="DAM">DAM/P04392</gene>; `agt/P04519`; `bgt/P04547`; `arn/P39510`; `stp/P62765` | ACCEPT for the antirestriction mechanism. This VZ-primary term is the right replacement target for broad non-VZ `innate immune suppression` on phage DNA-modification and restriction-evasion proteins. |
| VZ-3963 / KW-1256 DNA end degradation evasion by virus | GO:0099016 symbiont-mediated evasion of DNA end degradation by host | 1 | `2/P15076` | ACCEPT. gp2 binds T4 DNA ends and protects them against RecBCD-mediated degradation. The coexisting broad non-VZ `GO:0052170` should be removed or replaced. |
| VZ-3962 / KW-1257 CRISPR-cas system evasion by virus | GO:0098672 symbiont-mediated suppression of host CRISPR-cas system | 1 | `agt/P04519` | ACCEPT when the CRISPR protection evidence is present. For agt, UniProt states glucosyl-HMC protects against CRISPR-Cas9 as well as restriction systems, so both CRISPR-cas evasion and R-M evasion can be justified. |
| VZ-3947 / KW-1247 Degradation of host chromosome by virus | GO:0099015 degradation of host chromosome by virus | 3 | `46/P04522`; `47/P04521`; `denA/P07059` | Usually ACCEPT for the host-DNA degradation proteins. gp46/gp47 and DenA have direct host DNA degradation roles, but broad coannotations such as `suppression of host gene expression` should not be treated as the primary function. |
| VZ-260 / KW-1146 T=13 icosahedral capsid protein and VZ-4398 / KW-1232 Capsid decoration protein | GO:0039621 T=13 icosahedral viral capsid; GO:0098021 viral capsid, decoration | 1 / 1 | `gp23/P04535`; `soc/P03715` | ACCEPT. gp23 is the major T=13 capsid protein; Soc is a capsid decoration/stabilization protein. These are good VZ-primary structural rows. |

### VZ-Primary Rows That Still Need Caution

| VZ / KW | T4 row | Why caution is needed | Curation response |
|---------|--------|----------------------|------------------|
| VZ-884 / KW-1080 Inhibition of host adaptive immune response by virus | `agt/P04519` -> GO:0039504 | The specific CRISPR-cas term is present and better. The adaptive-immune parent is much broader and can look eukaryote-centric in phage reports. | KEEP_AS_NON_CORE at best, or MODIFY to GO:0098672 when CRISPR-cas is the supported mechanism. |
| VZ-1636 / KW-1121 Modulation of host cell cycle by virus | `ndd/P15556` -> GO:0044071 | Ndd disrupts the host nucleoid and inhibits host DNA replication, but `host cell cycle progression` is broader than the evidence in the UniProt record. | Prefer GO:0098673 symbiont-mediated suppression of host DNA replication. Treat the cell-cycle term as over-broad unless a reviewer finds direct cell-cycle evidence. |
| VZ-895 / KW-0347 Helicase | `41/P04530`; `dda/P32270`; `uvsW/P0DXF1` | The MF is directionally correct but generic. Some T4 helicases already have more specific replication/recombination context. | Usually KEEP_AS_NON_CORE or MODIFY if a specific helicase activity/process term is available. |

### Non-VZ Rows Driving the Original BPT4 Failures

| KW / GO term | T4 rows | Manual interpretation |
|--------------|---------|----------------------|
| KW-1090 -> GO:0052170 symbiont-mediated suppression of host innate immune response | `2/P15076`; <gene species="BPT4" symbol="DAM">DAM/P04392</gene>; `adfA/P39229`; `agt/P04519`; `arn/P39510`; `bgt/P04547`; `stp/P62765` | Systematic phage over-annotation. Replace with GO:0099018 R-M evasion, GO:0099016 DNA-end degradation evasion, or GO:0098672 CRISPR-cas suppression as appropriate. |
| KW-0081 -> GO:0042742 defense response to bacterium and GO:0031640 killing of cells of another organism | <gene species="BPT4" symbol="E">E/P00720</gene>; `5/P16009` | Defense/offense inversion. E is a lysis enzyme for viral release; gp5 is an entry spike/lysozyme. Use viral release/cytolysis for E and peptidoglycan-disruption entry terms for gp5. |
| KW-0204 -> GO:0031640 killing of cells of another organism | `rI/P13304`; `t/P06808`; `y13J/P39503`; `y13K/P39504` | Likely over-broad lysis outcome annotation. Review for holin/endolysin/spanin release biology rather than generic cell killing. |
| KW-0046 and KW-0487 -> response to antibiotic / response to methotrexate | `ac/P18924`; <gene species="BPT4" symbol="frd">frd/P04382</gene> | Drug-target conflation. Being inhibited by a drug or resembling a resistance enzyme is not a viral biological response. |
| KW-0946 -> GO:0044423 virion component | 39 structural rows including `18/P13332`, `19/P13333`, `gp23/P04535`, `soc/P03715`, `wac/P10104` | Usually not wrong, but too broad to be the main review conclusion when VZ-primary tail/capsid/baseplate/sheath/tube terms exist. |
| Generic MF keywords such as KW-0378 hydrolase, KW-0238 DNA binding, KW-0808 transferase, KW-0479 metal ion binding | 14-36 rows per keyword | Often true but weak. Prefer specific MF terms such as lysozyme activity, DNA alpha/beta-glucosyltransferase activity, DNA methyltransferase activity, exonuclease/endonuclease activity, or helicase activity. |

### VZ Impact on the BPT4 Conclusion

The BPT4 conclusion should be more nuanced than "SPKW is bad for phages":

1. The original local reviews remain valid: <gene species="BPT4" symbol="DAM">DAM/P04392</gene>, <gene species="BPT4" symbol="E">E/P00720</gene>, and <gene species="BPT4" symbol="frd">frd/P04382</gene> expose real SPKW over-annotation.
2. ViralZone-primary status strongly improves the prior for phage-specific terms: tail proteins, baseplate proteins, contractile-tail ejection, receptor attachment, peptidoglycan-disruption entry, R-M evasion, DNA-end protection, and CRISPR-cas evasion are mostly valid in the T4 spot check.
3. VZ-primary is not automatic acceptance: `agt/P04519` and `ndd/P15556` show that broad parent terms can remain too general even when the keyword is ViralZone-backed.
4. For T4 curation, the most actionable cleanup pattern is not "remove all SPKW"; it is "replace broad non-VZ parent terms with the precise VZ-primary phage mechanism where supported."

## Full YAML Review Pass

The BPT4 gene-review YAML files were then reviewed directly, not only via row-level spot checks. This pass reviewed every `existing_annotations` entry in the three local review files and updated action calls so that precise supported functions remain core, while broad parent terms are kept only as non-core.

| Review file | Existing annotations reviewed | Final action profile | Main changes from the direct YAML review |
|-------------|------------------------------:|----------------------|------------------------------------------|
| <gene species="BPT4" symbol="DAM">DAM/P04392</gene> | 13 | ACCEPT 3; KEEP_AS_NON_CORE 3; MODIFY 6; REMOVE 1 | Demoted broad DNA binding, methyltransferase, and transferase parent terms from ACCEPT to KEEP_AS_NON_CORE. Changed both `GO:0032259 methylation` rows to MODIFY with replacement `GO:0006304 DNA modification`. Recast the broad host-defense/innate-immune rows as MODIFY to the already present `GO:0099018` VZ-primary R-M evasion term, rather than relying on a blanket "bacteria lack immunity" argument. |
| <gene species="BPT4" symbol="E">E/P00720</gene> | 13 | ACCEPT 6; KEEP_AS_NON_CORE 4; MODIFY 1; REMOVE 2 | Demoted broad catalytic/hydrolase/cell-wall parent terms to KEEP_AS_NON_CORE and added primary-paper support to those non-core calls. Changed `GO:0031640 killing of cells of another organism` to MODIFY with replacement `GO:0044659 viral release from host cell by cytolysis`. Changed the `PMID:4582731` lysozyme annotation to REMOVE because that PMID is for T7 lysozyme, not T4 gene E. |
| <gene species="BPT4" symbol="frd">frd/P04382</gene> | 7 | ACCEPT 3; KEEP_AS_NON_CORE 2; REMOVE 2 | Kept DHFR activity and tetrahydrofolate biosynthesis as the core supported terms. Demoted broad one-carbon metabolism and oxidoreductase activity to KEEP_AS_NON_CORE. Retained removal of methotrexate and antibiotic response terms as drug-target conflation. Revised the description to avoid treating the historical virion/baseplate claim as settled, because later immunoblot work disputes DHFR as a bona fide virion structural protein. |

The only validator warning after this pass is intentional: `E/P00720` has three `GO:0003796 lysozyme activity` entries that remain accepted and one `GO:0003796` entry removed because its original reference is wrong. This is a reference-level curation exception, not a disagreement about T4 lysozyme activity.

## Deeper Evidence Review

The follow-up pass applied the AIGR review-skill standard explicitly: do not re-check schema details after validation; instead check biological judgment, GO specificity, evidence quality, and core-function coherence. Manual notes were added for each reviewed gene so the evidence trail is visible outside the rendered action table.

| Gene | Evidence reviewed | Deeper curation outcome |
|------|-------------------|-------------------------|
| <gene species="BPT4" symbol="DAM">DAM/P04392</gene> | `DAM-goa.tsv`, `DAM-uniprot.txt`, `DAM-deep-research-falcon.md`, `PMID_2510127.md`, `PMID_7782299.md`, `PMID_12937411.md`, `PMID_15882618.md`, `DAM-notes.md` | Core remains site-specific DNA adenine methyltransferase activity. The broad SPKW immune rows are now replacement calls to `GO:0099018` rather than simple removals; this is more curatorially precise because the real mechanism is phage antirestriction. |
| <gene species="BPT4" symbol="E">E/P00720</gene> | `E-goa.tsv`, `E-uniprot.txt`, `E-deep-research-falcon.md`, `PMID_1201752.md`, `PMID_4582731.md`, `PMID_4865643.md`, `PMID_8266098.md`, `PMID_22389108.md`, `E-notes.md` | Core remains lysozyme/muramidase activity directly involved in peptidoglycan catabolism and viral release by cytolysis. The cell-killing row is now a concrete MODIFY to viral release, and the T7 lysozyme citation remains removed. |
| <gene species="BPT4" symbol="frd">frd/P04382</gene> | `frd-goa.tsv`, `frd-uniprot.txt`, `frd-deep-research-falcon.md`, `PMID_4936128.md`, `PMID_10818362.md`, `PMID_6327673.md`, `PMID_1560001.md`, `frd-notes.md`; additional PubMed/PMC search for the baseplate dispute | Core remains DHFR activity in tetrahydrofolate biosynthesis. No virion/baseplate annotation should be proposed from the older structural claim without addressing the later immunoblot paper showing TS/DHFR are minor contaminants, not bona fide virion proteins. |

## Highlighted Gene Deep Research Coverage

All 49 BPT4 genes explicitly highlighted in the VZ/non-VZ tables and case summaries now have provider deep-research files. The three original full-review genes already had Falcon reports; the remaining highlighted genes were fetched with UniProt/GOA context and backfilled with Falcon reports on 2026-05-22. Coverage manifest: `reports/spkw_bpt4_highlighted_deep_research_coverage.tsv`.

| Coverage slice | Highlighted genes covered |
|----------------|---------------------------|
| Structural, entry, tail, baseplate, and capsid rows | <gene species="BPT4" symbol="10">10/P10928</gene>; <gene species="BPT4" symbol="11">11/P10929</gene>; <gene species="BPT4" symbol="12">12/P10930</gene>; <gene species="BPT4" symbol="18">18/P13332</gene>; <gene species="BPT4" symbol="19">19/P13333</gene>; <gene species="BPT4" symbol="20">20/P13334</gene>; <gene species="BPT4" symbol="25">25/P09425</gene>; <gene species="BPT4" symbol="26">26/P13335</gene>; <gene species="BPT4" symbol="27">27/P17172</gene>; <gene species="BPT4" symbol="28">28/P13336</gene>; <gene species="BPT4" symbol="29">29/P13337</gene>; <gene species="BPT4" symbol="35">35/P03742</gene>; <gene species="BPT4" symbol="36">36/P03743</gene>; <gene species="BPT4" symbol="37">37/P03744</gene>; <gene species="BPT4" symbol="38">38/P03739</gene>; <gene species="BPT4" symbol="48">48/P13339</gene>; <gene species="BPT4" symbol="5">5/P16009</gene>; <gene species="BPT4" symbol="51">51/P17173</gene>; <gene species="BPT4" symbol="53">53/P16011</gene>; <gene species="BPT4" symbol="54">54/P13341</gene>; <gene species="BPT4" symbol="57">57/P04532</gene>; <gene species="BPT4" symbol="6">6/P19060</gene>; <gene species="BPT4" symbol="7">7/P19061</gene>; <gene species="BPT4" symbol="8">8/P19062</gene>; <gene species="BPT4" symbol="9">9/P10927</gene>; <gene species="BPT4" symbol="gp23">gp23/P04535</gene>; <gene species="BPT4" symbol="soc">soc/P03715</gene>; <gene species="BPT4" symbol="wac">wac/P10104</gene> |
| Defense evasion and host-manipulation rows | <gene species="BPT4" symbol="DAM">DAM/P04392</gene>; <gene species="BPT4" symbol="2">2/P15076</gene>; <gene species="BPT4" symbol="adfA">adfA/P39229</gene>; <gene species="BPT4" symbol="agt">agt/P04519</gene>; <gene species="BPT4" symbol="arn">arn/P39510</gene>; <gene species="BPT4" symbol="bgt">bgt/P04547</gene>; <gene species="BPT4" symbol="stp">stp/P62765</gene>; <gene species="BPT4" symbol="ndd">ndd/P15556</gene>; <gene species="BPT4" symbol="46">46/P04522</gene>; <gene species="BPT4" symbol="47">47/P04521</gene>; <gene species="BPT4" symbol="denA">denA/P07059</gene> |
| Enzyme, helicase, lysis, and drug-response caution rows | <gene species="BPT4" symbol="E">E/P00720</gene>; <gene species="BPT4" symbol="frd">frd/P04382</gene>; <gene species="BPT4" symbol="ac">ac/P18924</gene>; <gene species="BPT4" symbol="41">41/P04530</gene>; <gene species="BPT4" symbol="dda">dda/P32270</gene>; <gene species="BPT4" symbol="uvsW">uvsW/P0DXF1</gene>; <gene species="BPT4" symbol="rI">rI/P13304</gene>; <gene species="BPT4" symbol="t">t/P06808</gene>; <gene species="BPT4" symbol="y13J">y13J/P39503</gene>; <gene species="BPT4" symbol="y13K">y13K/P39504</gene> |

## Problematic Term Categories

1. **Eukaryotic immune terms applied to phage-bacteria interactions**:
   - GO:0052170 (symbiont-mediated suppression of host innate immune response)
   - GO:0052031 (symbiont-mediated perturbation of host defense response)
   - GO:0042742 (defense response to bacterium)

2. **Antibiotic response terms applied to phage enzymes**:
   - GO:0046677 (response to antibiotic)
   - GO:0031427 (response to methotrexate)

## Status

- [x] Initial exploration complete (2026-01-31)
- [x] Deep research for all 3 genes (2026-01-31)
- [x] Annotation review complete for all 3 genes (2026-01-31)
- [x] Write-up complete (2026-01-31)

---

## Case Studies (3 genes reviewed)

### Case 1: DAM - DNA Adenine Methyltransferase

**Gene:** <gene species="BPT4" symbol="DAM">DAM/P04392</gene> - DNA adenine methylase

**Review file:** `genes/BPT4/DAM/DAM-ai-review.yaml`

**SPKW annotations to review:**
- GO:0052170 (symbiont-mediated suppression of host innate immune response)
- GO:0052031 (symbiont-mediated perturbation of host defense response)

**Review decision:** **MODIFY** both annotations to GO:0099018 (symbiont-mediated evasion of host restriction-modification system)

**Analysis:** This is a clear case where a broad immune/defense keyword should be converted to the specific phage counter-defense mechanism:

```
GO:0052170 Definition:
"Suppression by the symbiont of the innate immune response of the host organism"

The problem:
┌─────────────────────────────────────────────────────────────────────────────┐
│ The evidence does not show general host innate-immune suppression          │
│                                                                             │
│ Eukaryotic innate immunity: Pattern recognition receptors (TLRs), cytokines│
│ Bacterial anti-phage defense: Restriction-modification, CRISPR-Cas, Abi    │
│                                                                             │
│ T4 Dam fits the restriction-modification evasion branch, not a broad parent│
└─────────────────────────────────────────────────────────────────────────────┘
```

**Replacement term (already present):** GO:0099018 (symbiont-mediated evasion of host restriction-modification system)
- Definition explicitly mentions phages and bacterial R-M systems
- Accurately describes T4 Dam's biological role

**T4 Dam's actual function:**
1. Methylates `GATC` sites on phage DNA (Dam methylation)
2. Protects phage DNA from host restriction enzymes (DpnI, EcoRV, etc.)
3. May also regulate phage gene expression timing

**Why the SPKW keyword is too broad:** UniProt keyword "Inhibition of host innate immune response by virus" is not the right endpoint for T4 Dam. The supported biology is DNA adenine methylation that lets phage DNA evade host restriction enzymes, so the curation action is a replacement rather than a bare removal.

---

### Case 2: E - T4 Lysozyme

**Gene:** <gene species="BPT4" symbol="E">E/P00720</gene> - T4 phage lysozyme

**Review file:** `genes/BPT4/E/E-ai-review.yaml`

**SPKW annotations to review:**
- GO:0042742 (defense response to bacterium)
- GO:0031640 (killing of cells of another organism)

**Review decision:** **REMOVE** GO:0042742; **MODIFY** GO:0031640 to GO:0044659 (viral release from host cell by cytolysis)

**Analysis:** This annotation inverts the biological relationship:

```
GO:0042742 Definition:
"Reactions triggered in response to the presence of a bacterium that act
to protect the cell or organism"

How this term is properly used:
  Eukaryote (human) → produces lysozyme → kills invading bacteria
  This is DEFENSE

How it's misapplied to T4 lysozyme:
  T4 phage → produces lysozyme → lyses host bacterium for viral release
  This is PARASITISM, not defense!
```

**T4 lysozyme's actual function:**
1. Hydrolyzes peptidoglycan (beta-1,4 glycosidic bonds between NAM and NAG)
2. Part of the holin-endolysin-spanin lysis system
3. Enables progeny phage release through host cell lysis

**Correct annotation:** GO:0044659 (viral release from host cell by cytolysis) - already present and correctly describes the biological process.

**Additional issue found:**
- GO:0031640 (killing of cells of another organism) is directionally related to lysis but too broad.
- The host bacterium is the organism in which the phage replicates; viral release by cytolysis is the defensible process term.

**Reference error noted:** PMID:4582731 is about T7 lysozyme (an amidase), not T4 lysozyme (a muramidase). The citation was incorrectly associated in the source database.

---

### Case 3: frd - Dihydrofolate Reductase

**Gene:** <gene species="BPT4" symbol="frd">frd/P04382</gene> - Dihydrofolate reductase (T4 DHFR)

**Review file:** `genes/BPT4/frd/frd-ai-review.yaml`

**SPKW annotations to review:**
- GO:0046677 (response to antibiotic)
- GO:0031427 (response to methotrexate)

**Review decision:** **REMOVE** both annotations

**Analysis:** This conflates "being a drug target" with "responding to a drug":

```
The logic error:
┌─────────────────────────────────────────────────────────────────────────────┐
│ UniProt keywords: "Antibiotic resistance", "Trimethoprim resistance"        │
│                              ↓ (mapped to)                                  │
│ GO term: "response to antibiotic"                                           │
│                                                                             │
│ Problem: Being INHIBITED by an antibiotic ≠ RESPONDING to an antibiotic    │
│                                                                             │
│ - DHFR is the TARGET of trimethoprim (inhibits the enzyme)                  │
│ - Phages don't have "antibiotic response pathways"                          │
│ - T4 DHFR does NOT confer trimethoprim resistance                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Literature evidence (PMID:32253217, Sanchez-Osuna 2020):**
> "Phage-encoded DHFRs do NOT confer trimethoprim resistance despite homology"
> "Phage folA genes primarily serve phage nucleotide metabolism rather than resistance"

**T4 DHFR's actual function:**
1. Reduces dihydrofolate to tetrahydrofolate
2. Essential for thymidylate synthesis during phage DNA replication
3. Contributes to the phage's unique nucleotide pool (hydroxymethylcytosine production)

**Correct annotations (retained):**
- GO:0004146 (dihydrofolate reductase activity)
- GO:0046654 (tetrahydrofolate biosynthetic process)

---

## Reviewed High-Risk Over-Annotation Patterns

| Pattern | Example | Frequency | Severity |
|---------|---------|-----------|----------|
| **Eukaryotic immune terms for phage** | DAM (innate immune suppression) | High | **Critical** |
| **Defense/offense inversion** | E lysozyme (defense response) | Medium | High |
| **Drug target as drug response** | frd (antibiotic response) | Medium | Medium |

## Summary: Reviewed High-Risk Cases 3/3 Problematic

All three locally reviewed high-risk T4 phage genes had over-annotated SPKW-unique rows:

| Gene | UniProt | Problematic Annotation | Action | Correct Term |
|------|---------|------------------------|--------|--------------|
| <gene species="BPT4" symbol="DAM">DAM/P04392</gene> | P04392 | symbiont-mediated suppression of host innate immune response | **MODIFY** | GO:0099018 (R-M system evasion) |
| <gene species="BPT4" symbol="DAM">DAM/P04392</gene> | P04392 | symbiont-mediated perturbation of host defense response | **MODIFY** | GO:0099018 (R-M system evasion) |
| <gene species="BPT4" symbol="E">E/P00720</gene> | P00720 | defense response to bacterium | **REMOVE** | GO:0044659 (viral release by cytolysis) |
| <gene species="BPT4" symbol="E">E/P00720</gene> | P00720 | killing of cells of another organism | **MODIFY** | GO:0044659 (viral release by cytolysis) |
| <gene species="BPT4" symbol="frd">frd/P04382</gene> | P04382 | response to antibiotic | **REMOVE** | (MF terms sufficient) |
| <gene species="BPT4" symbol="frd">frd/P04382</gene> | P04382 | response to methotrexate | **REMOVE** | (MF terms sufficient) |

## Key Lessons from Bacteriophage Analysis

1. **GO terms encode eukaryote-centric biology**: Terms like "innate immune response" and "defense response" assume eukaryotic biology. Bacterial anti-phage systems (R-M, CRISPR) require different terminology.

2. **Host-pathogen terms need taxonomic context**: A term describing how a virus evades mammalian immunity should not be applied to a phage evading bacterial restriction.

3. **Some UniProt keywords are eukaryote-biased**: Keywords like "Inhibition of host innate immune response by virus" were created for eukaryotic viruses and don't translate cleanly to bacteriophages. ViralZone-primary phage terms are less prone to this problem but still need protein-level review.

4. **"Defense" depends on perspective**: From the phage's perspective, lysozyme enables reproduction. From the bacterium's perspective, it's attack. Neither is "defense response to bacterium."

5. **Drug target ≠ drug response**: An enzyme being inhibited by an antibiotic doesn't mean the organism "responds" to that antibiotic in a biological process sense.

6. **ViralZone helps separate signal from noise**: In T4, VZ-primary terms for tail structure, genome ejection, host-envelope penetration, R-M evasion, DNA-end protection, and CRISPR-cas evasion are usually stronger than the broad non-VZ parent terms that caused the original failures.

## Recommendations for Phage/Virus SPKW Curation

1. **Create phage-specific term mappings**: Keywords about host-pathogen interactions should map to different GO terms for phages vs. eukaryotic viruses

2. **Review all "innate immune" annotations on phage proteins**: These likely need replacement with precise phage counter-defense terms where the mechanism is known

3. **Distinguish R-M evasion from immune suppression**: GO:0099018 exists specifically for phage-bacteria interactions

4. **Validate "antibiotic resistance" claims**: Being a drug target does not equal conferring resistance, especially for phage enzymes

5. **Flag VZ-primary rows separately**: Treat ViralZone-primary status as a positive prior for phage-specific mechanisms, but keep reviewing broad parent terms and protein assignment.

6. **Prefer precise phage mechanisms over broad parents**: Use R-M evasion, CRISPR-cas evasion, DNA-end degradation evasion, tail fiber/baseplate/sheath/tube terms, contractile-tail ejection, and peptidoglycan-disruption entry when supported.

## Comparison: All Organisms Analyzed

| Organism | Domain | Over-Annotation Rate | Main Patterns |
|----------|--------|---------------------|---------------|
| Human | Eukarya | 80-100% | Process conflation |
| S. pombe | Eukarya | 100% (ATG-meiosis) | Support process conflation |
| D. melanogaster | Eukarya | 50% | Mixed |
| P. putida | Bacteria | 25% | RT defense keyword |
| Arabidopsis | Eukarya | 75% | Subclade divergence |
| **T4 Phage high-risk subset** | **Virus** | **100%** | **Eukaryote-centric terms, plus VZ-primary phage-specific rescue terms** |

## Review Files Location

```
genes/BPT4/
├── DAM/DAM-ai-review.yaml   (MODIFY: broad immune/defense rows -> R-M evasion)
├── E/E-ai-review.yaml       (REMOVE/MODIFY: defense/cell-killing rows -> viral release)
└── frd/frd-ai-review.yaml   (REMOVE: antibiotic response - drug target ≠ response)
```
