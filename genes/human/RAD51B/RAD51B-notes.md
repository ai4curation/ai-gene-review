# RAD51B (O15315) - review notes

Human RAD51B / RAD51L1 / REC2 / R51H2. RAD51 paralog, RecA/RAD51 family. Chr 14q23-24.
Trigger review: PMID:42682019 (Dwivedi et al., Biochem Soc Trans 2026, "Distinct functions of
mammalian RAD51 paralogs in genome maintenance").

Deep research: `just deep-research-falcon` failed (HTTP 402), perplexity provider unavailable,
openai key invalid (2026-10-06). No deep-research file was generated; these notes are the
research record.

## Complex membership

- RAD51B is the subunit that defines BCDX2 (RAD51B-RAD51C-RAD51D-XRCC2); it is absent from CX3
  (RAD51C-XRCC3) and from the more recently described X3CDX2 complex.
  [PMID:11751635 "one contains RAD51B, RAD51C, RAD51D, and XRCC2 (defined as BCDX2)"]
  [PMID:41196948 "the RAD51 paralogs assemble into two distinct heterotetrameric complexes"]
  [PMID:42682019 "including a RAD51B-independent X3CDX2 complex"]
- In the cryo-EM structure the CDX2 part mimics three RAD51 protomers, while RAD51B is mobile.
  [PMID:37344587 "RAD51C-RAD51D-XRCC2 mimics three RAD51 protomers aligned within a nucleoprotein filament, whereas RAD51B is highly dynamic"]
- The RAD51B and RAD51C N-terminal domains contribute to complex formation and ssDNA-binding
  specificity. [PMID:37344589 "The structures reveal how the amino-terminal domains of RAD51B, RAD51C and RAD51D participate in inter-subunit interactions that underpin complex formation and ssDNA-binding specificity"]

## Biochemistry of RAD51B itself

- Purified RAD51B binds ssDNA and dsDNA, has DNA-dependent ATPase activity, and selectively binds
  Holliday junctions. [PMID:12441335 "the purified Rad51B protein bound to single-stranded DNA and double-stranded DNA in the presence of ATP"; "hydrolyzed ATP in a DNA-dependent manner"; "the Rad51B protein only bound to the synthetic Holliday junction"] (abstract only)
- The RAD51B-RAD51C heterodimer has ssDNA binding and ssDNA-stimulated ATPase activity and partly
  relieves RPA inhibition of RAD51 strand exchange (mediator function).
  [PMID:11751636 "Rad51B-Rad51C complex has ssDNA binding and ssDNA-stimulated ATPase activities"; "The competition by RPA for substrate binding can be partially alleviated by Rad51B-Rad51C"] (abstract only)
- RAD51B is one of the two catalytic ATPase subunits of BCDX2 (with RAD51C). RAD51D and XRCC2 bind
  ATP but lack the catalytic glutamate.
  [PMID:37344587 "in reactions that depend on the coupled ATPase activities of RAD51B and RAD51C"]
  [PMID:37344587 "These glutamates are not conserved in RAD51D or XRCC2 explaining their inability to promote ATP hydrolysis while retaining nucleotide binding"]
  The RAD51C ATPase is the more critical: RAD51B-E144A BCDX2 keeps partial activity.
  [PMID:37344587 "ATPase deficient BCE161ADX2 and BE144ACE161ADX2 complexes failed to promote RAD51AF488 assembly, whereas BE144ACDX2 retained partial stimulation relative to wild-type"]

## Function in HR

- BCDX2 promotes nucleation and growth of RAD51 filaments on RPA-coated ssDNA.
  [PMID:37344587 "BCDX2 stimulates the nucleation and extension of RAD51"]
  [PMID:37344589 "BCDX2 functions as a mediator of nucleoprotein filament assembly by RAD51 and single-stranded DNA (ssDNA) during HR"]
- Acts downstream of BRCA2 recruitment and upstream of RAD51 recruitment.
  [PMID:23149936 "the BCDX2 complex acts downstream of BRCA2 recruitment but upstream of Rad51 recruitment"]
- Knockouts: Rad51b-/- mice die early in embryogenesis [PMID:10567591 "no homozygous pups were born after interbreeding of heterozygous mice"]. In human cell lines, RAD51B loss gives the weakest phenotype of the five paralogs and RAD51B is the only paralog not essential in MCF10A cells.
  [PMID:31584931 "with the exception of RAD51B, RAD51 paralogs are cell-essential in MCF10A cells"; "with the weakest phenotypes observed in RAD51B-deficient cells"]

## Replication forks

- BCDX2 and CX3 bind fork and Holliday-junction DNA with high specificity.
  [PMID:20207730 "both complexes bind with exceptionally high specificity to the DNA junctions"]
- BCDX2 restrains fork progression and promotes fork reversal in cells (shown with RAD51C and
  RAD51D depletion; RAD51B less directly tested). [PMID:32669601 "the BCDX2 subcomplex restrains fork progression upon stress, promoting fork reversal"]
- Purified BCDX2 has no fork-reversal activity of its own, but together with RAD51 filaments it
  protects DNA from MRE11/EXO1. [PMID:37843130 "both RAD51 paralog complexes lack fork reversal activities"; "BCDX2 significantly synergizes with RAD51 to protect DNA against attack by the nucleases MRE11 and EXO1"]
- Trigger review: the BC subcomplex protects forks remodelled by FANCM.
  [PMID:42682019 "The DX2 and CX3 complexes stabilize forks that have been remodeled by FBH1, while the BC subcomplex protects forks remodeled by the FANCM translocase"]

## Annotation decisions (summary)

- Protein binding IPI rows: all REMOVE. They are uninformative; the paralog interactions are
  captured by GO:0033063.
- GO:0140664 ATP-dependent DNA damage sensor activity (IEA): MARK_AS_OVER_ANNOTATED, consistent
  with the RAD51C and XRCC2 reviews.
- GO:0097435 supramolecular fiber organization: MODIFY to GO:0000730 DNA recombinase assembly,
  consistent with RAD51C and XRCC2.
- GO:0007131 reciprocal meiotic recombination (TAS, PMID:9441753): the discovery paper only
  speculates about this, there is no IBA for it, and the knockout is embryonic lethal, so there is
  no meiotic data. MARK_AS_OVER_ANNOTATED.
- GO:0010971 positive regulation of G2/M transition (IMP, PMID:23108668): depletion causes G2/M
  arrest, which is most likely an indirect checkpoint effect. KEEP_AS_NON_CORE, consistent with
  RAD51C.
- NEW GO:0031297 replication fork processing (IDA, PMID:37843130): reconstitution with purified
  BCDX2.
- Proposed MF "DNA recombinase loader activity" reused from the RAD51C review, because GO has no
  molecular function for the mediator activity.

## Disease

- RAD51B is a breast cancer susceptibility locus (GWAS; not curated here). There are rare germline
  loss-of-function variants. Chromosomal translocations with HMGA2 occur in uterine leiomyoma and
  with HMGA1 in pulmonary chondroid hamartoma (UniProt).
