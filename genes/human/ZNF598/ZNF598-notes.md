# ZNF598 (E3 ubiquitin-protein ligase ZNF598; Hel2 ortholog) notes

UniProt: Q86UK7 (ZNF598_HUMAN). RING-type E3 ligase, EC 2.3.2.27. Human ortholog of yeast Hel2/RQT1.

## Core function
ZNF598 is the RING E3 ubiquitin ligase that initiates ribosome-associated quality control (RQC)
by sensing collided ribosomes (disomes). On colliding ribosomes it monoubiquitinates 40S
proteins eS10 (RPS10) and uS3 (RPS3) and K63-polyubiquitinates uS10 (RPS20), which recruits the
RQT/hRQT complex to drive subunit dissociation and downstream nascent-chain degradation.

- UniProt FUNCTION: "Acts as a ribosome collision sensor: specifically recognizes and binds
  collided di-ribosome ... leading to terminally arrest translation."
- UniProt FUNCTION: "mediates monoubiquitination of 40S ribosomal proteins RPS10/eS10 and
  RPS3/uS3, and 'Lys-63'-linked polyubiquitination of RPS20/uS10"
- [PMID:28065601 "the ubiquitin ligase ZNF598 is required for ribosomes to terminally stall during translation of poly(A) sequences"]
- [PMID:28065601 "two sites of mono-ubiquitination on the 40S protein eS10 as the primary ribosomal target of ZNF598"]
- [PMID:30293783 "the minimal unit engaged by ZNF598 is the collided" di-ribosome]
- [PMID:36302773 "the collided ribosomes are first marked by the Hel2/ZNF598 E3 ubiquitin ligase to recruit the RQT complex for subunit dissociation"]
- E3 activity depends on E2 UBE2D3 (PMID:28685749).

## Sensor / MF annotations
- GO:0170011 stalled ribosome sensor activity (IDA PMID:30293783) - CORE; ZNF598 is the collision sensor.
- GO:0061630 ubiquitin protein ligase activity (IDA, many) - CORE.
- GO:0043022 ribosome binding (IDA PMID:28065601, PMID:28132843) - core; binds 40S/collided ribosomes.
- GO:0140517 protein-RNA adaptor activity (IDA PMID:32726578) - adapter recruiting 4EHP-GYF2 to mRNAs.
- GO:0003723 RNA binding (HDA) - ZNF598 is an RNA-binding protein; mRNA-interactome captures.

## BP annotations
- GO:0072344 rescue of stalled cytosolic ribosome (many IDA/IMP) - CORE.
- GO:1990116 ribosome-associated ubiquitin-dependent protein catabolic process (IMP) - core.
- GO:0070534 protein K63-linked ubiquitination (IDA PMID:36302773) - core; K63 polyUb of uS10.
- GO:0006513 protein monoubiquitination (IDA PMID:28065601) - core; monoUb of eS10/uS3.
- GO:0045947 negative regulation of translational initiation (IDA PMID:28065601) - via 4EHP-GYF2 / stalling.
- GO:0016567 protein ubiquitination (IMP/IEA) - parent.

## 4EHP-GYF2 adapter / mRNA decay
- Component of 4EHP-GYF2 complex (EIF4E2, GIGYF2, ZNF598); recruits translational repressor to
  defective mRNAs. [PMID:32726578] GIGYF2 and 4EHP inhibit translation initiation of defective mRNAs.
- GO:1990261 pre-mRNA catabolic process (NAS PMID:33053355, ComplexPortal) - 4EHP/GIGYF translation-
  coupled mRNA decay. KEEP_AS_NON_CORE (adapter role, peripheral to the RQC ligase core).
- protein binding IPI: GIGYF1 (O75420, PMID:33053355/33961781), YWHAE/14-3-3 (P62258,
  PMID:35271311/36931259), RACK1/GNB2L1 (P63244? actually P61077=UBE2D3), eS10/RPS10(P46783),
  uS3/RPS3(P23396), RPS20(P60866) - some IPI are the actual ribosomal substrates (informative-ish)
  but the bare term is uninformative -> KEEP_AS_NON_CORE.

## Moonlighting
- Negative regulator of interferon-stimulated genes (ISG) (PMID:29719242, not cached) - independent of RQC.
- Poxvirus protein synthesis (microbial infection). Minor.

## Localization
- Cytoplasm, cytosol; active on cytosolic ribosomes. ACCEPT cytosol/cytosolic ribosome.

## Actions summary
- Core MFs: GO:0170011 stalled ribosome sensor activity; GO:0061630 ubiquitin protein ligase activity.
- Core BPs: GO:0072344 rescue of stalled ribosome; GO:1990116 RQC catabolism; GO:0070534 K63 ubiquitination;
  GO:0006513 monoubiquitination.
- ribosome binding, RNA binding, protein-RNA adaptor -> ACCEPT/KEEP_AS_NON_CORE.
- 4EHP-GYF2 / pre-mRNA catabolic / neg reg translation initiation -> KEEP_AS_NON_CORE (adapter moonlighting).
- protein binding IPI -> KEEP_AS_NON_CORE.
