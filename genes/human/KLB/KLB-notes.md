# KLB curation notes

Date: 2026-07-18

## Retrieval record

- Fetched the reviewed UniProt record, all 38 GOA rows, and all four GOA-cited
  PubMed records.
- Fetched full text for the human KLB/FGF21 structural study PMID:29342135 and
  the abstract for the KLB/FGF19 structural study PMID:30944224.
- Falcon research failed with HTTP 402 and the Perplexity-lite fallback failed
  with HTTP 401. Manual evidence synthesis is recorded in
  `KLB-deep-research-manual.md`.

## Evidence synthesis

Core function: plasma-membrane KLB binds endocrine FGF ligands and fibroblast
growth factor receptors to enable Klotho-dependent FGFR signaling.

The tandem GH1-like domains are repurposed ligand-binding domains. Human
structural evidence shows that each domain lacks one of the two essential
catalytic glutamates [PMID:29342135, "neither GH domain in β-Klotho can function
as an active glycoside-hydrolase enzyme"]. Accordingly, the electronic hydrolase
and carbohydrate-metabolism transfers are removed rather than accepted on fold
similarity.

FGF binding is directly supported for both endocrine ligands: FGF21 binds KLB
through its carboxyl terminus [PMID:19059246, "FGF21 binds directly to
beta-Klotho through its C-terminus."], and the FGF19 carboxyl terminus determines
Klotho-family recognition [PMID:18829467, "C-terminal tail of FGF19 as a region
necessary for its recognition of Klotho family proteins"]. Generic protein
binding from the FGF21 experiment is therefore modified to the informative
fibroblast growth factor binding term.

The FGFR-binding annotation is retained. The cited work defines KLB as an FGFR4
coreceptor required for FGF19 binding and signaling [PMID:17627937, "KLB is
required for FGF19 binding to FGFR4, intracellular signaling, and downstream
modulation of gene expression."]. Human structural and cell-based experiments
also support KLB-FGFR1c association and KLB-dependent FGF21 signaling
[PMID:29342135, "β-Klotho is required for FGFR1c-mediated signaling induced by
FGF21."].

All plasma-membrane annotations are accepted consistently. The reviewed UniProt
record calls KLB a single-pass type III cell-membrane protein, and every
Reactome record places it in membrane-associated FGFR signaling complexes.

## Final decisions

- GO:0004553 hydrolase activity, hydrolyzing O-glycosyl compounds: REMOVE.
- GO:0005975 carbohydrate metabolic process: REMOVE because the InterPro
  transfer is driven by the inactive GH1-like fold.
- GO:0005515 protein binding from PMID:19059246: MODIFY to GO:0017134 fibroblast
  growth factor binding.
- GO:0005886 plasma membrane: ACCEPT for the IEA and every Reactome TAS record.
- GO:0017134 fibroblast growth factor binding: ACCEPT for all records.
- GO:0005104 fibroblast growth factor receptor binding: ACCEPT.
- Add GO:0015026 coreceptor activity and GO:0008543 fibroblast growth factor
  receptor signaling pathway from direct human structure/function evidence.
- Add GO:0070858 negative regulation of bile acid biosynthetic process with ISS
  because the physiological CYP7A1 experiment is in mouse.

## Experimental priorities

1. Quantify endogenous human KLB-FGFR stoichiometry and ligand-dependent complex
   assembly in hepatocytes and adipocytes.
2. Test separation-of-function KLB variants that selectively disrupt FGF19,
   FGF21, or FGFR binding while retaining surface expression.
3. Resolve whether any residual catalytic chemistry remains in either GH-like
   domain under physiological conditions, despite the missing catalytic
   glutamates.
