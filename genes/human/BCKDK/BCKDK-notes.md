# BCKDK research notes — 2026-09-30

Pre-application work from the authenticated normal Seed45 archive. All 45 existing assertions and all three alternative products remain unchanged at this stage. The immutable UniProt and GOA files are preserved. No provider research file has been manufactured. The normal provider attempt awaits canonical seed import.

## Main biochemical role

BCKDK is an ATP-dependent protein serine kinase that inhibits the branched-chain alpha-ketoacid dehydrogenase complex by phosphorylating its E1 alpha subunit, BCKDHA. It associates with the DBT/E2 core in the mitochondrial matrix. Loss of kinase activity releases this inhibition and increases branched-chain amino acid breakdown; it does not cause a failure of that breakdown. The human patient/fibroblast study [PMID:24449431](https://pubmed.ncbi.nlm.nih.gov/24449431/) supports this direction. Its cached abstract was read completely; the full paper was not available in the normal cache. The two normal Reactome records independently describe inhibitory phosphorylation and its loss.

The primary inhibitor study [PMID:37558654](https://pubmed.ncbi.nlm.nih.gov/37558654/) distinguishes thiophenes that reduce BDK association/protein abundance from thiazoles that increase them. Its complete abstract and selected Methods were read. These results inform the regulatory association; they do not establish every metabolic phenotype as a direct BCKDK function. No treatment recommendation is made.

## ACLY is a separate substrate

[PMID:29779826](https://pubmed.ncbi.nlm.nih.gov/29779826/) contains purified MBP-BDK phosphorylation assays and a separate V5-tagged protein assay showing phosphorylation of human ACLY Ser455. Methods identify human BCKDK and ACLY cDNAs. Rat liver fractionation, Fao cells, cytosolic targeting-sequence deletion, and rat hepatic lipogenesis experiments provide distinct localization and physiological evidence; the rat ACLY site is Ser454. Selected Results, construct Methods and kinase Methods were read, not every figure, supplement or duplicated extraction section.

BCKDK phosphorylates protein. ACLY produces acetyl-CoA; a later acetyl-CoA carboxylase reaction produces malonyl-CoA. The immutable UniProt prose contains an imprecise product description and a self-competition wording defect; neither is copied into the biological synthesis. The independent annotation consultation attributes phosphatase activity in the cited paper to PPM1K, supporting removal of the BCKDK phosphatase assertion after actual assay inspection.

## Conditional PDC activity and PAINT limits

[PMID:33773101](https://pubmed.ncbi.nlm.nih.gov/33773101/) and the [author-hosted manuscript](https://www.zelzerlab.com/_files/ugd/7ea8ed_efbf6044bf1f438ba08ee4417de3b692.pdf) provide mouse embryonic and primary-cell evidence for BCKDK-dependent regulation of PDC when PDK family function is absent. Selected Results, Figure 5 caption, Methods and Discussion were read. Reduced PDHA1 phosphorylation, increased PDC activity and pyruvate tracing support compensation in that context. No purified BCKDK-to-PDHA1 assay was identified in the inspected sections. The authors explicitly leave normal-condition PDC regulation open. This is not evidence that human BCKDK universally controls PDC.

The current source IBAs point to PANTHER:PTN000236514. PTHR11947 and its BCKDK subfamily assignment were observed, but family naming is not ancestral-node placement. A single local official tree request failed DNS; saved browser requests also failed to return the actual tree. No tree, MSA, inferred loss or misplacement is invented. Donor count and the target appearing in its own mitochondrial IBA donor set are not defects. Conditional PDC evidence prevents dismissing the PDK-related annotations merely because BCKDK has a different principal substrate.

## Ontology and scope decisions

Official definitions were checked for [GO:0009083](https://amigo.geneontology.org/amigo/term/GO:0009083), [GO:0045763](https://amigo.geneontology.org/amigo/term/GO:0045763), [GO:0046889](https://amigo.geneontology.org/amigo/term/GO:0046889), and [GO:0005829](https://amigo.geneontology.org/amigo/term/GO:0005829). The proposed process refinements record negative regulation of amino acid metabolism and positive regulation of lipid biosynthesis, respectively. They reflect the kinase's own regulatory chemistry, without adding redundant NEW process assertions.

The independent annotation reviewer assessed zero-based rows 3 and 34–36. Official GO:0045252 denotes the oxoglutarate-to-succinyl-CoA complex. [GO:0160157](https://amigo.geneontology.org/amigo/term/GO:0160157) denotes the branched-chain alpha-ketoacid complex and allows associated proteins. Selected original [PMID:11839747](https://pubmed.ncbi.nlm.nih.gov/11839747/) manuscript text distinguishes these complexes and places the regulatory kinase on the BCKD E2 core. The normal cache remains abstract-only; this decision uses separately inspected primary text, not a title inference. The rat donor annotation history was not reconstructed.

Generic interaction annotations are retained as non-core when the cited interaction evidence is compatible with the curated assertion. An interaction alone does not establish a substrate, adapter activity or pathway role. Exact interaction supplements have not all been independently inspected.

The spermatogenesis transfer points to rat Q00972. [PMID:27472223](https://pubmed.ncbi.nlm.nih.gov/27472223/) describes infertility with systemic BCAA depletion in mutant rats, but the inspected abstract does not establish a direct spermatogenic biochemical role. Direct manuscript access was unsuccessful; avoid turning this phenotype into a core activity.

## Read provenance

- Source object inventory and prior UniProt/abstract reads are recorded in the initial intake; later source reads were 10af7b, be73a6, 4774e8, e3c38a, 684199 and 110889.
- PDC selected primary responses: pdc-primary-web.json, pdc-primary-find-web.json and pdc-primary-mef-discussion-web.json. Tree failure: paint-tree-single-request.json.
- Independent bounded consultation: ../BCKDK-annotation-parser/bounded-consultation.json, SHA256 20bde3902d64ff16c0f4aea838ba2c3113dcc30f0f22e07dc6cd1f16bc5a76a9, actual 6ce125; consumed in e6ddef and ba95ed.
- No new verbatim quotations have been added in these notes.

## Source availability and normal attempt outcomes

The three normal BCKDK seed files were imported unchanged (apply 820f18, postcheck e2073e); the separate four-source cache import closed at 81ac99/postcheck 228018. The latter created PMID:2403034, PMID:24449431, PMID:29779826 and PMID:37558654 unchanged. Eight differing preexisting publication caches and two equal Reactome caches were preserved; no existing cache was refreshed. The 45 source assertions and three alternative products remain intact in the draft.

The normal provider command `just deep-research-falcon human BCKDK --fallback perplexity-lite` failed before either provider API was called because the offline environment could not resolve `deep-research-client[cyberian]==0.2.7rc1` (actual 1093d9). It created no provider research file. This manual research journal records the evidence and access limits instead.

One normal `just fetch-pmid 33773101` operation failed DNS with zero of one publications cached (start cd36e6, interim dbb1c4, final 91054c, session 32864). The saved filename containing `terminal` is the interim poll and carries no exit code; the actual terminal result is `pmid33773101-complete-tool-result.json`. No second local fetch was attempted. The requested PMID identity and selected primary text had already been verified independently of normal-cache availability; the bounded Source95 recovery is pending.

The canonical-cache census (43fee0) confirms all 12 existing PMID titles match the seeded references and the nine-word supporting quotation is present exactly in canonical PMID:29779826. PMID:20833797 requires an availability correction: its Seed45 fetched candidate was abstract-only, while its preserved canonical cache contains an HTML full-text extraction. The draft no longer labels that reference unavailable. Its complete body and protein-level supplements have not been audited. PMID:11839747, PMID:2403034 and PMID:24449431 remain abstract-only in the canonical cache; the indexed abstract of PMID:2403034 is itself explicitly truncated.

A subsequent complete read of the stored PMID:20833797 record (628d5b) shows that its HTML extraction contains the abstract and Discussion, while the main Methods/Results and supplements are not included. The availability flag therefore does not establish a complete paper cache. The Discussion supports the human muscle mitochondrial proteomics context, while the BCKDK protein-level assignment remains the curator's source annotation, consistent with independent pathway evidence. Its absence from the displayed prose is not used to challenge the curated HDA assertion. No new quotation was added.

## Final evidence anchors prepared

The principal BCKDH-inhibition core now has a 14-word exact supporting snippet from the normal PMID:24449431 abstract. The second core retains its existing nine-word PMID:29779826 snippet; no other quotation was added. Selected full UniProt function/localization sections and the complete PMID:24449431 abstract were checked again (a3187f, 38a2d7). Concise unquoted findings were added for the human loss-of-function, BCKDK/PPM1K and ACLY biochemistry, and inhibitor studies. The two complete normal Reactome records were read (830858): R-HSA-9912480 explicitly describes deficient BCKDK mutants, rather than a normal activation reaction. PMID:37558654 complete abstract was reread in bounded output (3f684c); an earlier broad line range was truncated and is not a full-paper read claim.

## Final normal-source reassessment

Source95 completed the sole required normal PMID:33773101 request. The exact 3,341-byte PRIMARY_RESEARCH cache was imported without overwrite (apply f2e2e7; postcheck 939f07; SHA256 c846e998f100c03c075d6348dc92b25bb5b347146e485abdb3f666d1b1593001). Its metadata and complete abstract were read after canonical import (0a173a). The normal record is abstract-only and reports no recovered PMC record. The selected author-hosted Results, Figure 5 caption, Methods and Discussion remain a separate primary-evidence read; no complete-paper or supplement audit is claimed.

The abstract agrees with the bounded interpretation already recorded: mouse PDK-family loss unmasks BCKDK-dependent compensation involving PDC phosphorylation, activity and pyruvate flux. This supports retaining the existing PDC-related annotations as contextual/non-core, without claiming normal PDK-intact human PDC control or a purified human BCKDK-to-PDHA1 assay. The PAINT ancestral placement remains unresolved because the actual tree was inaccessible; donor count is not used as contrary evidence. No new annotation or supporting quotation was added from this source.

The final proposal retains all 45 source assertions, including qualifiers and source identifiers, and all three alternative products. The sole experimental removal is the phosphatase claim after actual BCKDK-versus-PPM1K assay inspection; the three complex corrections distinguish the branched-chain complex from oxoglutarate dehydrogenase. Quotation totals are 14 words from PMID:24449431 and nine words from PMID:29779826, both exact and used once.

### Focused validation and rendered review

The exact independently reviewed proposal was applied with all 45 source annotation objects and all three alternative products preserved. Normal `just validate human BCKDK` passed (terminal ed28f8, exit 0). Six advisories remain: five generic protein-binding rows are retained as non-core physical associations under the project decision policy, and the cytosolic location of the separately supported ACLY kinase core has no corresponding source annotation row. The latter is a coverage advisory, not a reason to manufacture a new annotation; the core retains its explicitly bounded human biochemical and rodent cellular/physiological evidence.

Normal `just render human BCKDK` passed (6a4a0a, exit 0). These are focused gene checks; no repository-wide validation pass is claimed. The environment also emitted an eutils/pkg_resources deprecation warning. No immutable UniProt, GOA or reference cache was edited.


## Ontology specificity and evidence boundaries — 2026-10-01

The seven catabolism replacements retain GO:0045763 because the verified ontology supports the negative-regulatory direction, while the mechanistic evidence identifies BCAA breakdown specifically. BCKDK phosphorylates the BCKDH alpha subunit and reduces catalytic activity; it does not execute the oxidative decarboxylation. The human patient/fibroblast evidence is [PMID:24449431](https://pubmed.ncbi.nlm.nih.gov/24449431/), and the reaction is described in [Reactome R-HSA-5693148](https://reactome.org/content/detail/R-HSA-5693148). The existing exact 14-word quotation in the core function anchors the human study; no duplicate quotation is added here.

I inspected the official [GO:0045763 hierarchy](https://amigo.geneontology.org/amigo/term/GO:0045763) and [GO:0009083 definition](https://amigo.geneontology.org/amigo/term/GO:0009083). AmiGO reported a 2026-08-06 load date. The seven displayed immediate children of GO:0045763 concern arginine, ornithine, proline, GABA, tryptophan-derived NAD, amino acid biosynthesis and ammonia assimilation; none denotes BCAA catabolism. Targeted searches for regulation of branched-chain amino acid catabolism/metabolism and the local ontology label caches also found no matching term. This is a finding within the consulted snapshot and searches, not a claim that every current ontology axiom was downloaded. QuickGO/OLS API access and the AmiGO view including regulates relations were unsuccessful. No more specific verified identifier is available from these checks. The replacement and first core therefore retain GO:0045763, with BCAA specificity in their biological descriptions; the fact that this term was already annotated was not a valid reason for choosing it. A dedicated negative regulation of branched-chain amino acid catabolic process term remains a potential ontology request after checking the latest complete release.

For the second core, [PMID:29779826](https://pubmed.ncbi.nlm.nih.gov/29779826/) supports phosphorylation of human ACLY Ser455, whereas the localization and lipid-flux experiments described in these notes use rodent liver/cell systems. The human UniProt record attributes the cytosolic BCKDK pool to similarity with rat Q00972 (ECO:0000250). The machine-readable cytosol location is omitted from this core so that it does not imply direct human localization evidence; the experimental and orthology contexts remain explicit in the description. The mitochondrial role is unchanged.

The PDK-deficient mouse results in [PMID:33773101](https://pubmed.ncbi.nlm.nih.gov/33773101/) motivate a specific question about PDK-intact human cells. They do not establish constitutive human PDC control. The spermatogenesis assessment remains UNDECIDED, now naming the previously read abstract of [PMID:27472223](https://pubmed.ncbi.nlm.nih.gov/27472223/) as a follow-up lead; its full text and the donor annotation history remain unresolved, and no publication cache or formal verified reference has been fabricated.

All 45 source assertions, three alternative products, references, action choices and existing evidence quotations are preserved. The five generic interaction decisions remain an unresolved disagreement with the automated review policy; this follow-up makes no claim that those warnings are resolved.


The follow-up passed independent science review, focused gene validation, rendering and history validation. Validation retained five retained generic-binding policy warnings; these are documented unresolved issues, not a claim of warning-free review. No full-repository validation was run.
