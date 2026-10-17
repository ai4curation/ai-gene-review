---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-09T18:28:58.654117'
end_time: '2026-10-09T18:58:29.261669'
duration_seconds: 1770.61
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: IRC24
  gene_symbol: IRC24
  uniprot_accession: P40580
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae S288C
  focus_type: free_text
  hypothesis_slug: paralog-pocket-specificity-alphafold
  hypothesis_text: Irc24 (UniProt P40580) and its tandem paralog Nre1 (UniProt P40579)
    have diverged in substrate preference, and comparing the AlphaFold model of Irc24
    with the experimental Nre1 structures identifies the natural carbonyl substrate
    class that benzil is standing in for.
  term_context: '- Background the curator can state: both proteins are cytoplasmic
    short-chain dehydrogenase/reductases encoded 284 bp apart on chromosome IX and
    about 52 percent identical. Both reduce the synthetic diketone benzil in vitro
    with a roughly twofold preference for NADPH over NADH and with similar kinetics.
    GO obsoleted the benzil-specific term because benzil is not a physiologically
    relevant substrate, so the natural substrate of both enzymes is unknown.

    - Decide this with structural evidence. Retrieve the AlphaFold DB model for UniProt
    P40580 (https://alphafold.ebi.ac.uk/entry/P40580 ; mmCIF https://alphafold.ebi.ac.uk/files/AF-P40580-F1-model_v4.cif).
    Nre1 has experimental crystal structures under PDB 3KZV and 6UHX; use those as
    the comparison point rather than relying on sequence alignment alone.

    - The single decisive analysis: superpose the two structures, then compare their
    substrate-binding pockets residue by residue. Report pocket volume, shape and
    polarity for each, identify which pocket-lining positions differ between the paralogs,
    and state whether the differences predict divergent substrate preference or an
    essentially shared pocket. Reported kinetics are similar for benzil, so a shared
    pocket is a plausible and reportable outcome.

    - Then assess which natural substrate class either pocket best accommodates, comparing
    explicitly a flat fused quinone such as 1,4-naphthoquinone, a short aliphatic
    dicarbonyl such as methylglyoxal, a bulky diaryl diketone such as benzil itself,
    and a steroid or other ring carbonyl. Name the best-fitting class and the geometric
    reason.

    - Report per-residue pLDDT for the pocket and cofactor site and state whether
    model confidence supports the conclusion. Run Foldseek or an equivalent search
    against the PDB and AlphaFold DB and list the nearest structural neighbours with
    their annotated reactions and known substrates.

    - Name every tool and database version actually invoked and show the real output.
    If a tool cannot be run programmatically, say so plainly rather than substituting
    an inferred result for a computed one. An honest inconclusive answer is preferable
    to an overstated one.'
  reference_context: No specific reference context supplied.
  source_file: genes/yeast/IRC24/IRC24-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Irc24 (UniProt P40580) and its tandem paralog\
    \ Nre1 (UniProt P40579) have diverged in substrate\n  preference, and comparing\
    \ the AlphaFold model of Irc24 with the experimental Nre1 structures identifies\n\
    \  the natural carbonyl substrate class that benzil is standing in for.\nfocus_type:\
    \ free_text\ncontext:\n- 'Background the curator can state: both proteins are\
    \ cytoplasmic short-chain dehydrogenase/reductases\n  encoded 284 bp apart on\
    \ chromosome IX and about 52 percent identical. Both reduce the synthetic diketone\n\
    \  benzil in vitro with a roughly twofold preference for NADPH over NADH and with\
    \ similar kinetics. GO\n  obsoleted the benzil-specific term because benzil is\
    \ not a physiologically relevant substrate, so the\n  natural substrate of both\
    \ enzymes is unknown.'\n- Decide this with structural evidence. Retrieve the AlphaFold\
    \ DB model for UniProt P40580 (https://alphafold.ebi.ac.uk/entry/P40580\n  ; mmCIF\
    \ https://alphafold.ebi.ac.uk/files/AF-P40580-F1-model_v4.cif). Nre1 has experimental\
    \ crystal\n  structures under PDB 3KZV and 6UHX; use those as the comparison point\
    \ rather than relying on sequence\n  alignment alone.\n- 'The single decisive\
    \ analysis: superpose the two structures, then compare their substrate-binding\
    \ pockets\n  residue by residue. Report pocket volume, shape and polarity for\
    \ each, identify which pocket-lining\n  positions differ between the paralogs,\
    \ and state whether the differences predict divergent substrate\n  preference\
    \ or an essentially shared pocket. Reported kinetics are similar for benzil, so\
    \ a shared pocket\n  is a plausible and reportable outcome.'\n- Then assess which\
    \ natural substrate class either pocket best accommodates, comparing explicitly\
    \ a flat\n  fused quinone such as 1,4-naphthoquinone, a short aliphatic dicarbonyl\
    \ such as methylglyoxal, a bulky\n  diaryl diketone such as benzil itself, and\
    \ a steroid or other ring carbonyl. Name the best-fitting class\n  and the geometric\
    \ reason.\n- Report per-residue pLDDT for the pocket and cofactor site and state\
    \ whether model confidence supports\n  the conclusion. Run Foldseek or an equivalent\
    \ search against the PDB and AlphaFold DB and list the nearest\n  structural neighbours\
    \ with their annotated reactions and known substrates.\n- Name every tool and\
    \ database version actually invoked and show the real output. If a tool cannot\
    \ be\n  run programmatically, say so plainly rather than substituting an inferred\
    \ result for a computed one.\n  An honest inconclusive answer is preferable to\
    \ an overstated one.\nreference_id: []"
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
artifact_count: 7
artifact_sources:
  openscientist_artifacts_zip: 7
artifacts:
- filename: data_AF-P40579-F1-confidence_v6.json
  path: openscientist_artifacts/data_AF-P40579-F1-confidence_v6.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist AF P40579 F1 confidence v6
- filename: data_AF-P40580-F1-confidence_v6.json
  path: openscientist_artifacts/data_AF-P40580-F1-confidence_v6.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist AF P40580 F1 confidence v6
- filename: data_AF-P40580-F1-predicted_aligned_error_v6.json
  path: openscientist_artifacts/data_AF-P40580-F1-predicted_aligned_error_v6.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist AF P40580 F1 predicted aligned error v6
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
- filename: provenance_go_decision_and_evidence_matrix.csv
  path: openscientist_artifacts/provenance_go_decision_and_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go decision and evidence matrix
- filename: provenance_irc24_nre1_structural_analysis.md
  path: openscientist_artifacts/provenance_irc24_nre1_structural_analysis.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist irc24 nre1 structural analysis
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** yeast
- **Taxon:** Saccharomyces cerevisiae S288C (NCBITaxon:559292)
- **Gene directory:** IRC24
- **Gene symbol:** IRC24
- **UniProt accession:** P40580

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** paralog-pocket-specificity-alphafold
- **Source file:** genes/yeast/IRC24/IRC24-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Irc24 (UniProt P40580) and its tandem paralog Nre1 (UniProt P40579) have diverged in substrate preference, and comparing the AlphaFold model of Irc24 with the experimental Nre1 structures identifies the natural carbonyl substrate class that benzil is standing in for.

## Term and Decision Context

- Background the curator can state: both proteins are cytoplasmic short-chain dehydrogenase/reductases encoded 284 bp apart on chromosome IX and about 52 percent identical. Both reduce the synthetic diketone benzil in vitro with a roughly twofold preference for NADPH over NADH and with similar kinetics. GO obsoleted the benzil-specific term because benzil is not a physiologically relevant substrate, so the natural substrate of both enzymes is unknown.
- Decide this with structural evidence. Retrieve the AlphaFold DB model for UniProt P40580 (https://alphafold.ebi.ac.uk/entry/P40580 ; mmCIF https://alphafold.ebi.ac.uk/files/AF-P40580-F1-model_v4.cif). Nre1 has experimental crystal structures under PDB 3KZV and 6UHX; use those as the comparison point rather than relying on sequence alignment alone.
- The single decisive analysis: superpose the two structures, then compare their substrate-binding pockets residue by residue. Report pocket volume, shape and polarity for each, identify which pocket-lining positions differ between the paralogs, and state whether the differences predict divergent substrate preference or an essentially shared pocket. Reported kinetics are similar for benzil, so a shared pocket is a plausible and reportable outcome.
- Then assess which natural substrate class either pocket best accommodates, comparing explicitly a flat fused quinone such as 1,4-naphthoquinone, a short aliphatic dicarbonyl such as methylglyoxal, a bulky diaryl diketone such as benzil itself, and a steroid or other ring carbonyl. Name the best-fitting class and the geometric reason.
- Report per-residue pLDDT for the pocket and cofactor site and state whether model confidence supports the conclusion. Run Foldseek or an equivalent search against the PDB and AlphaFold DB and list the nearest structural neighbours with their annotated reactions and known substrates.
- Name every tool and database version actually invoked and show the real output. If a tool cannot be run programmatically, say so plainly rather than substituting an inferred result for a computed one. An honest inconclusive answer is preferable to an overstated one.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Irc24 (UniProt P40580) and its tandem paralog Nre1 (UniProt P40579) have diverged in substrate
  preference, and comparing the AlphaFold model of Irc24 with the experimental Nre1 structures identifies
  the natural carbonyl substrate class that benzil is standing in for.
focus_type: free_text
context:
- 'Background the curator can state: both proteins are cytoplasmic short-chain dehydrogenase/reductases
  encoded 284 bp apart on chromosome IX and about 52 percent identical. Both reduce the synthetic diketone
  benzil in vitro with a roughly twofold preference for NADPH over NADH and with similar kinetics. GO
  obsoleted the benzil-specific term because benzil is not a physiologically relevant substrate, so the
  natural substrate of both enzymes is unknown.'
- Decide this with structural evidence. Retrieve the AlphaFold DB model for UniProt P40580 (https://alphafold.ebi.ac.uk/entry/P40580
  ; mmCIF https://alphafold.ebi.ac.uk/files/AF-P40580-F1-model_v4.cif). Nre1 has experimental crystal
  structures under PDB 3KZV and 6UHX; use those as the comparison point rather than relying on sequence
  alignment alone.
- 'The single decisive analysis: superpose the two structures, then compare their substrate-binding pockets
  residue by residue. Report pocket volume, shape and polarity for each, identify which pocket-lining
  positions differ between the paralogs, and state whether the differences predict divergent substrate
  preference or an essentially shared pocket. Reported kinetics are similar for benzil, so a shared pocket
  is a plausible and reportable outcome.'
- Then assess which natural substrate class either pocket best accommodates, comparing explicitly a flat
  fused quinone such as 1,4-naphthoquinone, a short aliphatic dicarbonyl such as methylglyoxal, a bulky
  diaryl diketone such as benzil itself, and a steroid or other ring carbonyl. Name the best-fitting class
  and the geometric reason.
- Report per-residue pLDDT for the pocket and cofactor site and state whether model confidence supports
  the conclusion. Run Foldseek or an equivalent search against the PDB and AlphaFold DB and list the nearest
  structural neighbours with their annotated reactions and known substrates.
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

# IRC24 (P40580) vs Nre1 (P40579): Paralog Pocket Specificity — Curator Report

**Gene:** IRC24 / YIR036C, *Saccharomyces cerevisiae* S288C (NCBITaxon:559292); UniProt **P40580** ("Benzil reductase ((S)-benzoin forming) IRC24", BZRD_YEAST).
**Paralog:** Nre1 / YIR035C; UniProt **P40579** (uncharacterized oxidoreductase).
**Hypothesis slug:** paralog-pocket-specificity-alphafold.
**Focus type:** free_text.

---

## Executive Judgment

**Verdict: Partially supported — with the two halves of the seed hypothesis landing differently.**

1. **"The paralogs have *diverged* in substrate preference" → REFUTED by the structural evidence.** The AlphaFold Irc24 model and the experimental Nre1 crystal structure superpose at **1.36 Å CA RMSD**, and the substrate pocket is **more conserved than the protein overall (15/18 residues identical, 83%)** with a strictly conserved catalytic Ser–Tyr–Lys triad. This "essentially shared pocket" is exactly the outcome the seed flagged as plausible given the near-identical benzil kinetics, and it is what the data show. The only hint of divergence is subtle: Irc24's pocket is slightly more hydrophobic (loss of the Nre1 Asp138 carboxylate; Irc24 65% vs Nre1 50% hydrophobic lining), a second-shell change unlikely to constitute a specificity switch.

2. **"Comparing the structures *identifies the natural substrate class*" → PARTIALLY RESOLVED (narrowed, not named).** Structure + Foldseek constrain the chemistry but cannot name a single physiological substrate. A genuine Foldseek run shows every nearest neighbour with a known substrate reduces a **ring/cyclic carbonyl** (diaryl diketone, bicyclic alkaloid, pterin, alicyclic ketone, steroid); **no aliphatic-dicarbonyl (methylglyoxal-type) reductase** appears. Of the four options the seed asked us to rank, **methylglyoxal is the least supported**, and a **flat/fused aromatic ring carbonyl (e.g., a quinone such as 1,4-naphthoquinone)** or another ring carbonyl is the best geometric fit for the large, predominantly hydrophobic, aromatic-lined pocket. This is **inference from pocket properties + neighbour annotations, not a docking calculation**; no substrate-bound structure of either paralog exists.

**Most important caveats.** (a) There is **no experimental structure of Irc24 itself** — all Irc24 geometry is AlphaFold v6 (mean pLDDT 96.4; pocket pLDDT 93.6–98.8, so confidence is not the limiting factor). (b) **Neither Nre1 structure contains a substrate** (3KZV is apo + glycerol; 6UHX holds only NADP), so the pocket is inferred from the cofactor site and fold. (c) The closest *natural-substrate* homologs (sepiapterin reductase, tropinone reductase) act on substrates **yeast does not make**, so homology transfer of a specific substrate is unsafe. An honest answer is: the structure cannot upgrade the annotation from "carbonyl reductase (NADPH)" to a specific physiological substrate.

---

## Evidence Matrix

| # | Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | In-session computation (numpy NW-BLOSUM62 + Kabsch); AlphaFold DB AF-P40580-F1 **v6**; RCSB **6UHX** | structural/computational | **Refutes** "diverged pocket" | Do Irc24 and Nre1 pockets differ? | 53.4% global identity; **1.36 Å** CA RMSD; pocket **15/18 identical**; Ser–Tyr–Lys triad conserved | Yeast SDR; AF model vs 2.75 Å crystal | High for "shared pocket"; AF model (no Irc24 crystal); no bound substrate |
| 2 | In-session Foldseek web server (3diaa; afdb-swissprot/afdb50/pdb100) | structural/evolutionary | **Qualifies** substrate class | Which substrate class fits? | Neighbours = benzil reductase (6YC8 KRED1-Pglu), tropinone reductase, sepiapterin reductase, 17β-HSD14, cyclo(pent/hex)anol DH; **no methylglyoxal reductase** | Query = Irc24 AF v6 | High that neighbours are ring-carbonyl SDRs; annotation-transfer ≠ proof of yeast substrate |
| 3 | PMID **11796169** (Maruyama 2002) | direct assay | **Supports** core MF | Is YIR036C a benzil reductase? | "yeast YIR036C protein … also reduced benzil to (S)-benzoin in vitro"; SDR related to sepiapterin reductases | *S. cerevisiae* ORF, recombinant, NADPH | Direct in-vitro; benzil is synthetic/non-physiological |
| 4 | PMID **33486371** (Rabuffetti 2021) | direct assay + structure | **Qualifies** substrate class | What do benzil reductases prefer? | "Benzil reductases are dehydrogenases preferentially active on aromatic 1,2-diketones"; crystal 6YC8, prefers bulky aromatic substrates | *Pichia glucozyma* KRED1-Pglu, 1.77 Å | Closest characterized functional analog; different organism |
| 5 | PMID **26377422 / 26952764** (Contente 2015/2016) | direct assay | **Qualifies** | Pocket accommodates bulky aromatics? | KRED1-Pglu "prefers space-demanding substrates"; orientation in binding pocket sets stereochemistry | Pichia benzil reductase | Supports large hydrophobic aromatic pocket |
| 6 | PMID **11745140** (Maruyama 2001) | sequence/evolutionary | **Supports** SDR family | Family placement | Benzil reductase is "a novel short-chain dehydrogenases/reductase"; homology to YIR036C and sepiapterin reductases | *B. cereus* gene | Orientation-level family evidence |
| 7 | RCSB **3KZV** (apo) & **6UHX** (NADP) headers; in-session HETATM scan | structural | **Qualifies** (negative) | Is a substrate crystallized? | 3KZV: only glycerol+water; 6UHX: only NADP — **no substrate in any structure** | Nre1 crystals, 2.0 / 2.75 Å | Hard limit on naming a substrate from structure |

---

## GO Curation Implications (leads — require curator verification)

**Molecular Function (MF).** Evidence supports a **retained but generalized** MF. The obsoleted benzil-specific term was correctly removed (benzil is synthetic). The defensible computed/experimental MF is a **carbonyl/ketone reductase, NADPH-dependent** activity:
- Candidate MF: **GO:0004090 carbonyl reductase (NADPH) activity** (or the NADP-oxidoreductase parent GO:0016616 "oxidoreductase activity, acting on the CH-OH group of donors, NAD(P) as acceptor"), with evidence code **IDA** (PMID 11796169, in-vitro benzil reduction) for the activity and **ISS/ISA** for the structural class. The structure does **not** justify a more specific substrate term (e.g., a quinone- or steroid-specific MF) — do **not** add one as asserted.
- Avoid "protein binding" — a specific oxidoreductase MF is supported.

**Biological Process (BP).** No BP is supported by direct evidence. The "IRC24 = increased recombination centers" gene name derives from a **loss-of-function screen phenotype**, a downstream/pleiotropic readout, not the molecular function; do not annotate a DNA-repair/recombination BP from the enzymatic data. Leave BP **unknown / non-core** pending a physiological substrate.

**Cellular Component (CC).** **Cytoplasm** (GO:0005737) is consistent with both paralogs being soluble cytoplasmic SDRs (3KZV titled a "cytoplasmic protein"); retain if already supported by localization evidence.

**Paralog note for the curator:** because the pocket is ~83% identical and the fold is near-identical, any substrate/function annotation transferred to one paralog should be **applied symmetrically or flagged**, and benzil-reductase annotations on either gene should carry a "non-physiological substrate" qualifier.

---

## Mechanistic Scope

- **Direct molecular activity (what the structure tests):** NADPH-dependent reduction of a carbonyl (ketone/diketone) at the SDR catalytic centre (Tyr157/Ser143/Lys161 in Irc24), with the substrate carbonyl positioned over the nicotinamide C4 of NADP. This is the gene product's primary biochemical function.
- **Not direct / out of scope:** the "increased recombination centers" phenotype (loss-of-function, pleiotropic), any genome-stability role, and any specific physiological pathway — none are established and none follow from the enzymology.

---

## Conflicts and Alternatives

- **Against "diverged specificity":** identical fold, 83%-identical pocket, conserved catalytic triad, indistinguishable cavity volume, and the reported near-identical benzil kinetics all point to a **shared** pocket. The seed's primary framing (divergence) is contradicted.
- **Paralog/annotation carry-over risk:** P40580 is annotated "benzil reductase" in UniProt while P40579 is "uncharacterized"; given 52% identity and a shared pocket, this asymmetry is likely annotation history, not biology. Curators should treat benzil activity as a **shared, in-vitro, non-physiological** property.
- **Homology trap:** nearest natural-substrate neighbours (sepiapterin reductase → tetrahydrobiopterin pathway; tropinone reductase → plant alkaloids; 17β-HSD14 → steroids) have **no substrate counterpart in *S. cerevisiae***, so their annotations cannot be transferred as the yeast substrate.
- **Alternative substrate hypotheses not excluded:** a **quinone** (e.g., 1,4-naphthoquinone; fits a flat hydrophobic aromatic pocket and is chemically plausible for oxidative-stress/quinone handling) is the best geometric match among the four options, but this is **not proven**; a broader "ring carbonyl" class remains open.

---

## Knowledge Gaps

1. **No physiological substrate identified.** Checked: structure (no bound substrate in 3KZV/6UHX), Foldseek neighbours (all exogenous or non-yeast substrates), literature (only benzil assayed for the yeast protein). Matters because GO MF specificity and any BP depend on it. Resolve with substrate screening (see below).
2. **No Irc24 experimental structure.** Checked: AlphaFold v6 only (high confidence, pLDDT ~96). Matters marginally — confidence is high — but a crystal or a substrate co-complex would settle pocket geometry and the Asp138→Gly145 effect.
3. **Functional consequence of the Nre1 Asp138 / Irc24 Gly145 difference.** Checked: it is the single non-conservative near-pocket change (4.8 Å, second shell). Matters only if the paralogs are subtly specialized. Resolve by reciprocal point-mutant kinetics.
4. **Quantitative pocket volume/druggability.** Checked only with a crude grid (relative comparison valid, absolute unreliable); fpocket/CASTp/SiteMap were not run. Resolve with a dedicated cavity tool for a defensible volume and a docking panel (naphthoquinone vs methylglyoxal vs benzil vs a steroid).

---

## Discriminating Tests

1. **Substrate panel kinetics** on recombinant Irc24 **and** Nre1 in parallel: 1,4-naphthoquinone and other quinones (menadione, juglone), methylglyoxal, a model steroid/ring ketone, vs benzil — measure k_cat/K_M and NADPH vs NADH. This directly tests "shared vs diverged" and names the preferred class.
2. **Co-crystal or cryo-soak** of Nre1 (or Irc24) with a candidate substrate + NADP(H) to define the real pocket.
3. **Reciprocal mutants** Irc24 G145D and Nre1 D138G; assay for any substrate-preference shift.
4. **Dedicated pocket/docking analysis** (fpocket/CASTp + AutoDock Vina) on the AlphaFold Irc24 model with the four candidate ligands for a computed ranking to replace the current inference.
5. **Genetics/metabolomics:** irc24Δ nre1Δ (single and double) metabolite profiling and quinone/oxidative-stress sensitivity, to connect the enzyme to a pathway.

---

## Curation Leads (require curator verification)

- **Action on the review:** Treat the seed's "diverged substrate preference" claim as **not supported**; record the computed "shared pocket" result instead. Treat "identifies the natural substrate class" as **narrowed, not resolved** (ring/fused-ring carbonyl favoured; methylglyoxal disfavoured).
- **Candidate MF term:** **GO:0004090 (carbonyl reductase (NADPH) activity)** or the generalized NAD(P) CH-OH oxidoreductase parent — IDA from PMID 11796169; keep a "benzil = non-physiological substrate" note. Do **not** assert a quinone/steroid-specific MF.
- **BP/CC:** BP **unknown** (do not infer recombination/DNA-repair from the gene name); CC **cytoplasm** if localization-supported.
- **Candidate references + exact snippets to verify:**
  - PMID 11796169 — "We isolated the genes encoding yeast YIR036C protein and gerbil sepiapterin reductase, and both recombinant proteins also reduced benzil to (S)-benzoin in vitro."
  - PMID 33486371 — "Benzil reductases are dehydrogenases preferentially active on aromatic 1,2-diketones."
- **Suggested curator questions:** Is there localization evidence for P40580/P40579? Is the benzil annotation on P40580 experimental (IDA) or transferred? Should P40579 receive the same generalized carbonyl-reductase MF given the shared pocket?
- **Suggested experiments:** the substrate panel and reciprocal-mutant kinetics above.

---

## Tools and database versions actually invoked (with honest limitations)

- **AlphaFold DB** REST API + file server, model **AF-P40580-F1 v6** (modelCreatedDate 2025-08-01; AlphaFold Monomer v2.0 pipeline; globalMetric/mean pLDDT 96.38) and **AF-P40579-F1 v6** (96.62). *Note: the seed referenced v4; the current release is v6.*
- **RCSB PDB** coordinate files **3KZV** (2.00 Å, apo) and **6UHX** (2.75 Å, +NADP).
- **In-session Python (numpy)** for parsing, Needleman–Wunsch (BLOSUM62), Kabsch superposition, pocket detection, crude cavity grid, polarity. **Biopython and Phenix were not applied to the Irc24 model**: the code-executor sandbox is ephemeral and cannot share files with the Phenix-tool environment, and Biopython is not an allowed import there. (RCSB PDBs are staged in the job `data/` dir if a curator wishes to run `phenix.molprobity`/`phenix.superpose_pdbs` on the experimental structures.) The absolute cavity volume is an overestimate from a permissive enclosure criterion and is reported only as a **relative** paralog comparison.
- **Foldseek web server** (search.foldseek.com API, mode 3diaa; databases afdb-swissprot, afdb50, pdb100) — real output reproduced in `provenance/irc24_nre1_structural_analysis.md`.
- **PubMed** via search_pubmed.

Provenance (computed metrics, full per-residue pocket table with pLDDT, and the Foldseek hit list) is saved to **`provenance/irc24_nre1_structural_analysis.md`**.


## Artifacts

- [OpenScientist AF P40579 F1 confidence v6](openscientist_artifacts/data_AF-P40579-F1-confidence_v6.json)
- [OpenScientist AF P40580 F1 confidence v6](openscientist_artifacts/data_AF-P40580-F1-confidence_v6.json)
- [OpenScientist AF P40580 F1 predicted aligned error v6](openscientist_artifacts/data_AF-P40580-F1-predicted_aligned_error_v6.json)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist go decision and evidence matrix](openscientist_artifacts/provenance_go_decision_and_evidence_matrix.csv)
- [OpenScientist irc24 nre1 structural analysis](openscientist_artifacts/provenance_irc24_nre1_structural_analysis.md)