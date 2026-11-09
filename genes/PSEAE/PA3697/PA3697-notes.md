# PA3697 (Q9HXU3) notes

No deep-research provider was available; this is a manual literature review
(PubMed search, cached abstracts). Both P. aeruginosa papers are abstract-only.

## Identity

- UniProt Q9HXU3 (TrEMBL, PE 4 predicted), 431 aa. Name "Flavohemoglobin
  expression-modulating QEGLA motif protein" is a ProtNLM machine name
  (ECO:0008006), not curated.
- Domains: Pfam PF08014 MATCAP (formerly DUF1704), InterPro IPR012548 MATCAP and
  IPR012656 CHP02421_QEGLA, NCBIfam TIGR02421 QEGLA, SMART SM01154 DUF1704,
  PANTHER PTHR31817. Zn2+ cofactor and the Hydrolase / Metalloprotease / Protease
  keywords are ARBA predictions only (unvetted).
- The MATCAP domain is named after the animal microtubule-associated tyrosine
  carboxypeptidase, a metalloprotease that detyrosinates alpha-tubulin
  [PMID:35482892 "We used haploid genetic screens to identify an unannotated
  protein, microtubule associated tyrosine carboxypeptidase (MATCAP), as a
  remaining detyrosinating enzyme."]. Bacterial members have no characterised
  activity; tubulin is absent from P. aeruginosa, so the animal substrate does
  not transfer. No activity is proposed here.

## Literature

- Koskenkorva et al. 2008 (PMID:18043907, PseudoCAP seed paper). The fhp-fhpR
  intergenic region was used as bait "to isolate proteins affecting the
  transcription of fhp and fhpR", identifying FhpR plus PA0779 and PA3697.
  "Both PA0779 and PA3697 were found to be essential for NO3(-) and NO2(-)
  induced Pfhp activity under aerobic and low-oxygen conditions, and needed for
  the full function of Pfhp/PfhpR as NO responsive regulatory circuit under
  aerobic conditions." [PMID:18043907]. The measured readout is promoter
  activity of the flavohemoglobin gene in mutants; NO levels or NO metabolism
  were not reported in the abstract. Whether PA3697 binds the promoter directly
  (affinity isolation could be indirect or nonspecific) cannot be judged from
  the abstract.
- Koskenkorva-Frank and Kallio 2009 (PMID:19767835): ROS-induced fhp promoter
  activity also depended on FhpR, PA0779 and PA3697 [PMID:19767835 "ROS-induced
  fhp promoter activity was dependent on FhpR, PA0779, and PA3697 regulators."].
  Again a promoter-reporter phenotype.
- PubMed searches for PA3697 return only these two papers.

## GO term reasoning

- GO:0080164 regulation of nitric oxide metabolic process: "Any process that
  modulates the frequency, rate or extent of the chemical reactions and pathways
  involving nitric oxide". The evidence is that PA3697 is needed for full
  induction of the fhp promoter. Fhp detoxifies NO, so an effect on NO
  metabolism is a plausible downstream consequence, but it is two steps removed
  (gene -> fhp transcription -> Fhp protein -> NO) and was not measured. The
  mechanism (direct DNA binding? proteolysis of a regulator, as the MATCAP
  domain would suggest?) is unknown. Mutant reporter phenotype ->
  INDIRECT-PHENOTYPE.
- A more literal reading would be regulation of transcription of fhp (e.g.
  GO:0045893 positive regulation of DNA-templated transcription), but without
  evidence that PA3697 is a transcription factor or acts directly, proposing it
  would just restate the same phenotype with a different term. No NEW.
- Node breadth: QuickGO (2026-10-28) lists 175 GO:0080164 IBA rows citing
  PANTHER:PTN002422332 (worklist: 5 leaf IBAs in 5 taxa in the reference set).
  Leaves include dozens of Legionella spp. (Lfee_, Lbru_, LHA_, ...),
  Chondromyces (CMC5_), Planctomycetes (Pla133_, Poly30_) and many other
  lineages. A single promoter-fusion phenotype in one Pseudomonas strain, whose
  mechanism is unknown and which depends on the presence of the Fhp/FhpR system,
  cannot be inherited across such a clade.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002422332 | GO:0080164 regulation of nitric oxide metabolic process | 1 (sole seed) | 5 (5 taxa) in worklist; 175 in current GOA | GO:0080164 regulation of nitric oxide metabolic process, IMP, PMID:18043907 (PseudoCAP) | INDIRECT-PHENOTYPE | The paper shows PA3697 mutants lose NO3-/NO2--induced activity of the flavohemoglobin (fhp) promoter; NO metabolism itself was not measured and the mechanism is unknown. PA3697 is a MATCAP/QEGLA-domain protein of unknown activity (putative metalloprotease, ARBA only), not a known regulator. A reporter phenotype tied to the P. aeruginosa Fhp/FhpR circuit is not a heritable family function, and the node spans Legionella, myxobacteria, planctomycetes and others. The IBD should be withdrawn. |

## Decisions summary

- regulation of nitric oxide metabolic process, IMP: MARK_AS_OVER_ANNOTATED
  (real gene-specific phenotype, but the term goes beyond the assay); PSEUDOCAP
  WRONG_TERM CHECK (SUSPECTED).
- regulation of nitric oxide metabolic process, IBA: MARK_AS_OVER_ANNOTATED
  (consistent with the IMP row); GO_CENTRAL defect asking to withdraw the IBD at
  PTN002422332.
- No core MF can be assigned; core_functions records only the observed role in
  fhp expression, without a GO MF.
