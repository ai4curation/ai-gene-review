# TYMP (thymidine phosphorylase) review notes

UniProtKB: P19971 (TYPH_HUMAN). Gene: TYMP; synonym ECGF1. HGNC:3148.
Also known as: Platelet-derived endothelial cell growth factor (PD-ECGF), Gliostatin, TdRPase.

## Core biochemistry
- EC 2.4.2.4. Catalyzes reversible phosphorolysis of thymidine (and 2'-deoxyuridine).
  Reaction (RHEA:16037): thymidine + phosphate <=> 2-deoxy-alpha-D-ribose 1-phosphate + thymine.
  [file:human/TYMP/TYMP-uniprot.txt "Reaction=thymidine + phosphate = 2-deoxy-alpha-D-ribose 1-phosphate +"]
- UniProt FUNCTION: "Catalyzes the reversible phosphorolysis of thymidine. The produced molecules are then
  utilized as carbon and energy sources or in the rescue of pyrimidine bases for nucleotide synthesis."
- Homodimer; active form 90 kDa homodimer [PMID:1590793 "recombinant human PD-ECGF occurs as a 90 kDa homodimer"]
  and confirmed by X-ray crystallography [PMID:14725767, 16803458, 19555658 via UniProt SUBUNIT].
- Cytosolic (IBA + Reactome TAS + UniProt).
- Pathway (UniProt): Pyrimidine metabolism; dTMP biosynthesis via salvage pathway; dTMP from thymine: step 1/2.
- Reactome R-HSA-112265 / R-HSA-112266: forward and reverse cytosolic reactions
  (thymidine or deoxyuridine + orthophosphate <=> thymine or uracil + 2-deoxy-D-ribose 1-phosphate).

## Discovery / moonlighting
- PD-ECGF = TYMP: recombinant human PD-ECGF has TP activity; PD-ECGF stimulates angiogenesis in vivo
  [PMID:1590793 "PD-ECGF has thymidine phosphorylase activity", "stimulates angiogenesis in vivo"].
  UniProt FUNCTION also: "Has growth promoting activity on endothelial cells, angiogenic activity in vivo
  and chemotactic activity on endothelial cells in vitro." The angiogenic/growth-factor role is an
  extracellular moonlighting function (MoonDB/MoonProt curated). Treated as NON-CORE.

## Disease: MNGIE / MTDPS1
- Loss-of-function TYMP mutations cause MNGIE (mitochondrial neurogastrointestinal encephalomyopathy),
  = mitochondrial DNA depletion syndrome 1 (MTDPS1, MIM:603041).
  [PMID:9924029 "loss-of-function mutations in TP cause the disease"; TP activity <5% of controls in
  MNGIE leukocytes; associated with multiple mtDNA deletions]. Mechanism: thymidine/deoxyuridine
  accumulation causes mitochondrial dNTP pool imbalance -> mtDNA instability/depletion.
  This grounds the core BP: by controlling systemic thymidine/deoxyuridine, TYMP protects the mtDNA pool.

## Annotation review summary (actions)
MF:
- GO:0009032 thymidine phosphorylase activity (IBA/IEA/IDA/IMP) -> ACCEPT (core).
- GO:0016154 pyrimidine-nucleoside phosphorylase activity (IEA) -> ACCEPT (also acts on deoxyuridine).
- GO:0004645 1,4-alpha-oligoglucan phosphorylase activity (IEA InterPro) -> REMOVE (glycogen-phosphorylase
  activity; wrong-branch InterPro over-mapping from the shared glycosyltransferase-family-3 fold).
- GO:0016757 glycosyltransferase activity (IEA) -> MARK_AS_OVER_ANNOTATED (uninformative parent from fold).
- GO:0016763 pentosyltransferase activity (IEA) -> MARK_AS_OVER_ANNOTATED (parent of TP activity; too general).
- GO:0042803 protein homodimerization activity (IDA PMID:1590793) -> ACCEPT.
- GO:0005515 protein binding (IPI PMID:32296183, HuRI) -> MARK_AS_OVER_ANNOTATED (bare protein binding).
BP:
- GO:0006213 pyrimidine nucleoside metabolic process (IEA/IDA/IMP) -> ACCEPT (core process).
- GO:0006206 pyrimidine nucleobase metabolic process (IEA) -> ACCEPT (produces thymine/uracil).
- GO:0055086 nucleobase-containing small molecule metabolic process (IEA ARBA) -> MARK_AS_OVER_ANNOTATED (general).
- GO:0072527 pyrimidine-containing compound metabolic process (IEA ARBA) -> MARK_AS_OVER_ANNOTATED (general parent).
- GO:1901135 carbohydrate derivative metabolic process (IEA ARBA) -> MARK_AS_OVER_ANNOTATED (general; deoxyribose-1-P product).
CC:
- GO:0005829 cytosol (IBA + TAS x2) -> ACCEPT.

Note: UniProt DR-line KW-derived GO (growth factor activity, angiogenesis, chemotaxis, cell differentiation,
dTMP catabolic process) are not in the GOA TSV, so not reviewed as existing_annotations; the angiogenic
moonlighting role is captured in the description and as non-core context.
