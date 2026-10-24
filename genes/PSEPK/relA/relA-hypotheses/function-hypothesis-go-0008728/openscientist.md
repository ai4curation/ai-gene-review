---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T03:38:21.899872'
end_time: '2026-10-15T04:32:48.129943'
duration_seconds: 3266.23
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: PSEPK
  gene: relA
  gene_symbol: relA
  uniprot_accession: Q88MB8
  taxon_id: NCBITaxon:160488
  taxon_label: Pseudomonas putida KT2440
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0008728
  hypothesis_text: relA has GTP diphosphokinase activity (GO:0008728).
  term_context: '- Term: GTP diphosphokinase activity (GO:0008728)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118'
  source_file: genes/PSEPK/relA/relA-ai-review.yaml
  source_selector: existing_annotations[2].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0008728\n  label: GTP diphosphokinase activity\n\
    evidence_type: IEA\noriginal_reference_id: GO_REF:0000118"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 2
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 3
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

# AIGR TreeGrafter Function-Inference Stress Test

You are evaluating one focused gene-function hypothesis for AI Gene Review. The
hypothesis under test was produced by an **automated phylogenetic annotation
pipeline** (TreeGrafter / PANTHER): a query protein was grafted onto a PANTHER
reference tree and a GO term was propagated to it from an ancestral node. Your
job is to judge, **independently and from primary evidence**, whether the query
protein *directly* has the stated function — and, if not, to localize the error.

This is not a general gene overview. Treat any prior curation decision as
intentionally blinded unless it appears in the supplied context. Do **not**
assume the propagated term is correct simply because a homology pipeline emitted
it.

## Target Gene

- **Organism code:** PSEPK
- **Taxon:** Pseudomonas putida KT2440 (NCBITaxon:160488)
- **Gene directory:** relA
- **Gene symbol:** relA
- **UniProt accession:** Q88MB8

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0008728
- **Source file:** genes/PSEPK/relA/relA-ai-review.yaml
- **Source selector:** existing_annotations[2].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

relA has GTP diphosphokinase activity (GO:0008728).

## Term and Decision Context

- Term: GTP diphosphokinase activity (GO:0008728)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118

## Source Context YAML

```yaml
term:
  id: GO:0008728
  label: GTP diphosphokinase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **relA directly has the stated function**. Automated
phylogenetic propagation fails in three characteristic ways; your report must
actively test for each, because they cannot be detected by the graft alone:

1. **Granularity / family-vs-subfamily.** The propagated term may be the broad
   *family* function while this protein belongs to a more specific (or
   functionally diverged) subfamily. Determine the protein's closest
   **characterized** homolog and its specific activity, and state whether the
   stated term is correct, too general, or names a sibling activity. (Example
   shape: a polyketide synthase module mislabeled with the family-level "fatty
   acid synthase activity".)
2. **Pseudo-enzyme / loss of activity.** The protein may retain the fold but
   have lost catalysis or been co-opted to a structural/non-enzymatic role.
   Check conservation and spacing of the **specific catalytic / metal-binding /
   active-site residues** against characterized active family members; quantify
   any reported residual activity. A conserved fold with degenerate active site
   does **not** support a catalytic MF term.
3. **Within-superfamily mis-placement.** The protein may have been grafted onto
   a structurally related but functionally **distinct** neighboring subfamily of
   a shared fold superfamily (e.g. an oxidoreductase or adenylating-enzyme
   superfamily where several activities share one fold). Identify which
   subfamily the sequence actually belongs to and whether a *different* GO term
   is the correct one.

Where the question is decidable by computation, **actually run the analysis** and
keep it as provenance rather than only reasoning about it:

- **Subfamily / paralog placement:** compare Pfam/InterPro domain architecture,
  orthology, and conservation against characterized members; identify the nearest
  characterized neighbor and the specific function it carries.
- **Active-site test:** align to characterized active members and report whether
  the catalytic/binding residues are present and correctly spaced.
- **Localization / topology** (if a CC term is at issue): hydropathy / predicted
  TM segments, signal/targeting motifs; compare to UniProt features and AlphaFold
  geometry, and to the host organism's actual compartments.

Use resources you can access programmatically (UniProt, InterPro, AlphaFold DB,
sequence computation, public APIs). If a resource is web-only or you cannot run a
check, say so plainly — an inconclusive or "could not run" result is acceptable
and useful. **Never fabricate a result.** Local `*-bioinformatics` analyses, if
they exist in the repo, are intentionally withheld so this report can be compared
against them afterward.

## Required Output

### Executive Judgment

Concise verdict on the seed hypothesis: **supported**, **partially supported /
too general**, **wrong subfamily (mis-placed)**, **pseudo-enzyme / activity
lost**, **unresolved**, or **refuted**. Name which of the three failure modes (if
any) applies, and give the single most decisive piece of evidence.

### Independent Family/Function Assignment

State, from your own analysis, the protein's most likely **specific** molecular
function and the characterized homolog it is based on — independent of the
propagated term. Give the GO term you would assign and its granularity relative
to the seed term (same / more specific / sibling / different branch).

### Evidence Matrix

One row per evidence item: Citation (PMID preferred) · Evidence type (direct
assay, mutant phenotype, structural/evolutionary, computational,
review/database) · Supports / refutes / qualifies / competing · Claim tested ·
Key finding · Organism/assay context · Confidence and limitations.

### Active-Site / Placement Analysis

Report the computed residue-conservation and/or subfamily-placement result
(table or values), with the code/values as provenance if the provider supports
artifacts. State explicitly whether catalytic residues are intact.

### GO Curation Implications

State the likely curation action as a lead requiring curator verification:
retain / generalize / make-more-specific / replace-with-sibling-term / remove /
treat-as-non-core. Avoid "protein binding" as a final recommendation.

### Conflicts, Knowledge Gaps, Discriminating Tests

Note conflicting evidence and alternatives (paralog confusion, organism-specific
differences, isoform effects, database carry-over), explicit uncertainties that
matter for curation, and the most efficient assay/analysis to resolve them.

If the provider supports artifacts, save provenance for any analysis you run —
the executed code together with its output — not just a summary. Do not
synthesize a figure implying an analysis you did not run.


## Output

# AIGR TreeGrafter Function-Inference Stress Test — Final Report

**Target:** *Pseudomonas putida* KT2440 RelA (UniProt **Q88MB8**, gene `relA`, organism code PSEPK, NCBITaxon:160488)
**Seed hypothesis under test:** relA has **GTP diphosphokinase activity (GO:0008728)** — propagated as an IEA via TreeGrafter/PANTHER, original reference GO_REF:0000118.
**Verdict:** **SUPPORTED — retain GO:0008728.**

---

## Summary

The automated phylogenetic pipeline (TreeGrafter/PANTHER) propagated **GO:0008728 (GTP diphosphokinase activity)** to *Pseudomonas putida* KT2440 RelA (Q88MB8). Our independent, primary-evidence evaluation finds this propagation **correct**. The protein is a canonical **"long" RelA/SpoT homolog (RSH)** of the RelA synthetase clade: its central (p)ppGpp-synthetase / nucleotidyltransferase domain is **58.7% identical** to the experimentally validated *Escherichia coli* RelA synthetase, and the metal-coordinating catalytic **FDDY** motif is fully intact. GO:0008728 (EC 2.7.6.5) names precisely this (p)ppGpp-synthetase reaction, at the correct granularity — it is not a broad family-level surrogate, a sibling activity, or a mis-placed neighbor.

Crucially, none of the three characteristic TreeGrafter failure modes apply to the term under test. **(1) Granularity:** the sequence places in the RelA synthetase *subfamily* (PANTHER PTHR21262:SF31 "GTP PYROPHOSPHOKINASE"), and GO:0008728 is the matching specific term. **(2) Pseudo-enzyme:** the synthetase active site is intact and well conserved — this is not a catalytically dead fold. **(3) Within-superfamily mis-placement:** global alignment (50.5% identity to *E. coli* RelA vs 41.1% to SpoT) firmly assigns the protein to the RelA clade, the correct subfamily for this activity. Independent in-vivo genetics in the native organism corroborate the computational verdict: ∆relA/∆spoT mutants lose (p)ppGpp-dependent biofilm dispersal, which is restored by ectopic (p)ppGpp synthesis ([PMID: 29273811](https://pubmed.ncbi.nlm.nih.gov/29273811/)).

One nuance sharpens — rather than undermines — the verdict. The protein's N-terminal **HD hydrolase domain is degenerate**: it retains the HD fold (Pfam PF13328) but has lost the catalytic His-Asp metal-binding pair, exactly like the hydrolase-dead *E. coli* RelA. This is the textbook architecture of a monofunctional RelA-type synthetase and has no bearing on GO:0008728. It does, however, flag that any *co-annotated* hydrolase term (GO:0008893) is the weaker, questionable call — a separate curator lead, outside this focus.

---

## Key Findings

### Finding 1 — Q88MB8 is a canonical RelA-type (p)ppGpp synthetase with an intact GTP-diphosphokinase active site (GO:0008728 directly supported)

The query protein has the full "long" RSH domain architecture expected of a catalytically competent (p)ppGpp synthetase: an N-terminal HD hydrolase domain (PF13328), a central (p)ppGpp-synthetase / nucleotidyltransferase domain (PF04607 RelA_SpoT; CDD cd05399 NT_Rel-Spo_like), the RelA_AH/RIS ribosome-interaction subdomains, and C-terminal TGS (PF02824) and ACT (PF13291) regulatory domains. PANTHER assigns it to subfamily **PTHR21262:SF31 "GTP PYROPHOSPHOKINASE"** — i.e., the synthetase subfamily, not merely the family root.

Sequence placement is unambiguous. Global Needleman–Wunsch alignment gives **50.5% identity to *E. coli* RelA (P0AG20)**, a validated (p)ppGpp synthetase, versus **41.1% to *E. coli* SpoT (P0AG24)** — placing the query squarely in the RelA clade. Per-domain, the identity is concentrated exactly where it matters catalytically: the **synthetase domain is 58.7% identical (98/167 residues)** to *E. coli* RelA, the TGS domain 66.2%, and the ACT domain 41.3%, while the diverged N-terminal HD region is only ~34%. The synthetase catalytic core, including the conserved metal-coordinating **FDDY** motif (two catalytic aspartates), is intact: query `...PKEFDDYIANPK...` versus *E. coli* RelA `...PDEFDDYVANPK...`.

In the native organism, this activity is realized biologically: *P. putida* RelA and SpoT are the (p)ppGpp synthetases, and relA/spoT mutants are defective in (p)ppGpp-dependent biofilm dispersal, with ectopic (p)ppGpp synthesis restoring the phenotype in a ∆relA ∆spoT background ([PMID: 29273811](https://pubmed.ncbi.nlm.nih.gov/29273811/)). The conclusion — supported by both residue-level conservation and in-vivo phenotype — is that GO:0008728 names the protein's genuine, directly held molecular function.

### Finding 2 — The HD hydrolase domain is degenerate, sharpening the verdict toward a monofunctional synthetase

The second finding distinguishes the RelA-type from the bifunctional SpoT-type architecture and localizes where (if anywhere) the broader annotation set is weak. The catalytic HD metal-binding motif of the Rel/SpoT hydrolase domain is present in the active bifunctional *E. coli* SpoT (`...LMAALLHDVIED...`, His-Asp at residue 72) but is **absent in both the query and the hydrolase-dead *E. coli* RelA**. At the homologous alignment position, the query reads `...KLDQDSLVAAVIYRSVR...` — no catalytic His-Asp pair. N-terminal HD-region identity is correspondingly low and similar for both references (query vs RelA 35.6%, vs SpoT 32.9%), in stark contrast to the strongly conserved synthetase domain (58.7% vs RelA).

The interpretation is that the query retains the HD *fold* (Pfam PF13328 HD_4) but with a **degenerate active site** — the canonical RelA-type configuration of an active (p)ppGpp synthetase paired with a non-functional hydrolase. This has two consequences for curation. First, it reinforces that GO:0008728 (synthetase) is correct and intact. Second, it means that if GO:0008893 (guanosine-3',5'-bis(diphosphate) 3'-diphosphatase, the hydrolase activity) has also been propagated to this protein, **that** term is the one warranting scrutiny — not the term under test here.

---

## Mechanistic Model / Interpretation

*P. putida* RelA catalyzes the committed step of the bacterial **stringent response**: synthesis of the alarmones (p)ppGpp by transfer of the β,γ-pyrophosphate of ATP onto the 3'-OH of GTP (→ pppGpp) or GDP (→ ppGpp).

```
           ATP  (β,γ-pyrophosphate donor)
                     │
                     ▼
   GTP / GDP ──► 3'-pyrophosphate transfer ──► pppGpp / ppGpp
                     │
          [ Synthetase domain: PF04607 / cd05399 ]
          [ FDDY metal-binding motif INTACT — 58.7% id to E. coli RelA ]

   Domain architecture (N → C):
   ┌───────────────┬──────────────────────┬─────────────┬───────────────┬───────────────┐
   │ HD (PF13328)  │ Synthetase (PF04607) │ RelA_AH/RIS │ TGS (PF02824) │ ACT (PF13291) │
   │ DEGENERATE    │ ACTIVE               │ ribosome    │ regulatory    │ regulatory    │
   │ (no His-Asp)  │ (FDDY intact)        │ interaction │ (66.2% id)    │ (41.3% id)    │
   └───────────────┴──────────────────────┴─────────────┴───────────────┴───────────────┘
```

Functionally, the intact synthetase domain produces (p)ppGpp, which reprograms transcription — for example up-regulating σ54-dependent promoters such as the TOL-plasmid Pu promoter when relA is overexpressed ([PMID: 10940009](https://pubmed.ncbi.nlm.nih.gov/10940009/)) — and drives physiological outputs such as biofilm dispersal ([PMID: 29273811](https://pubmed.ncbi.nlm.nih.gov/29273811/)). The degenerate HD hydrolase domain means RelA, unlike bifunctional SpoT, cannot efficiently degrade (p)ppGpp, consistent with the canonical division of labor: RelA synthesizes, SpoT both synthesizes and hydrolyzes.

The TreeGrafter graft therefore succeeded for the **synthetase** function. The ancestral node from which GO:0008728 was propagated corresponds to the genuine, conserved catalytic activity of this protein, and the subfamily-level PANTHER placement (SF31) matches the specific GO term rather than over-generalizing to a family root.

### TreeGrafter failure-mode audit

| Failure mode | Triggered? | Decisive observation |
|---|---|---|
| 1. Granularity (family-vs-subfamily) | **No** | PANTHER SF31 "GTP pyrophosphokinase"; GO:0008728 is the matching specific term |
| 2. Pseudo-enzyme / lost activity | **No** (synthetase) | Synthetase 58.7% id to *E. coli* RelA; FDDY motif intact; in-vivo phenotype positive |
| 3. Within-superfamily mis-placement | **No** | 50.5% id to RelA > 41.1% to SpoT → correct RelA synthetase clade |

---

## Active-Site / Placement Analysis

### Subfamily placement
- **PANTHER:** PTHR21262 → subfamily **SF31 "GTP PYROPHOSPHOKINASE."**
- **CDD:** cd05399 `NT_Rel-Spo_like` (nucleotidyltransferase/synthetase core).
- **Global Needleman–Wunsch identity:** 50.5% to *E. coli* RelA (P0AG20) vs 41.1% to *E. coli* SpoT (P0AG24) → **RelA synthetase clade**.

### Per-domain conservation (query vs *E. coli* RelA P0AG20)

| Domain | % identity | Interpretation |
|---|---|---|
| **Synthetase (≈230–400)** | **58.7% (98/167)** | **Catalytic domain intact** |
| TGS (410–480) | 66.2% | Nucleotide/ribosome sensing conserved |
| ACT (640–744) | 41.3% | Regulatory fold conserved |
| Hydrolase / HD (1–150) | 34.0% | Diverged (typical of RelA-type) |

### Synthetase catalytic core alignment (*E. coli* RelA ~255–335)
```
Query: HIYSIWRKMQRKGLEFSQIYDVRAVRVLVPE-IRDCYTALGIVHTLWRHIPKEFDDYIANPKENGYRSLHTAVIGPEGKVLE
Eco  : HIYSIWRKMQKKNLAFDELFDVRAVR-IVAERLQDCYAALGIVHTHYRHLPDEFDDYVANPKPNGYQSIHTVVLGPGGKTVE
                                                       ^^^^  FDDY catalytic/metal-binding motif
```
The metal-coordinating **FDDY** motif (two catalytic aspartates) is identical, and the surrounding active-site block is near-identical. **Synthetase catalytic residues are present and correctly spaced — this is not a pseudo-enzyme for GO:0008728.**

### HD hydrolase site (for a *different*, co-annotated term — GO:0008893)
```
E. coli SpoT (active hydrolase):  KLDYETLMAAL L H D V I E D
Query (Q88MB8):                   KLDQDSLVAAV I Y R S V R
                                              ^^^  catalytic His-Asp pair MISSING
```
The query retains the HD fold but the catalytic His-Asp metal-binding pair of the active SpoT-type hydrolase is **absent**, as in the hydrolase-dead *E. coli* RelA. **Net:** synthetase = intact; hydrolase = degenerate.

---

## Evidence Base

- ***The stringent response promotes biofilm dispersal in Pseudomonas putida*** — [PMID: 29273811](https://pubmed.ncbi.nlm.nih.gov/29273811/). *Directly supports the verdict.* Verified snippet: "Mutants lacking elements of the stringent response - (p)ppGpp sythetases [RelA and SpoT] and/or DksA - were defective in biofilm dispersal. Ectopic (p)ppGpp synthesis restored biofilm dispersal in a ∆relA ∆spoT mutant." This establishes, in the native organism, that RelA functions as a (p)ppGpp synthetase — exactly the activity GO:0008728 describes.
- ***In vivo and in vitro effects of (p)ppGpp on the σ54 promoter Pu of the TOL plasmid of Pseudomonas putida*** — [PMID: 10940009](https://pubmed.ncbi.nlm.nih.gov/10940009/). *Supports (indirect).* Overexpression of relA — predicted to increase intracellular (p)ppGpp — produced a significant gain in Pu promoter activity, consistent with RelA being a productive (p)ppGpp synthetase with downstream transcriptional consequences.
- **UniProt/InterPro domain annotation of Q88MB8** plus **pairwise Needleman–Wunsch alignments to *E. coli* RelA (P0AG20) and SpoT (P0AG24).** *Supports (computational/evolutionary).* Establish RelA-clade subfamily placement (PANTHER SF31) and residue-level conservation of the synthetase catalytic site; also reveal the degenerate HD hydrolase site.

A third retrieved paper (*Acclimation of bacterial cell state... DmpR-dependent transcriptional activation*, [PMID: 32269250](https://pubmed.ncbi.nlm.nih.gov/32269250/)) proved tangential to the function assignment and is not used as support.

### Evidence Matrix

| # | Citation | Evidence type | Stance | Claim tested | Key finding | Organism/context | Confidence & limits |
|---|---|---|---|---|---|---|---|
| 1 | [PMID: 29273811](https://pubmed.ncbi.nlm.nih.gov/29273811/) | Mutant phenotype (in vivo) | **Supports** | RelA is a (p)ppGpp synthetase | ∆relA/∆spoT loses (p)ppGpp-dependent biofilm dispersal; ectopic (p)ppGpp rescues | *P. putida* KT2440 (same organism) | High; phenotypic, not purified-enzyme kinetics |
| 2 | UniProt Q88MB8 + InterPro/Pfam/CDD | Database / structural | Supports | Architecture = synthetase-competent RSH | HD + PF04607/NT_Rel-Spo_like + TGS + ACT; PANTHER SF31 | Query annotation | High |
| 3 | NW alignment vs *E. coli* RelA (P0AG20) | Computational (sequence) | Supports | Subfamily placement | 50.5% to RelA > 41.1% to SpoT; synthetase 58.7% | In silico | High for placement |
| 4 | Catalytic-motif conservation | Computational / evolutionary | Supports | Synthetase active site intact | FDDY metal-binding motif and core conserved | In silico | Moderate–high; no 3D/mutagenesis |
| 5 | HD-motif analysis vs *E. coli* SpoT | Computational / evolutionary | Qualifies (hydrolase only) | Is the HD hydrolase active? | Catalytic His-Asp pair absent; degenerate like *E. coli* RelA | In silico | High; affects GO:0008893, not GO:0008728 |
| 6 | [PMID: 10940009](https://pubmed.ncbi.nlm.nih.gov/10940009/) | Functional (indirect) | Supports | Does relA output raise (p)ppGpp effects? | relA overexpression increased σ54 Pu activity | *P. putida* / *E. coli* reporter | Moderate; physiological, indirect |

---

## GO Curation Implications

- **Focus term GO:0008728 (GTP diphosphokinase activity): RETAIN.** Correctly propagated, appropriately specific, active site intact, correct subfamily. An evidence-code upgrade from IEA is justified given the in-vivo support ([PMID: 29273811](https://pubmed.ncbi.nlm.nih.gov/29273811/)) plus conserved catalytic residues. No generalization, specialization, or sibling replacement needed.
- **Adjacent lead (not the focus term):** If the co-annotated **GO:0008893 (ppGpp 3'-diphosphatase/hydrolase)** is present, it rests on the HD domain whose catalytic His-Asp motif is degenerate/absent in the query (matching hydrolase-dead *E. coli* RelA, not bifunctional SpoT). Suggested action for that sibling term: **remove / treat-as-non-core**, pending experimental confirmation. This is the annotation needing curator scrutiny — not GO:0008728.
- Any propagated CC term such as **GO:0005886 (plasma membrane, IEA:TreeGrafter)** would be a likely over-call for a cytoplasmic ribosome-associated synthetase, but it is outside this focus.
- "Protein binding" is not recommended as any final call; the molecular function is well-defined enzymatically.

---

## Limitations and Knowledge Gaps

1. **No purified-enzyme kinetics for Q88MB8 specifically.** Catalytic competence is inferred from residue conservation and an in-vivo mutant phenotype, not from a direct in-vitro (p)ppGpp-synthesis assay on the *P. putida* protein.
2. **Hydrolase status not experimentally measured** in *P. putida*; the degenerate-HD call is computational.
3. **Substrate preference** (GTP vs GDP; pppGpp vs ppGpp output ratio) was not independently determined.
4. The active-site assessment is sequence/evolutionary; no solved Q88MB8 structure, mutagenesis, or independently rendered AlphaFold geometry was used in this run.
5. **relA vs spoT ambiguity:** *P. putida* encodes both; the query is closer to RelA (50.5% vs 41.1%), consistent with its gene name and a strong-synthetase/weak-hydrolase profile — no conflict for the synthetase term.

---

## Proposed Follow-up Experiments / Actions

1. **In-vitro (p)ppGpp synthetase assay** on purified recombinant Q88MB8 (ATP + GTP/GDP → pppGpp/ppGpp; TLC or HPLC readout) — converts the IEA to direct-assay evidence (IDA) and definitively confirms GO:0008728.
2. **Catalytic-Asp (FDDY) point-mutant complementation** in a ∆relA ∆spoT background, scoring (p)ppGpp-dependent phenotypes (e.g., biofilm dispersal) — links the conserved catalytic residues to in-vivo synthetase function.
3. **In-vitro (p)ppGpp hydrolysis assay** — settles the GO:0008893 co-annotation question; expected negative given the degenerate HD motif.
4. **Curator action:** retain GO:0008728 (consider evidence upgrade); flag GO:0008893, if present, for review/removal; review any CC over-calls.

---

### Bottom line

The TreeGrafter/PANTHER propagation of **GO:0008728 (GTP diphosphokinase activity)** to *P. putida* relA (Q88MB8) is **correct and should be retained**. The protein is a canonical RelA-type (p)ppGpp synthetase with an intact, conserved synthetase active site and in-vivo genetic confirmation of synthetase function; none of the three graft-failure modes (granularity, pseudo-enzyme, mis-placement) apply to the term under test.

---
*Provenance:* UniProt Q88MB8 / P0AG20 / P0AG24 retrieved programmatically; pairwise Needleman–Wunsch alignments and per-domain / catalytic-motif conservation computed in-session (code and outputs retained in the iteration log).


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)