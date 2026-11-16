# hemA (Rhodobacter capsulatus SB1003) review notes

UniProtKB: P18079 (HEM1_RHOCB), locus RCAP_rcc01447, 409 aa. EC 2.3.1.37.

## Deep research

No `-deep-research-*.md` exists. `just deep-research RHOCB hemA --provider perplexity` was tried
once and failed (template file missing in this sparse checkout; no provider output). This review
is built from the UniProt record and cached publications only.

## Core biology

- HemA is the 5-aminolevulinate synthase (ALAS) of R. capsulatus: PLP-dependent condensation of
  glycine and succinyl-CoA to 5-aminolevulinate (ALA), CO2 and CoA (the Shemin route used by
  alpha-proteobacteria and non-plant eukaryotes).
  [PMID:16121195 "It catalyzes the synthesis of 5-aminolevulinic acid, the first common precursor of all tetrapyrroles, from glycine and succinyl-coenzyme A (sCoA) in a pyridoxal 5'-phosphate (PLP)-dependent manner."]
- Purified recombinant enzyme is active (198.2 U/mg) with high catalytic efficiency for succinyl-CoA.
  [PMID:24793767 "the specific activity of RC-ALAS reached 198.2 U/mg"]
- Single ALAS gene in R. capsulatus; insertion mutant is ALA auxotroph, rescued by the cloned gene.
  [PMID:2381418 "restored ALA-independent growth of the mutant indicating that there is only one gene for ALA biosynthesis in R. capsulatus"]
  (R. sphaeroides instead has two isozymes, HemA and HemT.)
- Crystal structure (PDB 2BWN/2BWO/2BWP): homodimer with PLP bound; complexes with glycine and
  succinyl-CoA. Active-site Lys248 forms the PLP Schiff base (UniProt MOD_RES 248). 49% identity to
  human ALAS2; it is the structural model for XLSA mutations.
  [PMID:16121195 "We present the first crystal structure of homodimeric ALAS from Rhodobacter capsulatus (ALAS(Rc)) binding its cofactor PLP."]
- ALA in R. capsulatus is the common precursor of heme, bacteriochlorophyll and other
  tetrapyrroles, so the tetrapyrrole-level process term is genuinely informative here, beside
  the heme term.

## Annotation decisions (summary)

- 5-aminolevulinate synthase activity (IEA): ACCEPT, core.
- heme biosynthetic process (TreeGrafter IEA): ACCEPT.
- tetrapyrrole biosynthetic process (InterPro2GO): ACCEPT (ALA feeds heme and BChl).
- PLP binding (InterPro2GO): ACCEPT (cofactor shown in crystal structure).
- transferase activity (InterPro2GO IPR001917): TOO_GENERAL beside the accepted ALAS activity.

## PANTHER

UniProt places P18079 in PTHR13693:SF102, a mixed subfamily (fungal and alpha-proteobacterial ALAS
with KBL and GCAT) per interpro/panther/PTHR13693/PTHR13693-review.yaml. The eukaryotic ALAS PAINT
node PTN000343737 (taxon Eukaryota) does not cover this bacterial protein; its heme/ALAS rows arrive
via TreeGrafter/ARBA-combined IEA referencing PTN000343738.
