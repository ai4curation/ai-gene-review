---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T03:07:39.715974'
end_time: '2026-09-21T03:20:19.284154'
duration_seconds: 759.57
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: STABO
  gene: mdr
  gene_symbol: mdr
  uniprot_accession: H6TB12
  taxon_id: NCBITaxon:75736
  taxon_label: Starmerella bombicola
  focus_type: function_assignment
  hypothesis_slug: sophorolipid-export-and-mitochondrial-peptide-capacity
  hypothesis_text: Starmerella bombicola Mdr/SbSLMdr.1 (H6TB12) has mitochondrial
    inner-membrane localization and ATP-dependent oligopeptide export from mitochondria
    in addition to its established sophorolipid export role. Evaluate each claim separately
    using full primary studies and exact transporter architecture/localization and
    substrate assays. PMID23516968 and PMID34998388 demonstrate sophorolipid-secretion
    defects after deletion and redundancy with SbSLMdr.2; the latter distinguishes
    full-length MDR proteins from mitochondrial half-size transporters. Do these results
    or targeting/assembly interfaces establish loss of mitochondrial or oligopeptide
    capacity, or mainly the predominant secretory role? Frozen TreeGrafter node PTN008681462
    exists in current PTHR43394 SF11 tree as an Embryophyta subtree; H6TB12 is absent
    as an exact leaf. Current tree GO-slim retains mitochondrial/peptide terms there,
    while current IBD GAF recovered along that path supports broad membrane/ABC functions
    and places mitochondrial-peptide IBDs on other paths. Resolve this version discrepancy
    and graft plausibility without inventing a target lineage. Broad membrane/ATP/ABC
    functions remain compatible. Preferred sophorolipid cargo and inferred plasma-membrane
    localization alone do not prove every additional function absent.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/STABO/mdr/mdr-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Starmerella bombicola Mdr/SbSLMdr.1 (H6TB12) has\
    \ mitochondrial inner-membrane localization\n  and ATP-dependent oligopeptide\
    \ export from mitochondria in addition to its established sophorolipid\n  export\
    \ role. Evaluate each claim separately using full primary studies and exact transporter\
    \ architecture/localization\n  and substrate assays. PMID23516968 and PMID34998388\
    \ demonstrate sophorolipid-secretion defects after\n  deletion and redundancy\
    \ with SbSLMdr.2; the latter distinguishes full-length MDR proteins from mitochondrial\n\
    \  half-size transporters. Do these results or targeting/assembly interfaces establish\
    \ loss of mitochondrial\n  or oligopeptide capacity, or mainly the predominant\
    \ secretory role? Frozen TreeGrafter node PTN008681462\n  exists in current PTHR43394\
    \ SF11 tree as an Embryophyta subtree; H6TB12 is absent as an exact leaf.\n  Current\
    \ tree GO-slim retains mitochondrial/peptide terms there, while current IBD GAF\
    \ recovered along\n  that path supports broad membrane/ABC functions and places\
    \ mitochondrial-peptide IBDs on other paths.\n  Resolve this version discrepancy\
    \ and graft plausibility without inventing a target lineage. Broad membrane/ATP/ABC\n\
    \  functions remain compatible. Preferred sophorolipid cargo and inferred plasma-membrane\
    \ localization\n  alone do not prove every additional function absent.\nfocus_type:\
    \ function_assignment\ncontext: []\nreference_id: []"
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
citation_count: 1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** STABO
- **Taxon:** Starmerella bombicola (NCBITaxon:75736)
- **Gene directory:** mdr
- **Gene symbol:** mdr
- **UniProt accession:** H6TB12

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** sophorolipid-export-and-mitochondrial-peptide-capacity
- **Source file:** genes/STABO/mdr/mdr-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Starmerella bombicola Mdr/SbSLMdr.1 (H6TB12) has mitochondrial inner-membrane localization and ATP-dependent oligopeptide export from mitochondria in addition to its established sophorolipid export role. Evaluate each claim separately using full primary studies and exact transporter architecture/localization and substrate assays. PMID23516968 and PMID34998388 demonstrate sophorolipid-secretion defects after deletion and redundancy with SbSLMdr.2; the latter distinguishes full-length MDR proteins from mitochondrial half-size transporters. Do these results or targeting/assembly interfaces establish loss of mitochondrial or oligopeptide capacity, or mainly the predominant secretory role? Frozen TreeGrafter node PTN008681462 exists in current PTHR43394 SF11 tree as an Embryophyta subtree; H6TB12 is absent as an exact leaf. Current tree GO-slim retains mitochondrial/peptide terms there, while current IBD GAF recovered along that path supports broad membrane/ABC functions and places mitochondrial-peptide IBDs on other paths. Resolve this version discrepancy and graft plausibility without inventing a target lineage. Broad membrane/ATP/ABC functions remain compatible. Preferred sophorolipid cargo and inferred plasma-membrane localization alone do not prove every additional function absent.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Starmerella bombicola Mdr/SbSLMdr.1 (H6TB12) has mitochondrial inner-membrane localization
  and ATP-dependent oligopeptide export from mitochondria in addition to its established sophorolipid
  export role. Evaluate each claim separately using full primary studies and exact transporter architecture/localization
  and substrate assays. PMID23516968 and PMID34998388 demonstrate sophorolipid-secretion defects after
  deletion and redundancy with SbSLMdr.2; the latter distinguishes full-length MDR proteins from mitochondrial
  half-size transporters. Do these results or targeting/assembly interfaces establish loss of mitochondrial
  or oligopeptide capacity, or mainly the predominant secretory role? Frozen TreeGrafter node PTN008681462
  exists in current PTHR43394 SF11 tree as an Embryophyta subtree; H6TB12 is absent as an exact leaf.
  Current tree GO-slim retains mitochondrial/peptide terms there, while current IBD GAF recovered along
  that path supports broad membrane/ABC functions and places mitochondrial-peptide IBDs on other paths.
  Resolve this version discrepancy and graft plausibility without inventing a target lineage. Broad membrane/ATP/ABC
  functions remain compatible. Preferred sophorolipid cargo and inferred plasma-membrane localization
  alone do not prove every additional function absent.
focus_type: function_assignment
context: []
reference_id: []
```

## Research Objective

Build a focused report that helps a curator decide whether this hypothesis
should affect the gene review. Address the focus type directly:

1. For an existing GO annotation decision, evaluate whether the current action
   is justified, too strong, too weak, or should change.
2. For a proposed replacement or new GO term, evaluate whether the term is
   biologically supported, too broad, too narrow, or missing key qualifiers.
3. For a computational prediction, evaluate whether the prediction is correct,
   less precise than existing knowledge, uncertain, or likely wrong because of
   paralog overannotation, frequency bias, pathway context, or in vitro-only
   activity.
4. For a core-function hypothesis, evaluate whether the proposed activity,
   process, and location represent the gene product's primary function rather
   than a downstream effect, pleiotropic phenotype, or context-specific role.
5. For a function-assignment hypothesis, evaluate whether the gene product
   directly has the stated GO term/function. Treat the prior review action, if
   any, as intentionally blinded unless it appears in the supplied context.

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews and database records as
orientation unless they contain directly relevant synthesized evidence that is
clearly labeled as review-level or database-level support.

Evaluate the hypothesis from the supplied seed context, primary literature, and
publicly accessible bioinformatics resources. Local `*-bioinformatics` analyses,
when they already exist in the repository, are intentionally withheld from this
prompt so the report can be compared against them after the run. Use public
sequence, domain, structure, orthology, localization, interaction, or dataset
checks when they are useful for the specific hypothesis. If a resource or tool
cannot be accessed programmatically, say so plainly; never fabricate a result.
Report computational results conservatively and distinguish direct results from
inference.

## Required Output

### Executive Judgment

Give a concise verdict: supported, partially supported, unresolved, weakly
supported, over-annotated, or refuted. Explain the reasoning and the most
important caveats.

### Evidence Matrix

Create a table with one row per important evidence item:

- Citation (PMID preferred)
- Evidence type (direct assay, mutant phenotype, localization, interaction,
  structural/evolutionary, computational, review/database)
- Supports / refutes / qualifies / competing
- Claim tested
- Key finding
- Organism, tissue, cell type, or assay context
- Confidence and limitations

### GO Curation Implications

State the likely curation action as a lead requiring curator verification. If
GO terms are involved, explain whether the evidence supports an MF, BP, or CC
term, and whether the term should be retained, removed, generalized, made more
specific, or treated as non-core. Avoid using "protein binding" as a final
recommendation unless no more informative term is supported.

### Mechanistic Scope

Describe the immediate molecular or cellular function being tested. Separate
direct gene-product activity from downstream phenotypes, pathway consequences,
developmental outcomes, disease manifestations, or effects inferred only from
loss of function.

### Conflicts and Alternatives

Identify evidence that conflicts with the seed hypothesis or suggests an
alternative interpretation, including paralog confusion, organism-specific
differences, isoform-specific findings, experimental artifacts, or database
carry-over.

### Knowledge Gaps

List explicit uncertainties that matter for curation. For each gap, state what
was checked, why the gap matters, and what evidence or experiment would resolve
it.

### Discriminating Tests

Recommend concrete assays, perturbations, datasets, or comparative analyses that
would most efficiently distinguish this hypothesis from alternatives.

### Curation Leads

Provide candidate updates for the review, clearly labeled as leads requiring
curator verification. Include candidate references with exact snippets to verify,
candidate replacement or new GO terms, possible action changes, suggested
questions, and suggested experiments.

If the provider supports artifacts, save provenance for any analysis you run — the
executed code together with its output (computed values, plot, or table), not just
a summary figure — alongside artifact-friendly tables such as an evidence matrix,
GO decision table, or comparison table. Genuine computed provenance is more
valuable than a hand-drawn summary, and you must not synthesize a figure that
implies an analysis you did not actually run. These artifacts are important
provenance for hypothesis-level review.


## Output

# AIGR Deep Research Report — *Starmerella bombicola* Mdr / SbSLMdr.1 (UniProt H6TB12)

**Focus:** function_assignment
**Hypothesis slug:** sophorolipid-export-and-mitochondrial-peptide-capacity
**Source:** genes/STABO/mdr/mdr-ai-review.yaml (free-text)

---

## Executive Judgment

**Verdict: Sophorolipid-export role = SUPPORTED (primary, experimentally established). Additional mitochondrial-inner-membrane localization + ATP-dependent oligopeptide-export claim = OVER-ANNOTATED / weakly supported → recommend treating as non-core (candidate for removal or NOT qualifier).**

The seed hypothesis asks whether H6TB12 genuinely has a second, mitochondrial oligopeptide-export function in addition to sophorolipid export. The evidence resolves cleanly:

1. **The sophorolipid-export function is the only experimentally supported activity/location.** UniProt annotates it with IMP evidence (GO:0140377 sophorolipid biosynthetic process; GO:0005886 plasma membrane), anchored to the deletion phenotype in PMID 23516968 and reinforced by the transportome study PMID 34998388.
2. **The three mitochondrial/peptide GO terms are ALL `IEA:TreeGrafter`** — electronic, phylogenetically inferred annotations, not primary evidence. They are inherited at the family level from PANTHER **PTHR43394** ("ATP-DEPENDENT PERMEASE MDL1, MITOCHONDRIAL"), a family named after the yeast half-transporter Mdl1.
3. **Transporter architecture is diagnostic and refutes a genuine mitochondrial role.** H6TB12 is a **full-length** ABCB transporter (1299 aa, 12 TM helices, 2 NBDs; UniProt subfamily "Multidrug resistance exporter, TC 3.A.1.201") — the same structural class as human P-glycoprotein/ABCB1 (1280 aa, 12 TM, 2 NBD). Genuine mitochondrial peptide exporters (yeast Mdl1 P33310 = 695 aa/1 NBD; human ABCB10 Q9NRK6 = 738 aa/1 NBD) are **half-size, single-NBD** proteins of a distinct "Mitochondrial peptide exporter" subfamily. Full-length MDR exporters are plasma-membrane multidrug/lipid pumps; mitochondrial inner-membrane peptide export is exclusive to the half-size Mdl1/ABCB10 subfamily.

**Most important caveats.** Absence of a positive mitochondrial assay does not formally prove absence of a minor moonlighting role ("inferred plasma-membrane localization alone does not prove every additional function absent," per the seed). However, curation standards weigh *positive experimental localization/function* (plasma membrane, sophorolipid export) against *family-level electronic inference contradicted by architecture*. On that basis the mitochondrial/peptide terms should not be presented as established functions of this protein. Generic ABC/ATPase/transmembrane-transport MF terms remain fully compatible and should be retained.

---

## Evidence Matrix

| # | Citation | Evidence type | Supports / Refutes / Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|----------|---------------|-------------------------------|--------------|-------------|---------|--------------------------|
| 1 | PMID 23516968 (Van Bogaert 2013) | Mutant phenotype (deletion) | **Supports** sophorolipid-export role; **competing** with mito claim | Is Mdr a sophorolipid exporter? | Transporter knockout secretes SLs at only ~10% of WT → required for efficient SL export; part of SL biosynthetic gene cluster | *S. bombicola*, in vivo | High for secretory role; localization inferred (ECO:0000305), not imaged |
| 2 | PMID 34998388 (Claus 2022, transportome) | Mutant phenotype + comparative genomics | **Supports**; **qualifies** (redundancy) | Which transporters drive SL export? | ABC superfamily is "the main driver behind the highly efficient sophorolipid export"; identifies a **second** SL transporter outside the cluster (redundancy → SbSLMdr.2); distinguishes full-length MDR from half-size transporters | *S. bombicola*, in vivo | High; explicitly separates full-length MDR from mitochondrial half-size transporters |
| 3 | UniProt H6TB12 record | Database (feature/annotation provenance) | **Qualifies/Refutes** mito claim | Evidence class of each GO term | Mito/peptide terms (GO:0005743, GO:0015421, GO:0090374) are all `IEA:TreeGrafter`; SL export (GO:0140377) and plasma membrane (GO:0005886) are `IMP:UniProtKB` | Curated record | High; TreeGrafter = automated phylogenetic transfer |
| 4 | UniProt feature comparison (computed) | Structural/evolutionary (architecture) | **Refutes** mito peptide-exporter identity | Is H6TB12 a half-size mito transporter? | H6TB12 = 1299 aa, 12 TM, **2 NBD** (full-length), MDR-exporter subfamily = same class as ABCB1/P-gp (1280 aa, 12 TM, 2 NBD) | Sequence/domain | High; direct feature counts from UniProt |
| 5 | PMID 11251115 (Young 2001, *Science*) | Direct assay + localization (of Mdl1) | **Competing/contextual** | What protein does mito peptide export? | Mdl1 (a **half**-transporter in the mitochondrial inner membrane) exports ~600–2100 Da peptides from the matrix | *S. cerevisiae* | High; defines the true owner of the transferred GO terms |
| 6 | PMID 16710701 (Herget & Tampé 2007, review) | Review/synthesis | **Competing/contextual** | Which ABCB members are mitochondrial peptide exporters? | ABCB8/ABCB10 target inner mito membrane; MDL1 (yeast ABCB10 homolog) exports peptides — all **half**-transporters | Human/yeast | Review-level, but clearly labels architecture–localization link |
| 7 | PMID 15247210 (Galluhn & Langer 2004) | Direct assay (Mdl1 assembly) | Contextual | Mdl1 mechanism | Mdl1 half-transporter dimerizes and docks on F1F0-ATP synthase in inner membrane | *S. cerevisiae* | High; underscores mito-specific assembly interfaces absent from H6TB12 evidence |
| 8 | PMID 32474798 (Jezierska 2020) | Mutant phenotype | Contextual | *S. bombicola* mito carriers | S. bombicola's characterized mitochondrial transporters are SLC-type citrate carriers (SbCtp1/SbYhm2), not the SL-MDR | *S. bombicola* | High; no link of SL-MDR to mitochondria in this organism |
| 9 | QuickGO / GO_REF:0000118 (computed, Iter 3) | Computational (annotation provenance) | **Refutes/qualifies** mito claim | Independent support for mito terms? | GO:0015421, GO:0090374, GO:0005743 all share one provenance: IEA/ECO:0007826/GO_REF:0000118/TreeGrafter, with-from = node PTN008681462; no other evidence line | Curated annotation graph | High; single-graft dependency = single point of failure |

---

## GO Curation Implications (leads — require curator verification)

| GO term | Aspect | Current evidence | Lead recommendation |
|---------|--------|------------------|---------------------|
| GO:0140377 sophorolipid biosynthetic process | BP | IMP:UniProtKB (PMID 23516968) | **Retain** (core). Consider also a transport BP (e.g., GO:0140161 monocarboxylic-acid/glycolipid export or export across plasma membrane) to capture the direct transport activity. |
| GO:0005886 plasma membrane | CC | IMP:UniProtKB | **Retain** (core); note localization is inferred from secretion phenotype, not microscopy. |
| GO:0005524 ATP binding / GO:0016887 ATP hydrolysis / ABC transmembrane transporter activity | MF | IEA:InterPro | **Retain** (compatible, well-supported by domains). |
| GO:0015421 ABC-type oligopeptide transporter activity | MF | IEA:TreeGrafter only | **Generalize or remove for this protein.** No peptide-transport assay; substrate is sophorolipid. Prefer a generic ABC-type transmembrane transporter activity term over the oligopeptide-specific one. |
| GO:0090374 oligopeptide export from mitochondrion | BP | IEA:TreeGrafter only | **Remove / NOT qualifier (non-core).** Architecture (full-length MDR) contradicts; no mitochondrial assay. |
| GO:0005743 mitochondrial inner membrane | CC | IEA:TreeGrafter only | **Remove / NOT qualifier (non-core).** Conflicts with experimental plasma-membrane localization; full-length MDR class is not mitochondrial. |

Avoiding "protein binding" as a recommendation: the informative supported MF is **ABC-type transmembrane transporter activity coupled to ATP hydrolysis** (exporting sophorolipids), not oligopeptide transport.

---

## Mechanistic Scope

- **Immediate molecular function (direct):** ATP-driven ABC-type efflux transport. H6TB12 uses two nucleotide-binding domains to hydrolyze ATP and translocate **acidic acylated/non-acylated sophorolipids** across the **plasma membrane** into the extracellular space (PMID 23516968).
- **Downstream / process level:** contributes to sophorolipid secretion; loss reduces (does not abolish) export because of paralog redundancy with SbSLMdr.2 (PMID 34998388) and alternative routes (PMID 23516968).
- **Claimed second function (mitochondrial oligopeptide export):** would require inner-mitochondrial-membrane targeting, matrix-facing peptide substrate handling, and the half-transporter/F1F0 assembly interface documented for Mdl1 (PMID 15247210). None is demonstrated for H6TB12; the claim rests entirely on family-level electronic inference. This is best characterized as a **mis-transferred family annotation**, not a downstream phenotype of the real function.

---

## Computed Provenance (Iteration 2 — sequence/architecture check)

Analysis run: 5-mer sequence similarity + length-ratio of H6TB12 against full-length MDR exporters and half-size mitochondrial peptide exporters (UniProt REST sequences); PANTHER family metadata via InterPro API.

| Protein | Length (aa) | Len ratio vs H6TB12 | 5-mer Jaccard to H6TB12 | Class |
|---------|------------:|--------------------:|------------------------:|-------|
| H6TB12 (target) | 1299 | 1.00 | 1.000 | full-length target |
| P21439 human ABCB4 | 1286 | 0.99 | 0.024 | full-length MDR |
| P08183 human ABCB1/P-gp | 1280 | 0.99 | 0.020 | full-length MDR |
| Q9NRK6 human ABCB10 | 738 | 0.57 | 0.015 | half-size mito peptide exporter |
| P33310 yeast Mdl1 | 695 | 0.54 | 0.013 | half-size mito peptide exporter |
| P33311 yeast Mdl2 | 773 | 0.60 | 0.013 | half-size mito |
| O75027 human ABCB7 | 752 | 0.58 | 0.006 | half-size mito |

- **Length ratio is decisive:** H6TB12 (1299 aa) equals full-length MDR exporters (ratio ~1.0) and is ~1.8–2× the size of every half-size mitochondrial exporter (ratio ~0.54–0.60), consistent with a fused (TMD-NBD)×2 architecture.
- **Similarity direction:** mean 5-mer Jaccard to full-length MDR refs (0.022) > to half-size mito refs (0.012). *Caveat:* absolute k-mer Jaccard is low because the references are cross-kingdom (human/S. cerevisiae); k-mer Jaccard is a crude proxy, so this is corroborating, not primary — the decisive evidence remains the UniProt domain architecture (12 TM, 2 NBD) and the "Multidrug resistance exporter (TC 3.A.1.201)" subfamily assignment.
- **PANTHER PTHR43394** metadata confirmed: family name = "ATP-DEPENDENT PERMEASE MDL1, MITOCHONDRIAL" — i.e., the family is named for the mitochondrial half-transporter Mdl1, mechanistically explaining why the mito/peptide GO-slim terms were transferred to a full-length MDR exporter.

*(Executed code and full numeric output are retained in the Iteration 2 execution log as provenance.)*

### Iteration 3 — GO annotation provenance (QuickGO), resolving the PTN008681462 graft question

Analysis run: QuickGO annotation API for H6TB12 (evidence code, GO_REF, assigned-by, with/from).

| GO ID | Aspect | Term | Evidence | GO_REF | Assigned by | With/From |
|-------|--------|------|----------|--------|-------------|-----------|
| GO:0140377 | BP | sophorolipid biosynthetic process | **IMP** (ECO:0000315) | PMID:23516968 | UniProt | — |
| GO:0005886 | CC | plasma membrane | **IMP** (ECO:0000315) | PMID:23516968 | UniProt | — |
| GO:0005886 | CC | plasma membrane | IEA | GO_REF:0000044 | UniProt | keyword SL-0039 |
| GO:0005524 | MF | ATP binding | IEA | GO_REF:0000002 | InterPro | IPR003439… |
| GO:0016887 | MF | ATP hydrolysis activity | IEA | GO_REF:0000002 | InterPro | IPR003439/017871 |
| GO:0140359 | MF | ABC-type transmembrane transporter activity | IEA | GO_REF:0000002 | InterPro | IPR011527 |
| GO:0055085 | BP | transmembrane transport | IEA | GO_REF:0000002 | InterPro | IPR011527 |
| GO:0016020 | CC | membrane | IEA | GO_REF:0000002 | InterPro | IPR011527/036640 |
| **GO:0015421** | MF | **ABC-type oligopeptide transporter activity** | IEA (ECO:0007826) | **GO_REF:0000118** | **TreeGrafter** | **PTN008681462** |
| **GO:0090374** | BP | **oligopeptide export from mitochondrion** | IEA (ECO:0007826) | **GO_REF:0000118** | **TreeGrafter** | **PTN008681462** |
| **GO:0005743** | CC | **mitochondrial inner membrane** | IEA (ECO:0007826) | **GO_REF:0000118** | **TreeGrafter** | **PTN008681462** |

**Key result — the seed's version-discrepancy question is resolved.** All three disputed mitochondrial/oligopeptide terms carry the identical provenance: `IEA / ECO:0007826 / GO_REF:0000118 / TreeGrafter`, with-from = **PTN008681462** — exactly the graft node the seed flagged. They rest on **one** automated phylogenetic graft with **no** independent supporting evidence line. If that graft is unstable across PANTHER releases (the seed reports the current tree resolves PTN008681462 as an *Embryophyta* subtree with H6TB12 absent as an exact leaf), then **all three terms lose their sole support simultaneously** and can be treated as a single removable/NOT-qualifiable unit. The experimental terms (IMP, PMID:23516968) and the generic InterPro ABC/ATP/membrane terms (GO_REF:0000002) are entirely independent of that node and are unaffected.

*(Executed code and full QuickGO output are retained in the Iteration 3 execution log as provenance.)*

---

## Conflicts and Alternatives

- **Paralog/family confusion (primary driver of the over-annotation).** PANTHER PTHR43394 is named for Mdl1 and pools full-length and half-size ABCB proteins. TreeGrafter transferred Mdl1's GO-slim (mito inner membrane, oligopeptide export) to H6TB12 despite the architectural class difference. The seed's own citation (PMID 34998388) explicitly distinguishes full-length MDR proteins from mitochondrial half-size transporters.
- **Localization conflict.** Experimental evidence places the protein at the plasma/cell membrane (consistent with extracellular sophorolipid secretion), directly conflicting with the IEA mitochondrial-inner-membrane term.
- **Organism context.** In *S. bombicola*, the transporters experimentally tied to mitochondria are SLC-type citrate carriers (SbCtp1/SbYhm2; PMID 32474798), not the SL-MDR — no independent line links H6TB12 to mitochondria.
- **Version/graft discrepancy (seed's TreeGrafter note).** The seed reports that frozen node PTN008681462 in PTHR43394 SF11 now resolves as an *Embryophyta* subtree and that H6TB12 is not present as an exact leaf, while the current tree GO-slim still retains mito/peptide terms on that path and the current IBD/GAF places mitochondrial-peptide IBDs on other paths. I could not programmatically re-derive the internal TreeGrafter graft (PANTHER graft internals were not accessible in this run), so I report this conservatively: the discrepancy means the mito/peptide transfer is an **unstable, version-dependent electronic inference**, further weakening its use as evidence. Broad membrane/ATP/ABC IBDs along the path remain compatible.

---

## Knowledge Gaps

1. **No direct subcellular imaging of H6TB12.** Checked: UniProt localization is ECO:0000305 (inferred from secretion). Matters because it is the crux of the mito-vs-plasma-membrane conflict. Resolve with GFP/immunofluorescence or fractionation in *S. bombicola*.
2. **No peptide-transport assay.** Checked: neither PMID 23516968 nor 34998388 tests peptide substrates. Matters because GO:0015421/0090374 assert peptide handling. Resolve with in vitro reconstituted transport or peptide-efflux assays.
3. **TreeGrafter graft provenance (PTN008681462) — largely RESOLVED (Iter 3).** Confirmed via QuickGO that all three disputed terms share the exact provenance IEA/ECO:0007826/GO_REF:0000118/TreeGrafter with-from = PTN008681462, so they stand or fall together on that single graft. What remains unchecked: the internal PANTHER PTHR43394 tree topology (frozen vs current) that would confirm the seed's report of an *Embryophyta* resolution and H6TB12's absence as an exact leaf — the raw tree/GAF was not machine-accessible in this run. Resolve by inspecting the current PTHR43394 phylogeny and IBD GAF along the recovered path.
4. **Functional status of SbSLMdr.2 and cross-complementation.** Matters for how much of the export phenotype is attributable to H6TB12 specifically.

---

## Discriminating Tests

1. **Localization:** C-terminal fluorescent tag or subcellular fractionation of H6TB12 in *S. bombicola* → plasma membrane (predicted) vs mitochondrial inner membrane (mito hypothesis). Single most decisive experiment.
2. **Substrate specificity:** reconstituted-vesicle or whole-cell efflux assay comparing sophorolipids vs 600–2100 Da peptides (the Mdl1 substrate range). MDR hypothesis predicts sophorolipid/hydrophobic-drug transport, not peptide export.
3. **Architecture-aware phylogenetics:** align H6TB12 against full-length ABCB1-type vs half-size Mdl1/ABCB10 references; confirm it branches with full-length MDR exporters (predicted). This distinguishes the two subfamilies without wet-lab work.
4. **TreeGrafter re-grafting audit:** recompute the graft node for H6TB12 in the current PTHR43394 tree and check whether mito/peptide GO-slim terms are on the recovered ancestral path or only on divergent (e.g., Embryophyta/half-transporter) branches.

---

## Curation Leads (require curator verification)

- **Action change:** Downgrade the three `IEA:TreeGrafter` mitochondrial/peptide terms (GO:0005743, GO:0015421, GO:0090374) to **non-core**; candidate for removal or a **NOT** annotation given experimental plasma-membrane localization and full-length MDR architecture. Retain sophorolipid-export (GO:0140377) and plasma membrane (GO:0005886) as core; retain generic ATP/ABC MF terms.
- **Candidate references (verify snippets):**
  - PMID 23516968 — "knocking out the transporter gene yields mutants still able to secrete sophorolipids, though only at levels of 10% as compared with the wild type, suggesting alternative routes for secretion" (core secretory role + redundancy).
  - PMID 34998388 — ABC superfamily "harbors the main driver behind the highly efficient sophorolipid export"; "identify a second sophorolipid transporter that is located outside the sophorolipid biosynthetic gene cluster" (redundancy SbSLMdr.2; separates full-length MDR from half-size mito transporters).
  - PMID 11251115 / PMID 16710701 — establish that mitochondrial inner-membrane oligopeptide export is the function of the **half-size** Mdl1/ABCB10 subfamily (source of the transferred terms), not of full-length MDR exporters.
- **Suggested curator question:** Is there any experimental (imaging, fractionation, or peptide-transport) evidence for a mitochondrial or peptide role of H6TB12, or does all such support trace solely to PANTHER PTHR43394 TreeGrafter transfer?
- **Suggested experiment:** Fluorescent-tag localization + sophorolipid-vs-peptide efflux assay (Discriminating Tests 1–2).

---

## Bottom Line

The prior/AI-proposed mitochondrial-inner-membrane + ATP-dependent oligopeptide-export capacity for H6TB12 is a **family-level TreeGrafter over-annotation** inherited from the Mdl1-named PANTHER family, contradicted by the protein's full-length P-gp/MDR architecture and its experimentally supported plasma-membrane sophorolipid-export function. The deletion/redundancy studies establish the **secretory** role, not a mitochondrial one. Broad ABC/ATP/transmembrane-transport terms remain valid; the specific mitochondrial and oligopeptide terms should be treated as non-core (remove or NOT) pending direct localization/substrate evidence.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)