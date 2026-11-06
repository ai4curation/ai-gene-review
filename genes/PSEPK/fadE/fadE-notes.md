# Curation notes: *Pseudomonas putida* KT2440 fadE (Q88LN6, PP_1893)

## Sources

- `fadE-deep-research-openscientist.md` (provider report, already present).
- The UniProt entry is unreviewed; its reaction, EC and pathway lines carry
  ARBA evidence and are not cited. Family cross-references (PANTHER
  PTHR48083:SF18, InterPro FadE_C, Pfam ACDH_C) are cited instead.
- Experimental support is transferred from the E. coli orthologue FadE
  (Q47146; `genes/ECOLI/fadE/`), which is in the same PANTHER subfamily SF18
  and whose mutant cannot grow on C8-C18:1 fatty acids (PMID:12057976).

## Decisions (2026-11 completion pass)

- The earlier draft's UNDECIDED on GO:0005737 cytoplasm is resolved to ACCEPT.
  The Phobius helix at residues 43-64 is a single sequence-analysis line; the
  E. coli orthologue has the same hydrophobic N-terminal stretch, UniProt
  curates no transmembrane segment for it, and E. coli acyl-CoA dehydrogenase
  activity fractionates with the soluble fraction (PMID:334745). Membrane
  association remains a suggested question.
- GO:0003995 changed from MARK_AS_OVER_ANNOTATED to ACCEPT: it is the
  reaction-class term and the module's term for this step.
- GO:0016627 changed from MARK_AS_OVER_ANNOTATED to TOO_GENERAL (true but
  entailed by the accepted chain-length-specific activities).

## 2026-11-04 PR #5935 review round

- The cytoplasm reason now states what outweighs the Phobius helix (the E. coli
  orthologue's identical hydrophobic stretch without a curated TM segment, and
  soluble-fraction activity), and that the catalytic domains face the cytoplasm
  on either topology.

## 2026-11-06 comparative primary-source re-review

Current QuickGO GO0003995/4466/70991 definitions require ETF; all three rows are UNDECIDED, while broad CH-CH activity is refined to an explicitly proposed acceptor-unspecified reaction. No direct PP_1893 chain-length or electron-acceptor assay is established. Full32826213 highlights PP0368/PP0370, so PP1893 is not called the proven dominant native FadE. Cytoplasm is retained broadly with membrane topology unresolved; FAD binding is core-compatible. Existing OpenScientist report remains unchanged, with its ETF/topology overstatement recorded.

All original annotation payloads, including historical proposals, and raw/provider/prediction artifacts are preserved. Source-scope details and exact quotes are in `../fadB/fadB-source-analysis/primary-scope.md` (for fadB, its local source-analysis directory). Shared publication caches were not refreshed. New normal publications36763117 and12115060 were fetched; acquired full articles remain ignored. PAINT-losses cannot assess these targets because they are not cached tree leaves. Focused validations, renders and new helper histories accompany the handoff.

## 2026-11-06 — PR6136 description scope

Moved source-assessment wording out of the standalone description. Prior source-qualified summary retained here:

FadE (PP_1893) of Pseudomonas putida KT2440 is a predicted FAD-dependent acyl-CoA dehydrogenase with the extended bacterial FadE architecture. It is inferred to oxidize a saturated acyl-CoA to trans-2-enoyl-CoA in fatty-acid beta-oxidation. Its physiological electron acceptor, substrate-chain-length range and membrane association have not been established. Other KT2440 dehydrogenase paralogs have stronger native fitness evidence under the tested fatty-acid conditions.
