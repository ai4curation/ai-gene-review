# bll6428 review notes

## 2026-11-06 annotation review

Identity: Q89GB7, frozen official USDA110 taxon224911 record; retain locus symbol bll6428. The 2013 paper's Bradyrhizobium japonicum USDA110 name is the historical name of this strain. It describes related operon organization, explicitly leaving function unknown.

bll6428 versus Hsero_1004: 312/385 identical aligned residues (81.0%); lengths 389/386; target coverage 99.0%.

Bll6428 is an alpha/beta-fold hydrolase of the FrsA-like family in an aromatic-compound catabolic locus of Bradyrhizobium diazoefficiens USDA 110. It is closely related to Herbaspirillum FdeB, but exact ester-versus-carbon-carbon bond specificity and the proposed flavonoid-derived lactone substrate remain unresolved. Its S9-like catalytic-domain annotation does not independently establish physiological peptide hydrolysis.

Reviewed every seeded annotation; preserved each non-review payload and ordering. No new biological-process assertion: candidate locus membership is useful context, but the actual work of this protein in a USDA110 flavonoid reaction remains inferential and competing substrate/partner roles are not resolved. This is not a universal demand for direct assays; reaction-class inference is accepted where sequence, architecture and characterized homolog chemistry agree. No BP comparator query was used to manufacture a gap.

Research: genuine default-provider Falcon request (`just deep-research BRADU bll6428 --provider falcon`) failed with HTTP403 authentication error. No provider research file was created. Manual assessment uses frozen target record, primary PMID23125118, PMID27059806, PMID39107441 and PMID38707841 and the scoped source evidence and sequence comparison in `analysis/module_audits/bacterial_flavonoid_degradation/bradu-panel/`. These primaries are comparative, never target enzyme assays. Existing source files were not refreshed.

Core synthesis retains only supported reaction classes/cofactor properties. No precise molecular-function core is supplied for uncharacterized cupin/epimerase candidates solely to fill the module.

PAINT: normal lineage-loss query found no IRD/IKR. Cached IBD and actual seed were inspected; broad family function is retained and no evolutionary loss is claimed.

## 2026-11-06 — comparative review follow-up

Reassessed the PR #6140 review requests against the original row payloads and independent sources. See `analysis/module_audits/bacterial_flavonoid_degradation/round1-source-review.md` for the mapping, family and participation decisions. All original rows remain in their original order; inherited proposals that lack positive participation evidence are withdrawn by review action rather than deleted. No raw UniProt, GOA or provider artifact was edited.


## 2026-11-07 PR #6140 round-2 review follow-up

Broad GO:0016787 hydrolase activity is retained in the core synthesis as a family/fold/conserved-candidate inference, without selecting ester versus C-C chemistry, substrate, or native process participation. The independent sequence check corrects the provider report's Asp358 to actual Asp359 in PP_3195. Its H405 candidate corresponds to bll6428 Q374, while alignment of characterized Q93NG6 S217/D300/H329 maps to PP_3195 S268/D359/H394, Hsero_1004 S233/D324/H359 and bll6428 S237/D328/H363. Candidate correspondence is not proof of target geometry or catalytic loss. See PP_3195-bioinformatics/fdeb-round2/RESULTS.md and the reproducible round2 maps. The C-C family comparator is now cited directly to the primary PMID:16321959 (hydrolytic cleavage) and official reviewed Q93NG6 record; PMID:17275835 supports the comparator structure/mutagenesis context. Both fetched papers are abstract-only; no target experiment is attributed to them.

See `analysis/module_audits/bacterial_flavonoid_degradation/round2-review-response.md` for source provenance, limits and disposition of all seven review points. Earlier journal entries record superseded judgments and remain unchanged.
