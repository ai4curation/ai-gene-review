---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-26T20:08:16.290371'
end_time: '2026-10-26T21:03:45.883600'
duration_seconds: 3329.59
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: PRKDC
  gene_symbol: PRKDC
  uniprot_accession: P78527
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: free_text
  hypothesis_slug: prkdc-animal-distribution
  hypothesis_text: 'The efferocytosis-induced macrophage proliferation route senses
    apoptotic-cell DNA through DNA-PKcs (PRKDC). DNA-PKcs orthologs are absent from
    some animal lineages (for example Drosophila melanogaster and Caenorhabditis elegans),
    so this route cannot operate there. Test with one analysis: the phylogenetic distribution
    of PRKDC orthologs (PANTHER PTHR11139:SF68) across metazoan reference proteomes,
    reporting which lineages have lost it.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/PRKDC/PRKDC-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'The efferocytosis-induced macrophage proliferation\
    \ route senses apoptotic-cell DNA through\n  DNA-PKcs (PRKDC). DNA-PKcs orthologs\
    \ are absent from some animal lineages (for example Drosophila melanogaster\n\
    \  and Caenorhabditis elegans), so this route cannot operate there. Test with\
    \ one analysis: the phylogenetic\n  distribution of PRKDC orthologs (PANTHER PTHR11139:SF68)\
    \ across metazoan reference proteomes, reporting\n  which lineages have lost it.'\n\
    focus_type: free_text\ncontext: []\nreference_id: []"
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
citation_count: 2
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
- filename: prkdc_metazoan_phylum_census.csv
  path: openscientist_artifacts/prkdc_metazoan_phylum_census.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist prkdc metazoan phylum census
- filename: prkdc_pthr11139_family_census.csv
  path: openscientist_artifacts/prkdc_pthr11139_family_census.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist prkdc pthr11139 family census
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
- **Gene directory:** PRKDC
- **Gene symbol:** PRKDC
- **UniProt accession:** P78527

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** prkdc-animal-distribution
- **Source file:** genes/human/PRKDC/PRKDC-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

The efferocytosis-induced macrophage proliferation route senses apoptotic-cell DNA through DNA-PKcs (PRKDC). DNA-PKcs orthologs are absent from some animal lineages (for example Drosophila melanogaster and Caenorhabditis elegans), so this route cannot operate there. Test with one analysis: the phylogenetic distribution of PRKDC orthologs (PANTHER PTHR11139:SF68) across metazoan reference proteomes, reporting which lineages have lost it.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'The efferocytosis-induced macrophage proliferation route senses apoptotic-cell DNA through
  DNA-PKcs (PRKDC). DNA-PKcs orthologs are absent from some animal lineages (for example Drosophila melanogaster
  and Caenorhabditis elegans), so this route cannot operate there. Test with one analysis: the phylogenetic
  distribution of PRKDC orthologs (PANTHER PTHR11139:SF68) across metazoan reference proteomes, reporting
  which lineages have lost it.'
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

# PRKDC (DNA-PKcs) — Phylogenetic Distribution & the Efferocytosis Macrophage-Proliferation Route

**Gene:** PRKDC / DNA-PKcs (human) · **UniProt:** [P78527](https://www.uniprot.org/uniprotkb/P78527)
**Family:** PANTHER **PTHR11139:SF68** ("DNA-dependent protein kinase catalytic subunit"); OrthoDB `8724497at2759` (Eukaryota), `5996771at33208` (Metazoa)
**Focus:** free_text hypothesis `prkdc-animal-distribution` · **Taxon:** *Homo sapiens* (NCBITaxon:9606)
**Investigation:** 3 iterations · 4 confirmed findings · 2 primary papers

---

## Summary

**Verdict: Partially supported — the specific loss claim is verified, but the framing over-reaches, and the result is curation-irrelevant for human PRKDC.**

The seed hypothesis bundles an evolutionary claim with a mechanistic premise. The mechanistic premise — that the efferocytosis-induced macrophage-proliferation route involves DNA-PKcs sensing apoptotic-cell DNA — is **supported** by the primary source (Gerlach et al. 2021, [PMID: 34784501](https://pubmed.ncbi.nlm.nih.gov/34784501/)), with one refinement: the activating ligand is **DNase2a-derived nucleotides**, not intact double-strand DNA ends, and DNA-PKcs acts upstream of an **mTORC2/Rictor→Myc** axis in resolving macrophages. The evolutionary claim — that DNA-PKcs is absent from *Drosophila melanogaster* and *Caenorhabditis elegans* — is **directly verified**. However, the implied narrative that absence characterizes "some animal lineages" broadly is **overstated**: DNA-PKcs is an **ancient, metazoan-ancestral gene** retained across nearly all animal clades, with genuine losses confined narrowly to *Drosophila*, *Caenorhabditis*, and (outside animals) budding yeast.

Across three iterations, two independent orthology resources (OrthoDB and a per-organism UniProt/PANTHER PTHR11139 family census) converged on the same picture. The OrthoDB orthogroup places DNA-PKcs in 287 of 5,768 sampled eukaryotes, overwhelmingly single-copy, including non-vertebrate metazoans. The UniProt/PANTHER census then confirmed that fly and worm — both complete, gold-standard genomes — retain the sister kinases of the PIKK family (TRRAP, mTOR, ATR, SMG1) but have specifically lost the DNA-PKcs subfamily (SF68), while the mosquito *Anopheles* (same insect order as *Drosophila*) retains it. A phylum-broad census further showed SF68 present from sponges and cnidarians through most insects, and revealed that earlier OrthoDB insect "absences" (beetle, bee, silkmoth) were **sampling artifacts, not losses**.

**Bottom line for the curator:** this is a genuine and interesting evolutionary observation, but it provides **no basis to add, remove, generalize, or specialize any GO term on human PRKDC**. Ortholog presence/absence in flies and worms is a property of those genomes, not evidence about the human gene product's molecular function, biological process, or cellular component. The item should be logged as **non-core background/evolutionary context**, and the efferocytosis route (Gerlach 2021) treated as a context-specific, downstream role rather than a core human function.

---

## Key Findings

### Finding 1 — DNA-PKcs is an ancient eukaryotic gene lost independently in specific lineages, not vertebrate-restricted

The historical assumption that DNA-PKcs is a vertebrate-specific PIKK arose largely because it is absent from the two most-studied invertebrate models. The orthology data refute this reading. The OrthoDB orthogroup matching PANTHER PTHR11139:SF68 and UniProt P78527 (Eukaryota node `8724497at2759`; Metazoa node `5996771at33208`) has a phyletic profile of **present in 287 of 5,768 sampled eukaryotic species**, and is **overwhelmingly single-copy (283/287)**. Among the metazoan carriers are non-vertebrate representatives such as the cephalochordate *Branchiostoma lanceolatum*, the echinoderm *Acanthaster planci*, and the dipteran insects *Anopheles merus* and *Bradysia odoriphaga*. *Drosophila melanogaster*, *Caenorhabditis elegans*, and *Saccharomyces cerevisiae* are confirmed **absent**.

This broad-but-patchy, single-copy pattern is the hallmark of an ancient gene subject to independent secondary losses, not of a late vertebrate innovation. It is directly corroborated by Lees-Miller et al. 2021 ([PMID: 33035590](https://pubmed.ncbi.nlm.nih.gov/33035590/)), who report that DNA-PKcs "is widely distributed in invertebrates, fungi, plants, and protists." The fly/worm absences are therefore best read as lineage-specific losses against an ancient background — not as evidence of a narrow, derived distribution.

### Finding 2 — The efferocytosis route uses DNA-PKcs to sense DNase2a-derived nucleotides (context-specific, not a new GO assignment)

The mechanistic premise is accurate but requires precision about the stimulus. Gerlach et al. 2021 ([PMID: 34784501](https://pubmed.ncbi.nlm.nih.gov/34784501/)) showed that, after engulfment of apoptotic cells, **nucleotides derived from the hydrolysis of apoptotic-cell DNA by phagolysosomal DNase2a activate a DNA-PKcs–mTORC2/Rictor pathway that increases Myc to promote non-inflammatory macrophage proliferation**. Silencing macrophage DNase2a or Rictor blocked efferocyte proliferation in both a dexamethasone-thymus model and an atherosclerosis-regression model.

Two nuances matter for curation. First, the proximal stimulus is **degraded DNA/nucleotides**, not intact double-strand DNA ends — mechanistically distinct from DNA-PKcs's canonical role binding double-strand breaks during non-homologous end joining (NHEJ). Second, the role is **cell-type- and context-specific** (resolving/efferocytic macrophages), demonstrated in mouse and in vitro. It is a downstream signaling function layered on a specialized cell state, not a constitutive core activity of the gene product.

### Finding 3 — Drosophila and C. elegans absence is a true subfamily-specific loss; mosquito retains it

To exclude the possibility that fly/worm absences were database gaps, an independent census of the ATM-related parent family **PTHR11139** was run per organism via UniProt+PANTHER. Human carries the DNA-PKcs subfamily **PTHR11139:SF68** (P78527, 4,128 aa) alongside mTOR (SF9), ATR (SF69), SMG1 (SF71), and TRRAP (SF1). *Drosophila melanogaster* has **8 PTHR11139 members but zero SF68** (present: TRRAP/SF1, mTor/SF9, Smg1/SF119, ATR/SF69). *C. elegans* has **5 PTHR11139 members but zero SF68** (TRRAP, smg-1, ATR, TOR). Because both genomes are complete and the sister kinases are present, SF68 absence is a **genuine gene loss, not an unsequenced/unannotated genome**.

Critically, *Anopheles gambiae* retains one SF68 member (Q7Q293, 4,191 aa). The DNA-PKcs loss is therefore **lineage-specific within Diptera** — *Drosophila* lost it while mosquitoes kept it — rather than a general feature of flies or insects.

### Finding 4 — DNA-PKcs is ancestral to Metazoa and retained by most insects; verified losses are narrowly restricted

A phylum-broad UniProt+PANTHER PTHR11139 census across 14 additional metazoan proteomes places the origin of DNA-PKcs at the base of the animal tree. SF68 is **present** in the sponge *Amphimedon queenslandica*, the placozoan *Trichoplax adhaerens*, the cnidarians *Nematostella vectensis* and *Hydra vulgaris*, the mollusk *Crassostrea gigas*, the annelid *Capitella teleta*, the echinoderm *Strongylocentrotus purpuratus*, the chelicerate tick *Ixodes scapularis*, the crustacean *Daphnia pulex*, and the insects *Tribolium castaneum* (beetle), *Apis mellifera* (bee), *Bombyx mori* (silkmoth), and *Aedes aegypti* (mosquito). Several of these insects had been **absent from the OrthoDB orthogroup**, confirming those absences were sampling artifacts rather than losses. *Octopus bimaculoides* returned zero PTHR11139 members total (incomplete UniProt proteome), so it is uninformative and must not be scored as a loss.

Taken together, the genuine, verified losses among animals are confined to **Drosophila melanogaster** and **Caenorhabditis elegans** (plus *Saccharomyces cerevisiae* outside the animals) — precisely the historical model organisms that seeded the now-refuted "vertebrate-specific" myth.

---

## Mechanistic Model / Interpretation

The evidence separates cleanly into two threads the seed bundles together: an **evolutionary** thread and a **mechanistic/cell-biological** thread. Keeping them apart clarifies the curation implication.

```
                     ANCIENT EUKARYOTIC / METAZOAN-ANCESTRAL ORIGIN
                                        │
         DNA-PKcs (PTHR11139:SF68) present at the base of Metazoa
         (sponge, placozoan, cnidarian) and broadly retained
                                        │
     ┌──────────────────────────────────┼──────────────────────────────────┐
     │                                   │                                  │
  Deuterostomes                     Protostomes                        Non-bilaterians
  (vertebrates, amphioxus,      (most retain SF68: beetle, bee,        (retain SF68)
   echinoderms — retain)         silkmoth, mosquito, tick,
                                 Daphnia, mollusk, annelid)
                                        │
                              INDEPENDENT SECONDARY LOSSES
                                        │
                        ┌───────────────┴───────────────┐
                 Drosophila melanogaster          Caenorhabditis elegans
                   (0 SF68; 8 family)                (0 SF68; 5 family)
                 [sister Anopheles KEEPS it]
```

**Evolutionary thread.** DNA-PKcs is old, single-copy, and pan-metazoan. The losses in *Drosophila* and *C. elegans* are real but narrow — two convergent, lineage-specific deletions coinciding with the two most popular invertebrate models, which created the false impression of vertebrate specificity. The mosquito/fly contrast within Diptera is the single cleanest demonstration that these are lineage-specific events, not clade-wide absences.

**Mechanistic thread.** In mammals, within efferocytic macrophages, DNA-PKcs senses not intact DNA ends but **DNase2a-derived nucleotides** produced by phagolysosomal degradation of ingested apoptotic-cell DNA, signaling through mTORC2/Rictor to raise Myc and drive non-inflammatory proliferation that resolves tissue injury. This is a specialized, context-dependent signaling role distinct from the canonical NHEJ/DNA-repair function that anchors human PRKDC's core GO annotations.

The seed's logical step — "no DNA-PKcs ⇒ route cannot operate" — is valid for *Drosophila* and *C. elegans*. But as a general statement about "some animal lineages," it is misleadingly broad: the route's molecular hardware is present almost everywhere in animals.

| Thread | Claim | Status | Impact on human PRKDC GO |
|---|---|---|---|
| Evolutionary | Absent in fly and worm | **Confirmed (true loss)** | None |
| Evolutionary | Absent from "some animal lineages" broadly | **Overstated** — losses are narrow | None |
| Evolutionary | Vertebrate-specific | **Refuted** — ancient, pan-metazoan | None |
| Mechanistic | Senses apoptotic-cell DNA in efferocytosis | **Confirmed, with precision** (DNase2a-derived nucleotides) | Context-specific; non-core |

### Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 34784501](https://pubmed.ncbi.nlm.nih.gov/34784501/) (Gerlach 2021) | Direct assay + mutant phenotype | Supports (with refinement) | DNA-PKcs mediates efferocytosis-induced proliferation via apoptotic DNA | DNase2a nucleotides → DNA-PKcs→mTORC2/Rictor→Myc; silencing DNase2a or Rictor blocks proliferation | Mouse resolving macrophages; thymus & atherosclerosis-regression models; in vitro | High for route; ligand is degraded DNA, not dsDNA ends; context-specific |
| [PMID: 33035590](https://pubmed.ncbi.nlm.nih.gov/33035590/) (Lees-Miller 2021) | Structural/evolutionary (phylogenomics) | Qualifies/Refutes framing | DNA-PKcs vertebrate-restricted? | "Widely distributed in invertebrates, fungi, plants, and protists" | Pan-eukaryotic survey | High; authoritative; ancient origin + secondary loss model |
| OrthoDB `8724497at2759` / `5996771at33208` | Computational (orthology) | Supports losses / Qualifies framing | Metazoan distribution of SF68 | Present 287/5768 eukaryotes, 283 single-copy; carriers incl. *Branchiostoma*, *Acanthaster*, *Anopheles merus*; absent fly/worm/yeast | OrthoDB current release | Medium; bird-dominated sampling → absences need per-genome check |
| UniProt+PANTHER PTHR11139 census (fly/worm/mosquito/yeast) | Computational (2nd resource) | Supports losses; resolves sampling caveat | Fly/worm absence real? | Fly (8) & worm (5) carry TRRAP/mTOR/ATR/SMG1 but 0 SF68 (complete genomes → true loss); *Anopheles* retains SF68 (Q7Q293) | UniProt reference entries | High; complete genomes; independent of OrthoDB |
| UniProt+PANTHER census, 14 metazoan proteomes | Computational | Qualifies seed | Metazoan origin & breadth | SF68 in sponge, placozoan, cnidarians, mollusk, annelid, echinoderm, tick, Daphnia, 4 insects; only fly/worm/yeast lost | Pan-metazoan | High; OrthoDB insect absences shown artifactual; octopus uninformative |
| [UniProt P78527](https://www.uniprot.org/uniprotkb/P78527) | Database | Orientation | Family/domain identity | Confirms PTHR11139:SF68; PIKK FAT/FATC/PI3-4 kinase + DNA-PKcs N/CC domains | Human | High; database-level |

### PTHR11139 family census (provenance)

| Organism | Lineage | PTHR11139 members | DNA-PKcs (SF68) |
|---|---|---|---|
| *Homo sapiens* | Vertebrata | 6 subfamilies | **PRESENT** (P78527) |
| *Anopheles gambiae* | Insecta:Diptera | 5 | **PRESENT** (Q7Q293) |
| *Aedes aegypti* / *Tribolium* / *Apis* / *Bombyx* | Insecta | 1 SF68 each | **PRESENT** |
| *Amphimedon* / *Trichoplax* / *Nematostella* / *Hydra* | Non-bilaterian | ≥1 | **PRESENT** |
| *Crassostrea* / *Capitella* / *Strongylocentrotus* / *Ixodes* / *Daphnia* | Protostome/deuterostome | ≥1 | **PRESENT** |
| *Drosophila melanogaster* | Insecta:Diptera | 8 | **ABSENT** (0 SF68) |
| *Caenorhabditis elegans* | Nematoda | 5 | **ABSENT** (0 SF68) |
| *Saccharomyces cerevisiae* | Fungi | 4 | **ABSENT** (0 SF68) |
| *Octopus bimaculoides* | Mollusca | 0 (incomplete proteome) | uninformative |

### GO Decision Table

| GO aspect | Candidate term | Evidence basis | Recommended action (lead) |
|---|---|---|---|
| MF (core) | GO:0004677 DNA-dependent protein kinase activity | Extensive direct biochemistry (out of scope here) | **Retain** — unaffected by this hypothesis |
| BP (route) | regulation of macrophage proliferation / GO:0043277 apoptotic cell clearance | Gerlach 2021, mouse, context-specific | **Non-core**; annotate only with experimental evidence + cell-type qualifier, if at all |
| any | *(ortholog distribution)* | OrthoDB + UniProt/PANTHER census (this work) | **No GO change** — evolutionary context only; at most a taxon-constraint note, never a function assertion |
| MF | protein binding | — | **Avoid** as a recommendation (uninformative) |

---

## GO Curation Implications

**Lead (requires curator verification): treat `prkdc-animal-distribution` as non-core background context, not a GO-term change.**

- The phylogenetic-distribution observation does **not** support adding, removing, generalizing, or specializing any **MF/BP/CC** term on human PRKDC. Ortholog loss in flies/worms is a property of those genomes, not evidence about the human gene product's function.
- The canonical, well-evidenced molecular function — *GO:0004677 DNA-dependent protein kinase activity* — is **retained** and unaffected by this hypothesis.
- If the efferocytosis route were annotated at all, defensible terms (e.g., *GO:0043277 apoptotic cell clearance* or a regulation-of-macrophage-proliferation BP) must carry **experimental evidence codes and a cell-type/species qualifier**, and must **not** be promoted to a core PRKDC function. The stimulus should be described as DNase2a-derived nucleotides, not intact DNA.
- **Do not** use "protein binding" as the outcome; it is uninformative and not what the evidence addresses.

**Net:** log the seed as orientation/mechanistic color; it is not a curation-actionable change to the PRKDC GO set.

---

## Mechanistic Scope

- **Immediate molecular function tested:** DNA-PKcs serine/threonine kinase activity within a signaling cascade (→ mTORC2/Rictor → Myc). The direct gene-product activity is kinase signaling; the actual sensed species are **DNase2a-generated nucleotides**, placing DNA-PKcs downstream of DNA degradation rather than as a primary intact-DNA sensor.
- **Downstream phenotypes (not direct activity):** macrophage proliferation, apoptotic-cell clearance, tissue resolution, plaque stabilization — pathway/organismal outcomes partly inferred from loss-of-function (DNase2a/Rictor knockdown).
- **Evolutionary distribution:** a property of genomes, fully separable from the human gene product's biochemical function.

---

## Evidence Base (Literature)

- *Efferocytosis induces macrophage proliferation to help resolve tissue injury.* **[PMID: 34784501](https://pubmed.ncbi.nlm.nih.gov/34784501/)** (Gerlach et al., 2021). Establishes the efferocytosis-induced macrophage proliferation route and DNA-PKcs's role; clarifies the proximal stimulus is DNase2a-derived nucleotides. Verified snippet: *"nucleotides derived from the hydrolysis of apoptotic cell DNA by phagolysosomal DNase2a activate a DNA-PKcs-mTORC2/Rictor pathway that increases Myc to promote non-inflammatory macrophage proliferation."* **Supports Finding 2.**
- *Uncovering DNA-PKcs ancient phylogeny, unique sequence motifs and insights for human disease.* **[PMID: 33035590](https://pubmed.ncbi.nlm.nih.gov/33035590/)** (Lees-Miller et al., 2021). Shows DNA-PKcs is ancient and broadly distributed, refuting vertebrate specificity. Verified snippet: *"the absence of DNA-PKcs from many model organisms has led to the assumption that DNA-PKcs is a vertebrate-specific PIKK. Here, we find that DNA-PKcs is widely distributed in invertebrates, fungi, plants, and protists."* **Supports Findings 1, 3, 4.**

Public bioinformatics resources used for direct presence/absence calls: OrthoDB (orthogroup `8724497at2759` / `5996771at33208`), UniProt (P78527 and per-organism proteomes), PANTHER family PTHR11139 / subfamily SF68.

---

## Limitations and Knowledge Gaps

1. **Absence calls depend on proteome completeness.** True losses were confirmed only where the genome is complete and sister kinases are present (fly, worm, yeast). Incomplete proteomes (e.g., octopus, 0 family members) are uninformative, not evidence of loss. An exhaustive insect-wide loss map would require a per-proteome HMM sweep against assembled genomes.
2. **Sampling bias in OrthoDB.** The carrier set is bird-dominated; raw counts and clade-level absences must not be over-read. Iteration 3 demonstrated that beetle/bee/silkmoth OrthoDB absences were artifacts corrected by UniProt.
3. **No from-scratch phylogeny.** Conclusions rest on subfamily membership (PANTHER) and orthogroups (OrthoDB), not a maximum-likelihood tree with branch support; headline taxa are robust, but loss-event polarity would be strengthened by a formal reconstruction.
4. **Human-relevance of the efferocytosis route.** Gerlach 2021 is mouse/in-vitro; whether the DNase2a→DNA-PKcs→mTORC2→Myc axis operates identically in human macrophages, and merits a human-gene annotation, is unestablished.
5. **Mechanistic directness.** The proliferation phenotype relies substantially on knockdown of upstream (DNase2a) and parallel (Rictor) nodes; a catalytic-dead vs. kinase-active rescue would establish non-redundant DNA-PKcs requirement.

---

## Proposed Follow-up Experiments / Actions

1. **Genome-level loss confirmation.** Run an HMMER/tBLASTn sweep with the PTHR11139:SF68 HMM against assembled *Drosophila* and *C. elegans* genomes (not just proteomes), and against "absent" taxa like octopus, to separate true loss from annotation gaps. Expected: no SF68 in fly/worm genomic DNA; SF68 recovered in octopus genome. *This is the single most informative confirmatory analysis.*
2. **Formal phylogeny + ancestral-state reconstruction.** Build a PTHR11139 maximum-likelihood tree highlighting SF68 to confirm metazoan-ancestral origin and polarity of the two independent loss events.
3. **Human efferocytosis validation.** Inhibit (NU7441) or knock out DNA-PKcs in primary human efferocytic macrophages; measure Myc induction and proliferation — distinguishes conserved-in-human from mouse-specific.
4. **Stimulus-specificity reconstitution.** Compare DNA-PKcs activation by DNase2a-digested nucleotides vs. intact dsDNA ends to confirm the nucleotide-sensing mechanism.
5. **Curation action.** Mark `prkdc-animal-distribution` as non-core/background; make no GO change on its basis. Candidate references to verify: PMID 34784501 and PMID 33035590 (snippets above). Pose the curator question: is ortholog distribution intended to *scope* a BP annotation (valid as a taxon-constraint note) or to *assert* a function (not valid)? Only the former is defensible.

---

## Provenance

Computed via public OrthoDB REST (`data.orthodb.org/current`) and UniProt REST (`rest.uniprot.org`). Verified facts: PTHR11139:SF68 ↔ P78527; DNA-PKcs orthogroup present in 287 eukaryotic species (283 single-copy); *Drosophila melanogaster*, *C. elegans*, *S. cerevisiae* absent from the orthogroup; invertebrate carriers include *Branchiostoma lanceolatum*, *Acanthaster planci*, *Anopheles merus*, *Bradysia odoriphaga*. UniProt/PANTHER family census confirmed fly (8 members) and worm (5 members) retain TRRAP/mTOR/ATR/SMG1 but zero SF68 (true subfamily-specific loss); *Anopheles gambiae* retains SF68 (Q7Q293); phylum-broad census confirmed SF68 presence from sponges/cnidarians through most insects, with OrthoDB insect absences shown to be sampling artifacts.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist prkdc metazoan phylum census](openscientist_artifacts/prkdc_metazoan_phylum_census.csv)
- [OpenScientist prkdc pthr11139 family census](openscientist_artifacts/prkdc_pthr11139_family_census.csv)