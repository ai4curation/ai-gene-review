# pilM (PA5044, G3XD28) notes

No deep-research provider was available; this is my own literature review
(PubMed MCP plus cached publications).

## Identity

- UniProt G3XD28 (PILM_PSEAE), 354 aa, Swiss-Prot reviewed; locus PA5044,
  first gene of the pilMNOPQ operon. Matches the worklist accession.
- Actin-like / FtsA-MreB fold ATP-binding protein (IPR005883 PilM,
  TIGR01175, Pfam PF11104 PilM_2; PANTHER PTHR32432:SF3, a subfamily that
  PANTHER names after EutJ and that also contains the ethanolamine
  utilization protein EutJ).

## Function

- Identified in a twitching-motility transposon screen; pilM-P mutants lack
  functional fimbriae (twitching, fimbria-specific phage, EM), and PilM shares
  motifs with FtsA/MreB/actin ATPase domains [PMID:7565110 "PilM-P were found
  to be required for fimbrial biogenesis by complementation studies using
  twitching motility and sensitivity to fimbrial-specific phage as indicators
  of the presence of functional fimbriae"].
- PilM/N/O/P form an inner-membrane alignment subcomplex; PilM, although
  nominally cytoplasmic, co-fractionates with the inner membrane; loss of any
  component destabilises the others and the PilQ secretin [PMID:19857645
  "all four proteins, including the nominally cytoplasmic PilM, colocalized to
  the inner membrane"].
- The cytoplasmic N-terminal tail of PilN binds PilM [PMID:23457250 "the
  N-terminal cytoplasmic tail of PilN binds to the actin-like protein PilM,
  thereby connecting all cellular compartments via the PilMNOPQ protein
  interaction network"].
- Crystal structures of P. aeruginosa PilM and PilM-PilN(1-12) chimera: PilM
  binds ATP; PilN binding monomerises PilM and closes the domain around the
  ATP site; PilM binds PilB and PilT directly (pull-down) and PilC by
  two-hybrid [PMID:27022027 "Pull-down experiments demonstrated direct
  interactions of PilM with PilB and PilT"].
- Thermus PilM binds ATP but no ATP hydrolysis was detected [PMID:21596754
  "We find no evidence for the catalysis of ATP hydrolysis by PilM"];
  Myxococcus PilM-N(1-16) binds but does not hydrolyse ATP [PMID:26851283
  "PilM-N(1-16) was isolated as a monomer that bound but did not hydrolyze ATP"].
  So PilM is an ATP-binding, not an ATPase, protein.
- pilM deletion blocks PilNO disulfide heterodimer formation in vivo
  [PMID:27474743 "Deletion of genes encoding alignment subcomplex components,
  PilM or PilP, but not other T4P components, including the motor ATPases PilB
  or PilT, blocked in vivo formation of disulfide-bonded PilNO heterodimers"].

Summary: PilM is the cytoplasmic, ATP-binding, actin-like component of the
PilMNOP alignment subcomplex of the type IVa pilus machine. It docks on the
inner membrane through the PilN N-terminus and links the alignment subcomplex
to the motor (PilB, PilT, PilC). It is not a pilus fibre subunit.

## GO term check

- GO:0044096 type IV pilus: "A short filamentous structure on the surface of a
  bacterial cell distinguished from other pili by post-translational
  N-methylation of the pilin monomers." This is the fibre. PilM is
  cytoplasmic/inner-membrane-associated and is not part of the fibre. There is
  no GO CC for the type IV pilus assembly machine.
- Comparator check (QuickGO, exact GO:0044096, experimental codes): IDA rows are
  on pilins/minor pilins (pilA, fimU, pilV, pilW, pilX) and PilY1; the IMP rows
  are PseudoCAP pilM, pilN, pilO, pilP (all PMID:7565110) and fimV. The
  pilMNOP IMP rows all come from the same mutant screen, i.e. "mutant has no
  pili" was annotated as a location.

## PANTHER node PTN001286216

QuickGO IBA rows for both GO:0044096 and GO:0043107 from PTN001286216 (23
leaves each, WITH UniProtKB:G3XD28 only). Leaves include genuine PilM
orthologs (Neisseria NMB1808, Xanthomonas XCC3232, Shewanella SO_0281,
Geobacter GSU2032, Synechocystis, Deinococcus DR_0770, Vibrio VC_2634), but
also ethanolamine utilization protein EutJ of E. coli K-12 (P77277, b2454) and
Salmonella LT2 (P0A206, STM2462), an EutJ-named Fusobacterium protein
(Q8RI50), Listeria lmo1161 and other uncharacterised FtsA-like proteins (UniProt
REST, PANTHER PTHR32432:SF3 for all). EutJ belongs to the eut microcompartment
operon and is not a pilus protein, so the node is broader than the PilM clade:
both IBDs over-propagate to EutJ leaves.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN001286216 | GO:0044096 type IV pilus | 1 (sole) | 23 (20 taxa) | GO:0044096 type IV pilus, located_in, IMP, PMID:7565110 (PseudoCAP) | WRONG | A mutant phenotype (no fimbriae) annotated as a location. PilM is a cytoplasmic, inner-membrane-docked component of the assembly machine, not part of the surface fibre the term defines. The IBD has no other support; it also reaches EutJ proteins. |
| PTN001286216 | GO:0043107 type IV pilus-dependent motility | 1 (sole) | 23 (20 taxa) | GO:0043107, IMP, PMID:7565110 and PMID:19857645 (PseudoCAP) | SOUND (seed); node too broad | The seed is right for PilM: a core T4P machine component whose loss abolishes twitching. But the node includes E. coli and Salmonella EutJ and other non-pilus FtsA-like proteins, so the clade-wide claim over-propagates; GO_CENTRAL asked to move the IBD to a PilM-only node. |

## Decisions summary

- ACCEPT: cytoplasm (EXP, IEA); type IV pilus-dependent motility (IBA, IMP x2);
  type IV pilus assembly (IMP x2).
- REMOVE: type IV pilus (IMP PseudoCAP; IBA); cell division (IEA, SHS2 FtsA
  domain mapping).
- NEW: ATP binding (IDA, PMID:27022027); cytoplasmic side of plasma membrane
  (IC from PMID:19857645 fractionation + PilN-tail binding PMID:23457250).

## Leaf evidence check (2026-11-06)

Audit of the leaf claims in the `GO_CENTRAL` source defects on PTN001286216.
Leaf membership and subfamily confirmed with
`uv run python projects/PSEUDOCAP/panther_tree.py node PTN001286216 --leaves`
(23 leaves, all PTHR32432:SF3); UniProt flat files fetched for all 23 accessions.

Discriminator found: the seed and 14 other leaves match InterPro IPR005883 PilM
with Pfam PF11104 PilM_2 (10 of those also NCBIfam TIGR01175 pilM); four leaves
match InterPro IPR013366 EutJ with Pfam PF14450 FtsA and none of the PilM
signatures; four match neither family. No leaf other than G3XD28 carries any
experimental GO annotation.

| Leaf | Name and its evidence | Experimental annotations | Verdict |
|---|---|---|---|
| P77277 (E. coli b2454) | RecName "Ethanolamine utilization protein EutJ", curated (Reviewed); PE 3 | none; FUNCTION by ECO:0000250 from P0A206. Lies in the E. coli *eut* operon (CC CAUTION) | Claim survives on domain + operon context, not on the name: IPR013366 EutJ, PF14450 FtsA, no PilM signature |
| P0A206 (S. typhimurium STM2462) | RecName "Ethanolamine utilization protein EutJ", curated; GN from ECO:0000303 PubMed:7868611; PE 2 | no experimental GO rows, but curated ECO:0000269 FUNCTION/DISRUPTION PHENOTYPE from *eutJ* deletion and *eutJ/eutS* overexpression (PubMed:10464203, 16585748, 27063436), placing it in the 17-gene *eut* operon and its microcompartment | Claim survives, now on experimental curated statements |
| Q8RI50 (F. nucleatum FN1783) | **SubName** "Ethanolamine utilization protein eutJ" {ECO:0000313\|EMBL}; PE 3 | none | Name is **not evidence**; the EutJ claim is downgraded to the signature match (IPR013366, no PilM signature; Pfam HSP70 rather than FtsA) |
| Q8Y7V8 (L. monocytogenes lmo1161) | **SubName** "Lmo1161 protein" {ECO:0000313\|EMBL}; PE 4 Predicted | none | Not a pilus protein on two checkable grounds: IPR013366 EutJ / PF14450 FtsA with no PilM signature, and gene neighbourhood (lmo1160 phosphate propanoyltransferase, lmo1164 corrinoid adenosyltransferase) places it in the B12-dependent catabolic microcompartment locus |
| A0A0H2W2G1 (Y. pestis YPO0146) | SubName "Uncharacterized protein"; PE 4 | none | Carries IPR005883 PilM / PF11104, so the Enterobacteriaceae subclade PTN002089606 is **mixed**, not an "EutJ branch" |

Correction to the earlier entry: the tree offers **no PilM-only node** for the
seed. The smallest clade holding G3XD28 with other PilM-signature leaves is
PTN001596234, which already contains P77277 and P0A206, and the
Enterobacteriaceae clade below it is mixed (above). The requested change is
therefore NOT/IKR on the four EutJ-signature leaves, not a move.

Confidence: GO:0043107 defect PROBABLE -> CONFIRMED; GO:0044096 defect
PROBABLE -> CONFIRMED (the decisive fact for the latter is G3XD28's own
GO:0005737 cytoplasm EXP:UniProtKB annotation plus PMID:19857645, independent
of any leaf name).
