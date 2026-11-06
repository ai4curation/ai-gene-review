# PP_0544 curation notes

- A forced QuickGO refresh restored four source rows. Plasma-membrane localization is accepted, generic membrane and transport-process terms are retained as non-core, and GO:0022857 is modified to GO:0034228 using the exact Q88QF0 IPR004757/TIGR00908 signature evidence.
- Ethanolamine-catabolic-process participation remains a locus-based hypothesis rather than an IC annotation stacked on the proposed substrate-specific transport term.
- PP_0544 is not classical EutH: it is PTHR42770:SF7/APC-family, whereas verified Salmonella EutH P41796 is PTHR40089:SF1/IPR007441. The reusable module models these as alternative transporter implementations.
- No completed PP_0544 OpenScientist artifact was present. Research was not restarted.

## 2026-11-04 completion pass

- No deep-research provider file exists for PP_0544 (no provider keys in this
  session); none was fabricated.
- Literature search (PubMed esearch, 2026-11-04): "PP_0544" (hits are unrelated
  "PP" abbreviations), "ethanolamine AND putida AND transport" (two choline/choline-
  sulfate papers, PMID:18156257, PMID:17116241, not about PP_0544), "ethanolamine
  permease APC" (PMID:8069783, Rhodococcus eutBC cluster with an APC-like permease,
  sequence only). Web search found Lundgren et al. 2016 (PMID:27325678) on the
  P. aeruginosa PA4022-eat-eutBC operon. **No direct transport assay of PP_0544 or of
  any IPR004757/TIGR00908 member was found.**
- Lundgren et al. 2016 full text (PMC4984546, read online; only the abstract is
  cached) describe PA4023 as "a homolog of the ethanolamine transporter Eat, a member
  of the amino acid-polyamine-organocation family" and report that "The growth of the
  Δeat mutant on ethanolamine was identical to that of wild-type (WT) P. aeruginosa
  PAO1" [PMC4984546]. So even in the best-studied Pseudomonas, Eat is not required for
  ethanolamine growth at the concentrations tested (diffusion of the neutral amine may
  suffice). This is a caveat on the physiological necessity, not evidence against the
  transport assignment.
- `PP_0544-bioinformatics/locus_and_family.py` (stdlib; writes RESULTS.md from live
  InterPro/UniProt REST): TIGR00908 description says all three seeds (Burkholderia,
  P. aeruginosa, Clostridium) are adjacent to ethanolamine-catabolism genes; the KT2440
  neighbourhood is PP_0542 eutC, PP_0543 eutB, PP_0544, PP_0545 aldehyde
  dehydrogenase, PP_0546 sigma-54 regulator, the same order as P. aeruginosa
  eutC-eutB-eat-PA4022-eatR.
- Fitness data (`just fetch-fitness PSEPK PP_0544`) could not be fetched (no FEBA
  source reachable).
- Decisions: plasma membrane ACCEPT; membrane MODIFY -> plasma membrane (was
  KEEP_AS_NON_CORE while arguing it was general, which the action rules forbid);
  transmembrane transporter activity MODIFY -> GO:0034228 (prediction, two lines:
  family model + conserved locus); transmembrane transport MODIFY -> GO:0034229
  ethanolamine transport (the process GO:0034228 is part_of; no ethanolamine
  transmembrane transport term exists).
- PANTHER: PTHR42770:SF7 is named "MEMBRANE PROTEIN" in panther.obo and Q88QF0 is
  listed in it in `.cache/panther/panther-members-19.0.tsv`; SF7 also contains
  uncharacterized mycobacterial and Mycoplasma transporters (Rv1999c, MPN_095), so the
  ethanolamine-permease grounding belongs to IPR004757, not SF7 or PTHR42770.


## 2026-11-06 comparative re-audit

PP_0544 remains an explicitly inferred KT2440 ethanolamine permease based on IPR004757/TIGR00908 and eutBC neighborhood. Those clues are related, because the family model itself used gene-neighborhood evidence; they are not two independent transport assays. Full PMID27325678 confirms PAO1 delta-eat growth is normal at pH 7.0 and 20 mM ethanolamine, whereas the distinct EatR/PA4021 regulator is required. Neither phenotype is a direct PP_0544 transport assay. The negative growth requirement does not exclude transport at limiting uncharged substrate or different pH. Existing substrate-specific refinements are retained as predictions, with no asserted coupling ion, substrate charge or universal uptake requirement. The core remains a panel candidate rather than an experimentally confirmed native flux witness.

A normal Falcon research attempt failed with HTTP 403 authentication/access error; no provider report was fabricated. Review evidence comes from the primary sources, frozen UniProt/domain records and explicitly identified comparative inference. Original GOA/UniProt files and upstream row payloads are preserved. Source refreshes used only the normal publication fetch command; separately acquired full articles remain ignored, with small exact excerpts and provenance retained beside the reviews.
