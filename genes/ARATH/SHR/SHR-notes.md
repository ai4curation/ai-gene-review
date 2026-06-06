# SHR (SHORT-ROOT) curation notes

UniProt: Q9SZF7 (SHR_ARATH); locus AT4G37650; GRAS family (GRAS-26 / SGR7).
531 aa. GRAS domain 134-529 (LRI, VHIID, LRII, PFYRE, SAW subdomains). N-terminus disordered.

## Core biology

SHR is a GRAS-family transcriptional regulator that is transcribed only in the
stele but moves cell-to-cell (via plasmodesmata, endosome/SIEL-dependent) into
the adjacent cell layer, where it enters the nucleus and, together with
SCARECROW (SCR), specifies endodermis/ground-tissue identity, the quiescent
centre, and drives the asymmetric (formative) division of the cortex/endodermis
initial.

- [PMID:10850497 "The SHORT-ROOT (SHR) gene is required for the asymmetric cell division responsible for formation of ground tissue (endodermis and cortex) as well as specification of endodermis in the Arabidopsis root... SHR encodes a putative transcription factor with homology to SCARECROW (SCR)... SHR functions upstream of SCR"]
- [PMID:11565032 "the SHR protein, a putative transcription factor, moves from the stele to a single layer of adjacent cells, where it enters the nucleus... SHR protein acts both as a signal from the stele and as an activator of endodermal cell fate and SCR-mediated cell division"]
- [PMID:15498493 "SHR must be present in the cytoplasm to move... a cytoplasmic pool of SHR is not sufficient for movement"] (Thr289 mutant: loss of export and activity)

## Molecular function — DNA binding vs cofactor (key decision)

SHR was historically annotated as a DNA-binding transcription factor
(GO:0003700) and as having sequence-specific DNA binding (GO:0043565). The
structural work strongly argues that SHR does NOT bind DNA directly and instead
acts as a transcription cofactor recruited to target promoters by DNA-binding
BIRD/IDD zinc-finger transcription factors.

- [PMID:28211915 "there is no evidence for direct binding of SHR-SCR or other GRAS proteins to DNA. We did not find any DNA-binding motifs in our structure of the SHR-SCR complex, which comprises an overall negatively-charged surface potentials... unfavorable for binding to highly negatively-charged DNA"]
- [PMID:28211915 "These results suggest that SHR-SCR are transcriptional cofactors that regulate target gene transcription via binding of SHR to BIRD transcription factors"]
- [PMID:28211915 "the ZF1-ZF2-ZF3 of JKD in the JKD-SHR-SCR complex is involved in DNA binding"] (i.e. DNA contact is by the IDD partner, not SHR)
- [PMID:28211915 "ZF1, ZF2 and ZF3 are responsible for DNA binding, while ZF3 and ZF4 are involved in SHR binding"]

The original IDA "sequence-specific DNA binding" came from in vivo ChIP, which
detects promoter occupancy but not direct sequence-specific contact:
- [PMID:16640459 "Binding of SHR to four of the eight promoter regions was confirmed in vivo using chromatin immunoprecipitation (ChIP)... this demonstrates that SHR has transcription factor activity"]
The ChIP occupancy is fully consistent with indirect recruitment via IDD TFs.
The cleaner MF terms are therefore transcription coregulator activity
(GO:0003712) and DNA-binding transcription factor binding (GO:0140297) /
transcription factor binding (GO:0008134), rather than GO:0003700/GO:0043565.

The cis-regulatory-region binding (GO:0000976) IPI annotation comes from an
enhanced yeast-one-hybrid secondary-cell-wall GRN where SHR scored against
several promoters:
- [PMID:25533953 "Yeast one-hybrid (Y1H) protein-DNA interaction assays"]
Y1H reports promoter association but, in light of the structural data, this is
most plausibly indirect; kept as non-core with that caveat.

## Protein–protein interactions (central function)

SHR's defining biochemical activity is heterodimerization with SCR via the GRAS
α-helical caps, and binding of the SHR–SCR dimer to BIRD/IDD zinc-finger TFs
(JKD/IDD10, MGP/IDD3, etc.).

- [PMID:17446396 "SCARECROW (SCR) blocks SHR movement by sequestering it into the nucleus through protein-protein interaction and a safeguard mechanism that relies on a SHR/SCR-dependent positive feedback loop for SCR transcription"]
- [PMID:28211915 "SHR and SCR... form a head-to-head 1:1 heterodimer... Dimerization of the GRAS domains of SHR and SCR is mediated by the α-helical caps"]
- [PMID:28211915 "ZF4 is essential for binding to the SHR-SCR complex... high affinity of the SHR-SCR complex to MGP ZF3-ZF4 (the KD value of 36 nM) and JKD ZF3-ZF4 (124 nM)"]
- [PMID:17785527 "the JACKDAW and MAGPIE genes, which encode members of a plant-specific family of zinc finger proteins, act in a SHR-dependent feed-forward loop to regulate the range of action of SHORT-ROOT and SCARECROW"] (SHR interacts with JKD/AT1G03840 and MGP/AT5G03150)
- [PMID:18500650 "we confirmed the protein-protein interaction between SHORT-ROOT (SHR) and SCARECROW (SCR)... we identified a new SHR-interacting protein, SCARECROW-LIKE23 (SCL23)"]
- [PMID:22921914 "This cyclin (CYCD6;1) is itself under transcriptional control of SCR and its partner SHORT ROOT (SHR)"] (IntAct WITH = SCR Q9M384)
- [PMID:28746306 in vivo FRET-FLIM: SHR forms cell-type-specific complexes with SCR and JKD in roots]

The "protein binding" (GO:0005515) IPI entries are all SHR–SCR / SHR–IDD
interactions; the specific informative MF is DNA-binding transcription factor
binding (GO:0140297) for the IDD partners and protein homo/heterodimerization
for SCR.

## Downstream / non-core processes

- Radial pattern formation, asymmetric (formative) cell division of CEI: core developmental output [PMID:10850497].
- Leaf growth / S-phase progression (general cell proliferation in leaves), distinct from root role:
  [PMID:20739610 "SHR and SCR primarily function as general regulators of cell proliferation in leaves... primarily drive S-phase progression, presumably by a stimulation of E2F action"] — KEEP_AS_NON_CORE (leaf development, negative regulation of mitotic cell cycle).
- Bundle sheath cell fate in leaves [PMID:24517883 "SHR is also essential for BS cell-fate specification... the SHR protein moves into the BS cells, where it directly regulates SCR and SCL23 expression"].
- Iron homeostasis (GO:0060586, IMP PMID:19726572): the iron paper does not actually study or mention SHR; it identifies the endodermal vacuole as the embryo iron store. The link to SHR is indirect (SHR specifies endodermis). Treat as non-core / over-annotated downstream consequence. The TAIR IMP appears to be an inferred connection, not a direct SHR experiment in that paper.
- Regulation of hormone metabolic process (GO:0032350, NAS PMID:16640459): the paper reports SHR pathway intersects GA/BR/auxin pathways via indirect targets (e.g. SNE, BR6ox2); NAS, peripheral.

## Subcellular location

Cytoplasm + nucleus in the stele; restricted to nucleus in adjacent (endodermis)
cells (SCR sequesters it). Endosome (early/late/recycling) localization is part
of the SIEL-dependent intercellular trafficking machinery.
- [PMID:25124761 "in the cytoplasm of root or leaf cells, SHR localizes to endosomes in a SIEL-dependent manner. Interference of early and late endosomes disrupts intercellular movement of SHR"]
Nucleus is the functional compartment (transcriptional regulation); cytoplasm
and endosomes are part of the movement/trafficking route.

## Annotation action summary

- protein binding (GO:0005515) x6 → MODIFY to GO:0140297 (DNA-binding TF binding) where partner is an IDD; for SCR-only interactions, capture as protein dimerization / KEEP. Avoid bare "protein binding" as core.
- GO:0003700 (DNA-binding TF activity) TAS/ISS x3 → MODIFY to GO:0003712 transcription coregulator activity.
- GO:0043565 (sequence-specific DNA binding) IDA x2 → MARK_AS_OVER_ANNOTATED / MODIFY (no direct DNA binding per structure).
- GO:0000976 (cis-reg region binding) IPI → KEEP_AS_NON_CORE (Y1H; likely indirect).
- GO:0006355 (regulation of DNA-templated transcription) IBA → ACCEPT (core, correct level).
- Locations: nucleus ACCEPT (core); cytoplasm ACCEPT (trafficking); endosomes KEEP_AS_NON_CORE.
- Developmental BP: radial pattern formation ACCEPT; asymmetric cell division ACCEPT; leaf development / neg reg mitotic cell cycle / iron homeostasis / hormone metabolic = KEEP_AS_NON_CORE.
