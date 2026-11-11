# MYL2 (human, P10916) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This is a new review, written as the experimentally characterised reference for the
paralog MYL10 (Q9BUA6). No ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon human MYL2 --fallback perplexity-lite` failed: falcon
returned "Failed to authenticate", and the perplexity fallback returned HTTP 401
(insufficient quota). No deep-research file exists. The review uses the GOA-cited
papers (cached via `just fetch-gene-pmids`) and the mouse papers behind the
ortholog annotations, which I fetched by hand: PMID:9422794, 16908724, 10409661,
1379240, 8777429, 15308581, 11356630.

### Evolutionary placement

- PANTHER PTHR23049:SF9, "MYOSIN REGULATORY LIGHT CHAIN 2, VENTRICULAR_CARDIAC MUSCLE
  ISOFORM" (from panther.obo). MYL10 is in SF36 and MYL7 (atrial) in SF39.
- IBA nodes on MYL2:
  - PTN000549442 (sarcomeric RLCs: MYL2, MYL7, MYLPF, MYL10) carries calcium ion
    binding, with MYL2 as the experimental donor (IDA, PMID:11102452).
  - PTN002746142 (MYL2 branch; donors mouse Myl2 MGI:97272, rat RGD:1564245 and
    human) carries heart development, myofibril, cardiac muscle contraction and
    muscle cell fate specification.
  - PTN001495767 is a deep node that carries cytoplasm.
- I checked the mouse Myl2 (P51667) GOA rows in QuickGO. The relevant experimental
  donors are: KO with defective ventricular sarcomere assembly [PMID:9422794
  "ultrastructural analysis revealed defects in sarcomeric assembly"]; RLC
  phosphorylation increasing calcium sensitivity and force [PMID:16908724 "MLCK
  increased RLC phosphorylation, increased the Ca(2+) sensitivity of isometric
  force"]; nonphosphorylatable MLC2v transgenic mice [PMID:10409661]. The muscle
  cell fate specification donor is PMID:1379240, a promoter-luciferase study of
  MLC-2 expression and not a fate experiment. I therefore REMOVED that IBA.
- Mouse and rat Myl2 are one-to-one orthologs in SF9, so transferring the mouse
  physiology to human MYL2 is evolutionarily grounded.

### What is experimentally established in human, and what is inferred

The following come from experiments on the human protein or from human genetics:
- Ca2+ binding by recombinant human RLC, altered by HCM mutations and by
  phosphorylation [PMID:11102452 "the R58Q mutant did not bind Ca(2+)"].
- Binding of recombinant human MLC2 to the myosin heavy chain, S1 and myofibrils
  [PMID:8287067 "binds with specificity to MHC and to intact myofibrils"].
- Recessive loss of function causes lethal infantile myopathy with cardiomyopathy
  [PMID:23365102, PMID:32453731]. Wild-type human MYL2 partially rescues
  Drosophila Mlc2-knockdown heart function [PMID:32453731 "was partially rescued
  by the wildtype human MYL2 overexpression"].
- GFP-MYL2 localizes along the cytoskeleton of H9c2 cells [PMID:32453731]. MYL2
  is quantified as a myofilament protein in human cardiac tissue [PMID:25771144].
- Cardiac-MLCK (MYLK3) phosphorylates MLC2v [PMID:17885681].

The following are inferred from mouse or rat orthologs:
- Phosphorylation-dependent positive regulation of force, Ca2+ sensitivity and
  stretch activation.
- The requirement for ventricular sarcomere assembly.
- The A-band location (the UniProt statement is by similarity to rat).

### Annotation problems found

- Actin monomer binding (IDA, PMID:9180271). The abstract describes N-terminal
  peptides of the essential light chains (ALC-1/VLC-1, i.e. MYL4/MYL3) and does
  not mention RLC. This is probably a VLC-1/MLC-2v name confusion. Marked UNDECIDED
  because the cached record is abstract-only.
- Cytoskeleton and actin cytoskeleton (IDA, PMID:17043135). I read the full text.
  Staining used Thr18/Ser19 phospho-MLC2 antibodies in MG63 and other non-muscle
  cells, which detect the nonmuscle RLCs MYL9/MYL12. The cytoskeleton row is
  MODIFY, consistent with the true claim, with the evidence problem stated in the
  reason. The actin cytoskeleton colocalizes_with row is UNDECIDED.
- Negative regulation of cell growth (PMID:15824735) is based on ectopic
  expression in RCC cells. MARK_AS_OVER_ANNOTATED.
- Ventricular cardiac muscle tissue morphogenesis (IMP, PMID:8673105) records an
  HCM phenotype, which is downstream of MYL2's function. MARK_AS_OVER_ANNOTATED.
- Cytosol (ARBA plus Reactome compartment convention): MYL2 sits in thick
  filaments, so MARK_AS_OVER_ANNOTATED.
- General terms were refined to terms the gene already carries: heart development
  to cardiac myofibril assembly; cytoplasm, myofibril and sarcomere to A band;
  myosin complex and cytoskeleton to muscle myosin complex; heart contraction to
  cardiac muscle contraction; regulation of force to positive regulation of
  force. Actin filament-based movement became muscle filament sliding, and
  myosin heavy chain binding became myosin II heavy chain binding.
- The four generic protein binding IPIs (MYOC, USP6, IRX6, PSORS1C2) were
  REMOVED under the protein-binding policy.

### Notes for transfer to MYL10

The only MYL2 function that PAINT propagated to the node shared with MYL10 is
calcium ion binding. Heart, myofibril, contraction and myosin-heavy-chain terms
sit on the MYL2 branch (PTN002746142) or elsewhere, and were not propagated to
SF36. They should not be transferred to MYL10 on the basis of this review.
