# TUFM (mtEF-Tu) curation notes

## Deep research
`TUFM-deep-research-claude-code.md` ran for 46 s with 3 web searches (`web_search_requests: 3`) and 6 citations. It says
most mechanistic statements are from UniProt and general EF-Tu knowledge, not papers read in the session. Used as leads only.
Its suggested Valente 2007 PMID (17160894) is wrong; the paper is PMID:17160893, which UniProt cites and which is cached.

## Evidence
- Recombinant mammalian mtEF-Tu "is active in the poly(U)-directed polymerization of phenylalanine"; transit peptide of 43 aa [PMID:8547323].
- mtEF-Tu-GTP "delivers aminoacylated-tRNA to the mitoribosome in a manner similar to its bacterial EF-Tu counterparts"; it was also found on
  ~75% of GTPBP5-containing late mt-LSU assembly intermediates, bound in a non-canonical mode [PMID:34135318].
- COXPD4: first TUFM patient, "defective mitochondrial translation", pathogenicity shown by "functional complementation in vivo" [PMID:17160893].
- Non-canonical: NLRX1-TUFM complex, knockdown increases IFNB1 induction and reduces viral-induced LC3B-II [PMID:22749352]; viral
  M proteins (HPIV3, SARS-CoV-2) bind TUFM to induce mitophagy [PMID:28407488, Reactome:R-HSA-9754763].

## Decisions and flags
- Core: translation elongation factor activity, GTPase activity, mitochondrial translational elongation, matrix.
- PMID:11741979 protein binding (to ATP5F1A) is REMOVED: the paper studies p43, the EMAP II precursor of the multi-tRNA
  synthetase complex (AIMP1). TUFM's UniProt alternative name is also "P43", which is the likely source of the error. This is
  stated in the cached abstract itself, so it meets the bar for a name-confusion claim.
- Mitochondrial outer membrane (Reactome TAS, from the SARS-CoV-2 M events) MARK_AS_OVER_ANNOTATED: the event text says it
  assumes the interaction happens at the MAM.
- Mitochondrial large ribosomal subunit assembly (IDA, PMID:34135318) KEEP_AS_NON_CORE: binding is structural fact, the
  contribution to assembly is the authors' proposal.
- No NEW terms. The innate-immunity/autophagy role (UniProt FUNCTION) has no GOA annotation; it rests on overexpression and
  knockdown in cell lines and was left as a suggested question rather than proposed as NEW.
