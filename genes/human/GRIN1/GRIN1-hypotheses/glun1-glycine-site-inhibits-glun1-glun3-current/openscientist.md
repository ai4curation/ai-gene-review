---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-11T01:31:48.195832'
end_time: '2026-11-11T01:47:37.294215'
duration_seconds: 949.1
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: GRIN1
  gene_symbol: GRIN1
  uniprot_accession: Q05586
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: free_text
  hypothesis_slug: glun1-glycine-site-inhibits-glun1-glun3-current
  hypothesis_text: In heteromeric GluN1/GluN3A and GluN1/GluN3B glycine-gated receptors,
    glycine binding to the GluN1 (GRIN1) subunit reduces the glycine-evoked current
    (auto-inhibition or desensitisation), whereas glycine binding to the GluN3 subunit
    is what opens the channel. That is, occupancy of the GluN1 glycine site is a negative,
    not a positive, regulator of GluN1/GluN3 channel activity, opposite to its role
    in GluN1/GluN2 NMDA receptors.
  term_context: '- Term: glycine-gated cation channel activity (GO:0160212)

    - Decide the sign of the effect of GluN1 glycine-site occupancy on GluN1/GluN3
    receptor current, citing primary experiments (GluN1 glycine-site antagonists such
    as CGP-78608 or MDL-29951, GluN1 ligand-binding-domain mutants such as F484A,
    and structures). State whether the evidence is from recombinant or native receptors
    and whether any study contradicts it.'
  reference_context: '- PMID:26777280

    - PMID:17047094

    - PMID:38598639

    - PMID:11823786'
  source_file: genes/human/GRIN1/GRIN1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: In heteromeric GluN1/GluN3A and GluN1/GluN3B glycine-gated\
    \ receptors, glycine binding to the\n  GluN1 (GRIN1) subunit reduces the glycine-evoked\
    \ current (auto-inhibition or desensitisation), whereas\n  glycine binding to\
    \ the GluN3 subunit is what opens the channel. That is, occupancy of the GluN1\
    \ glycine\n  site is a negative, not a positive, regulator of GluN1/GluN3 channel\
    \ activity, opposite to its role\n  in GluN1/GluN2 NMDA receptors.\nfocus_type:\
    \ free_text\nterm_id: GO:0160212\nterm_label: glycine-gated cation channel activity\n\
    context:\n- Decide the sign of the effect of GluN1 glycine-site occupancy on GluN1/GluN3\
    \ receptor current, citing\n  primary experiments (GluN1 glycine-site antagonists\
    \ such as CGP-78608 or MDL-29951, GluN1 ligand-binding-domain\n  mutants such\
    \ as F484A, and structures). State whether the evidence is from recombinant or\
    \ native receptors\n  and whether any study contradicts it.\nreference_id:\n-\
    \ PMID:26777280\n- PMID:17047094\n- PMID:38598639\n- PMID:11823786"
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
citation_count: 17
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
- **Hypothesis slug:** glun1-glycine-site-inhibits-glun1-glun3-current
- **Source file:** genes/human/GRIN1/GRIN1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

In heteromeric GluN1/GluN3A and GluN1/GluN3B glycine-gated receptors, glycine binding to the GluN1 (GRIN1) subunit reduces the glycine-evoked current (auto-inhibition or desensitisation), whereas glycine binding to the GluN3 subunit is what opens the channel. That is, occupancy of the GluN1 glycine site is a negative, not a positive, regulator of GluN1/GluN3 channel activity, opposite to its role in GluN1/GluN2 NMDA receptors.

## Term and Decision Context

- Term: glycine-gated cation channel activity (GO:0160212)
- Decide the sign of the effect of GluN1 glycine-site occupancy on GluN1/GluN3 receptor current, citing primary experiments (GluN1 glycine-site antagonists such as CGP-78608 or MDL-29951, GluN1 ligand-binding-domain mutants such as F484A, and structures). State whether the evidence is from recombinant or native receptors and whether any study contradicts it.

## Reference Context

- PMID:26777280
- PMID:17047094
- PMID:38598639
- PMID:11823786

## Source Context YAML

```yaml
hypothesis: In heteromeric GluN1/GluN3A and GluN1/GluN3B glycine-gated receptors, glycine binding to the
  GluN1 (GRIN1) subunit reduces the glycine-evoked current (auto-inhibition or desensitisation), whereas
  glycine binding to the GluN3 subunit is what opens the channel. That is, occupancy of the GluN1 glycine
  site is a negative, not a positive, regulator of GluN1/GluN3 channel activity, opposite to its role
  in GluN1/GluN2 NMDA receptors.
focus_type: free_text
term_id: GO:0160212
term_label: glycine-gated cation channel activity
context:
- Decide the sign of the effect of GluN1 glycine-site occupancy on GluN1/GluN3 receptor current, citing
  primary experiments (GluN1 glycine-site antagonists such as CGP-78608 or MDL-29951, GluN1 ligand-binding-domain
  mutants such as F484A, and structures). State whether the evidence is from recombinant or native receptors
  and whether any study contradicts it.
reference_id:
- PMID:26777280
- PMID:17047094
- PMID:38598639
- PMID:11823786
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

# GRIN1 Hypothesis Deep Research — GluN1 Glycine-Site Occupancy Auto-Inhibits GluN1/GluN3 Current

**Gene:** GRIN1 (GluN1 / NR1) · **UniProt:** Q05586 · **Organism:** *Homo sapiens* (NCBITaxon:9606)
**Term under review:** glycine-gated cation channel activity (GO:0160212)
**Hypothesis slug:** `glun1-glycine-site-inhibits-glun1-glun3-current`

---

## Summary

**Verdict: SUPPORTED.** In diheteromeric GluN1/GluN3A and GluN1/GluN3B glycine-gated receptors ("excitatory glycine receptors," eGlyRs), occupancy of the **GluN1 (GRIN1) glycine-binding site is a negative regulator** of the glycine-evoked current. Glycine binding to GluN1 drives auto-inhibition and promotes desensitization of the maximal current (Imax), whereas glycine binding to the **GluN3 subunit is the event that opens the channel**. This is the mechanistic *opposite* of GluN1's role in conventional GluN1/GluN2 NMDA receptors, where GluN1 glycine-site occupancy is an obligatory *positive* co-agonist event. The seed hypothesis is directly affirmed by the primary literature, including all four reference PMIDs supplied in the source context, with no contradicting study identified.

The evidence base is convergent and spans multiple experimental paradigms and both recombinant and native receptors. Pharmacologically, GluN1 glycine-site **antagonists** (CGP-78608, MDL-29951-class competitive antagonists, 7-chlorokynurenate) and GluN1 ligand-binding-domain (LBD) **mutations** that disrupt glycine binding *potentiate* GluN1/GluN3A currents by roughly 10- to 30-fold, converting small, rapidly desensitizing responses into large, stable responses. Conversely, antagonism or mutation of the **GluN3** glycine site *reduces or abolishes* activation. Structural work by cryo-EM (2024–2026) shows that channel gating is driven solely by GluN3A conformational changes, while the glycine-bound/CGP-antagonized state of GluN1 governs entry into (or escape from) the desensitized state. These findings have been reproduced across Xenopus oocytes, HEK293 cells, and native mouse hippocampal neurons.

For GO curation, the specific term under review — GO:0160212 "glycine-gated cation channel activity" on Q05586 — is currently annotated by **ISS (inferred from sequence similarity)**, not by direct experiment. The hypothesis does not argue that GRIN1 lacks a role in a glycine-gated channel; it argues about the *sign* of GluN1 glycine-site occupancy. The channel activity is a property of the **assembled GluN1/GluN3 complex**, and the gating glycine sensor is GluN3, not GluN1. The recommended curation lead is therefore to **retain GO:0160212 as a complex-level / `contributes_to` qualified annotation**, and to ensure GRIN1 is **not** annotated as the activating glycine sensor for this receptor class; a complementary negative-regulation/desensitization annotation better captures GluN1's actual contribution.

---

## Key Findings

### Finding 1 — GluN1 glycine-site occupancy auto-inhibits GluN1/GluN3 current; GluN3 glycine site gates the channel

The central claim of the hypothesis is directly stated and experimentally demonstrated in the primary electrophysiology literature. Madry et al. (2007), in a study explicitly on the "principal role of NR3 subunits," reported that **"glycine bound to the NR1 subunit causes auto-inhibition of NR1/NR3 receptors whereas glycine binding to the NR3 subunits is required for opening of the ion channel"** ([PMID: 17214961](https://pubmed.ncbi.nlm.nih.gov/17214961/)). This is a verbatim statement of the seed hypothesis. The same study provided the quantitative backbone: **"antagonists of and substitutions within the glycine-binding site of NR1 potentiate NR1/NR3 receptor function up to 25-fold, but inhibition or mutation of the NR3 glycine binding site reduces or abolishes receptor activation."** The two glycine sites therefore carry *opposite signs*: disabling GluN1's site potentiates, while disabling GluN3's site abolishes.

This dissociation is reinforced by a compound-level result in native and recombinant systems. Grand et al. (2018) identified **CGP-78608**, a GluN1 glycine-site antagonist, which **"greatly enhances GluN1/GluN3A responses, converting small and rapidly desensitizing currents into large and stable responses"** ([PMID: 30425244](https://pubmed.ncbi.nlm.nih.gov/30425244/)). Critically, the potentiating effect of blocking the GluN1 site was observed not only in recombinant systems but also in **native P8–P12 mouse hippocampal neurons**, establishing physiological relevance beyond artificial expression systems.

The structural capstone comes from cryo-EM across the receptor's functional states. Kim/Gouaux and colleagues (2026) showed that **"glycine activates the receptor solely via GluN3A-dependent conformational changes, opening the gate with two-fold symmetry, and induces a roughly four-fold symmetric desensitized state. CGP-bound GluN1 restricts GluN3A rotation, promoting glycine-induced activation by blocking desensitization"** ([PMID: 42665662](https://pubmed.ncbi.nlm.nih.gov/42665662/)). This provides a physical mechanism: gating is a GluN3A motion, and GluN1 glycine occupancy biases the assembly toward the desensitized (non-conducting) conformation; antagonizing GluN1 (CGP) relieves that bias.

### Finding 2 — All four seed reference PMIDs independently confirm GluN1 glycine-site auto-inhibition

Each of the four references in the source context was resolved and independently supports the negative sign, with no contradiction:

- **Mesic et al. 2016 (Neuropharmacology)** states verbatim: **"Binding of glycine to the high-affinity GluN3 subunits triggers channel opening, whereas glycine binding to the low-affinity GluN1 subunits causes an auto-inhibition of the maximal glycine-inducible receptor current (Imax). Hence, competitive antagonists of the GluN1 subunit strongly potentiate glycine responses of wild type (wt) GluN1/GluN3 receptors."** ([PMID: 26777280](https://pubmed.ncbi.nlm.nih.gov/26777280/)). This is the most explicit statement of the hypothesis and adds the mechanistic nuance that the two glycine sites differ in affinity (GluN3 high-affinity / activating; GluN1 low-affinity / inhibitory).

- **Awobuluyi et al. 2007 (Mol Pharmacol)** adds a mechanistic refinement: **"the apo conformation of NR1 in NR1/NR3 receptors is permissive for receptor activation. Agonist-bound NR1 may also contribute to peak NR1/NR3 receptor currents but specifically enables significant NR1/NR3 receptor current decay under the conditions studied here, presumably via a slow component of desensitization"** ([PMID: 17047094](https://pubmed.ncbi.nlm.nih.gov/17047094/)). This clarifies that the *apo* (unliganded) GluN1 state is permissive for opening, and that liganded GluN1 principally drives current decay (desensitization) — consistent with the negative sign, while noting a context-dependent contribution to peak current.

- **Michalski & Furukawa 2024 (Sci Adv)** provides structural support: cryo-EM of GluN1/GluN3A with the antagonist CNQX versus glycine showed distinct GluN3A orientations between states, and **"Site-directed disruption of the unique subunit interface in the glycine-bound structure mitigated desensitization"** ([PMID: 38598639](https://pubmed.ncbi.nlm.nih.gov/38598639/)). This directly links the glycine-bound conformation to desensitization, i.e., glycine occupancy promotes the inhibited state.

- **Chatterton et al. 2002 (Nature)** is the founding description: NR1/NR3A or NR1/NR3B co-assemble into excitatory glycine receptors "unaffected by glutamate or NMDA, and **inhibited by D-serine**" ([PMID: 11823786](https://pubmed.ncbi.nlm.nih.gov/11823786/)). Because D-serine is a GluN1 glycine-site agonist, its inhibitory action on NR1/NR3 is early, direct evidence that occupancy of the GluN1 site is negative for current.

### Finding 3 — Independent replications and the GRIN1 F484 glycine-pocket residue

The negative sign has been independently replicated beyond the Madry/Mesic lineage. Smothers & Woodward (2009) reported that disrupting GluN1 glycine binding **"produced a greater than 30-fold potentiation of currents during coapplication of glycine and the glycine antagonist 7-chlorokynurenic acid"** in HEK293 cells, and that the effect was NR1 splice-variant-dependent ([PMID: 19726695](https://pubmed.ncbi.nlm.nih.gov/19726695/)). Madry et al. (2008) separately showed ~10-fold potentiation by an NR1 antagonist and supralinear (>120-fold) potentiation when combined with Zn²⁺ ([PMID: 18711142](https://pubmed.ncbi.nlm.nih.gov/18711142/)). The consistency of the direction (potentiation upon GluN1-site blockade) across three independent laboratories and expression systems is a strong convergence signal.

On the molecular anatomy relevant to the hypothesis's cited **F484A** LBD mutant: a direct UniProt REST query of Q05586 (938 aa) confirmed that **residue 484 is a phenylalanine (F)** located in the S1 glycine-binding lobe (sequence context 478-`LVADGKFGTQERVNN`-492). This confirms that the F484A mutation referenced in the hypothesis maps to the human GluN1 glycine-binding pocket, consistent with the experiments that use GluN1 LBD substitutions to disrupt glycine binding and thereby potentiate GluN1/GluN3 current.

The same UniProt record shows that the GO:0160212 annotation on Q05586 carries evidence code **ISS:UniProt** (inferred from sequence similarity), whereas the experimentally supported GO terms on the record include GO:0016594 "glycine binding" (IDA), GO:0017146 "NMDA selective glutamate receptor complex" (IDA), and GO:1905429 "response to glycine" (IDA). The term under curation is therefore an electronic/similarity inference rather than a direct experimental annotation.

---

## Mechanistic Model / Interpretation

The two classes of GluN1-containing NMDA-receptor-family channels invert the role of the GluN1 glycine site:

```
                     GluN1/GluN2 NMDAR                 GluN1/GluN3 eGlyR
                     (conventional)                     (excitatory glycine receptor)

Subunits             2x GluN1 + 2x GluN2                2x GluN1 + 2x GluN3
Gating agonist(s)    glutamate (GluN2) + glycine        glycine ONLY (no glutamate site)
                     (GluN1) — BOTH required

GluN1 glycine site   POSITIVE  (obligatory co-agonist;  NEGATIVE (occupancy drives
                     occupancy REQUIRED to open)        auto-inhibition / desensitization)

GluN3 glycine site   n/a                                POSITIVE (occupancy OPENS the gate)

Effect of blocking   Inhibits / closes channel          POTENTIATES current ~10–30x
the GluN1 site                                          (CGP-78608, 7-Cl-kynurenate,
                                                         F484-pocket mutants)

Effect of blocking   n/a                                ABOLISHES / reduces activation
the GluN3 site
```

A state-based reading reconciles the apparent nuance in Awobuluyi 2007:

```
  apo-GluN1 + glycine-GluN3   --->   OPEN (conducting)      [GluN1 apo is permissive]
                                        |
  glycine binds GluN1          -------->  promotes rotation toward
                                        DESENSITIZED (non-conducting, ~4-fold symmetric)
                                        |
  CGP-78608 bound to GluN1     -------->  restricts GluN3A rotation,
                                        BLOCKS desensitization --> large, stable current
```

In this model, glycine acting at the high-affinity GluN3 site is the gating trigger. Glycine at the lower-affinity GluN1 site is dispensable for opening (apo-GluN1 is permissive) and, when occupied, destabilizes the open state in favor of desensitization, lowering Imax. The GluN1 glycine-site antagonist CGP-78608 clamps the GluN1 LBD in an antagonist-bound conformation that sterically/allosterically prevents the GluN3A rotation underlying desensitization, yielding sustained current. This is a clean, structurally grounded mechanism that unifies the pharmacology (potentiation by GluN1 antagonists), the mutagenesis (potentiation by GluN1 glycine-pocket mutants such as those in the F484 region), and the cryo-EM state assignments.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| [PMID: 17214961](https://pubmed.ncbi.nlm.nih.gov/17214961/) Madry 2007 | Direct assay + mutant | **Supports** | Sign of GluN1 vs GluN3 glycine occupancy | GluN1-bound glycine = auto-inhibition; GluN3 glycine = opening; GluN1 antagonists/mutants potentiate up to 25×, GluN3-site disruption abolishes activation | Recombinant NR1/NR3, Xenopus oocytes | High; recombinant |
| [PMID: 26777280](https://pubmed.ncbi.nlm.nih.gov/26777280/) Mesic 2016 | Direct assay + mutant | **Supports** | Imax auto-inhibition via GluN1 | High-affinity GluN3 triggers opening; low-affinity GluN1 glycine causes auto-inhibition of Imax; GluN1 competitive antagonists strongly potentiate | Recombinant, Xenopus oocytes | High; seed reference |
| [PMID: 17047094](https://pubmed.ncbi.nlm.nih.gov/17047094/) Awobuluyi 2007 | Direct assay + mutant | **Supports (qualifies)** | Role of apo vs agonist-bound GluN1 | Apo-GluN1 permissive for activation; agonist-bound GluN1 enables current decay (slow desensitization); may contribute to peak | Recombinant, oocytes | High; adds nuance on peak contribution |
| [PMID: 38598639](https://pubmed.ncbi.nlm.nih.gov/38598639/) Michalski & Furukawa 2024 | Structural (cryo-EM) | **Supports** | Structural basis of desensitization | Glycine-bound state linked to desensitization; disrupting the glycine-bound subunit interface mitigates desensitization; 1-3-1-3 arrangement | Recombinant GluN1/GluN3A, cryo-EM | High; structural, in vitro |
| [PMID: 30425244](https://pubmed.ncbi.nlm.nih.gov/30425244/) Grand 2018 | Direct assay (pharmacology) | **Supports** | GluN1 antagonist potentiates | CGP-78608 converts small/desensitizing GluN1/GluN3A currents into large/stable responses | Recombinant + **native** P8–P12 mouse hippocampal neurons | High; includes native receptors |
| [PMID: 42665662](https://pubmed.ncbi.nlm.nih.gov/42665662/) Kim/Gouaux 2026 | Structural (cryo-EM) | **Supports** | Which subunit gates; GluN1 role in desensitization | Gating = GluN3A conformational change; CGP-bound GluN1 restricts GluN3A rotation and blocks desensitization | Recombinant GluN1-GluN3A, cryo-EM states | High; structural |
| [PMID: 19726695](https://pubmed.ncbi.nlm.nih.gov/19726695/) Smothers & Woodward 2009 | Direct assay + mutant | **Supports** | GluN1-site disruption potentiates | >30× potentiation with glycine + 7-chlorokynurenate when GluN1 glycine binding disrupted; NR1 splice-variant-dependent | Recombinant, HEK293 | High; independent replication |
| [PMID: 18711142](https://pubmed.ncbi.nlm.nih.gov/18711142/) Madry 2008 | Direct assay | **Supports** | GluN1 antagonist + Zn²⁺ potentiation | ~10× potentiation by NR1 antagonist; supralinear >120× with Zn²⁺; effect mapped to GluN1 LBD | Recombinant, oocytes | High; independent replication |
| [PMID: 11823786](https://pubmed.ncbi.nlm.nih.gov/11823786/) Chatterton 2002 | Direct assay | **Supports** | GluN1-site agonist inhibits | NR1/NR3 glycine-activated; **inhibited by D-serine** (GluN1-site agonist) | Recombinant + cortical neurons | High; founding study |
| [PMID: 32389749](https://pubmed.ncbi.nlm.nih.gov/32389749/) EU1180-438 2020 | Direct assay | **Qualifies** | Allosteric (non-glycine-site) negative modulation | Selective NAM of GluN1/GluN3; active at native GluN1/GluN3A in CA1 neurons | Recombinant + native hippocampus | Orthogonal pharmacology; not glycine-site specific |
| UniProt Q05586 (computational) | Computational / database | **Context** | Residue identity & annotation status | F484 confirmed in GluN1 S1 glycine lobe; GO:0160212 = ISS (not experimental) | REST query | Direct result; database-level |

No study in the reviewed literature (32 papers) contradicts the negative sign of GluN1 glycine-site occupancy for GluN1/GluN3 current.

---

## Evidence Base

The supporting literature forms three mutually reinforcing layers:

1. **Pharmacology/electrophysiology (functional sign).** Madry 2007 ([PMID: 17214961](https://pubmed.ncbi.nlm.nih.gov/17214961/)), Mesic 2016 ([PMID: 26777280](https://pubmed.ncbi.nlm.nih.gov/26777280/)), Madry 2008 ([PMID: 18711142](https://pubmed.ncbi.nlm.nih.gov/18711142/)), Smothers & Woodward 2009 ([PMID: 19726695](https://pubmed.ncbi.nlm.nih.gov/19726695/)), and Grand 2018 ([PMID: 30425244](https://pubmed.ncbi.nlm.nih.gov/30425244/)) collectively establish that blocking or mutating the GluN1 glycine site potentiates current (~10–30×, up to >120× with Zn²⁺), while blocking the GluN3 glycine site abolishes activation. This is the strongest, most direct evidence.

2. **Structural biology (mechanism).** Michalski & Furukawa 2024 ([PMID: 38598639](https://pubmed.ncbi.nlm.nih.gov/38598639/)) and Kim/Gouaux 2026 ([PMID: 42665662](https://pubmed.ncbi.nlm.nih.gov/42665662/)) show the gating motion is GluN3A-driven and that the glycine-bound GluN1 state promotes the desensitized conformation, which CGP-78608 blocks. Native-architecture cryo-EM ([PMID: 42039402](https://pubmed.ncbi.nlm.nih.gov/42039402/)) further corroborates the gating model.

3. **Founding/receptor-identity work and reviews (orientation).** Chatterton 2002 ([PMID: 11823786](https://pubmed.ncbi.nlm.nih.gov/11823786/)) defined NR1/NR3 as excitatory glycine receptors inhibited by D-serine. Reviews (e.g., [PMID: 37248111](https://pubmed.ncbi.nlm.nih.gov/37248111/), [PMID: 27558536](https://pubmed.ncbi.nlm.nih.gov/27558536/)) synthesize eGlyR biology and physiological roles (e.g., ventral hippocampus, medial habenula, anxiety behaviors — [PMID: 40924452](https://pubmed.ncbi.nlm.nih.gov/40924452/), [PMID: 31601771](https://pubmed.ncbi.nlm.nih.gov/31601771/)), providing in vivo relevance but used here only as orientation.

---

## GO Curation Implications

**The term under review:** GO:0160212 "glycine-gated cation channel activity" (MF), currently on Q05586 with evidence code **ISS:UniProt**.

**Lead (requires curator verification):**

- **Retain GO:0160212 as a complex-level, qualified annotation.** The glycine-gated cation channel is a genuine activity of the assembled GluN1/GluN3 receptor, and GluN1 is an obligatory structural subunit of that complex. However, the *gating glycine sensor* is GluN3, not GluN1. The most accurate representation annotates GRIN1 with a **`contributes_to`** qualifier on GO:0160212, acknowledging that the activity belongs to the complex while GluN1 is not the activating ligand sensor.

- **Do not annotate GRIN1 as the positive/activating glycine sensor for this receptor class.** GluN1 glycine-site occupancy is negative (auto-inhibition/desensitization) for GluN1/GluN3 current. An unqualified MF annotation risks implying the GluN1 glycine site drives opening, which is false for GluN1/GluN3 (and opposite to its true role there, though positive in GluN1/GluN2).

- **Consider complementary negative-regulation / desensitization annotations.** GluN1's actual contribution to GluN1/GluN3 physiology is captured by negative regulation of channel activity / promotion of receptor desensitization. A BP term such as "negative regulation of monoatomic cation transmembrane transport" or a desensitization-related term, annotated with `contributes_to`, would more faithfully represent the experimental data (Madry 2007; Mesic 2016; Michalski & Furukawa 2024).

- **Experimental upgrade opportunity.** GO:0160212 is currently ISS. Direct experimental evidence (IDA/IMP) for the complex-level activity exists and could support upgrading the evidence code for the *complex* while keeping the sign caveat for the GluN1 subunit.

This is an **MF**-centered decision with a **BP** complement. "Protein binding" is not an appropriate fallback here — the data support specific channel-activity and regulatory terms.

---

## Mechanistic Scope

The hypothesis concerns an **immediate molecular function**: the effect of ligand occupancy at the GluN1 glycine-binding pocket on ion flux through the assembled GluN1/GluN3 channel. The evidence addresses this directly via (i) competitive antagonists at the GluN1 glycine site (CGP-78608, 7-chlorokynurenate), (ii) point mutations/substitutions in the GluN1 LBD glycine pocket (including the F484-containing S1 lobe), and (iii) cryo-EM conformational state assignments. These are genuine measurements of channel current and receptor conformation — not downstream phenotypes.

Downstream/contextual phenomena that should be kept **separate** from this molecular-function claim include: the physiological roles of eGlyRs in ventral hippocampus plasticity and anxiety ([PMID: 40924452](https://pubmed.ncbi.nlm.nih.gov/40924452/)), aversion control in the medial habenula ([PMID: 31601771](https://pubmed.ncbi.nlm.nih.gov/31601771/)), myelin signaling ([PMID: 20739572](https://pubmed.ncbi.nlm.nih.gov/20739572/)), and non-neuronal contexts (erythroid cells, chondrocytes, heart). These establish in vivo relevance but are not evidence about the *sign* of GluN1 glycine-site occupancy per se.

---

## Conflicts and Alternatives

- **Peak-vs-decay nuance (not a true conflict).** Awobuluyi 2007 ([PMID: 17047094](https://pubmed.ncbi.nlm.nih.gov/17047094/)) notes that agonist-bound GluN1 "may also contribute to peak" current while principally enabling decay/desensitization. This refines, but does not reverse, the negative sign: apo-GluN1 is permissive for opening, and the dominant effect of GluN1 occupancy is desensitization/Imax reduction. Curators should note that "negative" here means suppression of maximal/sustained current, with a possible small positive contribution to transient peak under some conditions.

- **Paralog/subtype context.** The sign is *opposite* in GluN1/GluN2 NMDARs, where GluN1 glycine occupancy is an obligatory positive co-agonist. Any annotation must be subtype-qualified so that the GluN1/GluN3-specific negative role is not generalized to all GluN1-containing receptors, and vice versa.

- **Organism/system generality.** Most mechanistic data are recombinant (Xenopus oocytes, HEK293). Native confirmation exists for the *potentiation-by-GluN1-antagonist* phenomenon (Grand 2018, mouse hippocampal neurons; EU1180-438 at native CA1 GluN1/GluN3A). A caveat: diheteromeric GluN1/GluN3 receptors were historically hard to detect at the surface of mammalian cells ([PMID: 18779583](https://pubmed.ncbi.nlm.nih.gov/18779583/)), so quantitative native parameters remain less characterized than recombinant ones.

- **No contradicting study was found** across the 32 papers reviewed.

---

## Limitations and Knowledge Gaps

1. **Recombinant dominance of mechanistic detail.** The sign and magnitude (10–30×) of GluN1-site effects are best quantified in recombinant systems. *What was checked:* functional and structural primary literature. *Why it matters:* native receptor stoichiometry, triheteromers, and auxiliary factors could modulate the quantitative effect. *Resolution:* systematic native recordings (e.g., CGP-78608 potentiation) across brain regions and developmental stages.

2. **Peak contribution of GluN1 occupancy.** Awobuluyi's observation that agonist-bound GluN1 may contribute to peak current is condition-dependent. *Why it matters:* a blanket "negative" statement slightly oversimplifies. *Resolution:* kinetic modeling / single-channel analysis isolating peak vs steady-state components as a function of GluN1-site occupancy.

3. **F484A-specific data.** The hypothesis cites GluN1 F484A specifically; the knowledge base confirms F484 is in the human GluN1 S1 glycine lobe, but the strongest functional data use a range of GluN1 glycine-pocket perturbations rather than F484A uniquely in the human orthologue. *Resolution:* confirm the exact F484A current phenotype in a primary source and map to human numbering.

4. **GO structure for complex-level, subunit-divergent activity.** GO annotation of a channel activity whose ligand sensor is a *different* subunit than the one being annotated is inherently awkward. *Why it matters:* the sign caveat is easily lost in a bare MF annotation. *Resolution:* adopt `contributes_to` qualifiers and a paired negative-regulation BP term.

---

## Discriminating Tests

The hypothesis is already well supported; the following would most efficiently close residual gaps or stress-test it:

1. **Occupancy-clamped electrophysiology:** Titrate a GluN1-selective glycine-site agonist (e.g., D-serine) against a GluN1-selective antagonist (CGP-78608) at fixed GluN3-site saturation, measuring Imax and desensitization time constants — directly maps the sign and magnitude of GluN1 occupancy vs current.

2. **F484A (human numbering) functional test:** Express human GluN1-F484A / GluN3A and confirm potentiation and loss of desensitization relative to wild type, nailing down the exact residue cited in the hypothesis.

3. **State-resolved structure–function coupling:** Pair cryo-EM desensitized-state capture (glycine-bound GluN1) with interface-disrupting mutations (as in Michalski & Furukawa 2024) and single-channel recordings to quantify how GluN1 occupancy shifts open-probability vs desensitization.

4. **Native-receptor pharmacology panel:** Apply CGP-78608 and EU1180-438 to native GluN1/GluN3A currents across ventral hippocampus, medial habenula, and myelin to confirm the recombinant sign in situ.

---

## Proposed Follow-up Actions / Curation Leads (require curator verification)

**Candidate references with exact snippets to verify:**

- [PMID: 17214961](https://pubmed.ncbi.nlm.nih.gov/17214961/): *"glycine bound to the NR1 subunit causes auto-inhibition of NR1/NR3 receptors whereas glycine binding to the NR3 subunits is required for opening of the ion channel"* — core negative-sign statement.
- [PMID: 26777280](https://pubmed.ncbi.nlm.nih.gov/26777280/): *"glycine binding to the low-affinity GluN1 subunits causes an auto-inhibition of the maximal glycine-inducible receptor current (Imax). Hence, competitive antagonists of the GluN1 subunit strongly potentiate…"*
- [PMID: 30425244](https://pubmed.ncbi.nlm.nih.gov/30425244/): *"CGP-78608 … converting small and rapidly desensitizing currents into large and stable responses"* — antagonist potentiation; native + recombinant.
- [PMID: 42665662](https://pubmed.ncbi.nlm.nih.gov/42665662/): *"glycine activates the receptor solely via GluN3A-dependent conformational changes … CGP-bound GluN1 restricts GluN3A rotation, promoting glycine-induced activation by blocking desensitization"* — structural mechanism.
- [PMID: 17047094](https://pubmed.ncbi.nlm.nih.gov/17047094/): *"the apo conformation of NR1 … is permissive for receptor activation. Agonist-bound NR1 … enables significant NR1/NR3 receptor current decay … via a slow component of desensitization"* — peak-vs-decay nuance.

**Candidate GO actions:**

| Term | Current | Lead action |
|---|---|---|
| GO:0160212 glycine-gated cation channel activity (MF) | ISS, unqualified | **Retain** but add **`contributes_to`** qualifier (complex-level); do not imply GluN1 is the gating glycine sensor |
| Negative regulation of cation transmembrane transport / desensitization (BP) | absent | **Add** as `contributes_to` to capture GluN1's auto-inhibitory role |
| GO:0016594 glycine binding (MF) | IDA | Retain (experimental; accurate for GluN1) |

**Suggested curator questions:**
1. Should a subunit whose glycine site *negatively* regulates a complex-level channel activity carry the channel-activity MF term, or only a regulation term plus `contributes_to`?
2. Can GO:0160212 be upgraded from ISS to an experimental code at the complex level while preserving the subunit-level sign caveat?

**Suggested experiments:** human GluN1-F484A functional confirmation; CGP-78608/EU1180-438 native-tissue panel (see Discriminating Tests).

---

## Bottom Line

The seed hypothesis is **SUPPORTED** by convergent primary evidence (pharmacology, mutagenesis, structure) from recombinant and native receptors, including all four reference PMIDs, with no contradicting study. GluN1 glycine-site occupancy is a **negative** regulator of GluN1/GluN3 current (auto-inhibition/desensitization); GluN3 glycine binding opens the channel — the inverse of GluN1's positive co-agonist role in GluN1/GluN2 NMDARs. For curation, GO:0160212 on GRIN1 is currently ISS and should be retained as a **qualified, complex-level** annotation (`contributes_to`), paired with a negative-regulation/desensitization annotation, and must not portray GluN1 as the activating glycine sensor for this receptor class.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)