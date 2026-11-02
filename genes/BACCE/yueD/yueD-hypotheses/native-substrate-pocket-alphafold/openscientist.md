---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-09T18:28:43.711948'
end_time: '2026-10-09T19:20:12.236898'
duration_seconds: 3088.53
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: BACCE
  gene: yueD
  gene_symbol: yueD
  uniprot_accession: Q8RJB2
  taxon_id: NCBITaxon:1396
  taxon_label: Bacillus cereus
  focus_type: free_text
  hypothesis_slug: native-substrate-pocket-alphafold
  hypothesis_text: The physiological substrate of Bacillus cereus YueD (UniProt Q8RJB2)
    is not benzil but a naturally occurring aromatic carbonyl compound, most plausibly
    a quinone, and the substrate-binding pocket of its AlphaFold structure should
    discriminate between these candidate substrate classes.
  term_context: '- Background the curator can state: this short-chain dehydrogenase/reductase
    was identified by screening for the gene responsible for reducing benzil, a wholly
    synthetic diketone used in UV-curing plastics and as a laboratory reagent. GO
    obsoleted its substrate-specific term on the grounds that benzil is not a physiologically
    relevant substrate. The question is what the enzyme actually acts on in the cell.

    - Decide this with structural evidence. Retrieve the AlphaFold DB model for UniProt
    Q8RJB2 (https://alphafold.ebi.ac.uk/entry/Q8RJB2 ; mmCIF https://alphafold.ebi.ac.uk/files/AF-Q8RJB2-F1-model_v4.cif)
    and locate the NADPH site and the substrate pocket, using experimental SDR structures
    as reference where helpful.

    - The single decisive analysis: measure the substrate pocket and assess which
    candidate substrate class it best accommodates on steric and electronic grounds.
    Candidates to compare explicitly are benzil (a bulky, twisted diaryl alpha-diketone),
    1,4-naphthoquinone (a flat fused bicyclic quinone), a short aliphatic dicarbonyl
    such as methylglyoxal, and sepiapterin or a related pterin, since this protein
    is placed in a PANTHER sepiapterin reductase family.

    - Published kinetics for this enzyme give a much lower Michaelis constant for
    1,4-naphthoquinone than for benzil. State whether the pocket geometry you measure
    is consistent with that ordering, and if it is not, say so.

    - Report per-residue pLDDT for the pocket and cofactor site and state whether
    model confidence supports the conclusion. Run Foldseek or an equivalent search
    against the PDB and AlphaFold DB, list the nearest structural neighbours with
    their annotated reactions and known substrates, and report whether quinone reductases
    or pterin reductases are closer.

    - Name every tool and database version actually invoked and show the real output.
    If a tool cannot be run programmatically, say so plainly rather than substituting
    an inferred result for a computed one. An honest inconclusive answer is preferable
    to an overstated one.'
  reference_context: No specific reference context supplied.
  source_file: genes/BACCE/yueD/yueD-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: The physiological substrate of Bacillus cereus\
    \ YueD (UniProt Q8RJB2) is not benzil but a naturally\n  occurring aromatic carbonyl\
    \ compound, most plausibly a quinone, and the substrate-binding pocket of\n  its\
    \ AlphaFold structure should discriminate between these candidate substrate classes.\n\
    focus_type: free_text\ncontext:\n- 'Background the curator can state: this short-chain\
    \ dehydrogenase/reductase was identified by screening\n  for the gene responsible\
    \ for reducing benzil, a wholly synthetic diketone used in UV-curing plastics\n\
    \  and as a laboratory reagent. GO obsoleted its substrate-specific term on the\
    \ grounds that benzil is\n  not a physiologically relevant substrate. The question\
    \ is what the enzyme actually acts on in the cell.'\n- Decide this with structural\
    \ evidence. Retrieve the AlphaFold DB model for UniProt Q8RJB2 (https://alphafold.ebi.ac.uk/entry/Q8RJB2\n\
    \  ; mmCIF https://alphafold.ebi.ac.uk/files/AF-Q8RJB2-F1-model_v4.cif) and locate\
    \ the NADPH site and the\n  substrate pocket, using experimental SDR structures\
    \ as reference where helpful.\n- 'The single decisive analysis: measure the substrate\
    \ pocket and assess which candidate substrate class\n  it best accommodates on\
    \ steric and electronic grounds. Candidates to compare explicitly are benzil (a\n\
    \  bulky, twisted diaryl alpha-diketone), 1,4-naphthoquinone (a flat fused bicyclic\
    \ quinone), a short aliphatic\n  dicarbonyl such as methylglyoxal, and sepiapterin\
    \ or a related pterin, since this protein is placed\n  in a PANTHER sepiapterin\
    \ reductase family.'\n- Published kinetics for this enzyme give a much lower Michaelis\
    \ constant for 1,4-naphthoquinone than\n  for benzil. State whether the pocket\
    \ geometry you measure is consistent with that ordering, and if it\n  is not,\
    \ say so.\n- Report per-residue pLDDT for the pocket and cofactor site and state\
    \ whether model confidence supports\n  the conclusion. Run Foldseek or an equivalent\
    \ search against the PDB and AlphaFold DB, list the nearest\n  structural neighbours\
    \ with their annotated reactions and known substrates, and report whether quinone\n\
    \  reductases or pterin reductases are closer.\n- Name every tool and database\
    \ version actually invoked and show the real output. If a tool cannot be\n  run\
    \ programmatically, say so plainly rather than substituting an inferred result\
    \ for a computed one.\n  An honest inconclusive answer is preferable to an overstated\
    \ one.\nreference_id: []"
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
artifact_count: 6
artifact_sources:
  openscientist_artifacts_zip: 6
artifacts:
- filename: candidate_steric_comparison.csv
  path: openscientist_artifacts/candidate_steric_comparison.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist candidate steric comparison
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
- filename: go_decision_table.csv
  path: openscientist_artifacts/go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go decision table
- filename: kinetics_table.csv
  path: openscientist_artifacts/kinetics_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist kinetics table
- filename: structural_metrics.csv
  path: openscientist_artifacts/structural_metrics.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist structural metrics
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** BACCE
- **Taxon:** Bacillus cereus (NCBITaxon:1396)
- **Gene directory:** yueD
- **Gene symbol:** yueD
- **UniProt accession:** Q8RJB2

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** native-substrate-pocket-alphafold
- **Source file:** genes/BACCE/yueD/yueD-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

The physiological substrate of Bacillus cereus YueD (UniProt Q8RJB2) is not benzil but a naturally occurring aromatic carbonyl compound, most plausibly a quinone, and the substrate-binding pocket of its AlphaFold structure should discriminate between these candidate substrate classes.

## Term and Decision Context

- Background the curator can state: this short-chain dehydrogenase/reductase was identified by screening for the gene responsible for reducing benzil, a wholly synthetic diketone used in UV-curing plastics and as a laboratory reagent. GO obsoleted its substrate-specific term on the grounds that benzil is not a physiologically relevant substrate. The question is what the enzyme actually acts on in the cell.
- Decide this with structural evidence. Retrieve the AlphaFold DB model for UniProt Q8RJB2 (https://alphafold.ebi.ac.uk/entry/Q8RJB2 ; mmCIF https://alphafold.ebi.ac.uk/files/AF-Q8RJB2-F1-model_v4.cif) and locate the NADPH site and the substrate pocket, using experimental SDR structures as reference where helpful.
- The single decisive analysis: measure the substrate pocket and assess which candidate substrate class it best accommodates on steric and electronic grounds. Candidates to compare explicitly are benzil (a bulky, twisted diaryl alpha-diketone), 1,4-naphthoquinone (a flat fused bicyclic quinone), a short aliphatic dicarbonyl such as methylglyoxal, and sepiapterin or a related pterin, since this protein is placed in a PANTHER sepiapterin reductase family.
- Published kinetics for this enzyme give a much lower Michaelis constant for 1,4-naphthoquinone than for benzil. State whether the pocket geometry you measure is consistent with that ordering, and if it is not, say so.
- Report per-residue pLDDT for the pocket and cofactor site and state whether model confidence supports the conclusion. Run Foldseek or an equivalent search against the PDB and AlphaFold DB, list the nearest structural neighbours with their annotated reactions and known substrates, and report whether quinone reductases or pterin reductases are closer.
- Name every tool and database version actually invoked and show the real output. If a tool cannot be run programmatically, say so plainly rather than substituting an inferred result for a computed one. An honest inconclusive answer is preferable to an overstated one.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: The physiological substrate of Bacillus cereus YueD (UniProt Q8RJB2) is not benzil but a naturally
  occurring aromatic carbonyl compound, most plausibly a quinone, and the substrate-binding pocket of
  its AlphaFold structure should discriminate between these candidate substrate classes.
focus_type: free_text
context:
- 'Background the curator can state: this short-chain dehydrogenase/reductase was identified by screening
  for the gene responsible for reducing benzil, a wholly synthetic diketone used in UV-curing plastics
  and as a laboratory reagent. GO obsoleted its substrate-specific term on the grounds that benzil is
  not a physiologically relevant substrate. The question is what the enzyme actually acts on in the cell.'
- Decide this with structural evidence. Retrieve the AlphaFold DB model for UniProt Q8RJB2 (https://alphafold.ebi.ac.uk/entry/Q8RJB2
  ; mmCIF https://alphafold.ebi.ac.uk/files/AF-Q8RJB2-F1-model_v4.cif) and locate the NADPH site and the
  substrate pocket, using experimental SDR structures as reference where helpful.
- 'The single decisive analysis: measure the substrate pocket and assess which candidate substrate class
  it best accommodates on steric and electronic grounds. Candidates to compare explicitly are benzil (a
  bulky, twisted diaryl alpha-diketone), 1,4-naphthoquinone (a flat fused bicyclic quinone), a short aliphatic
  dicarbonyl such as methylglyoxal, and sepiapterin or a related pterin, since this protein is placed
  in a PANTHER sepiapterin reductase family.'
- Published kinetics for this enzyme give a much lower Michaelis constant for 1,4-naphthoquinone than
  for benzil. State whether the pocket geometry you measure is consistent with that ordering, and if it
  is not, say so.
- Report per-residue pLDDT for the pocket and cofactor site and state whether model confidence supports
  the conclusion. Run Foldseek or an equivalent search against the PDB and AlphaFold DB, list the nearest
  structural neighbours with their annotated reactions and known substrates, and report whether quinone
  reductases or pterin reductases are closer.
- Name every tool and database version actually invoked and show the real output. If a tool cannot be
  run programmatically, say so plainly rather than substituting an inferred result for a computed one.
  An honest inconclusive answer is preferable to an overstated one.
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

# YueD (Bacillus cereus, UniProt Q8RJB2) — Native Substrate & Pocket Hypothesis

**Focus:** `native-substrate-pocket-alphafold` (free-text)
**Seed hypothesis:** The physiological substrate of YueD is not benzil but a naturally occurring aromatic carbonyl compound, *most plausibly a quinone*, and the AlphaFold substrate pocket should *discriminate between candidate substrate classes*.

> **Note on this version:** Iteration 3 retrieved the actual Km/kcat constants from UniProt's BIOPHYSICOCHEMICAL PROPERTIES block (ECO:0000269, PMID 11796169). These data **correct** an iteration‑2 misreading in which the UniProt FUNCTION‑field phrase "in decreasing order" was taken as a substrate‑preference ranking. The quantitative kinetics actually **support** the seed's premise that 1,4‑naphthoquinone has a far lower Km than benzil. The judgment below reflects the corrected analysis.

---

## Executive Judgment

**Verdict: Partially supported.** The seed's structural/kinetic reasoning holds up better than a first pass suggested, but the specific identification of the native substrate as "a quinone" remains unresolved.

- **Supported — "not benzil":** Benzil is a wholly synthetic screening substrate (PMID 11745140) and the weakest-binding diketone tested (Km = 768 µM). GO's obsoletion of the benzil-specific term is justified.
- **Supported — pocket/kinetics alignment:** The measured **Km(1,4-naphthoquinone) = 27.6 µM is ~28× lower than Km(benzil) = 768 µM** (PMID 11796169). The AlphaFold pocket is enclosed and aromatic/hydrophobic, sterically disfavouring the bulky, twisted benzil (10 Å, plane-RMSD 0.39 Å) relative to a flat, compact aromatic such as naphthoquinone. **The pocket geometry I measured is consistent with the stated Km ordering** — i.e., the pocket does appear to discriminate on steric grounds, exactly as the seed proposed.
- **Unresolved — "most plausibly a quinone":** By catalytic efficiency (kcat/Km), the single best in-vitro substrate is **1-phenyl-1,2-propanedione (3.93 min⁻¹µM⁻¹), ~15× better than 1,4-naphthoquinone (0.268) and ~47× better than benzil (0.084)** — and it is also a synthetic aryl-alkyl diketone, not a quinone. Methylglyoxal and sepiapterin were never assayed. So the kinetics favour **small/flat aromatic carbonyls in general**, consistent with (but not uniquely pointing to) a quinone.
- **Competing signal — structural homology:** Foldseek's nearest characterized neighbours are **sepiapterin reductases and SDR ketoreductases, not quinone reductases**. So evolutionary context points to pterin/keto-reductase chemistry rather than a dedicated quinone reductase.
- **Mechanistic caveat:** In the homologous human SPR, quinone turnover can be NADPH-dependent **redox cycling at the cofactor site** rather than substrate-pocket reduction (PMID 23640889). For YueD, the defined Km/kcat for 1,4-NQ implies genuine substrate-pocket turnover, but the mechanism was not explicitly dissected for this enzyme.
- **Over-annotation flag:** `sepiapterin reductase activity` (GO:0004757) and `tetrahydrobiopterin biosynthetic process` (GO:0006729) on Q8RJB2 are **IEA:TreeGrafter** inferences from PANTHER PTHR44085, with no experimental support and no known BH4 pathway in *B. cereus*.

**Bottom line for the curator:** The AlphaFold model is high-confidence and the pocket **does** appear to discriminate sterically in a way consistent with the real kinetics (tight flat aromatics, weak bulky benzil). This supports treating benzil as non-physiological and favouring a small/flat aromatic carbonyl substrate. It does **not**, by itself, prove the native substrate is a quinone — a quinone is one plausible member of the favoured class, alongside other flat aromatic carbonyls and (untested) pterins. The most defensible annotation remains a **general NADPH-dependent aromatic carbonyl reductase of unknown physiological substrate**.

---

## Tools & Database Versions Actually Invoked (provenance)

| Tool / resource | Version / date | What was run | Real output (key values) |
|---|---|---|---|
| AlphaFold DB REST API + model | **AF-Q8RJB2-F1**, model **v6**, created **2025-08-01** | Downloaded model + confidence | global pLDDT **96.8**; 98% residues very-high. (Seed's `..._v4.cif` URL now 404s; v6 is current.) |
| Manual PDB parse (numpy/scipy) | — | Motif ID, pLDDT, pocket map, radial cavity probe | SDR tetrad **Asn86/Ser140/Tyr154/Lys158** (pLDDT 98.0–98.9); Rossmann **TGTSQGLG res 7–14**; pocket 33 res mean pLDDT 97.1; enclosed (7% of 400 rays open), median reach 5.4 Å |
| PubChem PUG REST 3D | 2026-10 | Candidate sterics | benzil 10.0 Å, plane-RMSD **0.39** (twisted); 1,4-NQ 5.3 Å, 0.00 (flat); methylglyoxal 3.7 Å; menadione 6.6 Å |
| **Foldseek** web server (search.foldseek.com) | pdb100, afdb-swissprot, afdb50 (2026-10) | 3Di search | Nearest named: B. subtilis YueD O32099 (40%), yeast IRC24 P40580, then **sepiapterin reductases**; PDB: human **SPR 1z6z/1nas/6i6v/6i6f/7dsf**, KRED1 6yc8, yeast YIR035C 6uhx, actinorhodin KR 1x7g, 3-OH-butyrate DH 5b4t/2q2v. **No quinone reductase.** |
| UniProtKB REST (`Q8RJB2.json`) | reviewed; evidence at protein level | EC, GO, family, **kinetics** | EC 1.1.1.320; PANTHER PTHR44085; Km/kcat table below (ECO:0000269 PMID 11796169) |
| kcat/Km computation (pandas) | — | Specificity constants | see kinetics table; 1,4-NQ 3.2× > benzil; best = 1-phenyl-1,2-propanedione |

*Honest limitations:* The AlphaFold model is apo (no NADP/substrate), so pocket metrics are geometric, not energetic; no docking/MD was run. Km/kcat were taken from UniProt's curated ECO:0000269 annotation of PMID 11796169 (full text not retrieved); methylglyoxal and sepiapterin were not among the tested substrates. Foldseek hits are remote (21–28% id), reflecting the common SDR fold.

---

## Kinetics (PMID 11796169, via UniProt Q8RJB2; NADPH, 37 °C, pH 6.5)

| Substrate | Km (µM) | kcat (min⁻¹) | kcat/Km (min⁻¹µM⁻¹) | rel. eff. vs benzil | class |
|---|---|---|---|---|---|
| 1-phenyl-1,2-propanedione | 42.0 | 165 | **3.93** | 46.9× | synthetic aryl-alkyl diketone |
| 1,4-naphthoquinone | **27.6** | 7.4 | 0.268 | 3.2× | flat fused quinone |
| benzil | **768** | 64.4 | 0.084 | 1.0× | bulky twisted diaryl diketone |
| 1-(4-Me-phenyl)-2-phenyl-diketone | 611 | 37.9 | 0.062 | 0.74× | diaryl diketone |
| 1-(4-F-phenyl)-2-phenyl-diketone | 584 | 31.9 | 0.055 | 0.65× | diaryl diketone |
| methyl benzoylformate | 1400 | 16.7 | 0.012 | 0.14× | aryl α-ketoester |
| p-nitrobenzaldehyde | 261 | 1.2 | 0.005 | 0.05× | aryl aldehyde |

*Interpretation:* **Lowest Km → 1,4-naphthoquinone (27.6 µM), tightest binder**; benzil is the weakest binder (768 µM). This is exactly the ordering the seed cited and is **consistent with the enclosed aromatic pocket favouring flat compact aromatics over bulky twisted benzil.** Highest catalytic efficiency, however, is a non-natural aryl-alkyl diketone, so "best substrate" ≠ "quinone." (methylglyoxal, sepiapterin not tested.)

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| PMID 11745140 | Direct assay / gene isolation | Qualifies | Is benzil physiological? | Gene isolated by screening for benzil→(S)-benzoin | *B. cereus* → *E. coli* | High for "benzil = bait" |
| PMID 11796169 (Km data) | Direct kinetics | **Supports** | Km(1,4-NQ) ≪ Km(benzil)? | Km 27.6 vs 768 µM (28× tighter for NQ); kcat/Km(NQ) 3.2× > benzil | recombinant enzyme in vitro | High; curated ECO:0000269 |
| PMID 11796169 (efficiency) | Direct kinetics | Qualifies | Is a quinone the best substrate? | Best kcat/Km = 1-phenyl-1,2-propanedione (synthetic), not a quinone | in vitro | High; natural substrates untested |
| PMID 11796169 (GFP) | Localization | Supports CC | Location | Bipolar cytoplasm | *B. cereus* | Moderate–high (tagged) |
| PMID 11796169 (homology) | Evolutionary | Qualifies | Nearest homologs | 28–30% to mammalian sepiapterin reductases | cross-species | High; remote (~30%) |
| PMID 23640889 | Mechanistic (human SPR) | Qualifies | How are quinones turned over? | Quinone redox cycling at cofactor site, not substrate pocket (D257H) | human SPR | High mechanism; different enzyme |
| AlphaFold AF-Q8RJB2-F1 v6 | Computational | **Supports** | Pocket discriminates? | Enclosed aromatic pocket disfavours bulky benzil; consistent with Km order | predicted apo model | High confidence; apo, geometric only |
| PubChem 3D | Computational | Supports | Candidate sterics | benzil bulky/twisted; 1,4-NQ flat/compact | small-molecule geometry | Geometric, no energy |
| Foldseek | Structural/evolutionary | **Competes** | Quinone vs pterin reductase closer? | Sepiapterin reductases & SDR ketoreductases closest; no quinone reductase | PDB100/AFDB | High; remote hits (generic SDR fold) |
| UniProt Q8RJB2 | Review/database | Flag | GO annotation quality | GO:0004757 & GO:0006729 are IEA:TreeGrafter only | PANTHER PTHR44085 | Database-level |

---

## GO Curation Implications (leads — require curator verification)

| GO term | Aspect | Current evidence | Recommendation |
|---|---|---|---|
| GO:0004090 carbonyl reductase (NADPH) activity | MF | IEA:RHEA (EC 1.1.1.320) | **Retain** — best-supported, appropriately general core MF |
| GO:0016616 oxidoreductase, CH-OH donor, NAD(P) acceptor | MF | EXP | **Retain** (parent) |
| GO:0005737 cytoplasm | CC | EXP (GFP, PMID 11796169) | **Retain** |
| GO:0004757 **sepiapterin reductase (NADP+) activity** | MF | **IEA:TreeGrafter only** | **Flag / downgrade** — no sepiapterin assay for YueD; ~25% id to true SPRs; not core |
| GO:0006729 **tetrahydrobiopterin biosynthetic process** | BP | **IEA:TreeGrafter only** | **Flag / consider removal** — no BH4 pathway known in *B. cereus* |
| (seed-proposed) quinone reductase activity | MF | Km/kcat for 1,4-NQ measured | **Do not assert as core.** Supported as *an* in-vitro activity, but not shown to be the physiological role; 1,4-NQ is not the most efficient substrate and structural neighbours are not quinone reductases. If annotated, use with "ISS/IDA for in-vitro 1,4-naphthoquinone reduction" caveat, not as the primary function |

**Net curation lead:** Keep a **general NADPH carbonyl/aryl-ketone reductase** MF + **cytoplasm** CC; treat **sepiapterin-reductase MF and BH4-biosynthesis BP as non-core phylogenetic over-annotations**; annotate the physiological substrate/process as **unknown**. The structural+kinetic evidence supports "benzil is non-physiological" and "pocket favours flat/compact aromatic carbonyls," but does not justify naming a quinone as the core function.

---

## Mechanistic Scope

Direct activity: **NADPH-dependent reduction of an aromatic carbonyl** (aryl α-diketone/aldehyde/quinone) to the alcohol, by a cytoplasmic SDR using the Ser140–Tyr154–Lys158 relay with Asn86 and an NADP(H) Rossmann site. All in-vitro substrates assayed are synthetic/xenobiotic; "quinone reductase," "sepiapterin reductase," and "tetrahydrobiopterin biosynthesis" are inferences, not demonstrated physiological roles. The pocket's steric preference for flat compact aromatics (low Km for 1,4-NQ) is a property of the enzyme; which natural flat aromatic carbonyl it acts on in the cell is unknown.

---

## Conflicts and Alternatives

1. **Efficiency vs affinity split:** 1,4-NQ has the lowest Km but modest kcat; the most *efficient* substrate (1-phenyl-1,2-propanedione) is a non-natural diketone — so tight binding of a quinone does not by itself make a quinone the physiological substrate.
2. **Family evidence cuts toward pterin/keto-reductase:** PANTHER PTHR44085 (sepiapterin reductase) and Foldseek neighbours argue for pterin/carbonyl chemistry, not a dedicated quinone reductase.
3. **Mechanistic category caveat:** homologous SPR handles quinones by cofactor-site redox cycling (PMID 23640889); YueD's defined Km/kcat suggest true pocket turnover but this was not dissected.
4. **Bacterial quinone size mismatch:** the natural bacterial quinone is **menaquinone** (large lipophilic isoprenoid), which would not fit this small soluble pocket — so "quinone" in vivo is unlikely to be a naphthoquinone-shaped molecule.
5. **Apo-model caveat:** no NADP/substrate in the model; pocket metrics are geometric approximations.
6. **Database carry-over:** sepiapterin/BH4 terms likely propagated across the PANTHER clade (also seen on orthologs).

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | Resolution |
|---|---|---|---|
| True physiological substrate | Lit + UniProt kinetics; all tested substrates synthetic | Determines correct MF/BP | ΔyueD metabolomics; screen natural flat aromatic carbonyls (o-quinones, isatin, aromatic aldehydes, pterins) |
| Pterin activity | Not assayed for YueD | Decides GO:0004757 | Direct sepiapterin→BH2 assay with recombinant YueD + NADPH |
| BH4 pathway in *B. cereus* | Not established | Decides GO:0006729 | Genomic check for GTPCH-I/PTPS; BH4 detection |
| Quinone mechanism (turnover vs redox cycling) | Km/kcat known; mechanism not dissected | Affects whether "quinone reductase" is a real pocket activity | Steady-state vs single-turnover; O2-consumption/ROS assay with 1,4-NQ |
| In-cell role | GFP localization only | Separates catalysis from biology | ΔyueD phenotyping under electrophile/oxidative stress |

---

## Discriminating Tests (most efficient first)

1. **ΔyueD metabolomics / stress phenotyping** — best route to the native substrate and BP.
2. **Direct sepiapterin and methylglyoxal assays** with recombinant YueD + NADPH — close the two untested candidate classes and settle GO:0004757.
3. **Quinone mechanism assay** (ROS/O2 consumption vs clean 2-electron reduction for 1,4-NQ) — tests whether the "quinone" activity is pocket turnover or redox cycling.
4. **NADP+-bound model + docking** — enables a real steric/electronic discrimination test rather than apo geometry.
5. **Operon/genomic-context analysis** in *B. cereus* — may reveal the served pathway.

---

## Curation Leads (require curator verification)

- **Reference snippets to verify**
  - PMID 11796169 (kinetics, via UniProt ECO:0000269): Km = 768 µM (benzil) vs 27.6 µM (1,4-naphthoquinone); kcat/Km best for 1-phenyl-1,2-propanedione → confirms NQ binds tighter than benzil but is not the most efficient substrate.
  - PMID 11796169: *"Green fluorescent protein-tagged B. cereus benzil reductase distributed in the bipolar cytoplasm in B. cereus cells."* → GO:0005737.
  - PMID 23640889: *"Site-directed mutagenesis of the SPR C-terminal substrate-binding site (D257H) completely inhibited sepiapterin reduction but had minimal effects on redox cycling."* → quinone activity need not be substrate-pocket-based.
- **Candidate GO actions:** retain GO:0004090, GO:0016616 (MF), GO:0005737 (CC); **downgrade/flag** GO:0004757 (MF) and GO:0006729 (BP) as IEA:TreeGrafter over-annotations; **do not elevate** any quinone-reductase term to core function (in-vitro only).
- **Action change vs seed:** accept "benzil non-physiological" and "pocket discriminates / favours flat aromatic carbonyls"; keep "quinone" as a *plausible but unproven* member of the favoured class, not the established native substrate.
- **Suggested curator question:** Does any source place a natural flat aromatic carbonyl (e.g., an o-quinone, isatin, or pterin) as a *B. cereus* metabolite that YueD could act on in vivo?
- **Suggested experiment:** ΔyueD vs WT metabolomics + targeted activity screen incl. sepiapterin and methylglyoxal.

---

## Supported vs Refuted (summary)

- **Supported:** Benzil is non-physiological (weakest binder, Km 768 µM, synthetic). YueD is a high-confidence cytoplasmic NADPH SDR carbonyl reductase. **Km(1,4-NQ) ≪ Km(benzil)**, and the enclosed aromatic pocket is **consistent** with that ordering — the pocket does discriminate sterically.
- **Partially supported:** "Native substrate is a naturally occurring aromatic carbonyl" — the enzyme clearly prefers flat/compact aromatic carbonyls, but no natural substrate has been identified.
- **Unresolved / not uniquely supported:** "Most plausibly a quinone" — a quinone fits the favoured class and binds tightly, but the most efficient substrate is a non-natural diketone, structural neighbours are pterin/keto-reductases, and the natural bacterial quinone (menaquinone) is too large. "Pocket discriminates between classes" — supported in the sense that bulky benzil binds poorly and flat aromatics bind well, but an apo model cannot by itself name the physiological substrate.

## Limitations

Apo AlphaFold model; geometric (not energetic) sterics; kinetics taken from UniProt's curated annotation (full text not retrieved); methylglyoxal/sepiapterin untested; remote Foldseek hits; single characterization study underlies most wet-lab claims.


## Artifacts

- [OpenScientist candidate steric comparison](openscientist_artifacts/candidate_steric_comparison.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist go decision table](openscientist_artifacts/go_decision_table.csv)
- [OpenScientist kinetics table](openscientist_artifacts/kinetics_table.csv)
- [OpenScientist structural metrics](openscientist_artifacts/structural_metrics.csv)