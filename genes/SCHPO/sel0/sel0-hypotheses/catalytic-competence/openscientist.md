---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T16:38:57.584507'
end_time: '2026-09-01T16:54:41.347074'
duration_seconds: 943.76
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: sel0
  gene_symbol: sel0
  uniprot_accession: O13890
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
  focus_type: free_text
  hypothesis_slug: catalytic-competence
  hypothesis_text: S. pombe sel0 (UniProt O13890) is a catalytically competent protein
    AMPylase rather than a catalytically inactive SelO-family pseudoenzyme.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/SCHPO/sel0/sel0-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: S. pombe sel0 (UniProt O13890) is a catalytically\
    \ competent protein AMPylase rather than a\n  catalytically inactive SelO-family\
    \ pseudoenzyme.\nfocus_type: free_text\ncontext: []\nreference_id: []"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: true
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

- **Organism code:** SCHPO
- **Taxon:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (NCBITaxon:284812)
- **Gene directory:** sel0
- **Gene symbol:** sel0
- **UniProt accession:** O13890

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** catalytic-competence
- **Source file:** genes/SCHPO/sel0/sel0-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

S. pombe sel0 (UniProt O13890) is a catalytically competent protein AMPylase rather than a catalytically inactive SelO-family pseudoenzyme.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: S. pombe sel0 (UniProt O13890) is a catalytically competent protein AMPylase rather than a
  catalytically inactive SelO-family pseudoenzyme.
focus_type: free_text
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

# sel0 (O13890) Catalytic Competence — Focused Curation Report

**Gene:** sel0 / SPAC20G4.05c (S. pombe, taxon 284812) · **UniProt:** O13890
**Hypothesis (slug: catalytic-competence):** *S. pombe sel0 is a catalytically competent protein AMPylase rather than a catalytically inactive SelO-family pseudoenzyme.*
**Iterations:** 1–3 of 3 (final)

---

## Executive Judgment

**Verdict: SUPPORTED (by strong evolutionary + structural conservation; not directly assayed in S. pombe).**

The "pseudoenzyme" framing rests on a well-known naming artifact: SelO adopts a
protein-kinase-like fold but lacks canonical **kinase** catalytic residues, so it
is called a **pseudokinase**. Sreelatha et al. 2018 (Cell, PMID **30270044**)
showed this is misleading — SelO binds ATP in an inverted orientation and is a
*bona fide active* protein **AMPylase/nucleotidyltransferase**. It is a pseudokinase
but **not** a catalytically inactive enzyme.

For the S. pombe ortholog specifically, all evidence is homology/structure-based
(there is **no direct in vitro or in vivo assay of sel0/O13890**). Within that
limit, the evidence is unusually strong:

- O13890 is in the **SELO family** (Pfam PF02696; InterPro IPR003846; PANTHER PTHR32057).
- **10/10** UniProt-annotated catalytic/nucleotide-binding residues are **identical**
  to the experimentally characterized, crystallized *Pseudomonas syringae* SelO
  (Q87VB1) and *E. coli* YdiU (P77649), and to human SELENOO (Q9BVL4).
- The AlphaFold model (mean pLDDT 95.8) shows these residues forming a single,
  high-confidence, compact active-site pocket.

The most important caveat: catalytic competence for S. pombe is **inferred**. The
UniProt functional annotations are ECO:0000250 (by similarity to S. cerevisiae
Q08968), and PomBase lists sel0's characterisation status as "biological role
inferred." No experiment has measured *S. pombe* sel0 AMPylation activity, substrate,
or the effect of active-site mutation in fission yeast.

**Update (Iteration 2) — the inference is better-anchored than distant-bacterial homology:**
- The by-similarity source, **S. cerevisiae SelO (Q08968), carries experimental
  evidence (ECO:0000269) for FUNCTION and CATALYTIC ACTIVITY** (references include
  Sreelatha 2018, PMID 30270044) and ECO:0000314 mitochondrial localization. The
  closest experimentally characterized ortholog is therefore *fungal*, not bacterial.
- **PomBase already curates sel0** with MF **GO:0070733 (protein adenylyltransferase
  activity)**, BP **GO:0098869 (cellular oxidant detoxification)**, CC **GO:0005739
  (mitochondrion)** — i.e., the AMPylase MF term is already the curated state.
- **Nucleotide-specificity nuance:** the bacterial homolog YdiU is a Mn²⁺-dependent
  protein **UMPylase** (PMID 32966796), whereas the eukaryotic mitochondrial branch
  (human SELENOO, S. cerevisiae, S. pombe) is the **AMPylase** branch. The
  branch-appropriate MF term for sel0 is protein adenylyltransferase activity
  (GO:0070733), not a UMP-transferase term.

---

## Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| PMID **30270044** (Sreelatha 2018, Cell) | Direct assay + structural | **Supports** | SelO family is an active AMPylase, not an inactive pseudoenzyme | SelO transfers AMP from ATP to Ser/Thr/Tyr; crystal structure shows kinase-like fold with **ATP flipped** → structural basis for catalysis; localizes to mitochondria, AMPylates redox proteins | Human SELENOO, *E. coli*, *P. syringae* (crystallized) | High for the family; not S. pombe |
| PMID **35101215** (Mukherjee & Sreelatha 2022) | Direct assay (method) | Supports | SelO catalytically AMPylates substrates | Bacterial SelO AMPylates substrates; enrichable with biotin-ATP analog | Bacterial SelO | High for family; not S. pombe |
| PMID **39185898** (Gonzalez & Sreelatha 2024) | Direct assay (biophysical) | Supports | SelO binds ATP/metal in inverted orientation to catalyze AMP transfer | TSA confirms metal + nucleotide binding underlying SelO AMPylation | SelO enzyme | High for family; not S. pombe |
| UniProt **O13890** (record) | Database | Supports (qualifies) | sel0 is an AMPylase | Annotated "Protein adenylyltransferase SelO, mitochondrial"; RHEA:54288; active site D287; Mg²⁺ cofactor; SELO family — **all ECO:0000250 (by similarity to Q08968)** | S. pombe | Annotation is inferred, not experimental |
| **This report — sequence alignment** (computed) | Structural/evolutionary (computational) | Supports | Catalytic residues conserved, not degenerated | NW/BLOSUM62: 10/10 active/binding residues **identical** to characterized Q87VB1 (37% global id), P77649 (39.5%), Q08968 (43.6%), Q9BVL4 (36.7%): D287, K144, G120, G122, D156, G157, R208, R215, N288, D297 | in silico | Homology inference; no wet-lab confirmation |
| **This report — AlphaFold AF-O13890** (computed) | Structural (computational) | Supports | Active site is structurally intact | Model mean pLDDT 95.8; 8 catalytic residues at pLDDT 87.6–98.5 form one compact pocket (mean 9.0 Å to centroid; D287–N288 3.9 Å, D287–D297 9.2 Å) | in silico | Predicted structure; no ligand/holo evidence |
| UniProt **Q08968** (record; refs incl. PMID 30270044) | Direct assay / database | **Supports** | Fungal ortholog is a catalytically active adenylyltransferase | S. cerevisiae SelO carries ECO:0000269 (experimental) for FUNCTION and CATALYTIC ACTIVITY, and ECO:0000314 mitochondrial localization | S. cerevisiae | Closest experimentally-supported ortholog; not S. pombe |
| PomBase **SPAC20G4.05c** (record) | Database | Supports (qualifies) | GO curation state for sel0 | Already annotated MF GO:0070733 (protein adenylyltransferase activity), BP GO:0098869 (cellular oxidant detoxification), CC GO:0005739 (mitochondrion); status "biological role inferred"; genome-wide-screen phenotypes present but no mechanism assay | S. pombe | Confirms curated state is inference, not S. pombe experiment |
| PMID **32966796** (Yang 2020) | Direct assay | Qualifies | SelO-family nucleotide specificity | Bacterial homolog YdiU is a Mn²⁺-dependent protein UMPylase (Tyr/His) — family transfers different NMPs | Bacteria (Salmonella/E. coli) | Shows AMP vs UMP branch difference; supports "adenylyltransferase" for the eukaryotic ortholog |

*One peripheral binding residue differs vs human (R123 vs A156); human SELENOO is
itself catalytically active, so this is not a competence-relevant substitution.*

---

## GO Curation Implications (leads — require curator verification)

- **Retain the molecular-function annotation of protein adenylyltransferase /
  AMPylase activity.** The most informative supported MF term is
  **GO:0070733 "protein adenylyltransferase activity"** (AMPylation), consistent
  with UniProt catalytic activity RHEA:54288. Do **not** downgrade to an
  "inactive"/"pseudo" characterization and do **not** fall back to "protein binding."
- **Evidence code:** Current support is homology (ISS/ISO, ECO:0000250) transferred
  from S. cerevisiae Q08968 and bacterial SelO. This is appropriate **as long as
  the annotation carries an ISS/ISO (by-similarity) qualifier**, not an experimental
  (IDA) code, because no S. pombe assay exists.
- **CC:** Mitochondrion (GO:0005739) — supported by orthology (ECO:0000250);
  reasonable to retain with ISS.
- **BP:** "cellular response to oxidative stress" / redox homeostasis is a
  **family-level, orthology-based** association (Sreelatha 2018) and should be
  treated as **plausible-but-not-core / needs S. pombe evidence**, i.e. weaker than
  the MF claim.
- **Net:** If the review action under evaluation was to weaken/remove the AMPylase
  MF term or brand sel0 an inactive pseudoenzyme, the evidence argues **against**
  that; the catalytic-AMPylase MF should be **retained** (as an ISS lead).
- **Already-curated state (PomBase, Iteration 2):** sel0 is *already* annotated
  MF GO:0070733, BP GO:0098869 (cellular oxidant detoxification), CC GO:0005739,
  with characterisation "biological role inferred." The hypothesis is therefore
  **consistent with, and reinforces, the existing curation** — the recommended
  action is *retain GO:0070733 with an ISS/ISO qualifier*, anchored to the
  experimentally-supported S. cerevisiae ortholog Q08968 (ECO:0000269) rather than
  bacterial YdiU. Do **not** add a UMP-transferase term (that is the bacterial branch).

---

## Mechanistic Scope

- **Immediate molecular function (what is being tested):** transfer of AMP from
  ATP onto a hydroxyl side chain (Tyr, and in the family Ser/Thr) of substrate
  proteins — protein AMPylation/adenylylation — Mg²⁺-dependent, via a kinase-like
  fold with inverted ATP.
- **Downstream / non-core (do not conflate with the MF claim):** redox homeostasis,
  regulation of protein S-glutathionylation, and cellular oxidative-stress response
  are downstream consequences of AMPylating redox enzymes (e.g. glutaredoxins).
  These are pathway/phenotype-level, not the direct catalytic activity, and are
  orthology-inferred for S. pombe.

---

## Conflicts and Alternatives

- **"Pseudoenzyme" reading:** The only basis is the pseudokinase label (missing
  *kinase* catalytic residues). This is resolved by the 2018 discovery that SelO is
  an active *AMPylase* — the kinase catalytic machinery is irrelevant to its true
  activity. No conflicting primary evidence indicates S. pombe sel0 is inactive.
- **Paralog confusion:** Low risk. sel0 is single-copy in the SELO family; the
  human accession Q9Y6D0 is *not* SELENOO (it returns Selenoprotein K) — the correct
  human ortholog is **Q9BVL4**. Curators reusing accessions should note this.
- **Selenocysteine caveat:** Some SelO orthologs (e.g., certain vertebrates) carry
  an active-site-proximal selenocysteine; S. pombe sel0 ends in a Cys-rich C-terminus
  (…QCSCSS) and is **not** predicted to be a selenoprotein. This does not affect the
  transferase active site (the AMP-transfer residues above are all standard and conserved).
- **Organism-specificity:** All functional data derive from bacterial/human/S.
  cerevisiae systems; a fission-yeast-specific loss of activity cannot be excluded
  from sequence alone, though nothing suggests it.

---

## Knowledge Gaps

1. **No direct S. pombe enzymatic assay.** Checked: PubMed (no S. pombe SelO paper),
   UniProt (S. pombe = all ECO:0000250), PomBase (status "biological role inferred").
   Mitigated but not closed by the experimentally-supported fungal ortholog Q08968
   (ECO:0000269). Matters because the S. pombe MF annotation is still inferred.
   Resolved by: in vitro AMPylation assay of recombinant sel0 ± α-³²P/biotin-ATP.
2. **Substrate identity in S. pombe unknown.** Family substrates are redox enzymes
   (glutaredoxins); the S. pombe targets are unverified. Resolved by: biotin-ATP
   substrate capture (per PMID 35101215) in fission yeast lysate.
3. **No active-site mutant phenotype in S. pombe.** Whether D287A/K144A abolishes an
   oxidative-stress phenotype is untested. Resolved by: catalytic-dead knock-in +
   oxidative-stress sensitivity assay.
4. **Holo/ligand structure absent.** AlphaFold is apo and predicted; no experimental
   S. pombe structure or ATP-bound model. Resolved by: crystallography/cryo-EM or
   docking of ATP·Mg²⁺ into the modeled pocket.

---

## Discriminating Tests

1. **In vitro AMPylation assay** of recombinant sel0 with ATP (radiolabeled or
   biotin-ATP analog) on candidate substrates — directly distinguishes active
   enzyme from pseudoenzyme.
2. **Active-site mutagenesis** (D287A catalytic Asp; K144A invariant Lys;
   D297A Mg-Asp) — loss of activity confirms these residues are catalytic, matching
   the family.
3. **Genetic complementation:** does S. pombe sel0 rescue an oxidative-stress
   phenotype of a SelO-null (yeast/bacterial) strain, and is rescue abolished by the
   catalytic mutation?
4. **Substrate capture** with biotin-ATP (PMID 35101215) to identify AMPylated
   targets and test the glutaredoxin/redox-homeostasis link in fission yeast.

---

## Curation Leads (require curator verification)

- **Candidate references to attach:**
  - PMID **30270044** — snippet: *"the highly conserved pseudokinase selenoprotein-O
    (SelO) transfers AMP from ATP to Ser, Thr, and Tyr residues on protein substrates
    (AMPylation)"* and *"reveals a protein kinase-like fold with ATP flipped in the
    active site, thus providing a structural basis for catalysis."*
  - PMID **35101215**, PMID **39185898** — supporting AMPylation activity/mechanism.
- **Candidate GO terms:** keep **GO:0070733 protein adenylyltransferase activity**
  (MF); **GO:0005739 mitochondrion** (CC, ISS); treat oxidative-stress-response BP as
  orthology-level (ISS), not core/experimental.
- **Possible action change:** if the blinded review action weakened or removed the
  AMPylase MF term (treating sel0 as an inactive pseudoenzyme), reverse toward
  **retain-with-ISS**; the pseudo**kinase** status must not be read as catalytic
  inactivity.
- **Suggested curator question:** Is there any *primary* S. pombe experimental
  evidence for sel0 activity/localization, or is the annotation entirely projected
  from Q08968/bacterial SelO? If entirely projected, ensure ISS/ISO evidence codes.
- **Suggested experiments:** the four discriminating tests above.

---

## Catalytic-Residue Conservation Table (computed provenance)

sel0/O13890 residue → aligned residue in each characterized homolog (Iteration 1 NW/BLOSUM62 alignments):

| sel0 (O13890) | Role | PsSelO Q87VB1 (xtal) | EcYdiU P77649 | ScSelO Q08968 | hSELENOO Q9BVL4 | Verdict |
|---|---|---|---|---|---|---|
| D287 | Active site: catalytic Asp (proton acceptor) | D252 | D246 | D338 | D338 | IDENTICAL in all |
| K144 | Invariant Lys (ATP α-phosphate positioning) | K113 | K107 | K156 | K176 | IDENTICAL in all |
| D156 | Mg²⁺-coordinating Asp | D125 | D119 | D168 | D188 | IDENTICAL in all |
| D297 | Mg²⁺-coordinating Asp | D262 | D256 | D348 | D348 | IDENTICAL in all |
| G120 | Gly-rich ATP-binding loop | G90 | G84 | G132 | G153 | IDENTICAL in all |
| G122 | Gly-rich ATP-binding loop | G92 | G86 | G134 | G155 | IDENTICAL in all |
| G157 | Gly (active-site loop) | G126 | G120 | G169 | G189 | IDENTICAL in all |
| R208 | Substrate/phosphate Arg | R176 | R170 | R220 | R246 | IDENTICAL in all |
| R215 | Substrate/phosphate Arg | R183 | R177 | R227 | R253 | IDENTICAL in all |
| N288 | Active-site Asn | N253 | N247 | N339 | N339 | IDENTICAL in all |
| R123 | Peripheral binding Arg | R93 | R87 | R135 | A156 | IDENTICAL except human (A) |

**Catalytic residues degenerated in sel0: 0.** 10/11 identical across all
characterized homologs (including the crystallized *P. syringae* SelO and the
experimentally-validated *S. cerevisiae* SelO); the single exception (R123→A) is a
peripheral residue that differs only vs human, and human SELENOO is itself active.

## GO Decision Table (leads — require curator verification)

| Aspect | GO ID | Term | Lead action | Rationale |
|---|---|---|---|---|
| MF | GO:0070733 | protein adenylyltransferase activity | **RETAIN (with ISS/ISO)** | Full active site conserved + AlphaFold pocket; anchored to ScSelO Q08968 (ECO:0000269); already curated in PomBase |
| CC | GO:0005739 | mitochondrion | RETAIN (ISS) | Ortholog localization (ScSelO ECO:0000314); UniProt SL-0173; already in PomBase |
| BP | GO:0098869 | cellular oxidant detoxification | RETAIN as non-core / orthology-level | Family redox role (PMID 30270044); downstream of AMPylation; not S. pombe-assayed |
| MF | — | protein binding | AVOID as final term | Less informative than GO:0070733 |
| MF | — | UMP-transferase / UMPylation | DO NOT ADD | Bacterial YdiU branch (PMID 32966796); sel0 is the eukaryotic AMPylase branch |

## Provenance

Computed in this run (executed code + outputs recorded in the job): (1) UniProt REST
retrieval of O13890 and homolog features; (2) Needleman–Wunsch/BLOSUM62 pairwise
alignments mapping the 10 annotated catalytic/binding residues onto Q87VB1, P77649,
Q08968, Q9BVL4 (all identical); (3) AlphaFold AF-O13890-F1 model parsing — pLDDT and
3D clustering of the catalytic pocket. No results were fabricated; homolog activity
data are from primary literature, and the S. pombe catalytic competence is reported
as an inference, not a measurement.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)