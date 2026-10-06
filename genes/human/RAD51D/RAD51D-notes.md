# RAD51D (O75771) - review notes

Human RAD51D / RAD51L3 / R51H3 / TRAD. RAD51 paralog, RecA/RAD51 family. Chr 17q11-12.
Trigger review: PMID:42682019 (Dwivedi et al., Biochem Soc Trans 2026).

Deep research: the falcon (HTTP 402), perplexity (not available) and openai (invalid key)
providers all failed on 2026-10-06. No deep-research file was generated; these notes are the
research record.

## Complex membership: BCDX2 and X3CDX2

- RAD51D is a BCDX2 subunit and binds XRCC2 directly, forming the DX2 subcomplex.
  [PMID:11751635 "one contains RAD51B, RAD51C, RAD51D, and XRCC2 (defined as BCDX2)"]
  [PMID:10871607 "the interaction between RAD51L3 and XRCC2 is direct"]
- In the 2026 work, DX2 also pairs with CX3 to form X3CDX2 (XRCC3-RAD51C-RAD51D-XRCC2). That
  complex caps the 5' ends of RAD51 filaments and promotes homologous pairing, whereas the RAD51B
  complex (BCDX2) promotes ATP-hydrolysis-dependent filament assembly.
  [PMID:41196948 "the RAD51 paralogs assemble into two distinct heterotetrameric complexes"; "the XRCC3 complex stably caps the 5' termini of RAD51 filaments to promote homologous pairing"]
  [PMID:42020761 "the RAD51D-XRCC2 paralog complex remodels RAD51-X3C into a pentameric RAD51-X3CDX2 assembly"; "enhances RAD51-ssDNA filament assembly, and promotes strand exchange on RPA-coated ssDNA"]
- GO has no cellular component term for X3CDX2. Recorded as a suggested question.

## ATP: binds, but does not hydrolyse in the complex

- Early biochemistry on isolated RAD51D (RAD51L3) reported ssDNA binding and DNA-stimulated ATPase
  activity. [PMID:10871607 "the purified RAD51L3 protein possesses single-stranded DNA binding activity and DNA-stimulated ATPase activity"] (abstract only)
- Structures show RAD51D bound to ATP but catalytically inactive: it lacks the catalytic glutamate
  that RAD51, RAD51B and RAD51C have.
  [PMID:37344587 "These glutamates are not conserved in RAD51D or XRCC2 explaining their inability to promote ATP hydrolysis while retaining nucleotide binding"]
  [PMID:41196948 "RAD51D and XRCC2 were both bound to ATP, as observed in the RAD51B complex, but neither is catalytically active due to the absence of an otherwise conserved catalytic glutamate residue"]
- Deep mutational scan (preprint): the RAD51D-RAD51C interface regulates BCDX2 ATPase activity,
  and the authors propose that RAD51D slows the BCDX2 ATPase.
  [PMID:41542474 "the primary function of RAD51D is to slow the ATPase activity of BCDX2"]
- Walker motifs: a Walker B mutant is defective in partner binding and HR, while the Walker A
  (K113) results conflict between CHO and MEF systems.
  [PMID:16717288 "a functional Walker B motif, but not A motif, is necessary for RAD51D's interactions with other paralogs and for efficient HRR"]
  [PMID:16236763 "ATP binding and hydrolysis by RAD51D are required for efficient HR repair of DNA interstrand crosslinks"]
- Conclusion: the GO:0008094 IDA (PMID:10871607) and IBA (RAD51D is the only listed donor) are
  both MARK_AS_OVER_ANNOTATED, not REMOVE. The isolated-protein assay is not dismissed, but a
  catalytic ATP-driven activity overstates RAD51D's role, given target-specific structural evidence
  that the catalytic glutamate is lost (RAD51C D159-T-E161 corresponds to RAD51D D206-S-V208,
  anchored on the Walker B aspartate). ATP binding is ACCEPTed.

## Function in HR and fork biology

- BCDX2 acts as a RAD51 filament mediator (see the RAD51B notes) and works downstream of BRCA2 and
  upstream of RAD51 [PMID:23149936].
- XRCC2-RAD51D catalyses homologous pairing in vitro and forms rings and ssDNA filaments.
  [PMID:11834724 "complex catalyzed homologous pairing between single-stranded and double-stranded DNA"]
- The RAD51D-XRCC2 interaction is needed for HR. Cancer variants G96C and G107V disrupt it.
  Isoform 1 is the functional isoform.
  [PMID:30836272 "the interaction of RAD51D with XRCC2 is required for DSB repair"]
- Fork reversal and slowing require RAD51D (siRNA and KO in U2OS).
  [PMID:32669601 "RAD51C and RAD51D downregulation by two independent siRNA sequences drastically impaired active fork slowing"]
  [PMID:32669601 "we indeed confirmed that downregulation of RAD51C and RAD51D, but not of XRCC3, markedly impairs CPT-induced replication fork reversal"]
- DX2 regulates fork progression in an ATR-dependent manner (trigger review; XRCC2 S247
  phosphorylation). [PMID:42682019 "a subset of the RAD51 paralogs, the RAD51D–XRCC2 (DX2) subcomplex, has an ATR-dependent role in regulating fork progression"]
- XRCC2-RAD51D stimulates BLM disruption of 4-way junctions through a direct RAD51D-BLM
  interaction. [PMID:12975363 "the RAD51L3-XRCC2 complex stimulates BLM to disrupt synthetic 4-way junctions"]

## Telomeres and centrosomes (non-core)

- RAD51D localises to telomeres. Its loss shortens telomeres and causes end-to-end fusions,
  including in telomerase-negative human cells.
  [PMID:15109494 "RAD51D was shown to localize to the telomeres of both meiotic and somatic cells"; "Inhibition of RAD51D synthesis in telomerase-negative immortalized human cells by siRNA also resulted in telomere erosion and chromosome fusion"]
- Centrosome co-localisation of HR proteins [PMID:21276791] (abstract only; names XRCC2 and
  RAD51). The gamma-tubulin binding IDA from this paper cannot be checked against the abstract,
  so UNDECIDED.

## Disease

- Germline loss-of-function variants confer ovarian cancer risk (RR about 6.3) and PARP-inhibitor
  sensitivity. [PMID:21822267 "The relative risk of ovarian cancer for RAD51D mutation carriers was estimated to be 6.30"]

## Annotation decisions (summary)

- Protein binding IPI rows (87): all REMOVE (uninformative). Most come from high-throughput Y2H
  screens (HuRI and earlier). The paralog partners are captured by GO:0033063.
- GO:0140664 IEA and IMP (PMID:16717288): MARK_AS_OVER_ANNOTATED. The paper tests Walker motif
  requirements for partner binding and HR, not damage sensing or signalling.
- NEW GO:0031297 replication fork processing (IMP, PMID:32669601).
- NEW GO:0036297 interstrand cross-link repair (IMP, PMID:16717288; the RAD51C and XRCC2 reviews
  make the same addition).
- GO:0097435 MODIFY to GO:0000730, consistent with the sibling reviews.
