# yihV (P32143) notes

## Session 2026-11-10

Deep research via `just deep-research` failed in this environment (deep-research-client
dependency unresolvable offline); review built from UniProt and cached literature:
PMID:24463506 (abstract), PMID:33791429 (full text), PMID:41676062 (review).

- SF kinase, second sulfo-EMP step [PMID:24463506].
- PfkB-family ATP-dependent kinase, SF + ATP -> SFP + ADP [PMID:33791429 "YihV is a
  member of the Pfam pfkB carbohydrate kinase family22 and is an ATP-dependent kinase
  that mediates phosphoryl transfer from ATP to SF to give SFP."]
- kcat 3.1 s-1, KM(ATP) 1.0 mM; no activity on F6P; complex regulation by SQ, SLA, DHAP,
  F6P, FBP, PEP, citrate, ADP; "important control point" [PMID:33791429].
- Homodimer (beta-clasp lid dimerization), minor tetramer; KRN sulfonate triad
  K27-R138-N109 conserved in YihV kinases [PMID:33791429].

PAINT (PTHR10584 paint.tsv): PTN000061922 (taxon:1224) IBD GO:0061594 seeded only by
UniProtKB:P32143 (date 20250326), plus IRD NOT GO:0004747 ribokinase blocking
PTN000061929. The cytosol IBA row comes from PTN000061929 (seed P0A9J6, RbsK); cytosol
is not blocked by the IRD.

Decisions: GO:0061594 x4 ACCEPT; kinase activity and transferase (P-containing groups)
MODIFY -> GO:0061594; GO:0046835 carbohydrate phosphorylation ACCEPT (phosphorylation
of the ketose SF is literally what YihV does; no more specific GO process exists);
GO:1902777 x2 MODIFY -> GO:0061722; cytosol ACCEPT (soluble intracellular enzyme, no
TM/signal; inherited from RbsK node).
