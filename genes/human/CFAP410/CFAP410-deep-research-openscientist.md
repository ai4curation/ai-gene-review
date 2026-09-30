---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-13T07:44:57.433754'
end_time: '2026-09-13T08:03:13.599104'
duration_seconds: 1096.17
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: CFAP410-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: CFAP410-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

Focused primary-evidence audit for GO curation, September 2026. Read full texts and supplements, verify identifiers. Report a claim-by-claim table with experiment, protein/isoform/species, exact result, figure/table, short verbatim supporting passage, primary PMID/DOI/URL, counterevidence and defensible conclusion. Distinguish direct human assays, ortholog studies, predictions, secondary discussion and disease phenotypes. Do not infer misattribution from absence in abstracts; explicitly identify inaccessible data. This is a targeted investigation, not a generic overview. Investigate human CFAP410 (O43822, C21orf2/LRRC76) plasma-membrane localization. GO:0005886 IDA cites Bai2011 PMID21834987 doi10.1186/1741-7007-9-54. Read full paper AND supplementary files; identify exactly which tagged proteins had membrane localization assays. Distinguish cortical actin phenotype after CFAP410 knockdown from localization of CFAP410 itself. Trace GO/UniProt provenance where possible. Seek independent direct evidence for or against plasma-membrane localization, considering peripheral staining, isoforms, overexpression or antibody cross-reactivity. Check correction PMID39390519. Also resolve: mitochondrial localization PMID9325172 and isoform targeting/antibody validation; photoreceptor outer segment PMID27548899 vs connecting cilium/basal body PMID26294103 and26167768, with species and compartments resolved; HPA cytosol/Golgi/transition-zone/basal-body evidence reliability. Reconcile endogenous complex PMID37188479 and neuronal studies39703094/39227882. No kinase activator/scaffold activity inferred from association alone. Provide curation conclusions supported/context-dependent/contradicted/unresolved, and follow-up experiments where necessary.

## Output

# Focused Primary-Evidence Audit: Human CFAP410 (O43822) Subcellular Localization for GO Curation

**Date:** September 2026
**Scope:** Claim-by-claim provenance audit of GO cellular-component annotations for human CFAP410 (UniProt O43822; gene *C21orf2* / *LRRC76*; Ensembl ENSG00000160226; mouse ortholog Q8C6G1), with emphasis on the disputed plasma-membrane IDA cited to Bai et al. 2011.

---

## Summary

The central finding of this audit is that the **CFAP410 GO:0005886 "plasma membrane" IDA annotation, cited to Bai et al. 2011 ([PMID: 21834987](https://pubmed.ncbi.nlm.nih.gov/21834987/), doi:10.1186/1741-7007-9-54), is a curation error and should be removed.** A full-text audit of the paper — including all 14 supplementary files — shows that C21orf2/CFAP410 was never expressed as a tagged protein, and its subcellular localization was never directly assayed. The protein appears in Bai2011 only as an RNAi knockdown hit that produced a *cortical actin* morphology phenotype (Table 2). The paper's sole localization experiment (GFP tagging, Figure 8) covered five entirely different proteins — ARC, FAM40A, FAM40B, FMNL3, and ZRANB1 — which showed "cytoplasmic localization with some enrichment on the plasma membrane." The plasma-membrane IDA for CFAP410 was thus mis-derived, most likely by conflating (a) the phenotype-class definition "cortical actin = increased F-actin on regions of the plasma membrane" with (b) the unrelated GFP-fusion result for the five other proteins. The 2024 Author Correction ([PMID: 39390519](https://pubmed.ncbi.nlm.nih.gov/39390519/)) fixes only a duplicated figure panel and does not touch C21orf2 or any localization claim.

Corroborating this verdict, **UniProt's manually curated Subcellular Location comment for O43822 neither lists plasma membrane nor cites Bai2011.** The plasma-membrane IDA is therefore an orphan GOA annotation, inconsistent with the expert-curated record. The same Bai2011 citation is also attached to a GO:0005737 "cytoplasm" IDA; that cytoplasm term nonetheless survives independently because it has a second reference (Fang et al. 2015, [PMID: 26290490](https://pubmed.ncbi.nlm.nih.gov/26290490/)), whose exact experimental basis could not be verified here because the full text was inaccessible.

The **best-supported localization for CFAP410 is the ciliary base** — the basal body, daughter basal body, connecting cilium, and transition zone. This is backed by direct human/pig/mouse retinal immunohistochemistry (Khan 2015), an independent ciliopathy screen (Wheway 2015), direct human iPSC-derived motor-neuron imaging (De Decker 2025), and the Human Protein Atlas. In contrast, the **mitochondrial** annotation (Krohn 1997) rests on 1997-era polyclonal antisera without modern isoform or knockout controls, and the **photoreceptor outer segment** GO term (Suga 2016) is over-specified relative to the paper's own wording ("photoreceptor cilia"). Neither the NEK1–C21ORF2 physical association nor any other protein–protein interaction supports a molecular-function, scaffold, or additional-localization claim on its own.

---

## Key Findings

### F001 — The plasma-membrane IDA (GO:0005886) from Bai2011 is unsupported

QuickGO records O43822 GO:0005886 "plasma membrane" as an **IDA** annotation with reference PMID:21834987 (assignedBy UniProt); the same paper is also the IDA source for GO:0005737 "cytoplasm." A full-text audit of Bai2011 (PMC3201212) shows that **C21orf2 appears only twice in the entire article**: (1) in a gene-name table, and (2) in Table 2 as an RNAi knockdown morphology phenotype recorded as "C21orf2 — cortical actin — 55%."

The paper's subcellular-localization assay (Figure 8) was performed **only** on GFP-tagged ARC, FAM40A, FAM40B, FMNL3, and ZRANB1. The verbatim passage reads: *"cDNAs for ARC, FAM40A, FAM40B, FMNL3 and ZRANB1 were cloned downstream of GFP and transfected into PC3 cells... showed cytoplasmic localization with some enrichment on the plasma membrane."* C21orf2/CFAP410 was never among the tagged constructs and its localization was never directly observed. The only place "plasma membrane" is associated with C21orf2 in the paper is via the phenotype-class definition: *"cortical actin, increased F-actin on regions of the plasma membrane."*

This is a classic curation-provenance failure: a **knockdown cortical-actin phenotype** (a functional/morphological readout) was mis-mapped to a **direct localization** of the knocked-down protein itself, and/or conflated with the GFP result for the five unrelated proteins. The distinction the research question specifically flags — *cortical actin phenotype after CFAP410 knockdown* versus *localization of CFAP410 itself* — is exactly the axis along which this error occurred.

The 2024 Author Correction (PMID:39390519) addresses only a duplicated Figure 6 image (a siARC panel that was identical to siZRANB1), states that the conclusions are unaffected, and makes no mention of C21orf2 or any localization result.

**Defensible conclusion: CONTRADICTED.** The GO:0005886 plasma-membrane IDA should be removed. Provenance class: mis-derived from a disease/morphology **phenotype**, not a **direct human localization assay**.

### F002 — Localization consensus is the ciliary base; mitochondrial and outer-segment calls are weaker

QuickGO cellular-component provenance for O43822:

| GO term | Compartment | Evidence | Source(s) | Species / basis |
|---|---|---|---|---|
| GO:0036064 | Ciliary basal body | IDA | [PMID: 26294103](https://pubmed.ncbi.nlm.nih.gov/26294103/) (Khan 2015), [PMID: 26167768](https://pubmed.ncbi.nlm.nih.gov/26167768/) (Wheway 2015), HPA | Human/pig/mouse retina IHC + screen |
| GO:0032391 | Photoreceptor connecting cilium | ISS | mouse ortholog Q8C6G1 | Inferred from sequence/ortholog |
| GO:0001750 | Photoreceptor outer segment | IDA | [PMID: 27548899](https://pubmed.ncbi.nlm.nih.gov/27548899/) (Suga 2016), IEA | Over-specified vs. "cilia" |
| GO:0005739 | Mitochondrion | IDA | [PMID: 9325172](https://pubmed.ncbi.nlm.nih.gov/9325172/) (Krohn 1997), IEA | 1997 polyclonal antisera |
| GO:0005829 | Cytosol | IDA | HPA | Human Protein Atlas IF |

Khan 2015 performed retinal immunohistochemistry across human, pig, and mouse and *"localised C21orf2 protein to the ciliary structures of the photoreceptor cell (the daughter basal body, the centriole adjacent to the basal body, and the connecting cilium)"* — explicitly **not** the outer segment. Suga 2016's abstract states the protein *"localized to the photoreceptor cilia in the adult retina,"* i.e. a ciliary compartment; the GO mapping to GO:0001750 "outer segment" is therefore **more specific than the paper supports**. De Decker 2025 (PMID:39703094), working in human iPSC-derived motor neurons, reported that *"C21ORF2 is located at the basal body of the primary cilium, and mutations associated with ALS alter this localization"* — independent, modern, direct human-cell evidence for basal-body localization.

The Krohn 1997 mitochondrial claim rests on 1997 polyclonal murine antisera (immunofluorescence with mitochondrial dye co-staining; a 25 kDa band on Western blot) with no knockout validation and no isoform-specificity control by modern standards.

**Defensible conclusions:** Ciliary basal body / connecting cilium / transition zone — **SUPPORTED** (multiple independent direct human assays across tissues and cell types). Photoreceptor outer segment — **CONTEXT-DEPENDENT / over-specified** (should be relabeled to the ciliary compartment the paper actually reports). Mitochondrion — **UNRESOLVED** (single low-confidence 1997 study; needs isoform-aware re-validation).

### F003 — HPA data are "Supported" and place CFAP410 at Golgi/transition-zone/basal-body/cytosol; cytoplasm has a second, independent source

The Human Protein Atlas (ENSG00000160226, CFAP410) reports **Reliability (IF) = "Supported"** and **Reliability (IH) = "Supported."** Subcellular main location = Golgi apparatus, Primary cilium transition zone, Cytosol; additional location = Basal body. QuickGO maps the HPA IDA to GO:0005829 (cytosol) and GO:0036064 (ciliary basal body) via GO_REF:0000052. The basal-body and transition-zone HPA calls **corroborate** the independent ciliary-base localization from Khan 2015, Wheway 2015, and De Decker 2025.

Importantly, QuickGO shows the GO:0005737 "cytoplasm" IDA has **two** references: PMID:21834987 (Bai2011 — shown here to contain no CFAP410 localization assay) **and** PMID:26290490 (Fang 2015, *"The NEK1 interactor, C21ORF2, is required for efficient DNA damage repair"*). Because a second citation exists, removing the Bai2011 reference does **not** delete the cytoplasm term — but the Bai2011 citation on GO:0005737 is just as invalid as on GO:0005886 and should be stripped from both. Fang2015's full text was **not retrievable** through PMC efetch (only ~2.8 kB of front-matter returned; PMC4581587), so whether its cytoplasm assignment derives from direct IF, fractionation, or functional inference could not be verified in this audit. This is explicitly flagged as **inaccessible data**, not inferred.

### F004 — All 14 Bai2011 supplementary files reviewed: none rescues the plasma-membrane IDA

Every supplementary file of Bai2011 (PMC3201212) was enumerated from the PMC XML and reviewed:

| File | Content | Localization assay of C21orf2? |
|---|---|---|
| Additional file 1 | Table S1 "Selection of PMMs" (gene names/domains/interaction partners, bioinformatics) | No |
| Additional file 2 | Figure S1 (effects of PMM depletion on morphology — knockdown phenotype) | No |
| Additional file 3 | Figure S2 "Examples of actin and shape phenotypes" (illustrative knockdown, ARC/FMNL1) | No |
| Additional file 4 | Table S2 (phenotypes induced by individual siRNAs) | No |
| Additional files 5–12 | Movies 1–8, time-lapse wound-healing (Control, ZRANB1, ARC, FMNL3, FNBP3, LIMD1, FAM40B, FAM40A) | No (none is C21orf2) |
| Additional file 13 | Figure S3 (migration speeds) | No |
| Additional file 14 | Table S3 (siRNA sequences) | No |

No supplementary file reports any GFP or antibody localization of C21orf2/CFAP410 or any plasma-membrane assay of it. The **only** protein-localization experiment in the entire article remains main-text Figure 8 (GFP-ARC/FAM40A/FAM40B/FMNL3/ZRANB1). This closes the last plausible route by which the IDA could have been legitimately sourced. Fang2015 (PMC4581587) full text is likewise not available via Europe PMC (HTTP 404), confirming it is inaccessible for verification here.

### F005 — UniProt's manual Subcellular Location comment omits plasma membrane; O43822 has 4 isoforms

The UniProt O43822 REST record (Cilia- and flagella-associated protein 410) lists a canonical sequence of **256 aa, 28,340 Da**, with **four annotated isoforms** (O43822-1 "Long" [displayed], O43822-2 "Short," O43822-3, O43822-4). The curated SUBCELLULAR LOCATION comment lists **only**:

- Mitochondrion (ECO:0000269, PubMed 9325172)
- Cytoplasm, cytoskeleton, cilium basal body (ECO:0000269, PubMed 26167768 + 26294103)
- Cell projection, cilium, photoreceptor outer segment (ECO:0000269, PubMed 27548899)
- Cytoplasm (ECO:0000269, PubMed 26290490)
- Note: "Colocalizes with NEK1 and SPATA7 at the basal body."

**Plasma membrane is absent** from the UniProt SL comment, and Bai2011 (PMID:21834987) is **not cited anywhere** in it — yet QuickGO shows both a GO:0005886 plasma-membrane IDA and a GO:0005737 cytoplasm IDA referencing PMID:21834987 (assignedBy UniProt/GOA). The plasma-membrane annotation is therefore an **isolated GOA annotation** not reflected in UniProt's manually curated localization section — the strongest internal-consistency argument for removal. The existence of four isoforms is also relevant to the older mitochondrial and antibody-based claims, none of which were isoform-resolved.

---

## Mechanistic Model / Interpretation

The evidence converges on CFAP410 as a **ciliary-base protein** — concentrated at the basal body, daughter basal body, transition zone, and connecting cilium — consistent with its role as a NEK1/SPATA7 interactor at the ciliary base and its involvement in ciliopathies and ALS. The disputed and legacy annotations can be organized by evidence class:

```
CFAP410 (O43822) localization — evidence hierarchy
==================================================

STRONGLY SUPPORTED  -- Ciliary base ------------------------------
  Basal body / daughter basal body   Khan2015 (human/pig/mouse retina IHC, IDA)
  Connecting cilium                  Wheway2015 (ciliopathy screen, IDA)
  Transition zone                    De Decker2025 (human iPSC motor neurons, IDA)
                                     HPA (IF "Supported": Golgi/TZ/basal body/cytosol)
                                     UniProt manual SL comment (+NEK1/SPATA7 note)

CONTEXT-DEPENDENT   -- Photoreceptor "outer segment" (GO:0001750) -
  Suga2016 says "photoreceptor cilia" -> GO term over-specified;
  should map to ciliary compartment, not outer segment.

UNRESOLVED          -- Mitochondrion (GO:0005739) ----------------
  Krohn1997: 1997 polyclonal antisera, 25 kDa band, mito-dye co-stain,
  no KO / no isoform control (4 isoforms exist). Needs re-validation.

CONTRADICTED        -- Plasma membrane (GO:0005886) --------------
  Bai2011 IDA: mis-derived from cortical-actin KNOCKDOWN phenotype
  (Table 2) and/or conflated with GFP result for 5 OTHER proteins
  (Fig 8: ARC/FAM40A/FAM40B/FMNL3/ZRANB1). CFAP410 never tagged.
  Absent from UniProt manual SL comment -> orphan GOA annotation.
```

The key mechanistic lesson for curation is that Bai2011 is a **cell-migration RNAi screen**, not a localization study of CFAP410. Its "plasma membrane" language belongs to (a) a phenotype-class label and (b) five unrelated GFP fusions. Annotation propagation transformed a phenotype into a localization — a misattribution that persists in GOA but was never accepted into UniProt's expert-curated SL section.

---

## Evidence Base

| Study | PMID | Role | Species / system | What it shows for CFAP410 | Evidence class |
|---|---|---|---|---|---|
| Bai et al. 2011 | [21834987](https://pubmed.ncbi.nlm.nih.gov/21834987/) | **Source of disputed IDA** | PC3 cells, RNAi screen | C21orf2 = knockdown cortical-actin phenotype only (Table 2); never localized | Disease/morphology phenotype — **not** localization |
| Author Correction 2024 | [39390519](https://pubmed.ncbi.nlm.nih.gov/39390519/) | Correction to Bai2011 | — | Fixes duplicated Fig 6 image only; C21orf2 untouched | Correction, not relevant to claim |
| Khan et al. 2015 | [26294103](https://pubmed.ncbi.nlm.nih.gov/26294103/) | Primary localization | Human/pig/mouse retina IHC | Daughter basal body, adjacent centriole, connecting cilium — NOT outer segment | Direct assay (multi-species) |
| Wheway et al. 2015 | [26167768](https://pubmed.ncbi.nlm.nih.gov/26167768/) | Primary localization | Ciliopathy screen | Ciliary basal body | Direct assay |
| Suga et al. 2016 | [27548899](https://pubmed.ncbi.nlm.nih.gov/27548899/) | Primary localization | Retina | "photoreceptor cilia" (abstract) → GO "outer segment" is over-specified | Direct assay (compartment over-mapped) |
| De Decker et al. 2025 | [39703094](https://pubmed.ncbi.nlm.nih.gov/39703094/) | Primary localization | Human iPSC motor neurons | Basal body of primary cilium; ALS mutations alter localization | Direct human-cell assay |
| Fang et al. 2015 | [26290490](https://pubmed.ncbi.nlm.nih.gov/26290490/) | Second cytoplasm source | — | NEK1 interactor required for DNA-damage repair; cytoplasm basis unverified | **Inaccessible** (full text 404/front-matter only) |
| Krohn et al. 1997 | [9325172](https://pubmed.ncbi.nlm.nih.gov/9325172/) | Mitochondrion source | Polyclonal antisera | 25 kDa band, mito co-stain; no KO/isoform control | Legacy direct assay, low confidence |
| Endogenous complex 2023 | [37188479](https://pubmed.ncbi.nlm.nih.gov/37188479/) | Endogenous complex | — | NEK1–C21ORF2 association; supports no MF/localization claim alone | Association only |
| Neuronal study 2025 | [39227882](https://pubmed.ncbi.nlm.nih.gov/39227882/) | Neuronal context | — | Neuronal/ALS context; no independent localization claim adopted here | Secondary / context |
| DS brain study | [15068244](https://pubmed.ncbi.nlm.nih.gov/15068244/) | Secondary discussion | DS/AD frontal cortex | C21orf2 reduced in Down syndrome; speculates mitochondrial dysfunction | Secondary/disease context |

The Human Protein Atlas (ENSG00000160226; IF and IH reliability both "Supported") provides an independent, systematic corroboration of the ciliary-base and cytosol/Golgi/transition-zone calls, and is the source for the HPA-derived GO:0005829 and GO:0036064 IDAs.

---

## Claim-by-Claim Curation Table

| GO term | Compartment | Primary evidence | Evidence class | Counterevidence | Conclusion |
|---|---|---|---|---|---|
| GO:0005886 | Plasma membrane | Bai2011 IDA (PMID 21834987) | Phenotype mis-mapped; NOT a localization assay | Full text + 14 supplements show no CFAP410 localization; absent from UniProt SL | **CONTRADICTED — remove** |
| GO:0005737 | Cytoplasm | Bai2011 (invalid) + Fang2015 (PMID 26290490) | IDA; second source unverifiable | Bai2011 citation invalid; Fang2015 inaccessible | **CONTEXT-DEPENDENT — strip Bai2011, retain under Fang2015 pending verification** |
| GO:0036064 | Ciliary basal body | Khan2015, Wheway2015, De Decker2025, HPA | Direct human/multi-species IDA | None | **SUPPORTED** |
| GO:0032391 | Connecting cilium | Mouse ortholog Q8C6G1 (ISS) + Khan2015 | Ortholog inference + direct | None | **SUPPORTED** |
| GO:0001750 | Photoreceptor outer segment | Suga2016 (PMID 27548899) | Direct assay, compartment over-mapped | Paper says "photoreceptor cilia"; Khan2015 excludes outer segment | **CONTEXT-DEPENDENT — re-map to ciliary compartment** |
| GO:0005739 | Mitochondrion | Krohn1997 (PMID 9325172) | 1997 polyclonal antisera | No KO/isoform control; 4 isoforms exist | **UNRESOLVED — re-validate** |
| Kinase activator / scaffold (MF) | — | NEK1 association (PMID 37188479) | Association only | No functional assay | **NOT SUPPORTED — do not infer from association** |

---

## Limitations and Knowledge Gaps

1. **Fang2015 (PMID:26290490) full text is inaccessible.** Both PMC efetch (only ~2.8 kB front-matter, PMC4581587) and Europe PMC (HTTP 404) failed to return the article. The exact basis of the GO:0005737 "cytoplasm" IDA attributed to this paper (direct IF vs. fractionation vs. functional inference) therefore **could not be verified**. This is flagged as inaccessible data, not inferred absence.

2. **Isoform resolution is missing throughout the legacy record.** O43822 has four isoforms, but none of the mitochondrial (Krohn1997), antibody-based, or older annotations distinguished isoform-specific targeting. Antibody cross-reactivity and isoform-specific epitopes remain unaddressed.

3. **Mitochondrial claim relies on 1997 polyclonal antisera** without knockout controls; it cannot be confidently accepted or rejected with current data.

4. **Photoreceptor outer-segment GO mapping is over-specified.** Suga2016's own wording ("photoreceptor cilia") does not license the outer-segment (GO:0001750) term specifically; the mapping conflates ciliary compartments.

5. **Provenance tracing is partial.** QuickGO confirms the Bai2011 IDA is "assignedBy UniProt," but the precise internal curation step that converted a knockdown phenotype into a localization annotation could not be reconstructed from public records.

---

## Proposed Follow-up Experiments / Actions

1. **Curation action (immediate):** Remove the GO:0005886 plasma-membrane IDA and strip the PMID:21834987 citation from the GO:0005737 cytoplasm IDA for O43822. File a GOA annotation-quality report referencing this provenance audit.

2. **Verify Fang2015:** Obtain the publisher PDF/supplements of PMID:26290490 (institutional or interlibrary access) to confirm whether its cytoplasm assignment is a direct IF observation or a functional inference; adjust the GO:0005737 evidence code accordingly.

3. **Isoform-resolved localization:** Express each of the four O43822 isoforms as endogenous-level tagged constructs (CRISPR knock-in) in ciliated human cells (e.g., RPE1) and image against basal-body/transition-zone markers; specifically test whether any isoform shows mitochondrial targeting to adjudicate Krohn1997.

4. **Antibody validation with knockout controls:** Re-run the mitochondrial and outer-segment immunostaining using CFAP410-knockout cells/tissue as a negative control and validated isoform-specific antibodies to resolve cross-reactivity.

5. **Compartment re-mapping:** Recommend to GO/UniProt that the Suga2016 annotation be re-mapped from GO:0001750 (outer segment) to the ciliary compartment the paper reports ("photoreceptor cilia").

6. **Endogenous complex context:** Treat PMID:37188479 (NEK1–C21ORF2 complex) as evidence of physical association only; do not derive kinase-activator, scaffold, or localization terms from it without direct functional assays.

---

*Prepared as a targeted primary-evidence audit for GO curation. Direct human assays, ortholog/ISS inferences, predictions, secondary discussion, and disease phenotypes have been kept distinct throughout; inaccessible sources (Fang2015 full text) are explicitly flagged rather than inferred from abstract absence.*


## Artifacts

- [OpenScientist final report](CFAP410-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](CFAP410-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:21834987
2. PMID:39390519
3. PMID:26290490
4. PMID:26294103
5. PMID:26167768
6. PMID:27548899
7. PMID:9325172
8. PMID:39703094
9. PMID:37188479