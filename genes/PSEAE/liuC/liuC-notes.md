# liuC (Q9I298, PA2013) notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol, worklist rank 40)

No deep-research provider was available. The two PseudoCAP-cited papers (PMID:16517656, PMID:16820476)
are abstract-only and the PubMed MCP returned no PMC full text. I cached four further papers on the Liu/Atu
pathways with `just fetch-pmid` (PMID:16272386, PMID:18625020, PMID:19459965, PMID:27271456); all are
abstract-only.

## Identity

- *P. aeruginosa* PAO1 locus PA2013, UniProt Q9I298 (unreviewed), 265 aa; submitted name
  "3-methylglutaconyl-CoA hydratase" (ECO:0000313, not evidence).
- Enoyl-CoA hydratase/isomerase (crotonase) family: Pfam PF00378 (ECH_1), PROSITE PS00166
  (ENOYL_COA_HYDRATASE), InterPro IPR001753, IPR018376; PANTHER PTHR42964:SF1.
- Third gene of the liuRABCDE cluster (PA2011-PA2016); LiuB/LiuD (PA2014/PA2012) are the
  methylcrotonyl-CoA carboxylase subunits [PMID:16272386 "The two subunits of MCase corresponded to
  liuB/liuD (PA2014/PA2012)"], LiuE (PA2011) the HMG-CoA lyase [PMID:19459965 "the liuE gene of P.
  aeruginosa encodes for the HMG-CoA lyase"].

## Pathway logic

Leucine/isovalerate catabolism: isovaleryl-CoA (LiuA) -> 3-methylcrotonyl-CoA -> carboxylation (LiuB/LiuD)
-> 3-methylglutaconyl-CoA -> hydration (LiuC, the step this gene is named for) -> HMG-CoA -> cleavage
(LiuE) -> acetyl-CoA + acetoacetate. Acyclic monoterpenoids (citronellol, geraniol) are degraded by the Atu
pathway, which joins the Liu pathway at methylcrotonyl-CoA [PMID:16272386 "The catabolic pathway of
citronellol (Atu, acyclic terpene utilization) enters that of leucine/isovalerate (Liu, leucine and
isovalerate utilization) at the level of methylcrotonyl-CoA."]. LiuC therefore acts in both pathways in
P. aeruginosa, and the genetics agree: [PMID:18625020 "Mutants with insertion in any of the liu genes were
unable to utilize acyclic terpenes or leucine/isovalerate"]; [PMID:16517656 "Our results suggest that the
atu and liu clusters are bifunctional operons involved in both the AMTC and leucine catabolic pathways."].

The terpene role is not a property of the hydratase: LiuC acts on 3-methylglutaconyl-CoA, which is a
leucine catabolic intermediate. Terpenoid catabolism uses LiuC only where an Atu pathway feeds
methylcrotonyl-CoA into the Liu pathway. Most organisms with a LiuC-type hydratase have leucine catabolism
and no Atu pathway; P. putida KT2440 grows on leucine but not on acyclic terpenes [PMID:16820476 "P.
fluorescens, but not P. putida, could grow on acyclic terpenes (citronellol and citronellate), while both
species were able to utilize leucine and isovalerate"].

## Term precision

GO:0046247 terpene catabolic process is defined for terpene hydrocarbons. Citronellol and geraniol are
monoterpenoid alcohols (C10), so GO:0016100 monoterpenoid catabolic process (is_a terpenoid catabolic
process is_a isoprenoid catabolic process GO:0008300) is the accurate term.

## Molecular function evidence

No purified-enzyme assay of P. aeruginosa LiuC was found. The PseudoCAP MF row is IMP to PMID:16517656, whose
abstract does not mention a liuC mutant or a hydratase assay. The MF is nevertheless well supported by
pathway logic (it is the only hydratase in the liu cluster, whose carboxylase product is
3-methylglutaconyl-CoA and whose lyase substrate is HMG-CoA), by the crotonase-family signature, and by the
characterised Myxococcus LiuC homolog [PMID:27271456 "The first step into this pathway is mediated by LiuC,
a member of the 3-methylglutaconyl CoA hydratases (MGCH)."] (a different paralog, which that paper notes is
more similar to human MGCH than to bacterial forms).

## Annotation decisions

- GO:0004490 methylglutaconyl-CoA hydratase activity (IMP PseudoCAP; IBA): ACCEPT, core MF (deferring on
  the IMP full text).
- GO:0006552 L-leucine catabolic process (IMP): ACCEPT, core BP.
- GO:0046247 terpene catabolic process (IMP PseudoCAP; IBA): MODIFY to GO:0016100 monoterpenoid catabolic
  process; KEEP the claim for PAO1, but the IBA should not have been propagated (GO_CENTRAL defect).
- GO:0008300 isoprenoid catabolic process (IMP): MODIFY to GO:0016100.
- GO:0003824 catalytic activity (IEA InterPro): MODIFY to GO:0004490.

## PseudoCAP IBA-seed assessment

QuickGO (2026-10-28, withFrom=PANTHER:PTN001733227) returns 13 leaves, each with GO:0004490 and GO:0046247:
PAO1 LiuC (Q9I298) and AtuE (Q9HZV7, isohexenylglutaconyl-CoA hydratase of the Atu pathway), *B. subtilis*
PksH (P40805, bacillaene synthase dehydratase, which per UniProt (ECO:0000269) dehydrates an HMG group
tethered to the carrier protein PksL, not a CoA thioester), Coxiella PksH-like and CBU_0976, *M.
tuberculosis* EchA7, Shewanella LiuC, Xanthomonas FadB and XCC1833, Bradyrhizobium bll0116, Streptomyces
SCO4384, Chloroflexus Caur_1565 and the choanoflagellate *Monosiga brevicollis*.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN001733227 | GO:0046247 terpene catabolic process | 1 (sole) | 13 (10 taxa) | GO:0046247, IMP, PMID:16820476 (PseudoCAP) | OVER-SPECIFIC | For PAO1 the claim holds (liu mutants cannot use acyclic terpenes, PMID:18625020; the Atu pathway enters the Liu pathway at methylcrotonyl-CoA, PMID:16272386), though GO:0016100 monoterpenoid catabolic process is the accurate term. But terpenoid catabolism is an organism-level pathway context (an Atu pathway feeding the leucine pathway), not a property of the hydratase. It is not inherited by the clade: Mycobacterium, Bacillus PksH, Coxiella, Xanthomonas, Streptomyces, Chloroflexus and Monosiga have no Atu pathway, and even P. putida, with a Liu pathway, cannot grow on acyclic terpenes. The IBD should be withdrawn. |
| PTN001733227 | GO:0004490 methylglutaconyl-CoA hydratase activity | 1 (sole) | 13 (10 taxa) | GO:0004490, IMP, PMID:16517656 (PseudoCAP) | UNVERIFIABLE | The seed is a mutant-based MF inference from an abstract-only paper that does not mention liuC or a hydratase assay. The activity is very likely right for LiuC by pathway logic. The node term is too specific for the clade: it includes AtuE (a different substrate, isohexenylglutaconyl-CoA) and B. subtilis PksH, an experimentally characterised polyketide-pathway dehydratase acting on a carrier-protein-bound HMG group rather than on HMG-CoA. A generic hydro-lyase/enoyl-CoA hydratase term, or a node restricted to LiuC orthologs, would be safer. |

## PANTHER tree check (2026-11-05)

Topology of PTN001733227 fetched with `projects/PSEUDOCAP/panther_tree.py node
PTN001733227 --depth 4 / --leaves / --contains` (PANTHER `treeinfo` for PTHR42964).

**PTN001733227: SPECIATION, placed at LUCA, 13 leaves, all PTHR42964:SF1.**

| child node | event / taxon | leaves | subfamilies | content | verdict |
|---|---|---|---|---|---|
| PTN000941888 | LEAF *Monosiga brevicollis* | 1 | SF1 | enoyl-CoA hydratase | no Liu/Atu pathway |
| PTN000234935 | SPECIATION Eubacteria | 12 | SF1 | all bacteria | — |
| └ PTN008092237 | SPECIATION Terrabacteria | 4 | SF1 | *B. subtilis* PksH (bacillaene dehydratase), *Chloroflexus*, *M. tuberculosis* EchA7, *S. coelicolor* | substrates not 3-methylglutaconyl-CoA |
| └ PTN000234939 | SPECIATION Proteobacteria | 8 | SF1 | *Bradyrhizobium* bll0116 + PTN001733230 | — |
| &nbsp;&nbsp;&nbsp;└ PTN001733230 | SPECIATION Gammaproteobacteria | 7 | SF1 | Coxiella pair PTN001733228, *Shewanella* LiuC, Xanthomonas pair PTN002873558 (one a p-hydroxycinnamoyl-CoA hydratase/lyase), PAO1 pair PTN002452381 | narrowest clade holding all three MG-CoA hydratases; still heterogeneous |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PTN002452381 | DUPLICATION *P. aeruginosa* | 2 | SF1 | AtuE (PTN002452382) + LiuC (PTN002452383) | the only clade in which acyclic terpenoid catabolism holds |

Conclusions:

- The node's event placement is **LUCA**, so both IBDs assert their term as ancestral
  to all life. For a substrate-specific crotonase activity, and still more for a
  pathway context that depends on an organism having an Atu cluster, that is not
  supportable.
- **LiuC's own sister leaf is AtuE**, a hydratase with a different substrate
  (`--contains Q9I298,Q9HZV7` -> PTN002452381, 2 leaves). The smallest clade holding
  the three methylglutaconyl-CoA hydratases of the family (PAO1 Q9I298, *Shewanella*
  Q8EFS1, *Coxiella* Q83CX5) is PTN001733230, which also holds AtuE, *Coxiella* PksH
  and the two *Xanthomonas* enzymes. So there is **no LiuC-ortholog-only subnode**;
  GO:0004490 belongs at the leaves, and the node should carry a generic enoyl-CoA
  hydratase/hydro-lyase term.
- For GO:0046247 the tree does supply one defensible target: PTN002452381, the PAO1
  LiuC/AtuE duplication pair, since both participate in acyclic terpene utilisation in
  P. aeruginosa. Everything above that is over-propagation.

Both defects raised to CONFIRMED (GO:0004490 SUSPECTED -> CONFIRMED, GO:0046247
PROBABLE -> CONFIRMED). Annotation actions unchanged: ACCEPT on the GO:0004490 IBA
(correct for this gene) and MODIFY to GO:0016100 on the GO:0046247 rows.
