# GEMIN7 (donkey, A0A9L0J5X5) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: A0A9L0J5X5 is the 131-aa product of donkey GEMIN7 (Ensembl gene ENSEASG00005033816.1). It is
the canonical-length relative of the longer gene-model product A0A9L0ICL9 (206 aa), which is reviewed in
`genes/EQUAS/GEMIN7/`. No ProtNLM2 files or prediction-evidence folders were opened.

Deep research: `just deep-research-falcon EQUAS GEMIN7__A0A9L0J5X5 --fallback perplexity-lite` failed
(falcon: "Failed to authenticate"; perplexity-lite fallback: HTTP 401 insufficient quota). The review is
based on cached publications that I read directly (abstracts unless noted).

### Evolutionary grounding

- UniProt and my own fetch place A0A9L0J5X5 in PANTHER PTHR14679:SF1 (GEM-ASSOCIATED PROTEIN 7), the
  same subfamily as human GEMIN7 Q9H840 and S. pombe gem7 G2TRR1
  [file:EQUAS/GEMIN7__A0A9L0J5X5/GEMIN7__A0A9L0J5X5-bioinformatics/RESULTS.md]. PTHR14679 has only one
  subfamily.
- Identity to human Q9H840 is 115/131 (87.8%), same length; to horse 130/131.
- Human GEMIN7 PAINT IBAs (QuickGO, checked 2026-10-21): GO:0000387 spliceosomal snRNP assembly and
  GO:0120114 Sm-like protein family complex, from node PTN001027441 with S. pombe SPBC32F12.16 and human
  Q9H840 as donors. PAINT did not propagate GO:0032797 SMN complex or the localisation terms, although
  human GEMIN7 has SMN complex by IDA; I treat that omission as a deliberate decision and do not add SMN
  complex as NEW. The donkey GOA rows come from TreeGrafter (GO_REF:0000118, node PTN001428136) and
  InterPro/SubCell mappings, not IBA.

### Literature (human unless noted)

- Gemin7 identified in native SMN complexes; direct interaction with SMN and Gemin6; mediates Gemin6
  association with SMN complex; RG repeats needed for SMN binding; interacts with Sm proteins, especially
  SmE; colocalises with SMN in cytoplasm and gems [PMID:12065586 "Gemin7 interacts directly with SMN and
  Gemin6 and mediates the association of Gemin6 with the SMN complex"].
- Gemin6-Gemin7 crystal structure: both have Sm folds and form an Sm-like heterodimer that binds Sm
  proteins [PMID:15939020 "both adopt canonical Sm folds"].
- Gemin6, Gemin7 and Unrip form a stable subunit tethered to SMN by Gemin8; this subunit recruits Sm
  proteins [PMID:17023415 "the involvement of the heteromeric subunit containing Gemin6, Gemin7, Gemin8,
  and Unrip in the recruitment of Sm proteins to the snRNP assembly pathway"].
- Gemin7 knockdown lowers snRNP assembly activity and SmE in the SMN complex [PMID:19321448 "Gemin7
  knockdown revealed a decrease in snRNP assembly activity"].
- SMN complex is the catalyst of Sm ring closure on snRNA after pICln trapping [PMID:18984161].
- snRNA recognition in the SMN complex is attributed to Gemin5-containing subunits [PMID:17640873], not
  Gemin7. I found no evidence that Gemin7 itself binds RNA; the RNA binding IEA comes from the Sm-domain
  InterPro signature, which in Gemin6/7 underlies protein heterodimerisation.
- S. pombe SMN complex contains Gem6/Gem7 recruited by Gemin8 [PMID:33754639].

### Decisions

- spliceosomal snRNP assembly: ACCEPT (Gemin6/7 module recruits Sm proteins; knockdown evidence).
- SMN-Sm protein complex: ACCEPT. Sm-like protein family complex: ACCEPT (PAINT placement; the
  Gemin6-7 Sm-like heterodimer associated with Sm proteins fits the definition).
- cytoplasm: ACCEPT (site of SMN-complex snRNP assembly). nucleoplasm, Gemini of Cajal bodies:
  KEEP_AS_NON_CORE.
- RNA binding: MARK_AS_OVER_ANNOTATED (domain-signature inference, no direct evidence).
- Nothing in this species is experimentally established; all functions are inferred from human (and
  fission yeast) orthologs in the same PANTHER subfamily.
