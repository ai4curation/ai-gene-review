# FAS (CD95/APO-1): biological notes

FAS is a type I cell-surface death receptor for FASLG. Its intracellular death domain recruits FADD into the CD95 DISC, coupling receptor activation to initiator-caspase activation and extrinsic apoptosis. The original APO-1 surface-expression/death experiments and FAS/FADD assembly studies support this mechanism ([PMID:1375228](https://pubmed.ncbi.nlm.nih.gov/1375228/), [PMID:20935634](https://pubmed.ncbi.nlm.nih.gov/20935634/)). FAS is the receptor, not the caspase, kinase or palmitoyltransferase in these pathways.

## Product architecture and measured phenotypes

The [preserved UniProt record](FAS-uniprot.txt) identifies the canonical membrane segment at residues 174–190 and death domain at 230–314. Alternative products are sequence-defined and should not be treated as functionally interchangeable.

| Product | Sequence architecture relative to P25445-1 | Evidence-bound functional interpretation |
|---|---|---|
| P25445-1 | 335 residues; membrane anchor and intracellular death domain | Membrane death-receptor signaling and DISC assembly. |
| P25445-2 (del2/D) | 103 residues; VSP_006481 replaces 66–103; VSP_006482 removes 104–335 | Short soluble product in expression studies; does not preserve the entire canonical ectodomain or intracellular death domain. |
| P25445-3 (del3/E) | 86 residues; VSP_006483 replaces 66–86; VSP_006484 removes 87–335 | Short soluble product in expression studies; no inference of an intact canonical ligand-binding ectodomain. |
| P25445-4 (B) | 149 residues; VSP_006485 replaces 112–149; VSP_006486 removes 150–335 | Soluble-product antagonism is supported within reported expression assays, without a universal sequestration mechanism. |
| P25445-5 (C) | 132 residues; VSP_006487 replaces 112–132; VSP_006488 removes 133–335 | Soluble-product antagonism is supported within reported expression assays; the death domain is absent. |
| P25445-6 (TMdel/A) | 314 residues; VSP_006489 removes 169–189, overlapping most of the membrane anchor; the downstream death domain remains | Soluble-product inhibition is reported, but the contribution of its retained death-domain sequence is not established by topology alone. |
| P25445-7 (FasExo8Del) | 220 residues; VSP_045235 changes 218–220 and VSP_045236 removes 221–335; membrane segment remains, death domain is lost | A dominant-negative phenotype was reported in mutation-bearing HUT78 lymphoma clones; this is neither an uncharacterized product nor evidence for universal normal-tissue expression. |

The source features and product identities are visible under ALTERNATIVE PRODUCTS, TRANSMEM, DOMAIN and VAR_SEQ in [UniProt P25445](https://www.uniprot.org/uniprotkb/P25445/entry). The table states sequence consequences separately from experimental function. The seven product objects in the review are preserved.

Human soluble-product expression studies report inhibition of apoptosis. [PMID:7533181](https://pubmed.ncbi.nlm.nih.gov/7533181/) studies FasTMDel, FasDel2 and FasDel3 transcripts and COS-cell expression; its accessible original abstract does not resolve every receptor-activity or localization claim. [PMID:8648105](https://pubmed.ncbi.nlm.nih.gov/8648105/) reports inhibition of both antibody- and natural-ligand-induced apoptosis by five soluble variants. That positive phenotype does not establish direct ligand sequestration as the common mechanism. The full original [PMID:7575433](https://pubmed.ncbi.nlm.nih.gov/7575433/) distinguishes transcript abundance, undetectable minor protein products and predicted ligand-binding consequences; a prediction is not a negative binding assay. [PMID:8598453](https://pubmed.ncbi.nlm.nih.gov/8598453/) specifically identifies a deletion-insertion mutation producing FasExo8Del in resistant HUT78 clones. The original abstracts, rather than full operative bodies, were accessible for the other three papers.

## Assembly, membrane compartments and conditional outputs

Receptor self-association and signaling-complex formation are supported by distinct assays. Human BEAS-2B experiments show FAS multimer formation in a hyperoxic CAV1-associated context ([PMID:21382479](https://pubmed.ncbi.nlm.nih.gov/21382479/)); the original RIP discovery abstract explicitly identifies FAS itself as an interacting intracellular-domain product ([PMID:7538908](https://pubmed.ncbi.nlm.nih.gov/7538908/)). The positive IntAct FAS–FAS record for [PMID:7536190](https://pubmed.ncbi.nlm.nih.gov/7536190/) is retained, but its operative self-binding experiment was not readable. The old quotation about FADD self-association does not independently establish FAS self-binding.

FAS participates in dynamic raft and non-raft membrane pools. Ligand-stimulated human receptor immunoprecipitation and gradient experiments support DISC association, without proving purified binary contact for every pair ([PMID:17159907](https://pubmed.ncbi.nlm.nih.gov/17159907/)). Human surface-labeling and fractionation experiments support membrane location and redistribution ([PMID:25301068](https://pubmed.ncbi.nlm.nih.gov/25301068/)). The concise core location is plasma membrane; positive raft annotations remain, without an exclusive raft claim.

Conditional responses do not confer another protein's catalytic activity on FAS. Original HeLa experiments show ASK1/JNK activation after FAS ligation during glutamine deprivation and ERK activation in both glutamine conditions ([PMID:11096076](https://pubmed.ncbi.nlm.nih.gov/11096076/)); this remains an apoptotic context, not evidence of direct nutrient sensing. The original glioblastoma abstract reports FASLG-induced YES1/PI3K recruitment and invasion ([PMID:18328427](https://pubmed.ncbi.nlm.nih.gov/18328427/)); it does not verify the separately imported SRC, FADD or CASP8 interaction contexts. FAS-peptide SPR and structure 3EWT support calmodulin binding, while full-receptor stoichiometry and universal regulation are outside the accessible evidence ([PMID:24914971](https://pubmed.ncbi.nlm.nih.gov/24914971/)).

The proposed isoform questions ask how the TMdel architecture contributes to the measured protective phenotype and whether the FasExo8Del tumor-cell result generalizes to other defined contexts. They do not assert that these products have never been assayed or that a comprehensive later-literature search established their mechanisms as globally unknown. The [source guide](FAS-source-guide.md) records access boundaries, source-specific uncertainty and the current ontology proposal.

## Historical journal

The entries below preserve earlier review history. Their source counts, lane terminology, old binding policy and pending-integration statements describe earlier stages. The biological account and architecture table above, the current source guide and current annotation reasons supersede conflicting historical interpretations.

## 2026-09-30 APOPTOSIS generic-binding cleanup

`just fetch-gene human FAS` appended 17 partner-specific `GO:0005515` rows
that were split out from IntAct/UniProt imports already represented by older
generic rows:

- Tightened canonical DISC-context rows with CASP8 or FADD support
  (PMIDs 11717445, 16498403, 17159907, 21382479, 21625644) to FAS
  `GO:0005031` receptor activity, matching the existing core function.
- Removed the NAS `cytosol` row sourced to PMID:7533181 because the paper
  supports secreted soluble FAS splice isoforms rather than cytosolic FAS.
- Left abstract-only rows `UNDECIDED` where the cached abstract did not verify
  the exact partner imported by IntAct: the TNFR1-specific PMID:12887920 row,
  the FADD/CASP8 rows from the CD95/Yes/PI3K glioblastoma paper
  (PMID:18328427), PMLRARalpha rows whose partners were not evident in
  PMID:21803845.
- Removed generic `protein binding` rows for non-core inhibitory cap proteins
  from PMID:18846110, the direct PMLRARalpha inhibitory interaction from
  PMID:21803845, the FADD/DAXX rows from the proximity-ligation screen
  (PMID:25241761), and the BioPlex AP-MS FAS-CASP8 row from PMID:33961781
  because none supports a more informative FAS-side molecular function.


## Direct-source reassessment (2026-10-26)

The current direct-source reassessment covers all42 present PMID groups plus the historical PMID:11717445 FAS–FADD/caspase8 contexts. Those historical positive associations remain valid records despite their absence from current imports. The source guide and exact partner table document operative evidence, assay boundaries and inaccessible contexts. Supported generic protein interactions are retained as non-core under the standing ClinGen project instruction. No molecular function is inferred merely from a partner name, and DISC cellular components are not substituted for molecular-function binding annotations.

FAS activity is refined to death receptor activity rather than literal TNF cytokine receptor activity. Original receptor-complex experiments support the CD95-specific DISC, and the relevant broad signaling assertion is refined to FAS signaling. Inaccessible exact SRC/FADD/caspase8 assays, source-specific self-association, exosome target identification, mechanical-stimulus support and soluble-paper cytosol/receptor contexts remain undecided. Earlier assertions of absence or generic-binding exclusion in these notes are historical reasoning superseded by the explicit current reviews.

All113 inherited annotation source objects,78 quotation paths and reference associations, seven products, inherited core/description/status and unowned reviews are preserved in this direct lane. The inherited all-soluble-products death-domain claims require a separate correction: current UniProt isoform6 retains the death domain, while isoform7 retains the membrane segment but lacks the death domain. Other soluble truncations need their own ligand-binding evidence. Sequence topology and predicted consequences must not be represented as measured isoform function. No new quotation, guessed mature product, natural isoform assignment or NEW annotation is proposed here.


# FAS database review — 2026-10-26

This is an appendable database-lane note, not a replacement for historical notes. Earlier blanket claims that all soluble products lack the intracellular/death domain or that only isoform 1 contains a membrane anchor are superseded by the accepted official sequence reconstruction. Existing product objects are unchanged here; ROOT owns their reconciliation.

Manual scope: 36 inherited database rows (32 current plus four historical), one separate fresh current context 62, and 20 complete database-reference successor objects. Current actions: 27 ACCEPT, four KEEP_AS_NON_CORE, two MODIFY. Historical actions: three ACCEPT and calmodulin binding KEEP_AS_NON_CORE. No REMOVE, authored NEW, added quote, or source-field mutation. All 77 inherited direct rows remain identical.

Actual phylogeny, IBD and donor assays were considered, including legitimate human self-WITH. The source-scope problem for GO:0005031 is literal TNF cytokine specificity, not orthology. Human CD95 stimulation and FAS/FADD assembly support death receptor activity; GO:0036337 captures the receptor's pathway. The retained provider and superfamily quotations remain historical context and are not independent evidence of TNF cytokine binding.

The official GO_REF:0000043 method restriction to viruses provides a genuine lifecycle consideration for historical human old11. Fresh62 replaces the provenance combination of old14 at the same apoptotic-process assertion. In contrast, old17 and old20 still have matching current ARBA rules. `lifecycle-proposal.json` offers explicit alternatives without automatically retiring any source to satisfy validation. Current absence does not mean the biology is false. Old27/96 are direct-lane historical sources and were not altered.

Source acquisition reused accepted caches byte-for-byte. Ten missing donor/corroboration PMIDs were genuinely fetched after an exact-head/base open-PR ownership inventory. The selected PTHR46874 entries/metadata remain the accepted main bytes; the timestamp-only fresh metadata stays private. No source is installed canonically by this packet.

The actual murine soluble FasB original was finally recovered through the author's uploaded article text after preserved PMC/PDF access failures. Read scope is explicit, not retrospectively labeled complete. The article's positive conditioned-medium effect is retained without claiming direct ligand sequestration or equivalence to each human natural product. Likewise the necroptosis donor paper's human FAS construct in mouse L929 cells is stated accurately.

Schema and exact reference validation are checked in a new isolated frozen runtime. The legacy-only candidate intentionally retains inherited source history and leaves fresh source adoption to integration. Its strict GOA/focused coverage failures therefore expose the known four current additions and six historical absences; the separate 111-context current projection passes strict GOA. No historical object or source code was rewritten to hide that difference.


## ROOT integration preparation (2026-10-26)

The sections above preserve the earlier source-specific review record. The proposed integration combines all 113 inherited source contexts and appends the four exact fresh contexts in fresh order. Six historical contexts retain their reviewed biology and evidence, with retirement scoped only to absence from the pinned current GOA snapshot; the marker is not a claim of biological invalidity or official withdrawal. The ROOT description, product, functional-class and core successors supersede the earlier pending-integration statements. All seven product identities, names and sequence notes and all 78 inherited supporting-text anchors are preserved. No new supporting text is introduced.

The shared PMID:25301068 assessment preserves both complete source-review notes. Normal-source selection retains 75 exact files; all 64 shared-path versions have identical hashes and modes. This preparation does not claim a completed whole-gene review. The candidate is provisional DRAFT until ROOT runs integrated validation and computed-status checks.

## 2026-10-26 — Product synthesis and preserved source boundary

The seven official product sequences have lengths 335, 103, 86, 149, 132, 314 and 220 residues. Isoform 6 removes the membrane-anchor region while retaining the death-domain sequence; isoform 7 retains the membrane segment and loses the death domain. Soluble-product antagonism is documented in expression assays without assigning a universal FASLG-sequestration mechanism. The FasExo8Del evidence is from lymphoma cells. Primary evidence and access limits are summarized in the source guide.

The existing UniProt cache remains byte-identical. Its sequence, product identities and variant edits agree with the fresh official record used for the architecture check; that newer record remains private evidence. The fresh GOA snapshot is adopted explicitly. Six historical contexts retain their source data, positive or uncertain scientific reviews and inherited quotations; their retired markers concern this snapshot’s active set, not official withdrawal or biological falsity.

Final synthesis also refines the broad InterPro signal-transduction assertion (historical index 16, current index 67) to Fas signaling, consistently with the literature-source refinement. The two fresh PMID:25301068 localization assertions carry reference-only support links; no quotation is added.

## 2026-10-26 — Canonical validation

All seven canonical checks pass: status update, standard validation, strict GOA matching, ontology terms, component checks, computed status and rendering of 236 narratives. DRAFT status retains 38 accounted advisories: 37 supported generic-binding cases under project policy and one intentional receptor-source MODIFY/UNDECIDED distinction. The existing UniProt cache, 75 normal dependencies, prior history and inherited HTML remain exact. Thirteen normal dependencies are genuine additions; the fresh GOA snapshot is adopted explicitly. Both evidence tables and a source guide document assay scope. Rendered HTML was checked privately. Unrelated workspace edits remain unchanged.

## 2026-10-26 — Authored record format

The interaction and database-decision tables are now YAML, following the repository rule for authored structured records. All 40 interaction records and 36 database records retain their field values and order. The source guide points to the YAML files; earlier notes describe the superseded TSV representation. Annotation decisions, source fields, normal caches, all 78 inherited quotations and product/core summaries are unchanged. The seven canonical checks and 236-narrative render remain applicable to the byte-identical main review.
