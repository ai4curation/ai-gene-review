# DOLK (dolichol kinase, Q9UPQ8) — review notes

## Summary of function
DOLK catalyses the CTP-dependent phosphorylation of dolichol to dolichyl monophosphate
(Dol-P), the terminal step of de novo Dol-P biosynthesis at the ER membrane. Dol-P is the
essential lipid carrier that primes dolichol-linked oligosaccharide (LLO) assembly for
protein N-glycosylation and is also required for O-mannosylation, C-mannosylation and
GPI-anchor biosynthesis.

- EC 2.7.1.108; RHEA:13133 (di-trans,poly-cis-dolichol + CTP = di-trans,poly-cis-dolichyl
  phosphate + CDP + H+).
- Polytopic ER membrane protein (~15 TM helices), cytoplasmically oriented CTP-binding site
  (loop between TMD11-12, (470)KKTXEG(475) motif). [PMID:16923818]
- KM 22.8 uM dolichol, 3.5 uM CTP. [PMID:16923818, UniProt]
- Belongs to the polyprenol kinase family; InterPro IPR032974; PANTHER PTHR13205:SF15.

## Key experimental evidence
- [PMID:12213788] Human cDNA (hDK1) complements yeast sec59-1 ts defect in DK activity;
  elevates DK activity, increases Dol-P, restores N-glycosylation of carboxypeptidase Y.
  Dolichol and DAG phosphorylation are separate CTP-mediated kinase activities.
  "Dolichol kinase (DK) catalyzes the CTP-mediated phosphorylation of dolichol in eukaryotic
  cells, the terminal step in dolichyl monophosphate (Dol-P) biosynthesis de novo." GOA
  attaches IGI (with yeast SEC59 P20048) + IDA to this paper.
- [PMID:16923818] Overexpression in CHO; polytopic ER membrane protein; CTP-binding site
  mapped; G443D inactivates. IDA for MF and located_in ER membrane.
- [PMID:17273964] DOLK-CDG (CDG1M / DK1 deficiency); Cys99Ser, Tyr441Ser variants with
  2-4% residual activity; death in early infancy; two patients died of dilative
  cardiomyopathy. Dol-P "involved in several glycosylation reactions, such as
  N-glycosylation, glycosylphosphatidylinositol (GPI)-anchor biosynthesis, and C- and
  O-mannosylation." EXP for MF.
- [PMID:22242004] Autosomal recessive dilated cardiomyopathy from DOLK mutations; DK
  deficiency confirmed in patient fibroblasts; reduced alpha-dystroglycan O-mannosylation.
  IMP for MF and BP.
- [PMID:23890587] purely neurological DOLK-CDG (UniProt disease ref; not in GOA lines).
- [PMID:28816422] two new DOLK-CDG cases, phenotype expansion (UniProt; not in GOA).

## Interactome / protein binding IPIs
IntAct GO:0005515 protein binding annotations derive from large-scale binary interactome /
AP-MS maps (PMID:25416956, 26871637, 28514442, 32296183, 33961781). Interactors are largely
co-ER membrane proteins (ion channels KCNA1/3/6/10, CD79A, GPX8, EDA, etc.). None establish a
specific molecular function for DOLK; per curation policy `protein binding` is uninformative
and these are MARK_AS_OVER_ANNOTATED (not REMOVE — experimental IPIs).

## Localization
- ER membrane: IDA (PMID:16923818), IBA, IEA (SubCell), Reactome TAS — all consistent. Core.
- Nucleolus: single HPA IDA (GO_REF:0000052). Inconsistent with an integral polytopic ER
  membrane kinase; HPA IF can give background nucleolar signal. MARK_AS_OVER_ANNOTATED.

## Term decisions
- MF: GO:0004168 dolichol kinase activity — GOA current term, EC 2.7.1.108. Core. ACCEPT all
  (IBA, IEA/RHEA, EXP, IMP, IDA, Reactome TAS).
- BP: GO:0043048 dolichyl monophosphate biosynthetic process — direct product of the reaction.
  Core. ACCEPT all. (Also relevant: GO:0006488 dolichol-linked oligosaccharide biosynthetic
  process for the downstream N-glycosylation role — used in core_functions.)
- CC: GO:0005789 ER membrane — Core. ACCEPT.
