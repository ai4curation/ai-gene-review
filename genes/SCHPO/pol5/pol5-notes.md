# pol5 review notes

## 2026-09-01 — source refresh and annotation audit

- Refreshed the gene bundle with `just fetch-gene SCHPO pol5 --force`. Current GOA contains 18 distinct annotation rows. The prior IDA `GO:0009303 rRNA transcription` row from PMID:16816948 is no longer present and was removed from the review rather than preserved as a stale annotation.
- The cached PMID:16816948 record is abstract-only. It directly reports that Pol5 is essential and nuclear, that reduced Pol5 inhibits rRNA production, that Pol5 binds rDNA promoter fragments, and that it interacts with Cdc10. It does not expose the full assay controls, so I retained the curator's IDA `GO:0001163` annotation rather than overruling sequence specificity from incomplete evidence. In the synthesized core function I used the broader, directly supported `GO:0000182 rDNA binding` claim.
- PMID:31745560 has cached full text and provides the strongest mechanistic evidence through the S. cerevisiae ortholog: Pol5 contacts the 5' ETS, ITS2, and domain III of 25S pre-rRNA; depletion disrupts processing for both ribosomal subunits; and Pol5 contributes to peptide-exit-tunnel assembly and recycling of pre-40S assembly factors.
- Launched OpenScientist through `just gene-hypothesis-research openscientist` to test whether direct Pol I regulation is the primary S. pombe function. The report rejected that primary-function model and favored conserved pre-rRNA processing/ribosome biogenesis. It also identified the decisive remaining gaps: no S. pombe nascent-transcription assay and no controlled DNA-versus-RNA substrate-preference test.
- Accepted the current NOT ISO annotation to `GO:0042790 nucleolar large rRNA transcription by RNA polymerase I`; it is compatible with promoter-fragment binding because a binding activity does not establish direct participation in the transcription process.
- Removed broad InterPro-derived `nucleotide binding` and `regulation of DNA-templated transcription`; modified broad nucleic-acid/DNA-binding rows to specific rDNA/rRNA-binding terms; removed generic `protein binding`; and retained target-supported nuclear/nucleolar localization plus the observed cytosolic pool as non-core.
- Verified from the refreshed PANTHER cache that O60094 is in `PTHR13213:SF2`; the official family name is `MYB-BINDING PROTEIN 1A FAMILY MEMBER` and the official subfamily name is `MYB-BINDING PROTEIN 1A`.

## 2026-09-01 — PR review follow-up

- Replaced the broad proposed `GO:0042254 ribosome biogenesis` transfer with the experimentally resolved `GO:0042273 ribosomal large subunit biogenesis` and `GO:0042274 ribosomal small subunit biogenesis` processes. Both proposals now identify PMID:31745560 and SGD Pol5 (`S000000781`) as their evidence and transfer source.
- Added the same publication and ortholog provenance to the proposed rRNA-binding transfer, removed an invalid reliance on a NOT transcription annotation when assessing broad transcription regulation, and recorded the unresolved functional consequence of Eso1-dependent K47 acetylation.
- A repository-wide prediction-audit failure exposed while shepherding this gene was fixed independently in PR #2845; the Pol5 review was then rebased onto that merged wrapper-layer fix.
