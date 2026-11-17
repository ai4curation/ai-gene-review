---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-11T01:47:54.026807'
end_time: '2026-11-11T02:01:39.301557'
duration_seconds: 825.28
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: GRIN1
  gene_symbol: GRIN1
  uniprot_accession: Q05586
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: free_text
  hypothesis_slug: homomeric-glun1-oocyte-currents-need-xenopus-glun2
  hypothesis_text: The small glutamate- and NMDA-activated, glycine-dependent currents
    recorded from Xenopus laevis oocytes injected with GluN1 (NR1, GRIN1) cRNA alone
    do not come from homomeric GluN1 channels. They come from heteromeric receptors
    formed between the injected GluN1 and an endogenous Xenopus oocyte GluN2-type
    subunit, so GluN1 by itself does not bind glutamate or form a functional glutamate-gated
    channel.
  term_context: '- Term: glutamate binding (GO:0016595)

    - Find the primary evidence for or against an endogenous Xenopus oocyte NMDA receptor
    subunit that pairs with exogenous GluN1 (for example the XenU1 / XenNR2B subunits),
    and whether GluN1 expressed alone is functional in mammalian cells such as HEK293.
    Give PMIDs for each primary study, and say explicitly if the claim is only asserted
    in reviews.'
  reference_context: '- PMID:7685113

    - PMID:7679115

    - PMID:12805203'
  source_file: genes/human/GRIN1/GRIN1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: The small glutamate- and NMDA-activated, glycine-dependent\
    \ currents recorded from Xenopus\n  laevis oocytes injected with GluN1 (NR1, GRIN1)\
    \ cRNA alone do not come from homomeric GluN1 channels.\n  They come from heteromeric\
    \ receptors formed between the injected GluN1 and an endogenous Xenopus oocyte\n\
    \  GluN2-type subunit, so GluN1 by itself does not bind glutamate or form a functional\
    \ glutamate-gated\n  channel.\nfocus_type: free_text\nterm_id: GO:0016595\nterm_label:\
    \ glutamate binding\ncontext:\n- Find the primary evidence for or against an endogenous\
    \ Xenopus oocyte NMDA receptor subunit that pairs\n  with exogenous GluN1 (for\
    \ example the XenU1 / XenNR2B subunits), and whether GluN1 expressed alone is\n\
    \  functional in mammalian cells such as HEK293. Give PMIDs for each primary study,\
    \ and say explicitly\n  if the claim is only asserted in reviews.\nreference_id:\n\
    - PMID:7685113\n- PMID:7679115\n- PMID:12805203"
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
citation_count: 10
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

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** GRIN1
- **Gene symbol:** GRIN1
- **UniProt accession:** Q05586

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** homomeric-glun1-oocyte-currents-need-xenopus-glun2
- **Source file:** genes/human/GRIN1/GRIN1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

The small glutamate- and NMDA-activated, glycine-dependent currents recorded from Xenopus laevis oocytes injected with GluN1 (NR1, GRIN1) cRNA alone do not come from homomeric GluN1 channels. They come from heteromeric receptors formed between the injected GluN1 and an endogenous Xenopus oocyte GluN2-type subunit, so GluN1 by itself does not bind glutamate or form a functional glutamate-gated channel.

## Term and Decision Context

- Term: glutamate binding (GO:0016595)
- Find the primary evidence for or against an endogenous Xenopus oocyte NMDA receptor subunit that pairs with exogenous GluN1 (for example the XenU1 / XenNR2B subunits), and whether GluN1 expressed alone is functional in mammalian cells such as HEK293. Give PMIDs for each primary study, and say explicitly if the claim is only asserted in reviews.

## Reference Context

- PMID:7685113
- PMID:7679115
- PMID:12805203

## Source Context YAML

```yaml
hypothesis: The small glutamate- and NMDA-activated, glycine-dependent currents recorded from Xenopus
  laevis oocytes injected with GluN1 (NR1, GRIN1) cRNA alone do not come from homomeric GluN1 channels.
  They come from heteromeric receptors formed between the injected GluN1 and an endogenous Xenopus oocyte
  GluN2-type subunit, so GluN1 by itself does not bind glutamate or form a functional glutamate-gated
  channel.
focus_type: free_text
term_id: GO:0016595
term_label: glutamate binding
context:
- Find the primary evidence for or against an endogenous Xenopus oocyte NMDA receptor subunit that pairs
  with exogenous GluN1 (for example the XenU1 / XenNR2B subunits), and whether GluN1 expressed alone is
  functional in mammalian cells such as HEK293. Give PMIDs for each primary study, and say explicitly
  if the claim is only asserted in reviews.
reference_id:
- PMID:7685113
- PMID:7679115
- PMID:12805203
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

# AIGR Gene Hypothesis Deep Research — GRIN1 (GluN1/NR1, Q05586)

**Hypothesis slug:** `homomeric-glun1-oocyte-currents-need-xenopus-glun2`
**Focus term:** glutamate binding (GO:0016595)
**Source:** `genes/human/GRIN1/GRIN1-ai-review.yaml` (free-text selector)

---

## Summary

**Executive verdict: PARTIALLY SUPPORTED.** The curation-relevant core of the seed hypothesis is correct and strongly supported by primary evidence, but the specific mechanism the hypothesis proposes for the historical *Xenopus* oocyte observations is refuted (for the named XenU1 candidate) or unsupported (for a hypothetical "XenNR2B").

The **curation-critical claim** — that GluN1/NR1 (GRIN1, UniProt Q05586) **does not bind glutamate** and does not by itself form a functional glutamate-gated channel — is well established by three independent and complementary lines of primary evidence: (1) direct ligand binding, where glutamate binding to the isolated NR1 S1S2 ligand-binding core is "not detectable even at a 300 mM concentration" ([PMID: 16641235](https://pubmed.ncbi.nlm.nih.gov/16641235/)); (2) two X-ray crystal structures that assign the glycine/D-serine site to NR1 ([PMID: 12805203](https://pubmed.ncbi.nlm.nih.gov/12805203/)) and the glutamate site to NR2A ([PMID: 16281028](https://pubmed.ncbi.nlm.nih.gov/16281028/)); and (3) clean mammalian (HEK293) heterologous expression, which lacks endogenous NMDAR subunits, where NR1 expressed alone is electrically silent unless an NR2 subunit is co-expressed ([PMID: 16214956](https://pubmed.ncbi.nlm.nih.gov/16214956/); [PMID: 17105944](https://pubmed.ncbi.nlm.nih.gov/17105944/); [PMID: 11809857](https://pubmed.ncbi.nlm.nih.gov/11809857/)). This directly implies that the GO molecular-function annotation **glutamate binding (GO:0016595) is an over-annotation for GluN1**; the appropriate molecular function for GluN1 is **glycine binding (GO:0016594)**.

The **mechanistic sub-claim** — that the small glutamate/NMDA-activated, glycine-dependent currents historically recorded from *Xenopus laevis* oocytes injected with NR1 cRNA alone (e.g., the human NR1 reports [PMID: 7685113](https://pubmed.ncbi.nlm.nih.gov/7685113/) and [PMID: 7679115](https://pubmed.ncbi.nlm.nih.gov/7679115/)) arise from heteromers between exogenous NR1 and an *endogenous Xenopus* GluN2-type subunit (named in the seed as "XenU1 / XenNR2B") — does **not** survive scrutiny. The proposed partner **XenU1 was experimentally excluded** by two independent primary studies ([PMID: 11809857](https://pubmed.ncbi.nlm.nih.gov/11809857/); [PMID: 16214956](https://pubmed.ncbi.nlm.nih.gov/16214956/)), and XenU1 is in any case a **kainate-binding protein, not a GluN2-type subunit**. A targeted literature search returned **no primary identification** of an endogenous *Xenopus* oocyte "XenNR2B" GluN2 subunit that pairs with exogenous NR1. Thus, although NR1-alone currents are almost certainly **not** from homomeric GluN1 channels (consistent with the direct and structural data above), the **true origin of those oocyte currents remains unresolved**, and the seed's named mechanism should not be adopted as fact.

For a curator, the bottom line is clean and actionable: **remove / do not assign GO:0016595 (glutamate binding) to GluN1**, assign/retain **GO:0016594 (glycine binding)**, and treat the "endogenous Xenopus GluN2/XenNR2B partner" narrative as an unverified hypothesis rather than a citable mechanism.

---

## Key Findings

### Finding 1 — GluN1 (NR1) does not bind glutamate: direct biochemistry plus clean HEK293 functional assays

The most decisive evidence is direct and does not depend on the ambiguous oocyte system. Using a soluble, isolated NR1 S1S2 ligand-binding domain, glutamate binding to NR1 was **"not detectable even at a 300 mM concentration"** ([PMID: 16641235](https://pubmed.ncbi.nlm.nih.gov/16641235/)), an extraordinarily high test concentration that effectively rules out any physiologically meaningful glutamate affinity. In the same body of work, glutamate binds the NR2 subunit and, weakly, the regulatory NR3A subunit — but not NR1.

This biochemical result is corroborated by functional reconstitution in HEK293 cells, a mammalian line that **lacks endogenous NMDAR subunits** and therefore provides a far cleaner test system than *Xenopus* oocytes. In HEK293, NR1 expressed alone does **not** produce a glutamate-gated response: "In HEK293 cells, we did not get receptor response unless an NR2 subunit was coexpressed" ([PMID: 16214956](https://pubmed.ncbi.nlm.nih.gov/16214956/)). A second independent study states the point directly — "NR1 alone, which does not form functional channels" ([PMID: 17105944](https://pubmed.ncbi.nlm.nih.gov/17105944/)). The field consensus architecture — a glycine-binding NR1 paired with a glutamate-binding NR2 — is reiterated across multiple recombinant studies ([PMID: 17962328](https://pubmed.ncbi.nlm.nih.gov/17962328/); [PMID: 20407581](https://pubmed.ncbi.nlm.nih.gov/20407581/)).

**Curation consequence:** glutamate binding is a property of **GluN2**, not GluN1. GO:0016595 on GluN1 is unsupported by direct evidence.

### Finding 2 — The specific XenU1 explanation for NR1-alone oocyte currents is refuted; the endogenous partner's identity is unresolved

The seed hypothesis names XenU1 (and a hypothetical "XenNR2B") as the endogenous *Xenopus* partner. Two independent primary studies directly tested, and rejected, the XenU1 hypothesis. Green et al. (2002) isolated XenU1 and XenU1a cDNAs and found that **co-injection of XenU1 with NR1 did not increase oocyte currents and did not form functional channels in HEK293**, with no pharmacological or biochemical evidence of association — concluding that "**XenU1 does not associate with the NR1 subunit and that an alternative explanation must be sought for the channels observed when NR1 is expressed alone in oocytes**" ([PMID: 11809857](https://pubmed.ncbi.nlm.nih.gov/11809857/)). Schmidt, Werner & Hollmann (2006) revisited the postulated "unitary glutamate receptor," cloned *Xenopus* NR1 variants, and showed that oocyte glutamate/glycine responses "**were independent of coexpressed XenU1**" ([PMID: 16214956](https://pubmed.ncbi.nlm.nih.gov/16214956/)).

Critically, **XenU1 is a kainate-binding protein, not a GluN2-type subunit**, so even its name in the seed hypothesis conflates two distinct molecular entities. A targeted search for a primary report of an endogenous *Xenopus* oocyte GluN2-type subunit ("XenNR2B") that pairs with exogenous NR1 returned **no primary identification**. The seed's mechanistic claim is therefore refuted in its specific (XenU1) form and merely asserted — without primary support — in its generalized ("XenNR2B") form.

### Finding 3 — Crystal structure: the GluN1 ligand-binding core forms the glycine/D-serine site, not a glutamate site

Furukawa & Gouaux (2003) solved co-crystal structures of the NR1 S1S2 ligand-binding core bound to glycine, D-serine, the partial agonist D-cycloserine, and the glycine-site antagonist 5,7-dichlorokynurenic acid. The bilobed "clamshell" domain closes on glycine-site agonists and opens with the antagonist, and the authors state that "**NMDA receptors require both glycine and glutamate for activation with NR1 and NR2 forming glycine and glutamate sites, respectively**" ([PMID: 12805203](https://pubmed.ncbi.nlm.nih.gov/12805203/)). This structurally assigns the **glycine** site to NR1 and complements the direct binding data (Finding 1).

### Finding 4 — The glutamate-binding site is structurally localized to GluN2 (NR2A), not GluN1

Furukawa, Singh, Mancusso & Gouaux (2005) solved the crystal structure of the NR2A ligand-binding core bound to glutamate and the NR1–NR2A heterodimer with glutamate plus glycine. The NR2A–glutamate complex "**defines the determinants of glutamate and NMDA recognition**," confirming the NR1–NR2A heterodimer as the functional ligand-binding unit ([PMID: 16281028](https://pubmed.ncbi.nlm.nih.gov/16281028/)). This directly localizes glutamate binding (GO:0016595) to **GluN2**, completing the structural case: the glutamate site is physically on NR2, not NR1.

---

## Mechanistic Model / Interpretation

The four findings converge on a single, internally consistent model of NMDA-receptor ligand-site architecture and explain why the historical oocyte observations were misleading.

```
            NMDA receptor ligand-binding architecture
            ------------------------------------------

   GluN1 (NR1, GRIN1, Q05586)            GluN2 (NR2A-D)
   ---------------------------           --------------------
   S1S2 clamshell binds:                 S1S2 clamshell binds:
     glycine / D-serine                    GLUTAMATE / NMDA
     (co-agonist site)                      (agonist site)
   GO:0016594 glycine binding  <--      --> GO:0016595 glutamate binding
   Does NOT bind glutamate                  Does NOT bind glycine
   (<none to 300 mM; PMID 16641235)         (PMID 16281028)

   Functional channel = (GluN1)2 : (GluN2)2 heterotetramer
   Requires BOTH co-agonists; NR1 alone is non-functional.
```

Why did NR1-alone oocyte currents ever appear (as in [PMID: 7685113](https://pubmed.ncbi.nlm.nih.gov/7685113/) and [PMID: 7679115](https://pubmed.ncbi.nlm.nih.gov/7679115/))? The seed's instinct is partially right: these currents are almost certainly **not** from homomeric GluN1 channels, because (a) the isolated NR1 domain cannot bind glutamate at all, and (b) in a clean mammalian system without endogenous subunits, NR1 alone is silent. The remaining question — what the exogenous NR1 assembles *with* in the oocyte — was the explicit subject of two follow-up studies, and the leading candidate (XenU1) was excluded. So the model is:

| Claim | Status | Basis |
|---|---|---|
| NR1-alone oocyte currents are from **homomeric GluN1** | **Refuted** | Direct binding (16641235), clean HEK293 silence (16214956, 17105944), structure (12805203, 16281028) |
| The currents require an **endogenous Xenopus partner** | Plausible but **unproven** | Inference from NR1 non-functionality; no partner positively identified |
| The partner is **XenU1** | **Refuted** | Direct tests (11809857, 16214956); XenU1 is a kainate-binding protein |
| The partner is an endogenous **"XenNR2B"** GluN2 | **Unsupported** | No primary report found |
| GluN1 **binds glutamate** (GO:0016595) | **Refuted / over-annotation** | All of the above |
| GluN1 **binds glycine** (GO:0016594) | **Supported** | Structure (12805203), consensus (17962328, 20407581) |

The practical upshot for GO curation is that the over-annotation and the correct annotation can both be resolved independently of ever settling what the oocyte partner was: the direct biochemistry and structures are sufficient.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 16641235](https://pubmed.ncbi.nlm.nih.gov/16641235/) | Direct assay (ligand binding) | **Supports** core (refutes glutamate-binding) | Does NR1 LBD bind glutamate? | Glutamate binding to NR1 "not detectable even at a 300 mM concentration" | Soluble NR1 S1S2 domain, in vitro | High; isolated-domain assay, but concentration tested is decisive |
| [PMID: 12805203](https://pubmed.ncbi.nlm.nih.gov/12805203/) | Structural | **Supports** (NR1 = glycine site) | Which ligand site does NR1 form? | NR1 S1S2 clamshell binds glycine/D-serine; "NR1 and NR2 forming glycine and glutamate sites, respectively" | X-ray crystallography, rat NR1 LBD | High; reference-context PMID |
| [PMID: 16281028](https://pubmed.ncbi.nlm.nih.gov/16281028/) | Structural | **Supports** (glutamate site = NR2) | Where is the glutamate site? | NR2A LBD + glutamate structure; NR1–NR2A heterodimer defines glutamate/NMDA recognition | X-ray crystallography | High |
| [PMID: 16214956](https://pubmed.ncbi.nlm.nih.gov/16214956/) | Direct assay + heterologous | **Supports** core; **refutes** XenU1 mechanism | Is NR1 functional alone? Does XenU1 mediate oocyte currents? | No HEK293 response without NR2; oocyte responses independent of coexpressed XenU1; no "unitary glutamate receptor" | HEK293 + Xenopus oocytes | High; directly addresses the seed |
| [PMID: 11809857](https://pubmed.ncbi.nlm.nih.gov/11809857/) | Interaction/functional | **Refutes** XenU1 mechanism | Does XenU1 associate with NR1? | XenU1 + NR1 gave no increased current, no HEK293 channels; "XenU1 does not associate with NR1" | Xenopus oocytes + HEK293 | High; definitive for XenU1 |
| [PMID: 17105944](https://pubmed.ncbi.nlm.nih.gov/17105944/) | Direct assay (heterologous) | **Supports** core | Is NR1 alone functional in HEK293? | "NR1 alone, which does not form functional channels" | HEK293 (NR1/NR2B toxicity study) | High for the stated point |
| [PMID: 7685113](https://pubmed.ncbi.nlm.nih.gov/7685113/) | Direct assay (electrophysiology) | **Competing / context** | Can NR1 cRNA alone yield NMDA currents? | Human NR1 cRNA in oocytes gave glutamate/NMDA-activated, glycine-dependent currents (interpreted then as homomeric) | Xenopus oocytes, human hNR1 | Historical source of the artifact; interpretation superseded |
| [PMID: 7679115](https://pubmed.ncbi.nlm.nih.gov/7679115/) | Direct assay (electrophysiology) | **Competing / context** | Same as above | Single cloned human NMDAR1 protein in oocytes shows NMDAR-like properties | Xenopus oocytes, human NMDAR1 | Historical source; interpretation superseded |
| [PMID: 17962328](https://pubmed.ncbi.nlm.nih.gov/17962328/) | Consensus + assay | **Supports** (architecture) | Co-agonist subunit assignment | "coagonist glycine-binding NR1 subunits and glutamate-binding NR2 subunits" | Recombinant NMDARs, oocytes | High for architecture statement |
| [PMID: 20407581](https://pubmed.ncbi.nlm.nih.gov/20407581/) | Assay + review | **Qualifies** | Glutamate-independent NR1/NR3 receptors | NR1/NR3 lack glutamate sites, gated by glycine alone; classical NMDARs = glycine-NR1 + glutamate-NR2 | Oocytes | Qualifier: NR1 functions without glutamate site in NR3 context |

---

## GO Curation Implications

**Lead (requires curator verification):** The molecular-function term **glutamate binding (GO:0016595) should NOT be annotated to GluN1/GRIN1 (Q05586)**. If it is currently present, it is an over-annotation and should be **removed or down-qualified**; if proposed, it should be **rejected**.

- **MF — remove/reject:** GO:0016595 *glutamate binding* for GluN1. Direct binding (PMID:16641235), structure (PMID:12805203, 16281028), and clean functional assays (PMID:16214956, 17105944) place the glutamate site on GluN2.
- **MF — assign/retain (more informative replacement):** **GO:0016594 *glycine binding*** for GluN1, supported structurally (PMID:12805203) and by consensus (PMID:17962328, 20407581). This is the correct, specific molecular function and directly replaces the incorrect glutamate-binding term. (Avoids the uninformative "protein binding" fallback.)
- **MF/CC context:** GluN1 is an obligatory subunit of the heterotetrameric NMDA receptor cation channel; GO terms for *glutamate-gated calcium-permeable cation channel activity* and *NMDA receptor complex* (CC) are appropriate for the **complex-level** function, but the glutamate *binding* activity itself belongs to the GluN2 subunits, not GluN1.
- **Provenance caveat:** The historical primary papers that reported NR1-alone oocyte currents ([PMID: 7685113](https://pubmed.ncbi.nlm.nih.gov/7685113/), [PMID: 7679115](https://pubmed.ncbi.nlm.nih.gov/7679115/)) are a likely **database carry-over source** for any glutamate-binding annotation on GluN1. Curators should check whether an existing GO:0016595 annotation traces (via IDA/IMP on these oocyte papers) to that superseded interpretation.

---

## Mechanistic Scope

The immediate molecular function under test is **ligand (glutamate) binding by the GluN1 gene product itself**. The evidence cleanly separates:

- **Direct gene-product activity (GluN1):** glycine/D-serine co-agonist binding (the NR1 S1S2 clamshell) and an obligatory structural/gating role in the heterotetramer. GluN1 does **not** directly bind glutamate.
- **Complex-level / downstream properties:** glutamate-gated cation flux, Ca²⁺ permeability, Mg²⁺ block, and channel gating are **emergent properties of the assembled GluN1/GluN2 heterotetramer**, not of GluN1 alone. The oocyte "NR1-alone" currents are a downstream, system-dependent artifact of expressing NR1 in a cell that may supply an unidentified endogenous partner — not evidence of a GluN1 intrinsic glutamate-binding activity.

Attributing glutamate binding to GluN1 conflates a **complex-level phenotype** (the channel opens to glutamate) with a **subunit-level molecular activity** (which subunit's pocket the glutamate occupies). GO MF annotations should capture the latter.

---

## Conflicts and Alternatives

1. **Historical primary data vs. modern biochemistry.** The 1993 oocyte papers ([PMID: 7685113](https://pubmed.ncbi.nlm.nih.gov/7685113/), [PMID: 7679115](https://pubmed.ncbi.nlm.nih.gov/7679115/)) genuinely recorded glutamate/NMDA-activated, glycine-dependent currents from NR1 cRNA alone and interpreted them as homomeric NR1 receptors. This is the principal conflicting evidence, but the interpretation is superseded: the currents are real, their *homomeric* attribution is not.
2. **Paralog/subunit confusion.** The seed's "glutamate binding" belongs to the **paralogous GluN2** subunits, not GluN1 — a classic subunit-level over-annotation.
3. **Entity confusion in the seed itself.** "XenU1" (a kainate-binding protein) and "XenNR2B" (a hypothetical GluN2) are different molecular classes; the seed treats them as interchangeable candidates. Only XenU1 has been tested (and excluded); "XenNR2B" has no primary report.
4. **Organism-specific expression system.** *Xenopus* oocytes are notorious for endogenous channels/partners; HEK293 (lacking endogenous NMDAR subunits) is the appropriate counter-system and shows NR1 silence — isolating the oocyte result as system-specific.
5. **Isoform qualifier (NR3 context).** NR1/NR3 receptors are glutamate-independent, glycine-gated "excitatory glycine receptors" ([PMID: 20407581](https://pubmed.ncbi.nlm.nih.gov/20407581/)) — reinforcing that GluN1's intrinsic ligand site is for glycine, not glutamate.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters for curation | What would resolve it |
|---|---|---|---|
| Identity of the endogenous *Xenopus* oocyte partner for exogenous NR1 | Targeted PubMed searches for "XenNR2B"/endogenous Xenopus GluN2 pairing with NR1; XenU1 excluded (PMID:11809857, 16214956) | Determines whether the seed's *mechanism* can be cited at all; currently it cannot | Pull-down/MS of NR1 complexes from injected oocytes; RNA-seq of oocyte NMDAR-family transcripts; knockdown of candidate endogenous subunits |
| Current GO annotation status of GO:0016595 on GluN1 in the live GO/UniProt record | Not directly queried in this run (reasoned from primary evidence) | The recommended action (remove vs. reject) depends on whether the term is already present and its evidence code | Query QuickGO/UniProt for Q05586 MF annotations and their evidence/reference IDs |
| Whether any GluN1 glutamate-binding annotation traces to PMID:7685113/7679115 | Inferred as likely carry-over | Identifies the citation to correct | Trace annotation provenance in GO annotation file (GAF) |
| Quantitative affinity of glutamate for NR3A vs. NR1 | Noted qualitatively (glutamate binds NR3A weakly; not NR1) | NR3-containing receptors are an exception to "glutamate on NR2" | Review PMID:16641235 primary binding constants |

**Additional limitations:** This run relied on literature evidence and reasoning; it did not programmatically query the live GO/QuickGO/UniProt annotation record for Q05586, so the precise current annotation status of GO:0016595 on GluN1 is **inferred, not verified**. Some supporting statements (PMID:12805203, 16281028) were taken from provided abstract snippets/reference context rather than re-read full texts in this run. The identity of the endogenous *Xenopus* oocyte partner remains genuinely unknown; no claim is made beyond "not XenU1, and no XenNR2B identified."

---

## Discriminating Tests / Proposed Follow-up Actions

1. **Trace the annotation provenance (highest-value curator action).** Query QuickGO/UniProt for Q05586 and determine whether GO:0016595 is present, its evidence code, and its `with/from` reference. This single check decides remove-vs-reject.
2. **Confirm the direct-binding and structural primaries.** Verify the exact quotes in PMID:16641235 (300 mM glutamate undetectable), PMID:12805203 (NR1 = glycine site), and PMID:16281028 (NR2A = glutamate site) against the full texts.
3. **(If the mechanism must be resolved)** Affinity-purify NR1 complexes from NR1-injected *Xenopus* oocytes and identify co-assembled endogenous subunits by mass spectrometry; complement with oocyte NMDAR-family transcriptome profiling. This would settle the unresolved partner question that the seed guessed at.
4. **Cross-system control.** Reaffirm NR1-alone silence in HEK293 and (ideally) in a second mammalian line to cement that the oocyte current is system-specific.

---

## Curation Leads (require curator verification)

- **Action change:** Remove / do not assign **GO:0016595 (glutamate binding)** to GluN1 (GRIN1, Q05586). Treat as over-annotation at the subunit level.
- **Replacement MF term:** Assign/retain **GO:0016594 (glycine binding)** as GluN1's specific, evidence-supported molecular function.
- **Candidate references with snippets to verify:**
  - [PMID: 16641235](https://pubmed.ncbi.nlm.nih.gov/16641235/) — "binding of glutamate to NR1 was not detectable even at a 300 mm concentration" (direct refutation of glutamate binding).
  - [PMID: 12805203](https://pubmed.ncbi.nlm.nih.gov/12805203/) — "NR1 and NR2 forming glycine and glutamate sites, respectively" (glycine site on NR1).
  - [PMID: 16281028](https://pubmed.ncbi.nlm.nih.gov/16281028/) — NR2A LBD + glutamate structure "defines the determinants of glutamate and NMDA recognition" (glutamate site on NR2).
  - [PMID: 16214956](https://pubmed.ncbi.nlm.nih.gov/16214956/) — "we did not get receptor response unless an NR2 subunit was coexpressed"; oocyte responses "independent of coexpressed XenU1."
  - [PMID: 11809857](https://pubmed.ncbi.nlm.nih.gov/11809857/) — "XenU1 does not associate with the NR1 subunit."
  - [PMID: 17105944](https://pubmed.ncbi.nlm.nih.gov/17105944/) — "NR1 alone, which does not form functional channels."
- **Candidate note for the review's free-text field:** The seed's claim that NR1-alone oocyte currents "come from heteromeric receptors formed between injected GluN1 and an endogenous *Xenopus* GluN2-type subunit" should be flagged as **mechanistically unverified** — XenU1 was tested and excluded, and no "XenNR2B" has been identified in primary literature. The *conclusion* (GluN1 does not bind glutamate / is not functional alone) is correct; the *stated mechanism* is not citable.
- **Suggested curator questions:** (a) Is GO:0016595 currently annotated to Q05586, and via which reference? (b) Does that annotation descend from the 1993 oocyte papers? (c) Is GO:0016594 already present?
- **Suggested experiments (for the record):** MS identification of the oocyte endogenous partner; oocyte NMDAR-family transcriptomics.

---

## Evidence Base (literature summary)

- **Reference-context primaries:** [PMID: 7685113](https://pubmed.ncbi.nlm.nih.gov/7685113/) and [PMID: 7679115](https://pubmed.ncbi.nlm.nih.gov/7679115/) are the historical human-NR1 oocyte reports whose "homomeric" interpretation the hypothesis (correctly) challenges; [PMID: 12805203](https://pubmed.ncbi.nlm.nih.gov/12805203/) is the NR1 glycine-site crystal structure.
- **Decisive refutation of glutamate binding:** [PMID: 16641235](https://pubmed.ncbi.nlm.nih.gov/16641235/) (direct binding) and [PMID: 16281028](https://pubmed.ncbi.nlm.nih.gov/16281028/) (glutamate site on NR2A).
- **Clean-system functional confirmation:** [PMID: 16214956](https://pubmed.ncbi.nlm.nih.gov/16214956/), [PMID: 17105944](https://pubmed.ncbi.nlm.nih.gov/17105944/).
- **XenU1 mechanism refutation:** [PMID: 11809857](https://pubmed.ncbi.nlm.nih.gov/11809857/), [PMID: 16214956](https://pubmed.ncbi.nlm.nih.gov/16214956/).
- **Architecture/consensus:** [PMID: 17962328](https://pubmed.ncbi.nlm.nih.gov/17962328/), [PMID: 20407581](https://pubmed.ncbi.nlm.nih.gov/20407581/).

---

## Conclusion

The hypothesis is **partially supported**: its curation-relevant conclusion (GluN1 does not bind glutamate and is not a functional glutamate-gated channel alone → GO:0016595 is an over-annotation for GluN1; GO:0016594 glycine binding is correct) is strongly supported by direct biochemistry, two crystal structures, and clean HEK293 assays. Its specific mechanistic explanation for the oocyte currents (an endogenous *Xenopus* GluN2 / XenU1 / "XenNR2B" partner) is refuted for XenU1 and unsupported for "XenNR2B," and should be treated as an unverified hypothesis rather than citable mechanism.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)