# At5g03810 (UniProtKB:Q9FFN0, GDL72_ARATH) notes

## What is actually known about AT5G03810

Essentially nothing beyond its sequence. This is one of the least-studied members
of the ~105-gene Arabidopsis GDSL (GELP) family.

- **No gene symbol.** UniProt lists only `OrderedLocusNames=At5g03810`; GOA uses
  `At5g03810` as the symbol, which is what this review uses. The names "GDSL
  esterase/lipase At5g03810" and "Extracellular lipase At5g03810" and `EC=3.1.1.-`
  are family-derived placeholders, not results, as are the keywords `Hydrolase`,
  `Lipid degradation`, `Lipid metabolism`.
- **Family/architecture only.** 353 aa precursor; predicted signal peptide 1..24;
  Pfam PF00657 `Lipase_GDSL`, PROSITE PS01098 `LIPASE_GDSL_SER`, CDD `cd01837
  SGNH_plant_lipase_like`, InterPro IPR001087 / IPR008265 / IPR035669 /
  IPR036514; PANTHER `PTHR45642:SF103`. Catalytic triad Ser37 (nucleophile),
  Asp328, His331 all `ACT_SITE ... /evidence="ECO:0000250"` — by similarity. Five
  predicted N-glycosylation sites (`ECO:0000255`).
- **Protein existence is only inferred.** `PE 3: Inferred from homology` — the
  weakest level, and consistent with the cross-references: every EMBL entry is
  `Genomic_DNA` (the EU3520xx series is ecotype resequencing from PMID:18273534),
  with no cDNA or EST and no proteomics hit. Contrast its paralog AT3G16370
  (Q9LU14, `PE 2`), which is repeatedly detected in apoplast proteomes.
- **Location is prediction only.** `CC SUBCELLULAR LOCATION: Secreted
  {ECO:0000305}`; the two GO rows for GO:0005576 are IEA (ARBA + SubCell
  mapping) and ISM (TAIR AtSubP). No experimental localisation.
- **No publication mentions it.** Literature searches, 2026-11-06:
  PubMed `At5g03810 OR "AT5G03810"` → 0 hits. Europe PMC full-text
  `"AT5G03810"` → 2 hits, both about other species (PMID:40926154, cabbage
  female sterility fine-mapping; PMID:34155325, *Angelica* bolting
  transcriptome), neither a study of this gene. Europe PMC `"Q9FFN0"` → **0
  hits**. It is absent from the Arabidopsis GDSL functional surveys that cover
  its relatives (it is not among the 19 guard-cell GGLs of PMID:34621289, nor
  among the suberin GELPs of PMID:33686223).

## The TAIR BP ND row is correct

`GO:0008150 biological_process` ND (`GO_REF:0000015`, TAIR, 2023-08-08) → **ACCEPT**,
`nd_case: TRUE_GAP`. No literature on this gene product in this species identifies
any biological process; the searches above are the record of that check. Per the
ND guideline, the two electronic BP rows in the same aspect (GO:0008610 IBA,
GO:0006629 IEA) are *not* literature on the gene and do not make the ND stale.
Paired with a BIOLOGY knowledge gap, `dark_aspect: WHOLLY_DARK` (only root terms,
family IEAs and IBAs survive review).

## Verdict on the GO:0008610 lipid biosynthetic process IBA

**The IBA does not hold for this gene. Action: MARK_AS_OVER_ANNOTATED.**

The analysis is the same as for its 171-leaf-clade relative AT3G16370 (see
`genes/ARATH/APG__Q9LU14/APG__Q9LU14-notes.md` for the full working); summarised:

1. **Nothing on this gene supports it** — no literature at all, no experimental
   annotation, and a predicted *hydrolase* name that points away from synthesis.
   TAIR's own BP ND is a curator statement that no process is known.
2. **The IBD is at a LUCA node with one bacterial seed.** Re-checked with
   `projects/PSEUDOCAP/panther_tree.py node PTN005219546` (2026-11-06):
   `SPECIATION LUCA`, 960 leaves — PTN005219547 Eukaryota 952 (PTN005219553
   Viridiplantae 940, PTN008144646 Dikarya 12) and PTN005220548 Eubacteria 8.
   The GO:0008610 IBD has the single seed UniProtKB:O33407 (*P. aeruginosa*
   EstA); QuickGO (2026-11-06) returns 885 leaf IBAs from it across 48 taxa,
   overwhelmingly plant GELPs. The seed row is an *estA* deletion that makes
   little rhamnolipid — necessity, not participation (`genes/PSEAE/estA`).
3. **The clade does contain one genuine biosynthetic member, which the estA
   review missed.** OSP1 / AT2G04570 (UniProtKB:Q9SJB4, PTHR45642:SF32) is a
   leaf of the same node and is experimentally tied to cuticular wax synthesis
   [PMID:32542680 "significant reduction in leaf wax synthesis and occlusion of
   stomata, leading to"; "demonstrated that OSP1 possesses thioesterase activity,
   particularly on C22:0"], curated by TAIR as GO:0016297 IDA with no BP term.
   So the estA review's claim that the clade "offers no positive evidence for a
   biosynthetic process" needs correcting.
4. **It still does not license this row.** OSP1's role is angiosperm-specific
   wax metabolism, unrelated to the bacterial glycolipid phenotype that seeded
   the node; the MRCA of OSP1 and AT5G03810 is PTN008693276 (892 leaves,
   DUPLICATION) — the base of the plant clade; and a survey of all 39
   Arabidopsis leaves of PTN005219546 (QuickGO, 2026-11-06) finds no
   experimental BP annotation anywhere in the clade.

Node-level defect recorded against GO_CENTRAL; `MARK_AS_OVER_ANNOTATED` rather
than `REMOVE` because the term is not demonstrably false for a secreted plant
GDSL enzyme, only unsupported here.

## Other annotation calls

- GO:0052689 carboxylic ester hydrolase activity IBA — **ACCEPT**, core. This is
  the other IBD at the same node, with two experimentally grounded seeds
  (EstA esterase, ChoE/PA4921 cholinesterase IDA), and the SGNH triad plus the
  PROSITE GDSL serine motif are intact here. No substrate has been measured, so
  no more specific term is warranted.
- GO:0016298 lipase activity IEA (InterPro:IPR008265) — **MODIFY** →
  GO:0052689. IPR008265 is the GDSL serine active-site motif, shared by
  esterases and lipases alike; "lipase activity" asserts a lipid (acylglycerol)
  substrate that has never been tested for this protein. Generalising to the
  carboxylic-ester-hydrolase term the gene already carries is the correction.
- GO:0006629 lipid metabolic process IEA (InterPro:IPR008265) — **MARK_AS_OVER_ANNOTATED**.
  Same signature; no lipid substrate established. (Characterised GELPs in this
  family act on many non-acylglycerol esters.)
- GO:0016746 acyltransferase activity IEA (ARBA:ARBA00027718) — **REMOVE**. An
  unvetted ARBA rule asserting the *opposite* chemistry (acyl transfer rather
  than hydrolysis). GDSL acyltransferases do exist (cutin synthases), but this
  protein has no such evidence, and the rule is applied family-wide: the same
  ARBA row sits on AT1G20120, AT1G20132, AT1G20135, AT1G58525, AT3G43550,
  AT3G43570, AT1G73610, EXL1–6 and more (QuickGO, 2026-11-06). Asserting both
  hydrolase and acyltransferase activity from one signature is over-propagation.
- GO:0016788 hydrolase activity, acting on ester bonds IEA — **TOO_GENERAL**,
  entailed by GO:0052689.
- GO:0005576 extracellular region ×2 (IEA, ISM) — **ACCEPT** both (consistent
  actions for the shared term). Prediction-only, but it is the only location
  claim the evidence allows: a cleavable signal peptide, no TM segment, and a
  curated `Secreted` statement.

## Open questions / experiments

- Is the gene expressed at all, and where? It has no cDNA, EST or proteomics
  support. RT-qPCR / promoter-GUS across tissues and stresses, and a check of
  single-cell and apoplast datasets, would establish whether a protein is made
  (if not, the right record is an EXISTENCE-style gap, not a function gap).
- What does it hydrolyse? Purified-enzyme substrate panel as for AT3G16370.
- AT5G03810 and its tandem neighbour AT5G03820 (Q9LZC5) carry identical
  predicted annotations and the same two IBAs; a double mutant is the obvious
  first genetic test, given the redundancy that dominates this family.
