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


## Source-based reassessment — 2026-10-18

This entry supersedes the earlier blanket interpretation of interaction screens, nucleolar staining and the duplicate glycan-supply core; the earlier notes remain intact. The 25 historical imported assertions retain all source fields. All 45 current GOA contexts map to those same 25 term/evidence/reference triples, with additional partner detail rather than new biological assertions. The inherited authored GO:0006488 proposal remains visible with `retired: true`; no imported GOA assertion is retired.

The single core is CTP-dependent dolichol phosphorylation at the ER membrane, directly producing Dol-P. The human cDNA and topology papers support this mechanism at their available complete-abstract scope. Later human patient-cell studies directly assay the reaction: [PMID:17273964, Methods and Figure 4](https://pmc.ncbi.nlm.nih.gov/articles/PMC1821118/) uses crude fibroblast extracts, radiolabeled CTP, dolichol and a no-dolichol background; [PMID:22242004](https://pubmed.ncbi.nlm.nih.gov/22242004/) independently measures Dol-P formation and uses sequence-verified human ORFs for yeast complementation. These assays are not purified-enzyme kinetics.

GO:0006488 describes glycosyl-chain assembly on the lipid carrier. DOLK supplies Dol-P, while downstream enzymes add the glycosyl residues. Rescue of CPY glycosylation and reduced LLO abundance establish downstream dependence, without identifying a DOLK glycosyl-addition step. Same-role comparator annotations are mixed: SRD5A3 carries GO:0006488, whereas the checked DHDDS, DOLPP1 and yeast SEC59 records do not. This is not evidence for a universal exclusion convention or a missing-annotation gap. The target GO-CAM models the established kinase/Dol-P process. The conservative revision withdraws the historical additional authored assertion rather than treating necessity alone as direct participation.

The positive EDA binary pair supports cytokine-partner binding, and the KCNA3 53–575 pair supports transmembrane-transporter binding. Neither asserts receptor agonism, channel regulation or a native DOLK signaling pathway. Three heterogeneous BioPlex/HuRI aggregate rows remain non-core. The [executed interaction audit](DOLK-bioinformatics/interaction-audit/RESULTS.md) preserves all 42 raw fields, roles, regions, source contexts and independently computed sequence checks. Different actions for repeated partners reflect the scope of each historical aggregate. No interaction is rejected merely because its term is generic.

[PMID:26871637, Figure 6D and Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC4882190/) reports divergent yeast rescue and interaction profiles for historical clones DOLK_1 and DOLK_2: DOLK_1 rescues and binds KCNA3, whereas DOLK_2 does not rescue and binds UBQLN1 splice constructs. The figure itself was inspected. Clone-sequence supplements were not recovered, so these names are not assigned to additional official isoforms. The current official record contains one 538-residue protein and no alternative-products block. A failed yeast rescue in that construct context is not universal inactivity in every setting.

The target-resolved HPA XML supports nucleolar staining with two approved ICC/IF antibodies, including nucleolar observations in three cell lines for HPA068706. Multipass ER topology alone does not establish that this signal is background. The observation is retained as contextual localization, without assigning nucleolar kinase activity or claiming that image pixels or genetic antibody controls were assessed.

PAINT tree, alignment and the three literal IBD placements support the target lineage and the established activity/process/location. Target experimental evidence within the IBD descendants is legitimate. Reactome's normal reaction and the failed-reaction variant set are treated separately; a gene-level kinase assignment does not imply normal activity for every pathogenic variant.

The [source and assay guide](DOLK-source-guide.md) supplies public source locators, model paths and access limits. Existing publication files and flags are unchanged. The configured Falcon research attempt failed with HTTP 403 and its configured fallback failed with HTTP 401; no provider report was fabricated. Manual evidence and notes supply the assessment.
