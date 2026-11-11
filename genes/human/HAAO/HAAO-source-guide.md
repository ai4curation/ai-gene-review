# HAAO source guide

## Scope and access

This authored guide records the 2026-11-11 reassessment of human HAAO (UniProtKB:P46952). It is not a provider-generated deep-research report. Falcon returned HTTP 403; the Perplexity-lite fallback returned HTTP 401 with insufficient quota. Manual primary-source reading and database checks therefore support this review. Existing publication caches and inherited `supporting_text` quotations remain unchanged.

All ten PMID identities and titles were checked against NCBI PubMed. Identity verification does not establish every claim attributed to a paper. The reading limits below govern individual annotation decisions. [Source checks and retrieval provenance](HAAO-source-evidence.json) record the supporting observations.

## Human enzyme and pathway evidence

| Source | Evidence read and usable conclusion | Limit |
|---|---|---|
| [PMID:7514594](https://pubmed.ncbi.nlm.nih.gov/7514594/) | Abstract: human cDNA and active recombinant enzyme expressed in HEK293 cells. | Original localization methods were not inspected. The cytosol annotation is retained with curator deference and independent UniProt/Reactome support. |
| [PMID:12007609](https://pubmed.ncbi.nlm.nih.gov/12007609/) | Abstract: purified recombinant human enzyme, Fe(II) requirement and zinc inhibition. | Full original methods were not accessible. The second inhibitory metal is not named in the abstract. Cellular zinc/cadmium-response claims remain UNDECIDED. |
| [PMID:28375145](https://pmc.ncbi.nlm.nih.gov/articles/PMC8493610/) | Original Methods §§2.1–2.5 and Results §§3.1–3.4: human metal-binding structures and biophysical characterization. | The air-prepared crystal contains Fe(III), whereas Fe(II) is the catalytic cofactor. Bacterial mechanistic observations discussed in this paper are distinguished from human experiments. |
| [PMID:28792876](https://pubmed.ncbi.nlm.nih.gov/28792876/) | Abstract and indexed original results: human HAAO variants, reduced catalytic activity and NAD deficiency. | Mouse gestational niacin rescue does not establish human therapeutic rescue. |
| [PMID:2967497](https://pubmed.ncbi.nlm.nih.gov/2967497/) | Abstract: increased enzyme activity in human postmortem Huntington disease tissue. | PMC challenge, publisher 403 and unsuccessful alternative full-text access prevented original causal-evidence review. Neuronal homeostasis remains UNDECIDED. |
| [UniProt P46952](https://www.uniprot.org/uniprotkb/P46952/entry) and [Reactome R-HSA-71218](https://reactome.org/content/detail/R-HSA-71218) | The catalytic reaction produces ACMS; subsequent spontaneous cyclization supplies quinolinate. Curated reaction/localization records place HAAO in cytosol. | Cytosol is established curated localization, not a newly inspected imaging result. Activity of the shorter alternative product was not established. |

The core is one Fe(II)-dependent dioxygenase activity. Quinolinate biosynthesis, NAD+ biosynthesis and tryptophan catabolism describe different pathway roles of that same catalytic step. Fresh QuickGO checks found all five core terms active and no directed `is_a` or `part_of` path between any pair of the three process terms.

## Interaction evidence

The [archived IntAct response](HAAO-interactions.tsv) contains 13 positive HAAO-target records. It is a bounded response, not proof that omitted interactions are absent. Source-paper identifiers and exact partner accessions were checked in the returned rows.

| PMID | Retained partner context | IMEx evidence | Decision |
|---|---|---|---|
| [16189514](https://pubmed.ncbi.nlm.nih.gov/16189514/) | GAD1, Q99259 | IM-16520-414; two-hybrid pooling | KEEP_AS_NON_CORE |
| [25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/) | GAD1, Q8IVA8 | IM-23318-38393; validated two-hybrid | KEEP_AS_NON_CORE |
| [25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/) | GAD1, Q99259 | IM-23318-32712; validated two-hybrid | KEEP_AS_NON_CORE |
| [31515488](https://pubmed.ncbi.nlm.nih.gov/31515488/) | GAD1, Q99259 | IM-27438-3932; two-hybrid array | KEEP_AS_NON_CORE |
| [32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/) | GAD1, Q99259 | IM-25472-131849 and associated screening records | KEEP_AS_NON_CORE |
| [21044950](https://pubmed.ncbi.nlm.nih.gov/21044950/) | POT1, Q9NUX5 | Positive UniProt interaction entry; the paper-specific target/supplementary row was not recovered | UNDECIDED |

Supported generic binding is retained under the [ClinGen project instruction](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions). These interactions do not establish a more specific molecular function. Both partner-accession contexts from PMID:25416956 are retained separately.

## Ontology and propagation checks

- On 2026-11-11 [QuickGO](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034354) marked GO:0034354 obsolete, while the [OLS response](https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0034354) exposed it as non-obsolete. Neither returned a replacement. The incoming IDs and older stored labels are preserved. ACCEPT records the supported biological pathway claim; the authored core uses active GO:0009435.
- [GO:0009055](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009055) includes enzymatic redox reactions. The older draft's electron-carrier-only rationale is withdrawn; the broad annotation is retained as non-core.
- The zinc/cadmium-response terms require a cell or organism response. Purified-enzyme inhibition alone does not resolve those process assertions. GO:0070050 requires maintenance of a stable differentiated neuron; a postmortem association leaves that role unresolved.
- Literal [PTHR15497 PAINT records](../../../interpro/panther/PTHR15497/PTHR15497-paint.tsv) contain the four IBDs at PTN000398325. Target presence among donors is legitimate experimental grounding. No new tree/MSA replay is claimed.
- An inherited family/BNA1 prose defect calls P46952 bacterial NbaC (family review lines 44–45, 64, 80 and 111 at the intake revision). UniProt and the member inventory identify it as human HAAO. This review relies on the literal PAINT records and verified identity, not that authored taxonomic label. Its quoted HAAO summary opening is preserved so existing references remain valid.

## Input conservation

The [literal QuickGO archive](HAAO-context-archive.json) contains 35 current records. Its unchanged production-exporter projection exactly equals the 35-row downloaded TSV. The prior 35 TSV contexts and current 35 contexts share 32, yielding 38 retained review contexts. The older draft had only 34 authored rows; native seeding restored the second PMID:25416956 partner context and added three updated combined-source mappings.

[The context audit](HAAO-context-audit.json) maps every source record to its stored context, identifies the three historical-only mappings, preserves WITH/FROM grouping in the raw archive, and explicitly records the two obsolete-prefix label differences. There are no incoming extensions, isoform-qualified rows or negated rows. No NEW annotation is proposed.

The three historical-only mappings are explicitly marked `retired: true` because their exact source contexts were replaced in current GOA. They remain reviewed and traceable; the lifecycle flag does not reject the underlying catalytic, localization or pathway function.
