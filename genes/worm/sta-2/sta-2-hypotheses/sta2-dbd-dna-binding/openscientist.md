---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-04T18:37:37.633156'
end_time: '2026-10-04T18:56:01.710963'
duration_seconds: 1104.08
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: worm
  gene: sta-2
  gene_symbol: sta-2
  uniprot_accession: Q20977
  taxon_id: NCBITaxon:6239
  taxon_label: Caenorhabditis elegans
  focus_type: function_assignment
  hypothesis_slug: sta2-dbd-dna-binding
  hypothesis_text: 'C. elegans STA-2 (UniProt Q20977) retains a functional STAT DNA-binding
    domain capable of sequence-specific DNA binding. Test this with one decisive structural
    analysis: align the STA-2 DNA-binding-domain region to human STAT1/STAT3, Drosophila
    Stat92E and C. elegans STA-1 (Q9NAD6, which binds DNA in ChIP-seq, as a nematode
    positive control), assess conservation of the DNA-contacting residues seen in
    the DNA-bound STAT1 structure (PDB 1BF5), and compare the AlphaFold model of STA-2
    to that fold.'
  term_context: '- Term: RNA polymerase II cis-regulatory region sequence-specific
    DNA binding (GO:0000978)'
  reference_context: No specific reference context supplied.
  source_file: genes/worm/sta-2/sta-2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'C. elegans STA-2 (UniProt Q20977) retains a functional\
    \ STAT DNA-binding domain capable of\n  sequence-specific DNA binding. Test this\
    \ with one decisive structural analysis: align the STA-2 DNA-binding-domain\n\
    \  region to human STAT1/STAT3, Drosophila Stat92E and C. elegans STA-1 (Q9NAD6,\
    \ which binds DNA in ChIP-seq,\n  as a nematode positive control), assess conservation\
    \ of the DNA-contacting residues seen in the DNA-bound\n  STAT1 structure (PDB\
    \ 1BF5), and compare the AlphaFold model of STA-2 to that fold.'\nfocus_type:\
    \ function_assignment\nterm_id: GO:0000978\nterm_label: RNA polymerase II cis-regulatory\
    \ region sequence-specific DNA binding\ncontext: []\nreference_id: []"
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
citation_count: 3
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
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
- filename: provenance_sta2_dbd_comparison_table.csv
  path: openscientist_artifacts/provenance_sta2_dbd_comparison_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist sta2 dbd comparison table
- filename: provenance_sta2_evidence_matrix.csv
  path: openscientist_artifacts/provenance_sta2_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist sta2 evidence matrix
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** worm
- **Taxon:** Caenorhabditis elegans (NCBITaxon:6239)
- **Gene directory:** sta-2
- **Gene symbol:** sta-2
- **UniProt accession:** Q20977

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** sta2-dbd-dna-binding
- **Source file:** genes/worm/sta-2/sta-2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

C. elegans STA-2 (UniProt Q20977) retains a functional STAT DNA-binding domain capable of sequence-specific DNA binding. Test this with one decisive structural analysis: align the STA-2 DNA-binding-domain region to human STAT1/STAT3, Drosophila Stat92E and C. elegans STA-1 (Q9NAD6, which binds DNA in ChIP-seq, as a nematode positive control), assess conservation of the DNA-contacting residues seen in the DNA-bound STAT1 structure (PDB 1BF5), and compare the AlphaFold model of STA-2 to that fold.

## Term and Decision Context

- Term: RNA polymerase II cis-regulatory region sequence-specific DNA binding (GO:0000978)

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'C. elegans STA-2 (UniProt Q20977) retains a functional STAT DNA-binding domain capable of
  sequence-specific DNA binding. Test this with one decisive structural analysis: align the STA-2 DNA-binding-domain
  region to human STAT1/STAT3, Drosophila Stat92E and C. elegans STA-1 (Q9NAD6, which binds DNA in ChIP-seq,
  as a nematode positive control), assess conservation of the DNA-contacting residues seen in the DNA-bound
  STAT1 structure (PDB 1BF5), and compare the AlphaFold model of STA-2 to that fold.'
focus_type: function_assignment
term_id: GO:0000978
term_label: RNA polymerase II cis-regulatory region sequence-specific DNA binding
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

# AIGR Gene Hypothesis Deep Research — C. elegans STA-2 (UniProt Q20977)

**Focus:** function_assignment · Hypothesis slug `sta2-dbd-dna-binding`
**Term under test:** GO:0000978 — *RNA polymerase II cis-regulatory region sequence-specific DNA binding*
**Source:** `genes/worm/sta-2/sta-2-ai-review.yaml` (free-text)

---

## Executive Judgment

**Verdict: Partially supported — the STAT fold is retained, but functional sequence-specific DNA binding (GO:0000978) is NOT supported (likely homology-driven over-annotation).**

The seed hypothesis has two separable claims. The first — that STA-2 *retains a STAT DNA-binding-domain fold* — is **supported**. The second — that this fold is *capable of sequence-specific DNA binding* and therefore justifies GO:0000978 — is **unresolved-to-refuted** on the available evidence and should be treated conservatively by curators.

Structurally, the AlphaFold model of STA-2 (AF-Q20977-F1) reproduces the STAT DBD fold with high confidence (mean pLDDT ≈ 88 over the DBD region), and its DBD-region backbone deviates from the DNA-bound human STAT1 crystal (PDB 1BF5) by essentially the same amount (8.2 Å) as the ChIP-validated nematode binder STA-1 (8.0 Å). So the *scaffold* is present. However, every sequence-level and functional test points away from autonomous sequence-specific DNA binding: STA-2 is the **most divergent** STAT examined (only ~20% DBD identity to STAT1), it **uniquely fails** the Pfam STAT-DBD profile HMM (PF02864) that human STAT1, Drosophila Stat92E and C. elegans STA-1 all pass, it **conserves none** of the three base-contacting (sequence-specificity-determining) residues of STAT1 (E421, S459, N460), and it **lacks the canonical activating tyrosine** (STAT1 Y701) required for the phospho-dimerization that drives high-affinity STAT–DNA binding. No direct DNA-binding assay (EMSA, ChIP-seq, or defined consensus motif) exists for STA-2 in the primary literature; its function as a transcriptional activator of epidermal antimicrobial peptide (AMP) genes is established genetically and by localization, and it physically partners with the SLC6 transporter SNF-12 in an explicitly "unorthodox" mode of STAT regulation.

**Most important caveats:** (1) Fold conservation does not establish DNA-binding chemistry — it is necessary but not sufficient. (2) The absence of a direct binding assay is an *absence of evidence*, not proof of no binding; STA-2 could bind DNA in a partner-assisted or low-specificity manner. (3) The rigid-body RMSD values are crude (no outlier trimming) and should be read comparatively, not absolutely. The appropriate curation posture is to treat GO:0000978 on STA-2 as a homology-propagated prediction that is **less precise than the direct experimental knowledge** (nuclear transcriptional-activator role + SNF-12 interaction) and to generalize or remove it pending a direct assay.

---

## Key Findings

### F001 — STA-2 lacks the Pfam STAT DNA-binding-domain HMM that its DNA-binding paralog STA-1 retains

An InterPro/Pfam domain scan cleanly separates STA-2 from the canonical STATs and from its own nematode paralog. Human STAT1 (P42224), Drosophila Stat92E (Q24151) and C. elegans **STA-1 (Q9NAD6)** all match **Pfam PF02864 "STAT protein, DNA binding domain"** (STA-1 at residues 204–356; also the CDD cd14801 STAT-DBD model). **C. elegans STA-2 (Q20977) does NOT match PF02864** or the STAT-DBD CDD model. STA-2 hits only the weaker *fold-level* superfamilies — IPR008967 (p53-like transcription-factor DNA-binding superfamily, 164–443) and IPR012345 (STAT DNA-binding N-terminal superfamily, 167–313) — while retaining a clear SH2 domain (cd09919/PS50001, 449–526) and a divergent STAT-b N-terminal domain (PF24629, 27–163). STA-2 is additionally N-terminally truncated (567 aa versus 706–770 aa for canonical STATs) and lacks the coiled-coil (PF01017) and N-terminal interaction (PF02865) domains present in canonical STATs.

The interpretation is pivotal: a profile HMM like PF02864 is tuned to the conserved residues that *define* a functional STAT DBD. The fact that the ChIP-validated binder STA-1 passes it while STA-2 fails it — within the same organism and the same gene family — is a strong, discriminating signal that STA-2's DBD has diverged beyond the family's functional consensus, even though a fold-level signal persists.

### F002 — STA-2 conserves the STAT DBD fold (AlphaFold pLDDT ≈ 88) but not the DNA-contacting residues of STAT1

Structural contact mapping on the DNA-bound STAT1 crystal (PDB **1BF5**) identified **16 STAT1 residues within 3.6 Å of DNA**, of which **3 make base-specific (sequence-reading) contacts: E421, S459, N460**. Pairwise Needleman–Wunsch (BLOSUM62) alignment of STAT1 to each ortholog, mapped onto these positions, gives a clear gradient of conservation:

| Protein | Base-contacting (of 3) identical | BLOSUM-similar | All DNA-contacting (of 16) identical | DBD-region identity (STAT1 320–490) |
|---|---|---|---|---|
| Human STAT3 | 2/3 | 3/3 | 11/16 | 66% |
| Drosophila Stat92E | 1/3 (E421 conserved) | — | 5/16 | 30% |
| C. elegans STA-1 (ChIP+ control) | 0/3 | 1/3 | 4/16 | 26% |
| **C. elegans STA-2** | **0/3** | **0/3** (E421→S, S459→G, N460→P) | **3/16** | **20% (most divergent)** |

STA-2 is the most divergent protein on every metric and uniquely loses *all* base-contacting residues with no conservative substitution (E421→S, S459→G, N460→P — charge/shape-disruptive changes at exactly the positions that read DNA sequence). Notably, even the positive-control binder STA-1 conserves 0/3 base-contacting residues identically — a reminder that nematode STATs read DNA through a diverged interface and that residue-identity at human positions is an imperfect proxy. The distinguishing feature for STA-2 is therefore the **combination** of (a) failing PF02864, (b) losing all base contacts without conservative substitution, and (c) being the overall most divergent DBD.

Despite this sequence divergence, AlphaFold (AF-Q20977-F1, v6) predicts the STA-2 DBD-region fold with high confidence: **mean pLDDT 88.1 over residues 164–443** (90% of residues > 70), comparable to the STA-1 DBD (81.4) and to STA-2's own SH2 domain (95.0). The scaffold is intact; the DNA-reading chemistry is not conserved.

### F003 — STA-2 is a transcriptional activator of epidermal antimicrobial-peptide genes, but direct sequence-specific DNA binding is not demonstrated

Primary literature firmly establishes STA-2 as a STAT-like transcription factor controlling C. elegans epidermal antimicrobial peptide (AMP; e.g. *nlp-29*) gene expression — but always through genetics, localization, and target-gene readouts, never through a direct DNA-binding assay. Zhang et al. 2015 ([PMID: 25692704](https://pubmed.ncbi.nlm.nih.gov/25692704/)) show STA-2 is tethered to apical hemidesmosomes and that architectural damage causes *"detachment of STA-2 molecules from hemidesmosomes and transcription of AMPs,"* with STA-2 release inducing an innate immune response. Zhang et al. 2021 ([PMID: 34166401](https://pubmed.ncbi.nlm.nih.gov/34166401/)) describe fungal effectors that act by *"preventing the key STAT-like transcription factor STA-2 from activating defensive antimicrobial peptide gene expression,"* and report that one effector increases STA-2 levels in the nucleus.

Crucially, none of these studies report an EMSA, ChIP-seq, or a defined sequence motif for STA-2. The transcriptional-activator role is *inferred* from genetic epistasis, nuclear localization, and downstream target expression. The seed hypothesis itself uses STA-1 ChIP-seq as the "nematode positive control" for DNA binding — implicitly conceding that equivalent direct DNA-binding data for STA-2 do not exist.

### F004 — STA-2 lacks the canonical STAT activating tyrosine (STAT1 Y701) and shows DBD backbone deviation equal to the binding control STA-1

Global BLOSUM62 alignment of STAT1 to each nematode STAT shows that the canonical C-terminal **activating tyrosine STAT1-Y701** — phosphorylated to drive STAT dimerization and high-affinity, sequence-specific DNA binding — aligns to a conserved tyrosine in STA-1 (Tyr588) but has **NO aligned residue in STA-2** (it maps to a gap at the STA-2 C-terminus; STA-2 is truncated at 567 aa, just past its SH2 domain at 449–526). Loss of the phospho-tyrosine switch removes the canonical mechanism by which STATs achieve the stable, reciprocal SH2–phosphotyrosine dimer that clamps onto DNA. This is mechanistically consistent with the "unorthodox" regulation described below.

Alignment-anchored Cα superposition of the STAT1 DBD (Pfam region 322–458, PDB 1BF5 chain A) onto the AlphaFold models gives **STA-2 Kabsch RMSD = 8.22 Å over 126 residue pairs** versus **STA-1 = 8.00 Å over 127 pairs** — essentially identical backbone deviation. (These are crude rigid-body RMSDs without outlier trimming and should be read comparatively: STA-2's fold is no more deviant than the binding-competent STA-1's.) The structural scaffold similarity therefore cannot discriminate binders from non-binders here; the discriminating information lies in the sequence/residue-level and functional data.

### F005 — STA-2 is an unorthodox STAT that acts with the SLC6 transporter SNF-12; its DNA engagement may be partner-assisted

Dierking et al. 2011 ([PMID: 21575913](https://pubmed.ncbi.nlm.nih.gov/21575913/)) identify the SLC6/solute-carrier transporter **SNF-12** as essential for epidermal AMP induction and show *"the STAT transcription factor-like protein STA-2 as a direct physical interactor of SNF-12,"* with the two proteins *"function[ing] together to regulate AMP gene expression in the epidermis."* The authors explicitly state their findings *"reveal an unorthodox mode of regulation for a STAT factor."* No DNA-binding assay, consensus motif, or ChIP for STA-2 is reported.

Combined with the structural findings — no activating tyrosine, a degenerate DBD that fails PF02864, and loss of all three STAT1 base-contacting residues — this supports a model in which STA-2's transcriptional output is achieved **non-canonically and possibly via protein partners** rather than, or in addition to, autonomous sequence-specific DNA binding.

---

## Mechanistic Model / Interpretation

The evidence converges on STA-2 as a **degenerate / unorthodox STAT** that has retained the STAT architecture as a scaffold while losing the canonical features that make a STAT an autonomous sequence-specific DNA-binding transcription factor.

```
 Canonical STAT (human STAT1)            C. elegans STA-2 (Q20977)
 ============================            ==========================
 N-domain + coiled-coil (PF01017,        [ABSENT]  N-terminally truncated
   PF02865)                                 (567 aa vs ~706-770 aa)
        |                                       |
 DNA-binding domain (PF02864) ----DNA     STAT-DBD FOLD present (pLDDT~88,
   base contacts E421/S459/N460            IPR008967/IPR012345) BUT:
   reads GAS/ISRE motif                     - FAILS Pfam PF02864
        |                                    - 0/3 base contacts conserved
 Linker + SH2 domain                        - most divergent DBD (20% id)
        |                                       |
 Activating Tyr (Y701) --(P)--> dimer    SH2 domain present (cd09919)
   -> high-affinity DNA binding          Activating Tyr ABSENT (truncated)
                                              |
                                          Partners with SNF-12 (SLC6)
                                          tethered at hemidesmosomes;
                                          released on damage -> nucleus
                                          -> AMP gene activation
                                          ("unorthodox" STAT regulation)
```

The functional output (activation of epidermal AMP genes such as *nlp-29*) is genetically real and important for innate immunity, but the *immediate molecular mechanism* by which STA-2 engages chromatin is not established. Three mechanistic possibilities remain open and are not mutually exclusive:

1. **Partner-assisted / tethered DNA engagement** — STA-2 may be recruited to target promoters via SNF-12 or other partners rather than by autonomous sequence reading (most consistent with F001–F005).
2. **Low-specificity or diverged-motif binding** — the retained fold could still contact DNA, but with a motif unlike the mammalian GAS/ISRE and not captured by human-residue conservation metrics (STA-1 also conserves 0/3 human base contacts yet binds DNA).
3. **Non-DNA-binding co-activator role** — STA-2 could act primarily through protein–protein interactions in a transcriptional complex.

For GO curation, the key point is that **GO:0000978 asserts a specific molecular activity (RNA Pol II cis-regulatory region sequence-specific DNA binding) that is currently unproven for STA-2**, while the directly supported activities are (i) a nuclear transcriptional-regulator role in AMP gene expression (BP/MF, genetically inferred) and (ii) a direct physical interaction with SNF-12 (MF: protein binding, experimentally demonstrated).

---

## Evidence Base

| Citation (PMID) | Evidence type | Supports / refutes / qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| InterPro/Pfam scan (F001) | Structural/evolutionary; computational | **Refutes** (functional DBD) | Does STA-2 carry a bona fide STAT DBD signature? | STA-2 fails PF02864 / STAT-DBD CDD that STA-1, STAT1, Stat92E all pass; only fold-level superfamily hits | Sequence analysis, 4 proteins | High for the HMM result; HMM failure indicates divergence, not proof of non-binding |
| 1BF5 contact mapping + alignments (F002) | Structural/evolutionary; computational | **Refutes/qualifies** | Are DNA-contacting residues conserved in STA-2? | 0/3 base contacts conserved (E421→S, S459→G, N460→P); most divergent DBD (20%); yet AlphaFold fold intact (pLDDT 88) | Human 1BF5 vs AF models | High for conservation gradient; human-residue metric imperfect (STA-1 also 0/3) |
| AlphaFold AF-Q20977-F1 (F002, F004) | Structural; computational | **Supports** (fold only) | Is the STAT DBD fold retained? | DBD fold predicted at pLDDT 88; DBD backbone RMSD vs 1BF5 = 8.2 Å ≈ STA-1 8.0 Å | In silico model | High-confidence model; RMSD crude, comparative only |
| [25692704](https://pubmed.ncbi.nlm.nih.gov/25692704/) | Mutant phenotype; localization | **Qualifies** (TF role, no binding assay) | Is STA-2 a transcriptional driver of AMPs? | STA-2 release from hemidesmosomes → AMP transcription / innate immune response | C. elegans epidermis | High for TF role; no direct DNA-binding assay |
| [34166401](https://pubmed.ncbi.nlm.nih.gov/34166401/) | Mutant phenotype; genetic | **Qualifies** (TF role, no binding assay) | Is STA-2 a key AMP transcriptional activator? | Fungal effectors block/enhance STA-2 activation of AMP genes; one raises nuclear STA-2 | C. elegans epidermis / fungal infection | High for TF role; activity genetically inferred |
| [21575913](https://pubmed.ncbi.nlm.nih.gov/21575913/) | Interaction; genetic | **Competing/qualifies** | How does STA-2 regulate transcription mechanistically? | Direct STA-2–SNF-12 (SLC6) interaction; "unorthodox mode of regulation for a STAT factor" | C. elegans epidermis | High for interaction; proposes partner-assisted, non-canonical mechanism |

---

## GO Curation Implications

**Lead for curator verification — GO:0000978 (RNA Pol II cis-regulatory region sequence-specific DNA binding) on STA-2 should be generalized or removed pending a direct binding assay.**

- The term asserts a **specific molecular function (MF)** that is **not experimentally demonstrated** for STA-2 and is contradicted by multiple convergent computational/evolutionary signals (fails PF02864; loses all STAT1 base contacts; most divergent DBD; no activating tyrosine; no EMSA/ChIP/motif). This is the signature of a **homology-propagated over-annotation**.
- **Recommended action:** Do not retain GO:0000978 with an experimental evidence code. If any annotation to DNA binding is kept, generalize to the less-specific parent **GO:0003677 (DNA binding)** or **GO:0003700 (DNA-binding transcription factor activity)** only with a non-experimental/inferred evidence code (e.g., ISS/IBA) and an explicit caveat, OR remove it as unsupported. A sequence-specificity claim (GO:0000978) is too strong.
- **Better-supported terms to foreground instead:**
  - **MF — protein binding (GO:0005515)** is directly supported by the STA-2–SNF-12 interaction ([PMID: 21575913](https://pubmed.ncbi.nlm.nih.gov/21575913/)). *(Per guidance, this is not a satisfying final MF on its own, but it is the one directly demonstrated molecular activity.)*
  - **BP — regulation of antimicrobial peptide / innate immune response gene expression** (e.g., defense response to fungus; regulation of transcription in the innate immune pathway) is supported genetically ([PMID: 25692704](https://pubmed.ncbi.nlm.nih.gov/25692704/), [PMID: 34166401](https://pubmed.ncbi.nlm.nih.gov/34166401/)).
  - **CC — nucleus** (regulated nuclear accumulation on activation) and the hemidesmosome-tethered cytoplasmic pool are both experimentally described.
- **Net:** Treat STA-2's "sequence-specific DNA binding" as **non-core / unproven**. The core, directly supported story is a damage-released, SNF-12-partnered, nuclear transcriptional regulator of epidermal AMP genes. The DBD is a retained *scaffold*, not a demonstrated *sequence-reading* module.

---

## Mechanistic Scope

The immediate molecular function under test is **autonomous, sequence-specific binding of STA-2 to RNA Pol II cis-regulatory DNA (GO:0000978)**. The investigation deliberately separates this from downstream and inferred layers:

- **Direct gene-product activity (tested here):** sequence-specific DNA binding — *not demonstrated*; demonstrated direct activity is protein–protein binding to SNF-12.
- **Downstream / pathway consequence:** activation of AMP genes (*nlp-29* and others) — genetically established but one or more steps removed from "does STA-2 touch the DNA sequence-specifically."
- **Developmental/physiological outcome:** epidermal innate immune response to fungal infection and physical damage — a phenotype, not a molecular activity.
- **Loss-of-function inference:** the transcription-factor assignment rests on genetics and localization, i.e., inferred from perturbation and nuclear accumulation, not from a biochemical DNA-binding measurement.

GO:0000978 is a claim at the *first* (direct molecular) level; the strong evidence sits at the *downstream* levels. That mismatch is the crux of the curation decision.

---

## Conflicts and Alternatives

1. **Paralog confusion (STA-1 vs STA-2).** The seed hypothesis uses STA-1 (Q9NAD6, ChIP-validated) as the "nematode positive control." STA-1 passes PF02864; STA-2 does not. Annotations or intuitions transferred from STA-1 (or from mammalian STATs) to STA-2 would constitute paralog over-annotation. The two worm STATs are functionally and structurally distinguishable at exactly the DNA-binding interface.
2. **Fold ≠ function.** AlphaFold fold conservation and near-identical DBD backbone RMSD (8.2 vs 8.0 Å) could be mis-read as evidence of DNA binding. The RMSD metric cannot discriminate STA-2 from the binding-competent STA-1, so it is uninformative for the specific claim and should not be cited as support for GO:0000978.
3. **Human-residue metric caveat (possible under-call).** STA-1 conserves 0/3 human STAT1 base contacts yet binds DNA in ChIP-seq. This means nematode STATs read DNA through a diverged interface, and "0/3 conserved" alone does not prove STA-2 cannot bind. STA-2's case against binding rests on the *combination* of signals (PF02864 failure + most-divergent DBD + no activating Tyr + no assay), not on residue identity alone.
4. **Non-canonical mechanism (competing model).** The explicit "unorthodox mode of regulation" and direct SNF-12 interaction ([PMID: 21575913](https://pubmed.ncbi.nlm.nih.gov/21575913/)) offer a genuine alternative: partner-assisted recruitment rather than autonomous sequence reading. This is the strongest competing interpretation and is compatible with all structural findings.
5. **Database carry-over.** GO:0000978 on STA-2 may originate from family-level/electronic annotation of "STAT transcription factor," which would propagate the mammalian sequence-specific DNA-binding activity without worm-specific experimental backing.

---

## Limitations and Knowledge Gaps

- **No direct DNA-binding assay for STA-2.** *Checked:* primary literature (3 key papers) and the seed context. *Why it matters:* this is the single datum that would decisively confirm or refute GO:0000978. *Resolution:* EMSA with candidate AMP-promoter probes, or ChIP-seq of tagged STA-2 in epidermis.
- **No defined STA-2 binding motif.** *Checked:* literature; none reported. *Why it matters:* "sequence-specific" requires a demonstrable sequence preference. *Resolution:* SELEX/PBM, or motif discovery from STA-2 ChIP-seq peaks.
- **Human-centric contact mapping.** *Checked:* 1BF5 contacts mapped by pairwise alignment. *Why it matters:* nematode STATs use a diverged DNA interface (STA-1 control also 0/3), so residue identity at human positions under-samples true binding determinants. *Resolution:* a nematode STAT–DNA co-structure or STA-1 ChIP motif to define the worm contact code.
- **Crude RMSD.** *Checked:* rigid-body Kabsch without outlier trimming. *Why it matters:* absolute RMSD (8 Å) is inflated and non-discriminative. *Resolution:* refined structural superposition / local DBD alignment; but note this would not resolve function.
- **Partner dependency not mapped to chromatin.** *Checked:* SNF-12 interaction demonstrated, but whether SNF-12 (or another factor) provides DNA-contact specificity is unknown. *Resolution:* ChIP of STA-2 with and without SNF-12, and reciprocal.
- **Activating-tyrosine inference.** *Checked:* alignment shows no aligned Y701 equivalent (STA-2 truncated). *Why it matters:* STA-2 may use a different activation switch; absence of the canonical Tyr does not preclude all DNA binding, only the canonical phospho-dimer route.

---

## Proposed Follow-up Experiments / Discriminating Tests

The following would most efficiently separate "STA-2 binds DNA sequence-specifically" from "STA-2 is a partner-recruited / non-DNA-binding regulator":

1. **STA-2 ChIP-seq in C. elegans epidermis** (ideally comparing basal vs. damage/infection-activated states). Direct occupancy at AMP promoters + a recovered motif would support GO:0000978; absence or exclusively partner-dependent, motif-less occupancy would refute autonomous sequence-specific binding. This mirrors the STA-1 positive-control design in the seed.
2. **In vitro DNA binding (EMSA) of recombinant STA-2 DBD** against candidate AMP-promoter elements and a STAT GAS consensus. Positive binding (with specificity by competition) would rescue the molecular claim despite the degenerate sequence; no binding would corroborate the computational prediction.
3. **PBM / SELEX** on the purified STA-2 DBD to establish whether any sequence preference exists and, if so, how it differs from the GAS/ISRE motif.
4. **SNF-12-dependence test:** STA-2 ChIP in *snf-12* loss-of-function vs. wild type. Loss of occupancy would support a partner-assisted (non-autonomous) model.
5. **Structure-guided mutagenesis:** restore/ablate predicted DNA-contacting positions and assay AMP-reporter activation, to test whether the retained fold's residues matter for function.

---

## Curation Leads (require curator verification)

**Candidate action on GO:0000978 (sequence-specific cis-regulatory DNA binding):**
- **Lead:** Downgrade/remove as an experimentally-coded MF on STA-2; treat as homology-driven over-annotation. If retained at all, generalize to GO:0003700 (DNA-binding transcription factor activity) or GO:0003677 (DNA binding) with a non-experimental evidence code **and a caveat** that direct binding is unproven and sequence-specificity is not demonstrated.

**Candidate better-supported terms (leads):**
- **GO:0005515 protein binding** — directly supported by STA-2–SNF-12 interaction. Candidate reference: [PMID: 21575913](https://pubmed.ncbi.nlm.nih.gov/21575913/), snippet to verify: *"the STAT transcription factor-like protein STA-2 as a direct physical interactor of SNF-12."*
- **BP: regulation of antimicrobial peptide / innate immune gene expression (defense response to fungus).** Candidate references: [PMID: 25692704](https://pubmed.ncbi.nlm.nih.gov/25692704/), snippet: *"detachment of STA-2 molecules from hemidesmosomes and transcription of AMPs"*; [PMID: 34166401](https://pubmed.ncbi.nlm.nih.gov/34166401/), snippet: *"preventing the key STAT-like transcription factor STA-2 from activating defensive antimicrobial peptide gene expression."*
- **CC: nucleus** (activation-dependent nuclear accumulation) and cytoplasmic/hemidesmosome-tethered pool.

**Suggested curator questions:**
- Is the existing GO:0000978 annotation on STA-2 experimental or electronic/ISS? If electronic family-level, it should not stand as evidence of worm-specific sequence-specific binding.
- Was the annotation transferred from STA-1 or mammalian STATs (paralog carry-over)?

**Suggested experiments:** STA-2 ChIP-seq (±SNF-12) and recombinant STA-2 DBD EMSA/PBM, as detailed above.

**Evidence snippets to verify (exact, from stored abstracts):**
- [PMID: 21575913](https://pubmed.ncbi.nlm.nih.gov/21575913/): *"reveal an unorthodox mode of regulation for a STAT factor."*
- [PMID: 21575913](https://pubmed.ncbi.nlm.nih.gov/21575913/): *"the STAT transcription factor-like protein STA-2 as a direct physical interactor of SNF-12."*
- [PMID: 25692704](https://pubmed.ncbi.nlm.nih.gov/25692704/): *"detachment of STA-2 molecules from hemidesmosomes and transcription of AMPs."*
- [PMID: 34166401](https://pubmed.ncbi.nlm.nih.gov/34166401/): *"preventing the key STAT-like transcription factor STA-2 from activating defensive antimicrobial peptide gene expression."*

---

## Bottom Line

STA-2 keeps the STAT DNA-binding-domain **fold** (AlphaFold pLDDT ≈ 88; DBD backbone RMSD vs. DNA-bound STAT1 1BF5 = 8.2 Å, matching the ChIP-validated binder STA-1 at 8.0 Å), so the hypothesis's first clause holds. But **functional, sequence-specific DNA binding (GO:0000978) is not supported**: STA-2 is the most divergent STAT tested (20% DBD identity), uniquely fails Pfam STAT-DBD PF02864 that STA-1 passes, conserves none of STAT1's three base-contacting residues, lacks the canonical activating tyrosine, and has no direct DNA-binding assay in the literature. The directly demonstrated biology is a damage-released, SNF-12-partnered, nuclear transcriptional regulator of epidermal antimicrobial-peptide genes operating via an explicitly "unorthodox" STAT mechanism. **Curation lead: treat GO:0000978 on STA-2 as homology-driven over-annotation — generalize or remove pending a direct binding assay — while retaining the demonstrated SNF-12 interaction and the AMP/innate-immunity transcriptional-regulation roles.**


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist sta2 dbd comparison table](openscientist_artifacts/provenance_sta2_dbd_comparison_table.csv)
- [OpenScientist sta2 evidence matrix](openscientist_artifacts/provenance_sta2_evidence_matrix.csv)