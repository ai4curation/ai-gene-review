# BCAP31 Review Notes

## Gene Identity

- Human BCAP31 encodes B-cell receptor-associated protein 31, also known as BAP31, UniProt P51572.
- The UniProt record describes BCAP31 as a 246 aa, reviewed Swiss-Prot ER membrane protein with three transmembrane segments and a cytosolic C-terminal domain. UniProt summarizes it as a chaperone protein involved in ER export, recognition of abnormally folded proteins, ERAD targeting, and TOMM40-dependent mitochondrial complex I assembly [UniProt:P51572 "Functions as a chaperone protein"].

## Core Functional Picture

BCAP31 is best curated as an ER-resident membrane protein-sorting factor with three linked roles:

1. ER cargo selection and export of selected membrane proteins.
2. ER quality control and ER-associated degradation of misfolded membrane proteins.
3. ER-mitochondria contact site function that supports mitochondrial complex I component import.

The ERAD role is directly supported by the Cell paper showing that BAP31 binds Sec61beta and TRAM, associates with CFTRDeltaF508, and promotes retrotranslocation and proteasomal degradation [PMID:18555783 "BAP31 is an endoplasmic reticulum protein-sorting factor"; PMID:18555783 "promotes its retrotranslocation from the ER and degradation by the cytoplasmic 26S proteasome system"]. This supports keeping the positive regulation annotations and adding the direct ERAD pathway annotation (GO:0036503).

The ER-mitochondria contact role is supported by the Tom40 study: BAP31 forms an ER-mitochondria bridging complex and stimulates NDUFS4 translocation to mitochondria for complex I assembly [PMID:31206022 "BAP31 acts as a key factor in mitochondrial homeostasis"; PMID:31206022 "interacts with mitochondria-localized proteins, including Tom40"]. This supports the MAM localization and protein localization to mitochondrion annotations as core/non-incidental.

## Localization Calls

The primary localization is ER membrane. The early BAP31 paper identifies p28 Bap31 as a polytopic ER protein [PMID:9334338 "polytopic integral protein of the endoplasmic reticulum"], and UniProt also states ER membrane plus ERGIC/cis-Golgi shuttling [UniProt:P51572 "May shuttle between the ER and the intermediate compartment/cis-Golgi complex"].

ERGIC/Golgi membrane annotations are acceptable as trafficking-related localizations, but ER membrane is the core site. Lipid droplet annotation is treated as non-core because the cited study is a lipid droplet fraction proteomics experiment in HuH7 cells, not a mechanistic BCAP31 localization paper [PMID:14741744 "a fraction enriched with lipid droplets was isolated"]. Plasma membrane remains undecided because the original surface-antigen study supports antibody-accessible surface expression [PMID:8706661 "expression of a 28-kDa surface protein"], but later work establishes ER/ERGIC residency as the primary biology.

## Apoptosis Annotations

BCAP31 is a caspase substrate and ER-mitochondria apoptosis platform component, but broad apoptosis annotations overstate the intact protein's core function. The original Bap31 apoptosis paper shows caspase cleavage and the p20 fragment, not a constitutive apoptotic regulator function for intact BCAP31 [PMID:9334338 "cleavage of p28 at the two caspase recognition sites"; PMID:9334338 "p20 fragment induces apoptosis"]. The Fis1 paper similarly frames the event as Fis1 facilitating Bap31 cleavage into p20Bap31 [PMID:21183955 "facilitating its cleavage into the pro-apoptotic p20Bap31"].

Therefore:

- Broad apoptotic process and positive regulation of intrinsic apoptotic signaling pathway are marked over-annotated.
- ER-mitochondria contact and stress sensor annotations from PMID:31206022 remain supported.

## Protein Binding Annotations

Generic protein binding rows should be removed. BCAP31 has many real interactors, including Sec61beta, TRAM, Derlin-1, CFTR, BCL2, CASP8, Fis1, TOMM40, and viral SH protein, but GO:0005515 does not capture the function. The biologically informative terms are ERAD pathway/regulation, retrograde ER-to-cytosol transport, ER-to-Golgi transport, MHC class I protein binding, MAM localization, and mitochondrial protein localization.

## New Term Rationale

GO:0036503 ERAD pathway is justified because the strongest mechanistic evidence places BCAP31 directly in the ERAD substrate-handling pathway rather than only upstream regulation. PMID:18555783 shows BCAP31 associating with the misfolded CFTRDeltaF508 substrate, Sec61 translocon components, and Derlin-1, and reducing BAP31 reduces proteasomal degradation [PMID:18555783 "Depletion of BAP31 reduces the proteasomal degradation of DeltaF508"; PMID:18555783 "associates physically and functionally with the Derlin-1 protein disclocation complex"].

## Open Questions

- Which BCAP31 client proteins are physiologically most important in neurons and oligodendrocyte lineage cells affected in DDCH syndrome?
- Can separation-of-function variants distinguish the ERAD/cargo-export role from the TOMM40/MAM mitochondrial homeostasis role?
- Are the apoptosis annotations better represented by annotations to the p20 cleavage product context, or should they remain pathway-context-only references rather than BCAP31 core function terms?

## Resolution Notes

- The plasma membrane (`GO:0005886`) call referenced under "Localization Calls" was resolved as `MARK_AS_OVER_ANNOTATED` in PR #317. The PMID:8706661 surface-antigen detection is real but represents a trafficking intermediate / overexpression artifact in transfected cells; later work establishes ER/ERGIC residency as the primary biology, consistent with the cytoplasmic KKXX retrieval motif.
- The clathrin-coated vesicle (`GO:0030136`) IEA was resolved as `MARK_AS_OVER_ANNOTATED` in the same PR — Ensembl rat transfer with no human-specific support, and BCAP31 traffics via COPI/COPII machinery rather than the clathrin pathway.

## Re-review prompted by geneontology/go-annotation#6385 (2026-05-22)

GO curators raised a PAINT issue (PANTHER:PTN000294723) questioning the
`involved_in GO:0006888 endoplasmic reticulum to Golgi vesicle-mediated transport`
IBA on human BCAP31 and its orthologs, plus `GO:0070973 protein localization to ER
exit site` on the *S. pombe* ortholog SPAC9E9.04. The curator argument is that
BCAP31 acts *upstream* of the ER exit site as a quality-control / translocation
chaperone, so the anterograde-transport IBA is an erroneous over-propagation:

- Engagement begins at the earliest folding steps (heavy chain + β2-microglobulin
  association for MHC class I), far upstream of any exit-site decision.
- BCAP31 knockout only *delays*, does not abolish, surface class I export.
- The C-terminal KKXX dilysine motif is a COPI retrieval signal (retention), not
  an anterograde export signal.

Curator M. Feuermann (GO_Central PAINT) commented (2026-05-21) that the family
lacked the right terms and recommends MF `GO:0140388 protein translocation
chaperone activity`; he is re-annotating the family. Curator V. Wood notes the
core biology is BAP31 interacting with Sec61 translocons and promoting
retrotranslocation of CFTRΔF508 via the Derlin-1 complex (PMID:18555783).

Actions taken in this review update:
- `GO:0006888` and `GO:0070973`: `ACCEPT` → `MARK_AS_OVER_ANNOTATED`.
- `core_functions` entry 1: MF changed `GO:0140597 protein carrier activity` →
  `GO:0140388 protein translocation chaperone activity`; `directly_involved_in`
  changed `GO:0006888` → `GO:0036503 ERAD pathway`; "cargo receptor" framing
  removed in favour of translocon-associated chaperone framing.
- `description` and several annotation `reason` fields reworded to drop the
  "cargo receptor" characterization.
## Source-complete BCAP31 reassessment

The normal projection contains 61 distinct source assertions from 64 raw rows, including eight previously omitted partner records and three exact duplicate raw records. All source identities, qualifiers and partners are retained. Three old authored NEW entries are assessed separately; their proposed withdrawal removes no GOA assertion.

This reassessment supersedes the earlier substrate-only apoptosis rationale. Intact BCAP31 helps assemble the FIS1/procaspase-8 signaling platform, and a cleavage product can transmit a signal. The carrier role is grounded in client binding/delivery, while an intrinsic ATP-dependent ratchet has not been established by the available evidence. The two disputed PAINT trafficking assertions remain unresolved; the real curator issue and positive MHC-I experiments must both be represented.

The rat clathrin transfer is contradicted by the cited donor fractionation experiment. In contrast, the experimental cell-surface and lipid-droplet annotations are retained as secondary contexts without speculative artifact explanations. Mouse spermatogenesis remains unresolved because the traced evidence is an expression survey whose BCAP31-specific body evidence was not inspected.

Reactome's cytosolic cleavage entity is the terminal 238–246 fragment, not p20. The two machine-derived UniProt alternative products are a separate splicing record and do not imply RefSeq-numbering equivalence or isoform-specific function.

Supported generic interactions are kept as non-core under the user-supplied ActionEnum. The CFTR client and the separate FIS1/CASP8 platform rows receive evidence-specific refinements; machinery, combined-partner and high-throughput records are not indiscriminately relabeled. No NEW process assertion or new direct quotation is proposed.

The existing Falcon report and all raw/cached sources are preserved. Normal cache availability and selected external primary reading are recorded separately. Full-paper, figure-pixel, supplemental-pair and PAINT-node reconstruction are not claimed where not performed. Five of six additional normal sources were subsequently imported through Source92 and reassessed before this integrated proposal. PMID:19342655 remained unrecovered; its provisional extra citations are omitted, while its earlier bounded web-reading evidence and the actual normal-fetch failure remain recorded. The precise recovered-source read scopes are recorded in each reference review.

The integrated proposal retains 61 source annotations: 18 ACCEPT, 36 KEEP_AS_NON_CORE, three MODIFY, three UNDECIDED and one REMOVE. Three old authored NEW entries are withdrawn separately. It incorporates the two machine-derived UniProt alternative products and three reviewed core functions, without assigning function by isoform number. No new direct quotation is added.

The revised authored pathway supersedes the earlier substrate-only exclusion of apoptosis, an intrinsic ATP-translocation mechanism, and universal cytoplasmic coiled-coil client recognition. ER-associated p20 is distinguished from the cytosolic terminal fragment. HACD2 is stabilized in its reported client context; it is not described as a BAP31-promoted degradation target. TOMM40-associated localization and turnover remain bounded to the experiments. The provider report and all raw or cached sources are unchanged.

Source92 recovered five normal records: PMID:9396746, PMID:14581517, PMID:15187134, PMID:17056546 and PMID:23967155. Their canonical bytes match the staged bytes used for the bounded reading recorded here. PMID:19342655 returned exit1 without a timeout or quarantined output and remains absent; this establishes a failed normal retrieval only, not retraction, inaccessibility or absence of biological evidence. Earlier official abstract/selected web reading is preserved in the original consultation. Its provisional extra citations are removed from rows1,2,9 and the revised pathway; no original GOA source assertion is removed. The two detailed trafficking inferences remain UNDECIDED and the broad vesicle-transport context remains non-core, supported by the available15187134/17056546 material. New sources do not alter the reviewed annotation actions or three core functions. The human MHC-I experiment is context dependent; the isolated-domain coiled-coil study does not disprove full-length BAP29/BAP31 association.


## Final validation and source boundary

The applied review retains all 61 distinct source assertions from 64 raw GOA rows, restores eight omitted assertions and 32 supporting-entity lists, and withdraws only three old authored NEW entries. The two alternative products are derived from the unchanged UniProt record without assigning RefSeq or functional equivalence. The pathway now reflects the reviewed client-handling, signaling-platform and selective mitochondrial-localization evidence.

Focused validation and pathway PMID checks passed. The 23 advisories comprise 18 supported generic protein-binding annotations retained as non-core under the supplied ActionEnum; two UNDECIDED IBA annotations whose ancestral nodes were not reconstructed; one unchanged Falcon report not used as direct annotation evidence; one ERAD core process absent from the source annotation block; and one ontology-label version discrepancy. GO:0140597 retains the current official label protein carrier activity verified during the review, whereas the local validator expected protein carrier chaperone. No additional NEW assertion is introduced to silence these advisories. Rendering and generated Codex EDIT history validation are recorded separately.

Five of six requested additional normal references were recovered and reviewed within the documented reading limits. PMID:19342655 remains absent after the recorded normal retrieval failure; this is neither a retraction claim nor a claim that its publication is inaccessible. Its provisional extra citations were omitted without changing the associated decisions. No repository-wide validation result is claimed.

## 2026-09-30: curator discussion and evidence clarification

This entry supersedes the earlier counts and the statement that both trafficking IBAs remain unresolved. All 61 source assertions and both UniProt alternative products remain intact. The current decisions are 18 ACCEPT, 37 KEEP_AS_NON_CORE, three MODIFY, two UNDECIDED and one REMOVE. No NEW annotation is added. Older notes above are retained as a journal of prior interpretations.

[GO issue 6385](https://github.com/geneontology/go-annotation/issues/6385#issuecomment-4507045781) contains a genuine recommendation from M. Feuermann on 21 May and his completion message on 3 June. The previous reasons incorrectly dismissed the whole discussion as copied AI text. His proposed GO:0140388 is considered explicitly: its [current definition](https://amigo.geneontology.org/amigo/term/GO:0140388) requires an ATP-dependent translocation ratchet. The CFTR study supports client delivery to the Derlin-1 degradation pathway but does not establish that motor mechanism [PMID:18555783]. GO:0140597 retains the [current official label](https://amigo.geneontology.org/amigo/term/GO:0140597), protein carrier activity; protein carrier chaperone is an official synonym and the label expected by the older validator ontology.

Mouse MHC-I association and reduced mSec31 colocalization after combined Bap29/Bap31 loss support exit-site localization as a non-core function [PMID:15187134]. The vesicle-transport IBA remains UNDECIDED because direct participation in that step and the revised ancestral assertion were not resolved here. Conditional or redundant human export effects are positive evidence with limits; lack of a surface-MHC-I decrease after depletion does not prove absence of function [PMID:17056546].

The ERAD core now uses the accepted positive-regulation term GO:1904294. The mitochondrial-localization core records an explicit molecular-function knowledge gap: crosslinked association with TOMM40 and precursor proteins, together with fractionation and turnover effects, does not by itself isolate the proposed capture-and-handoff reaction [PMID:31206022]. This gap is preserved rather than filled with an unsupported carrier or motor assertion.

The clathrin donor is rat/RGD; MGI supplies the cross-species comparison display. The primary rat-liver fractionation result remains decisive: [PMID:9396746 "virtually no BAP31 was detected in the coated vesicle fraction."]. Reference assessments now emphasize each paper's contribution and reading limits, without internal recovery identifiers or repeated procedural sentences.

### Follow-up validation

The final independent science peer passed before applying this follow-up. `just validate human BCAP31` exited 0 with 21 warnings: 18 retained non-core protein-binding records, one unresolved IBA lacking an independently inspected PAINT node, one uncited provider-output warning, and one ontology-version label warning. The current official label for GO:0140597 is protein carrier activity; the local validator expects its older synonym protein carrier chaperone. Supported interaction records remain non-core under the supplied action definitions; no unsupported replacement activity or propagation diagnosis was invented to suppress warnings. The separate `pkg_resources` deprecation notice is an environment warning. The pathway PMID check passed. No repository-wide validation is claimed.

`just render human BCAP31` succeeded. A new Codex/gpt-6 history session was scaffolded for PR #3605, with its validation recorded separately. The prior history and pathway, immutable source files, and all 30 publication/Reactome dependencies are preserved unchanged. This entry supersedes the earlier 23-warning validation count.
