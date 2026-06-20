# DCAF10 (WDR32) Review Notes

UniProt: Q5QP82 (DCA10_HUMAN). HGNC:23686. Gene on chromosome 9. 559 aa.

## Identity and structure
- DDB1- and CUL4-associated factor 10; AltName WD repeat-containing protein 32 (WDR32) [file:human/DCAF10/DCAF10-uniprot.txt].
- WD40-repeat protein: UniProt annotates 7 WD repeats (REPEAT 166-205, 209-247, 251-290, 296-335, 408-448, 470-508, 526-559) forming a beta-propeller; InterPro IPR039085 (DCA10), WD40 domains; PANTHER PTHR14588 [file:human/DCAF10/DCAF10-uniprot.txt].
- Belongs to the "WD repeat DCAF10 family" (UniProt SIMILARITY) [file:human/DCAF10/DCAF10-uniprot.txt].
- N-terminal disordered region (1-119), with phosphoserine sites (S53, S63, S89, S92, S349) and methylarginine R134 from large-scale proteomics; no functional studies on these PTMs [file:human/DCAF10/DCAF10-uniprot.txt].
- Two isoforms (Q5QP82-1 displayed; Q5QP82-2 missing 352-388, VSP_028513) [file:human/DCAF10/DCAF10-uniprot.txt].

## Function — CRL4 substrate receptor (inferred / homology)
- UniProt FUNCTION: "May function as a substrate receptor for CUL4-DDB1 E3 ubiquitin-protein ligase complex" [ECO:0000269|PubMed:16949367]. SUBUNIT: "Interacts with DDB1" [ECO:0000269|PubMed:16949367] [file:human/DCAF10/DCAF10-uniprot.txt].
- PMID:16949367 (Jin et al., Mol Cell 2006) identified 18 DCAFs (incl. DCAF10/WDR32) that co-purify with CUL4-DDB1; WD40-containing DCAFs bind DDB1 via a conserved "WDXR" motif and act as substrate receptors. DCAF10 was identified by mass spectrometry as a DDB1/CUL4 interactor [PMID:16949367 "we identify 18 Ddb1- and Cul4-associated factors (DCAFs), including 14 containing WD40 repeats... the interaction of WD40-containing DCAFs with Ddb1 requires a conserved WDXR motif"]. This is the founding biochemical evidence for DCAF10 being a CRL4 substrate-receptor candidate. No specific endogenous DCAF10 substrate was identified in this paper.
- ComplexPortal defines two complexes: CPX-2817 "CRL4-DCAF10 E3 ubiquitin ligase complex, CUL4A variant" and CPX-2819 "CRL4-DCAF10 E3 ubiquitin ligase complex, CUL4B variant" [file:human/DCAF10/DCAF10-uniprot.txt]. These underpin the NAS Cul4A/Cul4B complex annotations.

## Apoptosis / MCL1 link (single study, indirect)
- PMID:33898171 (Luo et al., Adv Sci 2021): primarily about OTUD1/AIF. Reports that OTUD1 deubiquitinates and stabilizes DCAF10, and that DCAF10 (with CUL4A-DDB1) promotes MCL1 degradation, contributing to caspase-dependent apoptosis [PMID:33898171 "OTUD1 stabilizes DDB1 and CUL4 associated factor 10 (DCAF10) and recruits the cullin 4A (CUL4A)-damage specific DNA binding protein 1 (DDB1) complex to promote myeloid cell leukemia sequence 1 (MCL1) degradation, thereby activating caspase-dependent apoptotic signaling"].
- This is the only report proposing a specific substrate (MCL1) for a DCAF10-containing CRL4. It is a single study in an ESCC chemoresistance context; DCAF10 is a downstream/secondary player, not the focus. Note the paper specifies the CUL4A variant, whereas the GOA "Cul4B-RING" (GO:0031465) NAS annotation traces to this same PMID via ComplexPortal. The "regulation of apoptotic process" (GO:0042981) NAS annotation also traces here.
- Treat MCL1/apoptosis role as plausible but not core; not independently replicated.

## Interactome / protein binding (IPI)
- Generic GO:0005515 protein binding annotations come from high-throughput interactome screens:
  - PMID:32296183 (HuRI binary interactome) — partner UniProtKB:Q969G2 (LHX4) [file:human/DCAF10/DCAF10-goa.tsv].
  - PMID:33961781 (BioPlex) — partners O60884 (DNAJA2), Q13356 (PPIL2), Q9HB07 (MYG1) [file:human/DCAF10/DCAF10-goa.tsv].
  - PMID:40205054 (multimodal cell maps) — partner O60884 (DNAJA2) [file:human/DCAF10/DCAF10-goa.tsv].
- UniProt INTERACTION block lists DNAJA2, LHX4, MYG1, PPIL2, and (isoform-2) PRKN [file:human/DCAF10/DCAF10-uniprot.txt]. None of these are DDB1; none establish a specific molecular-function term. These are bare `protein binding` and uninformative as MF; mark over-annotated.

## Localization
- Reactome TAS annotations place DCAF10 in nucleoplasm (GO:0005654) as part of generic CRL4 neddylation/CAND1/COP9 reactions (R-HSA-8952638/8952639/8955245/8955285/8956045) [file:human/DCAF10/DCAF10-goa.tsv]. These are inferred from generic CRL4 assembly/neddylation pathway reactions where DCAF10 stands in as one of many possible DCAFs; reasonable but not DCAF10-specific experimental localization. Keep as non-core.

## Phylogenetic (IBA)
- GO:0080008 Cul4-RING E3 ubiquitin ligase complex, IBA from PANTHER PTN001026455 (GO_REF:0000033) [file:human/DCAF10/DCAF10-goa.tsv]. Consistent with the DCAF family assignment; ACCEPT as core complex membership.

## Pathway / EC
- GO:0016567 protein ubiquitination, IEA via UniPathway UPA00143 (GO_REF:0000041) [file:human/DCAF10/DCAF10-goa.tsv]. DCAF10 itself is a substrate receptor (no catalytic activity); the ubiquitination is carried out by the CRL4 complex. Reasonable as a process annotation for a CRL4 component but inferred via pathway mapping; keep as non-core.

## Summary assessment
- Core (inferred): substrate-recognition receptor / WD40 adaptor subunit of CRL4 (DDB1-CUL4-RBX1) E3 ubiquitin ligase; docks DDB1 via WD40 propeller / WDxR motif.
- Best-supported direct evidence: DDB1/CUL4 association (PMID:16949367, IDA/NAS) and complex membership.
- Pharos lists DCAF10 as "Tdark" (understudied) [file:human/DCAF10/DCAF10-uniprot.txt] — consistent with sparse functional literature. Be conservative.

