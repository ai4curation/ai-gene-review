# Rice momilactone module: curation journal

## 2026-09-12: creation and evidence checks

Created a japonica-rice functional module associated with [MIBiG BGC0000671.3](https://mibig.secondarymetabolites.org/repository/BGC0000671.3/index.html). The curated boundary includes chromosome 4 cluster enzymes and the external P450s needed for momilactone chemistry. The [manual literature report](rice_momilactone_biosynthesis-deep-research-manual.md) records primary studies and supporting passages.

The automated command `just module-deep-research-falcon rice_momilactone_biosynthesis --timeout 300` exited 124 after its time limit and produced no provider report. The manual report is explicitly labeled as manual. Repository `just fetch-pmid` commands subsequently cached the two principal 2021 papers in full, allowing direct inspection of Results and Discussion beyond the initial indexed web passages. Cached publications were not manually edited.

### Verified participant mapping

UniProt REST records were retrieved with `https://rest.uniprot.org/uniprotkb/<accession>.json` on 2026-09-12. Their gene/locus cross-references support the following identities. Roles in the module are supported separately by the cited primary studies, rather than inferred from the displayed protein names.

| Participant | UniProt record | Locus | Cluster relationship |
|---|---|---|---|
| CPS4 | [Q0JF02](https://rest.uniprot.org/uniprotkb/Q0JF02.json) | Os04g0178300 / LOC_Os04g09900 | Chromosome 4 BGC |
| KSL4 | [Q0JEZ8](https://rest.uniprot.org/uniprotkb/Q0JEZ8.json) | Os04g0179700 / LOC_Os04g10060 | Chromosome 4 BGC |
| CYP99A2 | [Q7X7X4](https://rest.uniprot.org/uniprotkb/Q7X7X4.json) | Os04g0180400 / LOC_Os04g10160 | Chromosome 4 BGC |
| CYP99A3 | [Q0JF01](https://rest.uniprot.org/uniprotkb/Q0JF01.json) | Os04g0178400 / LOC_Os04g09920 | Chromosome 4 BGC |
| CYP76M8 | [Q6YTF1](https://rest.uniprot.org/uniprotkb/Q6YTF1.json) | Os02g0569400 / LOC_Os02g36070 | Chromosome 2 diterpenoid BGC |
| OsMAS | [Q7FAE1](https://rest.uniprot.org/uniprotkb/Q7FAE1.json) | Os04g0179200 / LOC_Os04g10010 | Chromosome 4 BGC |
| CYP701A8 | [Q0DBF4](https://rest.uniprot.org/uniprotkb/Q0DBF4.json) | Os06g0569500 / LOC_Os06g37300 | Chromosome 6, outside the BGC |
| CYP76M14 | [Q8LJD2](https://rest.uniprot.org/uniprotkb/Q8LJD2.json) | Os01g0561600 | Chromosome 1, outside the BGC |

The CYP76M14 symbol-to-locus join was independently checked against the [RAP-DB transcript record](https://rapdb.dna.naro.go.jp/transcript/?name=Os01t0561600-01). The three external chromosomal locations are corroborated by [PMID:39887739](https://pubmed.ncbi.nlm.nih.gov/39887739/).

### Second MAS paralog is not fully mapped

[PMID:27337377](https://pubmed.ncbi.nlm.nih.gov/27337377/) links the previously characterized OsMAS/MS1 to clone AK103462, which UniProt explicitly cross-references for Q7FAE1. The paper's MS2 assays used a synthetic construct after cloning failed; its full sequence is in supplementary Data S1. The named clone [AK240900](https://www.ebi.ac.uk/ena/browser/view/AK240900) is partial. [Q7FAE2](https://rest.uniprot.org/uniprotkb/Q7FAE2.json) is an OsMAS2 entry, but the complete experimental construct could not be checked against it because the supplementary download was inaccessible. Numeric MS1/MAS1 and MS2/MAS2 naming is insufficient to resolve the mapping.

Consequently, only **Q7FAE1** grounds the two SDR roles. The second assayed MAS is acknowledged in prose and is not assigned a guessed accession. A genome scan failing to find Q7FAE1 would therefore leave a possible native alternative unresolved. No broad PANTHER family or ancestral node is inferred from these paralogs.

### Reaction and ontology decisions

- CYP99A2 and CYP99A3 are alternatives for the C19 role. Their biochemical capacity does not by itself prove individual dispensability in native rice. [PMID:17872948](https://pubmed.ncbi.nlm.nih.gov/17872948/), [PMID:33793769](https://pubmed.ncbi.nlm.nih.gov/33793769/).
- The C19 aldehyde is hydroxylated at C6, the resulting hemiacetal is oxidized to a lactone, and C3 tailoring generates momilactone A. Spontaneous closure is described without inventing a separate enzyme. [PMID:33793769](https://pubmed.ncbi.nlm.nih.gov/33793769/).
- The optional C20 branch starts from the demonstrated pre-C3 lactone substrate. It combines with shared C3 tailoring to yield momilactone B. Isolated momilactone A is not asserted as a directly assayed CYP76M14 substrate. [PMID:33106662](https://pubmed.ncbi.nlm.nih.gov/33106662/).
- QuickGO term definitions were retrieved from `https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/<GO:id>`. GO:0051498 and GO:0034279 match the two cyclases. GO:0102960 matches C3-alcohol oxidation by the SDR, but not its hemiacetal-to-lactone role. GO:0036209 ends at C19 carboxylate, and GO:0102612 starts with unoxidized syn-pimaradiene; neither matches the represented aldehyde pathway roles. Precise free-text descriptors are retained for these steps.
- The root requires A-producing chemistry; B additionally requires the optional CYP76M14 branch. Connections describe chemical flow, not chromosomal gene order. Presence of a route expresses supported biochemical capacity rather than guaranteed flux or metabolite production in a native plant.

### Validation and review outcome

LinkML structure and custom module validation passed. The custom validator emitted one warning because its OAK taxon adapter was unavailable; a direct query to the [official OLS REST endpoint](https://www.ebi.ac.uk/ols4/api/ontologies/ncbitaxon/terms?obo_id=NCBITaxon%3A39947) independently returned `NCBITaxon:39947` with the exact label `Oryza sativa Japonica Group`. No ontology label was guessed or changed to bypass the warning.

Derived QC found zero terminal nodes lacking a protein grounding. All eight distinct proteins have verified accessions; only CPS4 currently has a local gene review, and that review is complete with its own research. The other seven gene reviews remain separate future curation work. Independent reviews checked biological assertions and module structure; the rendered HTML was inspected for content and template completion.

The Boolean engine evaluates activity availability, not reaction kinetics or physical gene clustering. Its `core_atoms` API intersects activity IDs; a protein used by different alternative activity IDs (here CYP701A8) can be required even when no single corresponding activity ID appears in every route. This was considered in checking the module's route behavior.

## 2026-09-12: module-to-review function compliance

Ran the new deterministic module function compliance check through the module validator and regenerated the module page. CPS4 (`UniProtKB:Q0JF02`) is `CORE_SUPPORTED`: its module assertion `GO:0051498` exactly matches `core_functions[].molecular_function` in `genes/ORYSJ/CPS4/CPS4-ai-review.yaml`. The other seven distinct proteins account for nine `REVIEW_MISSING` activity findings because OsMAS and CYP701A8 each have two explicit roles. Seven of these nine activity assertions also lack a matching GO identifier, as explained above; their precise chemistry remains free text and cannot be checked automatically against GO functions.

There are no detected functional contradictions. Missing reviews are advisory gaps, not evidence that a protein lacks the activity. The new QC panel distinguishes these outcomes; no gene review or biological claim was changed to satisfy the check. LinkML structure validation passed, and custom validation passed with nine function-coverage warnings plus the previously documented unavailable taxon-ontology warning.

## 2026-09-25: PR #3106 review follow-up

Narrowed the title and scope to momilactone A biosynthesis with a documented optional C20 extension. The graph explicitly ends at A and the C20-hydroxylated lactone; it does not encode the unresolved convergence/order required for a complete route to B. Removed the complete heterologous-reconstruction evidence item from the CYP701A8-alone variant, retaining the discriminating cell-free assay in PMID:33793769. Complete reconstruction still supports the pathway-level account, where OsMAS was also present.

Retained CYP99A2 as an experimentally supported alternative after checking the full Results and Methods of [PMID:33793769](https://pubmed.ncbi.nlm.nih.gov/33793769/). Figure 4 separately tests CYP76M8 paired with CYP99A2 or CYP99A3; Figure 5 compares substrate-feeding orders. The study explicitly reports “co-expression of CYP76M8 with CYP99A2 or CYP99A3”. This is separate from the earlier joint-knockdown evidence. The two annoton evidence statements now identify these experiments rather than relying on a general pathway summary.

Recorded the spontaneous hemiacetal-closure gap with chaining_status and chaining_note. Included the six previously fetched, cited publication caches unchanged so the source checks are reproducible offline. The uncited PMID:35781905 cache remains local.

History provenance clarification: the earlier 183848Z record was generated by the helper with its default actor-name (claude-code), while agent-tool was codex; its actor metadata was corrected before commit. The generated filename/session id is preserved as an append-only record. Its empty PR links predate creation of the PR. This follow-up is scaffolded with explicit actor-name codex and PR #3106.
